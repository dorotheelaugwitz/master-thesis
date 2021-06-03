<p align="center">
  <img src="stadtrad.jpeg" width="500"/>
</p>

This repository contains the source code for my master thesis titled

# Predictive analytics for shared bicycle mobility in the city of Hamburg

## How to use the notebooks

1. Acquire data from the data sources below.
2. Run the notebooks in `/notebooks/clean` in any order.
3. Run the notebooks in `/notebooks/prepare` in any order.
4. Run the notebooks in `/notebooks/explore` and `/notebooks/predict` in any order.

Or just look at them here.

## Data sources

**Call a bike**

* [Call a Bike rentals](https://data.deutschebahn.com/dataset/data-call-a-bike/resource/0fcce4dd-7fc6-43f8-a59c-983a7945f8ba.html)
* [Call a Bike stations](https://data.deutschebahn.com/dataset/data-call-a-bike/resource/abe748e1-a4a5-4923-a501-319217fb5c10.html)

Unpack the contents to `/data/call_a_bike/`.

**Additional station coordinates**

* [Transparenzportal Hamburg](https://suche.transparenz.hamburg.de/dataset/stadtrad-stationen-hamburg20)

Download GML and save as `/data/hamburg/stations.gml`, convert to GeoJSON with the `scripts/ogr2ogr` script and transform to CSV with the `scripts/hamburg_stations_data_to_csv.rb` script.

**Public transport stations geodata**

* [Esri Deutschland](https://opendata-esri-de.opendata.arcgis.com/datasets/esri-de-content::bahnh%C3%B6fe-hamburg/about)

Download GeoJSON and save as `/data/esri/pt_lines.geojson`.

**Weather data**

* [DarkSky API](https://darksky.net/dev/docs)

Sadly, the DarkSky API is not public anymore and only available to already registered users. If possible, acquire weather for the time between 2014-01-01 and 2017-05-16. The data is expected to be located under `/data/weather` as CSV looking like this:

```csv
datetime,precip_intensity,precip_probability,precip_type,precip_accumulation,temperature,apparent_temperature,dew_point,humidity,wind_speed,wind_gust,wind_bearing,uv_index,visibility,cloud_cover,pressure
2015-11-11 03:00:00,0.0055,0.03,rain,,15.06,15.14,14.53,0.97,5.97,5.97,252,0,10.003,0.75,1016.9
```
