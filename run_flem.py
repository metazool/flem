# -*- coding: utf-8 -*-
"""
Test of flem

@author: armitage
"""

from __future__ import print_function
import numpy as np
from flem import *
import os

# Directory name
name = 'test'
dirtest = './%s/' % name
directory = os.path.dirname(dirtest)
if not os.path.exists(directory) :
  os.makedirs(directory)


# Domain dimensions
model_space = [1e5, 8e5, 256] # lx, ly, resolution

# Physical parameters
physical_space = [1e+0,1e-5,1.5,1,1e-4] # [kappa, c, nexp, alpha, U]

# 0 = MFD node-to-node; 1 = MFD cell-to-cell; 2 = SD node-to-node; 3 = SD cell-to-cell
flow = 0

# Time
dt = 1e4
num_steps = 20

# Output
out_time = 0

# Plot stuff
plot = 0

# Calculate valley to valley wavelength
statistics = 0

[sed_flux, time, wavelength] = solve_flem(model_space,physical_space,flow,dt,num_steps,out_time,plot,statistics,name)


