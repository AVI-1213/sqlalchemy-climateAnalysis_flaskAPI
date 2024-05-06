# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

import datetime as dt
from flask import Flask,jsonify
import numpy as np


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine) 

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
#   1 
#   create your routes as follows:
#   /
#   Start at the homepage.
#   List all the available routes.

@app.route("/")
def welcome():
    return (
        f"Welcome to Climate Analysis of Hawaii API" <br>
        f"List of available routes"<br>
        f"/api/v1.0/precipitation" <br>
        f"/api/v1.0/stations"<br>
        f"/api/v1.0/tobs"<br>
        f"/api/v1.0/start (as YYYY-MM-DD)"<br>
        f"/api/v1.0/start/end(as YYYY-MM-DD)"<br>
        )


#2
#     /api/v1.0/precipitation
#     Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
#     Return the JSON representation of your dictionary.


#3
#   /api/v1.0/stations
#   Return a JSON list of stations from the dataset.





#4
#   /api/v1.0/tobs
#   Query the dates and temperature observations of the most-active station for the previous year of data.
#   Return a JSON list of temperature observations for the previous year.




#5
#   /api/v1.0/<start> and /api/v1.0/<start>/<end>
#     Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
#     For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
#     For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.




