# Weather-data-analysis
This project will analyze and visualize the meteorological data of the northern coast of Italy. During the experiment, we will first use the matplotlib library in Python to graph the data, and then call the SVM library in the scikit-learn library to perform regression analysis on the data, and finally draw our conclusions with the support of graph analysis.

## Research System: Adriatic Sea and Po River Basin
The area of the Po River Basin in Italy is very suitable for studying the impact of the ocean on the climate. This plain stretches from the Adriatic Sea to the east for hundreds of kilometers inland (see Figure below). Although it is surrounded by mountains, its wide area weakens the influence of the mountains. In addition, the area is densely populated with cities and towns, and it is also convenient to select a group of cities with different distances from the sea. In the selected cities, the maximum distance between the two cities is about 400 kilometers.

<p align="center">
	<img src="https://github.com/bochendong/Weather-data-analysis/raw/master/image/map.png"
        width="900" height="500">
	<p align="center">
</p>

We selected 9 cities. Then, their weather data will be analyzed. Among them, 4 cities are within 100 kilometers from the sea, and the remaining 5 are 100-400 kilometers from the sea.
<p align="center">
	<img src="https://github.com/bochendong/Weather-data-analysis/raw/master/image/map2.png"
        width="900" height="500">
	<p align="center">
</p>

The city we choose are listed below:
* Ferrara
* Mantova
* Milano
* Asti
* Ravenna
* Bologna
* Piacenza
* Cesena
* Faenza

## Data collection：
Get data from Open Weather Map, http://openweathermap.org/
<p align="center">
	<img src="https://github.com/bochendong/Weather-data-analysis/raw/master/image/dta.png"
        width="900" height="500">
	<p align="center">
</p>

## Result:
The ocean has a certain degree of influence on meteorological data, and the influence of the ocean decays rapidly. The temperature has risen to a high level 60 to 70 kilometers away from the sea.
<p align="center">
	<img src="https://github.com/bochendong/Weather-data-analysis/raw/master/image/dis_temp.png"
        width="900" height="500">
	<p align="center">
</p>
