# Global_Warming_Git

## 1) Introduction
___
The goal of this exercise is to visualize a dataset provided by Nasa in an effective an meaningful way, so the user can evaluate the levels of the global warming phenomenon,  for  a predetermined period of time.



## 2) Requirements – Installation – Run
___
For the implementation, **python3** and **VSCode** were used, as well as some essential python libraries which are listed below together with their respective installation commands:
+ **Numpy**:  `$ pip install numpy`
+ **Matplotlib**: `$ python –m pip install matplotlib`
+ ****netCDF4****: `$ pip install netCDF4`
+ **Cartopy.crs**: `$ pip install cartopy`
+ **os**: `$ pip install os-sys`

To run the python script not much effort is needed as it is executable within any IDE (VS Code in my case), but also the command mentioned below can be used to run it from bash:

`$ python3 ‘specify the script path here’/globalWarming.py`

Lastly in this section,  I want to mention Panoply, which is an additional application provided by Nasa and I used to get a better understanding of the data provided. This application is not essential but helped me get a first grasp of the dataset structure. The link to download Panoply is mentioned below:

[Panoply tool](https://www.giss.nasa.gov/tools/panoply/download/)


## 3) Dataset
___
The dataset used in this project is called [Land-Ocean Temperature Index, ERSSTv5](https://data.giss.nasa.gov/pub/gistemp/gistemp1200_GHCNv4_ERSSTv5.nc.gz) . It is a netCDF file containing information about the temperature anomaly (temperature variation), the time period the aforementioned temperature measurements were taken as well as the longitude and latitude values that represent the globe. More information about the variables used in this dataset, such as the units of measurement for each one, are listed below:

+ **Longitude**: -180 < Longitude < 180, **units**  = “degrees east”
+ **Latitude**: -90 < Latitude < 90, **units**  = ”degrees north”
+ **Temperature Anomaly**: Function of Time, Longitude and Latitude, **units** =  “Kelvin degrees”
+ **Time**: **units** = “days since 1800-01-01 00:00:00”


## 4) Code Analysis
___
1. **Loading the dataset**<br>
The netCDF4 library contains a very useful module called “**Dataset**” which lets us load any file with the .nc extension and parse its data.<br>**Note:** No data cleansing is needed for this dataset even though it contains NaN values. That is because the data are provided in a masked numpy array form which ignores NaN values in any further calculations by default.

2. **Calculate the average global temperature variation**<br>
The dataset provides temperature value measurements once a month for each month since the year 1880 (the first measurement provided in the dataset is at 29233 days after 1800 which translates to the year 1880). By using the ``np.mean()`` function I can calculate the average temperature variation for the whole globe for each month so it is possible get an overall estimate of the global temperature value instead of individual areas of the globe.

3. **Calculate the average global temperature variation per year**<br>
To reduce the visual clutter of the following visualizations and also get a more generalized view of the temperature variation, a yearly average temperature variation calculation is needed. This provides more meaningful information to determine the course of the global warming phenomenon.

4. **Calculate the rolling average for visualization**<br>
The rolling (or moving) average is a variable that eliminates the extreme peaks in the “Temperature variation in regards to Time” curve. Those peaks often times lead to “wrong” assumptions about individual situations so the rolling average is a nice tool to have. It provides a smoother, more understandable curve.

5. **Visualization**<br>
+ Colored map<br>
The first visualization method used, is an updating plot of the global map. This map updates with a rate of 2fps and each frame corresponds to a different year (starts from year 1880 all the way to year 2022). The average global temperature variation we calculated in “step 3”, denotes the hue each frame is colored. The min and the max values of the yearly average temperature variation array are matched with the first and last color (blue and red) of the “coolwarm” colormap of matplotlib. A ``matplotlib.cm.ScalarMappable()`` object is the used to map the in-between temperature values to the spectrum of colors provided in the colormap. Also a colorbar is displayed for the user to help understand the correspondence of map colors and temperatures.
+ Graph<br>
After the colored map reaches the last year (year 2022), a more analytical visualization approach is displayed, in the form of a curve graph which provides an essential analysis of the data provided by the colored map of the previous step. In this graph we plot both the average yearly temperature variation (blue curve) as well as the rolling average (red curve) in regards to time (in years), so the user can get a more precise evaluation and clearly see the upwards trend of the global warming phenomenon.


## 5) Colncusion - Future Work
___
### Conclusion
In this exercise, two visualization methods were selected to depict the global warming phenomenon.  The first one, the colored map, provides a more visual approach which is easily comprehensible by users that may not be familiar with graph and curve representations. The graph that follows serves as a more analytical explanation of the information displayed on the colored map and gives the user a better understanding about the issue, meanwhile avoiding information overload.

### Future Work<br>
The dataset used in this exercise contained a significant amount of missing values which could be a problem in precise temperature calculations. To combat this, a forecast time series predicting model can be developed, specifically using the LSTM architecture of neural networks. This suggested method is often used in relevant bibliography the last 20 years and it is a suitable solution to our missing data problem since our data also form a time series.  The fact that our data consist of chronologically related measurements and also their distribution produces average and fluctuation values proves that the suggested LSTM approach is applicable in this case.
