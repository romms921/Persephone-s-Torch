#!/usr/bin/env python
import glafic

glafic.init(0.3089, 0.6910, -1.0, 0.6736, 'Lens Models/pow_pos+flux', -2, -1.4, 1.4, 2.0, 0.01, 0.01, 1, verb = 0)
glafic.set_secondary('chi2_splane 1', verb = 0)
glafic.set_secondary('chi2_checknimg 0', verb = 0)
glafic.set_secondary('chi2_restart   -1', verb = 0)
glafic.set_secondary('chi2_usemag    0', verb = 0)
glafic.set_secondary('hvary          0', verb = 0)
glafic.set_secondary('ran_seed -122000', verb = 0)

glafic.startup_setnum(2, 0, 1)

glafic.set_lens(1, 'pow', 0.5, 2.2245, -0.3, 0.4, 0.626, -94.93, 0.446, 2.011)
glafic.set_lens(2, 'pert', 0.5, 2.2245, -0.3, 0.4, 0.075, -109.26, 0.0, 0.0)
glafic.set_point(1, 2.2245, -0.3, 0.4)

glafic.setopt_lens(1, 0, 0, 1, 1, 0, 0, 0, 0)
glafic.setopt_lens(2, 0, 0, 1, 1, 0, 0, 0, 0)
glafic.setopt_point(1, 0, 1, 1)

glafic.model_init(verb = 0)

glafic.readobs_point('obs_pos+flux.dat')
glafic.parprior('prior.dat')
glafic.optimize()
glafic.findimg()
glafic.writecrit(2.2245)
glafic.writelens(2.2245)

glafic.quit()
