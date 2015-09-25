import sys
import os, os.path
import csv
import subprocess
import numpy
from galpy import potential
from galpy.util import bovy_coords
from galpy.actionAngle import actionAngleIsochroneApprox
def calc_actions(snapfile=None,first=0):
    #Setup potential and actionAngle object
    lp= potential.LogarithmicHaloPotential(normalize=1.,q=0.9)
    aA= actionAngleIsochroneApprox(pot=lp,b=0.8)
    # Load snapshot and convert to cylindrical coordinates
    xvid= numpy.loadtxt(snapfile)
    xv= xvid[:,:6]
    id= xvid[:,6]
    xv= xv[numpy.argsort(id)]
    id= id[numpy.argsort(id)].astype(int)
    R,phi,Z= bovy_coords.rect_to_cyl(xv[:,0],xv[:,1],xv[:,2])
    vR,vT,vZ= bovy_coords.rect_to_cyl_vec(xv[:,3],xv[:,4],xv[:,5],R,phi,Z,
                                          cyl=True)
    R/= 8.
    Z/= 8.
    vR/= 220.
    vT/= 220.
    vZ/= 220.
    if False: #Used for testing
        R= R[0:100]
        vR= vR[0:100]
        vT= vT[0:100]
        Z= Z[0:100]
        vZ= vZ[0:100]
        phi= phi[0:100]
    nx= len(R)
    if first:
        R= R[:nx//2]
        vR= vR[:nx//2]
        vT= vT[:nx//2]
        Z= Z[:nx//2]
        vZ= vZ[:nx//2]
        phi= phi[:nx//2]
        id= id[:nx//2]
    else:
        R= R[nx//2:]
        vR= vR[nx//2:]
        vT= vT[nx//2:]
        Z= Z[nx//2:]
        vZ= vZ[nx//2:]
        phi= phi[nx//2:]
        id= id[nx//2:]
    nx/= 2
    #calculation actions, frequencies, and angles
    #Processes in batches to not run out of memory
    if first:
        csvfilename= snapfile.replace('.txt','_aA1.txt')
    else:
        csvfilename= snapfile.replace('.txt','_aA2.txt')
    if os.path.exists(csvfilename):
        #Don't recalculate those that have already been calculated
        nstart= int(subprocess.check_output(['wc','-l',csvfilename]).split(' ')[0])
        csvfile= open(csvfilename,'ab')
    else:
        csvfile= open(csvfilename,'wb')
        nstart= 0
    if nstart >= nx: return 1 #Done already
    print "Starting from %i ..." % nstart
    nx-= nstart
    writer= csv.writer(csvfile,delimiter=',')
    nbatch= 20
    for ii in range(nx//nbatch):
        print "Working on batch %i out of %i ..." % (ii+1,nx//nbatch)
        tR= R[nstart+ii*nbatch:numpy.amin([nstart+(ii+1)*nbatch,nstart+nx])]
        tvR= vR[nstart+ii*nbatch:numpy.amin([nstart+(ii+1)*nbatch,nstart+nx])]
        tvT= vT[nstart+ii*nbatch:numpy.amin([nstart+(ii+1)*nbatch,nstart+nx])]
        tZ= Z[nstart+ii*nbatch:numpy.amin([nstart+(ii+1)*nbatch,nstart+nx])]
        tvZ= vZ[nstart+ii*nbatch:numpy.amin([nstart+(ii+1)*nbatch,nstart+nx])]
        tphi= phi[nstart+ii*nbatch:numpy.amin([nstart+(ii+1)*nbatch,nstart+nx])]
        try:
            tacfs= aA.actionsFreqsAngles(tR,tvR,tvT,tZ,tvZ,tphi)
        except numpy.linalg.linalg.LinAlgError:
            print tR,tvR,tvT,tZ,tvZ,tphi
            raise
        for jj in range(len(tacfs[0])):
            writer.writerow([tacfs[0][jj],tacfs[1][jj],tacfs[2][jj],
                             tacfs[3][jj],tacfs[4][jj],tacfs[5][jj],
                             tacfs[6][jj],tacfs[7][jj],tacfs[8][jj],
                             id[nstart+ii*nbatch+jj]])
            csvfile.flush()
    csvfile.close()
    return None


if __name__ == '__main__':
    calc_actions(snapfile=sys.argv[1],first=int(sys.argv[2]))
