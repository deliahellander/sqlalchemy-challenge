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

#################################################
# Flask Setup
#################################################

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Home Page with all routes listed
@app.route("/")
def home():
    print("Below is a list of all available routes")
    return (/api/v1.0/precipitation)

if __name__ == "__main__":
    app.run(debug=True)
