#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path = "archive/dnn-roi-paper/dnn-roi-service/"
tags = ['1apa-gpu', '2apa-gpu', '6apa-gpu', '6apa-gpu-100loop']
labels = ['1apa-gpu', '2apa-gpu', '6apa-gpu', '6apa-gpu-100loop']
dfs = [pd.read_csv(path+tag+'.device', sep=' ', header=None) for tag in tags]

path = "./"
tags = ["gpu-kokkos-mt-8.log"]
labels = ["gpu-kokkos-mt-8.log"]
dfs = [pd.read_csv(path+tag, sep=' ', header=None) for tag in tags]

xscale = 593./2370
xscale = 186./753
gpu_lim = [0, 120]
vram_lim = [0, 3]
vram_base = 0.247
vram_base = 0.459

plt.figure()

for i in range(len(tags)) :
    x = np.linspace(0,dfs[i][0].shape[0]*xscale,dfs[i][0].shape[0])
    plt.plot(x,dfs[i][0],label=labels[i])
plt.legend(loc='best',fontsize=15)
plt.grid()
plt.ylim(gpu_lim)
plt.xlabel("time [sec]", fontsize=15)
plt.ylabel("GPU [%]", fontsize=15)
plt.show()

plt.figure()

for i in range(len(tags)) :
    x = np.linspace(0,dfs[i][0].shape[0]*xscale,dfs[i][0].shape[0])
    plt.plot(x,dfs[i][1]/1000.-vram_base,label=labels[i])
# plt.plot((dfs[1][1]-dfs[0][1])*31.3/100,label="TBB-single - Pgrapher")
plt.legend(loc='best',fontsize=15)
plt.grid()
plt.ylim(vram_lim)
plt.xlabel("time [sec]", fontsize=15)
plt.ylabel("VRAM [GB]", fontsize=15)
plt.show()
