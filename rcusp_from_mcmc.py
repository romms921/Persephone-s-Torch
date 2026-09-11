#!/usr/bin/env python
import glafic
import pandas as pd 
import time
import tqdm
import numpy as np

mcmc_file = pd.read_csv('pow_pos+flux_mcmc.dat', delim_whitespace=True, header=None, names=['chi2', 'z', 'x', 'y', 'e', 'PA', 'rein', 'pwi'])

rcusp_values = []

for i in tqdm.tqdm(np.random.randint(0, len(mcmc_file), 60)):

    chi2 = mcmc_file['chi2'][i]
    z = mcmc_file['z'][i]
    x = mcmc_file['x'][i]
    y = mcmc_file['y'][i]
    e = mcmc_file['e'][i]
    PA = mcmc_file['PA'][i]
    rein = mcmc_file['rein'][i]
    pwi = mcmc_file['pwi'][i]

    glafic.init(0.3089, 0.6910, -1.0, 0.6736, 'temp/mcmc', -1, -0.4, 0.4, 1.0, 0.001, 0.001, 1, verb = 0)
    glafic.set_secondary('chi2_splane 1', verb = 0)
    glafic.set_secondary('chi2_checknimg 0', verb = 0)
    glafic.set_secondary('chi2_restart   -1', verb = 0)
    glafic.set_secondary('chi2_usemag    0', verb = 0)
    glafic.set_secondary('hvary          0', verb = 0)
    glafic.set_secondary('ran_seed -122000', verb = 0)

    glafic.startup_setnum(1, 0, 1)

    glafic.set_lens(1, 'pow', mcmc_file['z'][i], 2.2245, mcmc_file['x'][i], mcmc_file['y'][i], mcmc_file['e'][i], mcmc_file['PA'][i], mcmc_file['rein'][i], mcmc_file['pwi'][i])
    glafic.set_point(1, 2.2245, -0.3, 0.4)

    glafic.setopt_lens(1, 0, 0, 0, 0, 0, 0, 0, 0)
    glafic.setopt_point(1, 0, 1, 1)

    glafic.model_init(verb = 0)

    glafic.readobs_point('obs_pos+flux.dat')
    glafic.parprior('prior.dat')
    glafic.optimize()
    glafic.findimg()

    glafic.quit()

    # Calculation of RCusp Parameter
    out_dat = pd.read_csv('temp/mcmc_point.dat', delim_whitespace=True, header=None, names=['x', 'y', 'mag', 'td'], skiprows=1)

    # If more than 4 images are found, keep only the 4 brightest images from absolute magnification
    if len(out_dat) > 4:
        # Make negative magnifications positive for comparison
        out_dat['abs_mag'] = abs(out_dat['mag'])
        # Sort by absolute magnification and keep the 4 brightest images
        out_dat = out_dat.nlargest(4, 'abs_mag')

    # Mask out the dimmest image (the one with the lowest magnification)
    out_dat = out_dat[out_dat['mag'] != abs(out_dat['mag']).min()]

    # Calculate the RCusp parameter using the remaining three images
    mag_sum = abs(out_dat['mag']).sum()
    rcusp = out_dat['mag'].sum() / mag_sum

    rcusp_values.append(rcusp)
    
# Save values as text file
np.savetxt('rcusp_values.txt', rcusp_values, fmt='%.6f')



