#!/usr/bin/env python
import glafic

glafic.init(0.3089, 0.6910, -1.0, 0.6736, 'Lens Models/pow_pos+flux_mpol1', -1, -0.4, 0.4, 1.0, 0.001, 0.001, 1, verb = 0)
glafic.set_secondary('chi2_splane 1', verb = 0)
glafic.set_secondary('chi2_checknimg 0', verb = 0)
glafic.set_secondary('chi2_restart   -1', verb = 0)
glafic.set_secondary('chi2_usemag    0', verb = 0)
glafic.set_secondary('hvary          0', verb = 0)
glafic.set_secondary('ran_seed -122000', verb = 0)

glafic.startup_setnum(2, 0, 1)

glafic.set_lens(1, 'pow', 1.1009,  2.224500e+00, -2.718057e-01 , 4.137265e-01 , 1.485158e-01,  2.828679e+00,  4.561778e-01,  1.718503e+00)
glafic.set_lens(2, 'mpole', 1.0, 2.2245, -0.3, 0.4, 0.001, 0, 1.0, 2.0)
glafic.set_point(1, 2.2245, -2.694114e-01,  3.610592e-01)

glafic.setopt_lens(1, 1, 0, 1, 1, 1, 1, 1, 1)
glafic.setopt_lens(2, 1, 0, 1, 1, 1, 1, 0, 1)
glafic.setopt_point(1, 0, 1, 1)

glafic.model_init(verb = 0)

glafic.readobs_point('obs_pos+flux.dat')
glafic.parprior('prior.dat')
glafic.optimize()
glafic.findimg()
glafic.writecrit(2.2245)
glafic.writelens(2.2245)

glafic.quit()
