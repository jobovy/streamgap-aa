# streamgap-aa

Modeling stream gaps in action-angle coordinates.

This repository contains the code associated with the paper Sanders, Bovy \& Erkal (2015, SBE15). The paper source code is in [paper/](paper/) and ipython notebooks used to generate the plots in the paper can be found in [py/](py/). This code is provided for illustration purposes only; full use of the code requires simulation data that is not included here.

There are three useful notebooks. We explain what each contains below:

## 1. [StreamGapExample.ipynb](py/StreamGapExample.ipynb)

1. We test the analytic computation of the velocity kicks for both Plummer and Hernquist profiles.
2. We generate Fig. 2 of SBE15 which compares the kicks from different subhalo profiles.
3. We generate Fig. 1 of SBE15 which computes the kicks for a curved stream track with increasing levels of complexity

## 2. [GapsAngleFreqJz!=0.ipynb](py/GapsAngleFreqJz!=0.ipynb)

1. We inspect a snapshot of the perturbed and unperturbed stream at 880Myr after the impact and calculate the actions, angles and frequencies (Fig. 3, 4, 5 SBE15).
2. We compute a stream track using the unperturbed simulation at the impact time, calculate the linear maps between angle and frequency kicks and the velocity kicks, and compare with the angle and frequency kicks from the simulation (Fig. 6, 7, 8 SBE15).
3. We compare our predictions for the perturbed stream at future times t=3Gyr and t=5Gyr (Fig. 9 SBE15)
3. WE compute some approximate analytic results for the action, angle and frequency kicks (Fig 9, 10 SBE15).
4. We compute the gap size in parallel angle as a function of time, and compare with the true gap size (Fig. 11, 13 SBE15).
5. We investigate the impact of different mass subhaloes (Fig. 14 SBE15) and different impact points (Fig. 15 SBE15)

## 3. [galpyModelnonzeroJz.ipynb](py/galpyModelnonzeroJz.ipynb)
1. We generate an unperturbed stream model using the angle-frequency formalism from Bovy (2014) and Sanders (2014) and modify it slightly to match the simulation (Fig. 16 SBE15)
2. We compute the angle and frequency kicks along the unperturbed stream track, perturb the stream model and compare to the simulation (Fig. 17 and 18 SBE15). This uses the modified stripping distribution from Sec. 6.1 in the paper, which is implemented in [custom_stripping_df.py](py/custom_stripping_df.py).

## AUTHORS

Jo Bovy - bovy at astro dot utoronto dot edu

Denis Erkal - derkal at ast dot cam dot ac dot uk

Jason Sanders - jls at ast dot cam dot ac dot uk

