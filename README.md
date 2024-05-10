
# Climate Analysis and Flask API

## Overview

This project provides a climate analysis and a Flask API for exploring climate data in Honolulu, Hawaii. It includes the analysis of precipitation and temperature data, as well as the design of a Flask API to serve this data.

## Part 1: Analyze and Explore the Climate Data

### Precipitation Analysis

- Find the most recent date in the dataset.
- Query the previous 12 months of precipitation data.
- Plot the precipitation data and print summary statistics.
---
![prc](https://github.com/AVI-1213/sqlalchemy-challenge/assets/156638175/3b214467-be84-459a-9e0d-81eb9811706a)

### Station Analysis

- Calculate the total number of stations.
- Find the most active stations and their observation counts.
- Query temperature data for the most active station and plot it as a histogram.
---
![tob](https://github.com/AVI-1213/sqlalchemy-challenge/assets/156638175/f2540564-064e-400c-be8d-3f2e259f6cb1)

## Part 2: Design Your Climate App

### Flask API Routes

- **/**: Homepage, lists all available routes.
- **/api/v1.0/precipitation**: Returns JSON representation of precipitation data for the last 12 months.
- **/api/v1.0/stations**: Returns JSON list of stations from the dataset.
- **/api/v1.0/tobs**: Returns JSON list of temperature observations for the previous year from the most active station.
- **/api/v1.0/<start>**: Returns JSON list of temperature statistics (TMIN, TAVG, TMAX) for dates greater than or equal to the specified start date.
- **/api/v1.0/<start>/<end>**: Returns JSON list of temperature statistics (TMIN, TAVG, TMAX) for dates between the specified start and end dates.

## Tools Used

- Python
- SQLAlchemy
- Pandas
- Matplotlib
- Flask

## Usage

1. Clone the repository.
2. Install the required dependencies.
3. Run the Flask app using `python app.py`.
4. Access the API endpoints using the provided routes.

## Contributors

- [Avinas K]([link to your GitHub profile](https://github.com/AVI-1213))

