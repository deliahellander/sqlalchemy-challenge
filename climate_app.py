# 1. import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup, referenced lesson plan for this code
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Home Page with all routes listed
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )
#################################################

@app.route("/api/v1.0/precipitation")
def precipitation():
    """List of rain fall for previous year"""
    # Using the query from part 1 (most recent 12 months of precipitation data), convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    # Return the JSON representation of your dictionary (note the specific format of your dictionary as required from above).
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation_data = session.query(Measurement.date, func.avg(Measurement.prcp)).filter(Measurement.date >= one_year_ago).group_by(Measurement.date).all()
    return jsonify(precipitation_data)

#################################################

@app.route("/api/v1.0/stations")
def stations():
    most_active_stations = session.query(Station.station, Station.name).all()
    return jsonify(most_active_stations)

#################################################

@app.route("/api/v1.0/tobs")
def tobs():
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    highest_num_temp_station = session.query(Measurement.date, Measurement.station, Measurement.tobs).filter(Measurement.date >= one_year_ago).all()
    return jsonify(highest_num_temp_station)

#################################################

@app.route("/api/v1.0/<start>")
def start_date(start):
    start_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    return jsonify(start_temp)

#################################################

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start,end):
    day_range = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    return jsonify(day_range)

if __name__ == "__main__":
    app.run(debug=True)
