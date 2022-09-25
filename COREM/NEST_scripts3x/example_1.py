#!/usr/bin/python
# coding: utf-8

import nest
import nest.raster_plot
import numpy as np
import matplotlib.pyplot as plt

# simulation parameters
ganglionCells = 25*25
simTime = 1200.0

# Reset kernel and network
nest.ResetKernel()

# Number of threads (must be 1) and resolution (the same of the retina script)
nest.SetKernelStatus({"local_num_threads": 1,'resolution': 1.0})

# Install module just once
if 'corem' not in nest.node_models:
    nest.Install("corem_module")

# Create spike detector and spiking nodes
mult = nest.Create('spike_recorder',1)
spikingGanglion=nest.Create('iaf_psc_alpha',ganglionCells,{'E_L':-56.0})
nest.Connect(spikingGanglion,mult)

# COREM nodes
for i in range(0,ganglionCells):
    g=nest.Create('corem',1,{'port':float(i),'filename':"Retina_scripts/example_1.py"})
    nest.Connect(g,spikingGanglion[i])

# Simulation
nest.Simulate(simTime)

# Raster plot
nest.raster_plot.from_device(mult,hist=False)
plt.show()
