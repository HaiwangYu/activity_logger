#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

import matplotlib
print("Backend used by matplotlib is: ", matplotlib.get_backend())

inputs = [
    "log",
    # "trad.log",
    # "dnn-haiwang-nchunk1.log",
    # "dnn-haiwang-nchunk2.log",
    # "dnn-haiwang-nchunk4.log",
    # "dnn-mobilenetv3-nchunk1.log",
    # "dnn-mobilenetv3-nchunk2.log",
]
labels = inputs
linestyles = [
"--",
"--",
"--",
"--",
"-",
"-",
"-",
"-",
"-",
"-",
]

# Function to replace pandas read_csv
def read_csv_file(filename, sep=' '):
    class SimpleDataFrame:
        def __init__(self, data_array):
            self.data = data_array
            self.shape = data_array.shape
        
        def __getitem__(self, idx):
            # Return the column at index idx
            return self.data[:, idx]
    
    try:
        data = np.loadtxt(filename, delimiter=sep)
        return SimpleDataFrame(data)
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return None

dfs = [read_csv_file(tag) for tag in inputs]
xscale = 9./24
xscale = 204./740
cpu_lim = [0, 200]
ram_size = 92.5 # 31.3, 10
ram_lim = [0, 10]

fontsize = 18

# memory in GB
for i in range(len(inputs)) :
    x = np.linspace(0,dfs[i][0].shape[0]*xscale,dfs[i][0].shape[0])
    plt.plot(x,dfs[i][1]*ram_size/100,label=labels[i]
             , linestyle=linestyles[i]
    )
# plt.plot((dfs[1][1]-dfs[0][1])*31.3/100,label="TBB-single - Pgrapher")
plt.legend(loc='best',fontsize=fontsize)
plt.grid()
plt.ylim(ram_lim)
plt.xlabel("time [sec]", fontsize=fontsize)
plt.ylabel("memory [GB]", fontsize=fontsize)
plt.yticks(fontsize=fontsize)
plt.xticks(fontsize=fontsize)
plt.tight_layout()
plt.show()
exit()

# cpu in %
for i in range(len(inputs)) :
    x = np.linspace(0,dfs[i][0].shape[0]*xscale,dfs[i][0].shape[0])
    plt.plot(x,dfs[i][0],label=labels[i]
        , linestyle=linestyles[i]
    )
plt.legend(loc='best',fontsize=fontsize)
plt.grid()
plt.ylim(cpu_lim)
plt.xlabel("time [sec]", fontsize=fontsize)
plt.ylabel("cpu [%]", fontsize=fontsize)
plt.yticks(fontsize=fontsize)
plt.xticks(fontsize=fontsize)
plt.tight_layout()
plt.show()


# plt.plot((dfs[1][1]-dfs[0][1])*31.3/100,label="TBB-single - Pgrapher")
# plt.legend(loc='best',fontsize=fontsize)
# plt.grid()
# plt.ylim(-1,1)
# plt.xlabel("time [sec]", fontsize=fontsize)
# plt.ylabel("memory [GB]", fontsize=fontsize)
# plt.show()

# for i in range(len(inputs)) :
#     plt.plot(dfs[i][1]*31.3/dfs[i][0],label=labels[i])
# plt.legend(loc='best',fontsize=fontsize)
# plt.grid()
# plt.ylim(0,2)
# plt.xlabel("time [sec]", fontsize=fontsize)
# plt.ylabel("memory/CPU load [GB]", fontsize=fontsize)
# plt.show()

#%%
