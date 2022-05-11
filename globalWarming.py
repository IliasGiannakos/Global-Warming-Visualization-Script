#Importing essential libraries
from netCDF4 import Dataset
import numpy as np
import os

#Loading the dataset
dir = os.path.dirname(__file__)
file_path = dir + "\gistemp1200_GHCNv4_ERSSTv5.nc"
dataset = Dataset(file_path, mode='r', format="NETCDF4")

#Seperate dataset variables
lat = dataset.variables['lat'][:]
lon = dataset.variables['lon'][:]
time = dataset.variables['time'][:] 
temp = dataset.variables['tempanomaly'][:]

#Calculate the mean global temrature variation over 1707 months
average_global_temp = []
for i in range(len(time)):
    average_global_temp.append(temp[i].mean())

#Convert days to years
date = []
for i in range(len(time)):
   years = time[i] // 365
   date.append(1800+years)

#Reduce the visual clutter by calculating the average temprature variation
#for each year instead of each month
yearly_mean_temp = []
for k in range(1880,2022):
    temp1 = []
    for i in range(len(date)):
        if date[i]==k:
            temp1.append(i)
        sum = 0
        for j in temp1:
            sum = sum + average_global_temp[j]
            mean1 = sum / len(temp1)
    yearly_mean_temp.append(mean1)

#Calculate the rolling average for visualization
window_size = 4
i = 0
moving_avg = []
while i < len(yearly_mean_temp)-window_size+1:
    this_window = yearly_mean_temp[i:i+window_size]
    window_average = np.sum(this_window)/window_size
    moving_avg.append(window_average)
    i +=1

#Visualize
#Colored map of the globe
import cartopy.crs as ccrs
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt

cmap= matplotlib.cm.get_cmap('coolwarm')
vmin=min(yearly_mean_temp)
vmax=max(yearly_mean_temp)
normalized_values = plt.Normalize(vmin = vmin, vmax = vmax )
scalarMap = matplotlib.cm.ScalarMappable(norm = normalized_values, cmap = cmap)
rgba = scalarMap.to_rgba(yearly_mean_temp)
year = range(1880,2023)
for i in range(len(yearly_mean_temp)):
    ax = plt.axes(projection = ccrs.PlateCarree())
    ax.coastlines(resolution='110m')
    ax.set_facecolor(rgba[i])
    ax.gridlines()
    gl = ax.gridlines(draw_labels=True)
    gl.top_labels=False
    gl.right_labels = False
    plt.text(-180,100, "Year="+str(year[i])+"   Temprature variation (Kelvin degrees)=%.2f"%yearly_mean_temp[i])
    cb = plt.colorbar(scalarMap, shrink = 0.7, label = 'Temprature variation to color')
    plt.draw()
    plt.pause(0.5)
    ax.cla()
    cb.remove()

#Average yearly temprature variation graph
plt.figure(figsize=(18,7))
plt.grid()
plt.title('Average global temprature variation over time')
plt.xlabel('Year')
plt.ylabel('Average temprature variation (Kelvin degrees)')
plt.xlim(1880,2022)
plt.xticks(np.arange(1880, 2022+1,4))
plt.xticks(rotation = 45)
plt.plot(range(1880,2022),yearly_mean_temp, label = 'Temprature variation')
plt.plot(range(1880,2019),moving_avg, 'r', linewidth=3, label = 'Moving average')
plt.legend(loc="upper left")
#Remove the # from the row below and specify a path if the Temprature variation graph needs to be saved
#plt.savefig("Specify the path to the save folder here"+"/GlobalWarmingPlot.jpg")
plt.show()
