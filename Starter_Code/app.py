# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, text, func
from sqlalchemy.orm import Session

import datetime as dt
from flask import Flask, jsonify
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

# defining a function to find most recent dates
def previous_year():
# creating a session
    session = Session(engine)

    recent_date = session.query(measurement.date).order_by(measurement.date.desc()).first()[0]
    # Convert recent_date to a date object
    recent_date = dt.datetime.strptime(recent_date, '%Y-%m-%d').date()
    
    first_year_date = recent_date - dt.timedelta(days=365)
    
    session.close()

    return first_year_date
    
    
    # session.close()

    # return (first_year_date)

 # Create our session (link) from Python to the DB
#session = Session(engine)

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
def homepage():
        return (
        f"Welcome to Climate Analysis of Hawaii API <br/>" 
        f"List of available routes <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/start/YYYY-MM-DD <br/>"
        f"/api/v1.0/start/YYYY-MM-DD/end/YYYY-MM-DD"

        )


#2
#     /api/v1.0/precipitation
#     Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

@app.route("/api/v1.0/precipitation")
def percipitation():
# Create our session (link) from Python to the DB
    session = Session(engine)

    annual_percp = session.query(measurement.date, measurement.prcp).filter(measurement.date>= previous_year()).all()
    session.close()
# Return the JSON representation of your dictionary.
    prcp_date = []
    prcp_total = []
    for date,prcp in annual_percp:
        prcp_date.append(date)
        prcp_total.append(prcp)
    prcp_dict = dict(zip(prcp_date,prcp_total))
    
    return jsonify(prcp_dict)

#3
#   /api/v1.0/stations
#   Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    station_results = session.query(station.station).all()
    
    session.close()
# Convert list of tuples into normal list
    station_list = list(np.ravel(station_results))

    return jsonify(station_list)


#4
#   /api/v1.0/tobs
#   Query the dates and temperature observations of the most-active station for the previous year of data.
#   Return a JSON list of temperature observations for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    
    temp_obs = session.query(measurement.date, measurement.tobs).\
                    filter(measurement.station == 'USC00519281').\
                    filter(measurement.date>= previous_year()).all()
    
    session.close()

    tobs_list = []
    for date,tobs in temp_obs:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["tobs"] = tobs

        tobs_list.append(temp_dict)

    return jsonify(tobs_list)
    
#5
#   /api/v1.0/<start> and /api/v1.0/<start>/<end>
#     Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
#     For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
#     For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

@app.route("/api/v1.0/start/<start>")
def temp_stats_start(start):
    session = Session(engine)
    start = previous_year()
    
    
    # Query for minimum, average, and maximum temperature for dates greater than or equal to the start date
    temp_stats = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
                 filter(measurement.date >= start).all()
    
    session.close()

    # Convert the query result into a dictionary
    temp_stats_dict = {
        "start_date": start,
        "TMIN": temp_stats[0][0],
        "TAVG": temp_stats[0][1],
        "TMAX": temp_stats[0][2]
    }

    return jsonify(temp_stats_dict)

@app.route("/api/v1.0/start/<start>/end/<end>")
def temp_stats_range(start, end):
    session = Session(engine)
    start = previous_year()
    end = start + dt.timedelta(days=365)
    
    # Query for minimum, average, and maximum temperature for the date range
    temp_stats = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
                 filter(measurement.date >= start).filter(measurement.date <= end).all()
    
    session.close()

    # Convert the query result into a dictionary
    temp_stats_dict = {
        "start_date": start,
        "end_date": end,
        "TMIN": temp_stats[0][0],
        "TAVG": temp_stats[0][1],
        "TMAX": temp_stats[0][2]
    }

    return jsonify(temp_stats_dict)


# Define main branch 
if __name__ == "__main__":
    app.run(debug = True)