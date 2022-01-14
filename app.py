# flask imports
from flask import Flask, render_template, jsonify
import json
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

from postgres_key import DB_USER, DB_KEY, DB_NAME
from createDatabase import create_db


# -------------------------------------------------------------------- #
#                             DB functions
# -------------------------------------------------------------------- #


def open_connection():
    conn = psycopg2.connect(host="localhost", port=5432,
                            database=DB_NAME, user=DB_USER, password=DB_KEY)
    return conn


def close_connection(conn):
    conn.close()


# -------------------------------------------------------------------- #
#                               Flask
# -------------------------------------------------------------------- #
app = Flask(__name__)


# -------------------------------------------------------------------- #
#                           Route - Home
# -------------------------------------------------------------------- #


@app.route('/')
def index():
    # Connect to the database to get the list of countries

    heading: str = '''
    Fossil Fuel Consumption and 
    Greenhouse Gas Emission Dashboard
    '''
    #heading2: str = 'Pages:'
    #content_1_title: str = 'Fossil Fuel Consumption'
    #content_1_location: str = '/api/v1.0/consumption'
    #content_2_title: str = 'CO2 Emissions'
    #content_2_location: str = '/api/v1.0/emissions'
    return render_template(
        'index.html',
        heading=heading
        #content_1_title=content_1_title, content_1_location=content_1_location,
        #content_2_title=content_2_title, content_2_location=content_2_location
    )


# -------------------------------------------------------------------- #
#                Route - get the list of countries
# -------------------------------------------------------------------- #


@app.route("/api/v1.0/countries")
def get_countries():
    """Return Countries data as json"""
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute("""Select country from country_master order by 1""")
    results = cursor.fetchall()
    cursor.close()

    close_connection(conn)
    return jsonify(results)


# -------------------------------------------------------------------- #
#                 Route - get the list of year ranges
# -------------------------------------------------------------------- #


@app.route("/api/v1.0/groupings")
def get_year_groupings():
    """Return Year Ranges data as json"""
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute(
        """select distinct year_range from fuel_consumption order by year_range asc""")
    results = cursor.fetchall()
    cursor.close()

    close_connection(conn)
    return jsonify(results)


# -------------------------------------------------------------------- #
#           Route - gdp for a country in a specified year range
# -------------------------------------------------------------------- #


@app.route("/api/v1.0/gdp/<country>/<year_range>")
def get_gdp(country, year_range):
    """Return GDP data as json"""
    conn = open_connection()

    years = year_range.split('-')

    fromYear = int(years[0])
    toYear = int(years[1])

    cursor = conn.cursor()
    cursor.execute("""select year, gdp from gdp where country = (%s) and year between (%s) and (%s) """,
                   (country, fromYear, toYear))
    results = cursor.fetchall()
    # print(results)
    cursor.close()
    close_connection(conn)

    years = []
    gdpValue = []
    returnValue = []

    # Loop through the result to seperate the year and the gdp value
    for result in results:
        years.append(result[0])
        gdpValue.append(result[1])

    returnValue.append(years)
    returnValue.append(gdpValue)

    # print(returnValue)
    return jsonify(returnValue)


# -------------------------------------------------------------------- #
#                  Route - Fossil Fuel Consumption
# -------------------------------------------------------------------- #


@app.route('/api/v1.0/consumption')
def consumption(country, year_range):
    title: str = 'Fossil Fuel Consumption by Country'
    heading: str = 'Fossil Fuel Consumption by Country'
    info: str = 'This is the consumption page.'
    # TODO Is there a better way to structure this? Global variables?
    # TODO convert all hardcoded page info to variables that can be stored here
    content_1_title: str = 'Fossil Fuel Consumption'
    content_1_location: str = '/api/v1.0/consumption'
    content_2_title: str = 'CO2 Emissions'
    content_2_location: str = '/api/v1.0/emissions'
    return render_template(
        "page1.html", title=title,
        heading=heading, info=info,
        content_1_title=content_1_title, content_1_location=content_1_location,
        content_2_title=content_2_title, content_2_location=content_2_location
    )


# -------------------------------------------------------------------- #
#                  Route - Greenhouse Gas Emissions
# -------------------------------------------------------------------- #


@app.route('/api/v1.0/emissions/<country>/<year_range>')
def emissions(country, year_range):

    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute(
        """select year,emission_value from co2_emission where country = (%s) and year_range=(%s)""",
        (country, year_range)
    )
    results = cursor.fetchall()
    # print(results)
    cursor.close()
    close_connection(conn)

    years = []
    EmissionValue = []
    returnValue = []

    # Loop through the result to seperate the year and the gdp value
    for result in results:
        years.append(result[0])
        EmissionValue.append(result[1])

    returnValue.append(years)
    returnValue.append(EmissionValue)

    # print(returnValue)
    return jsonify(returnValue)


# -------------------------------------------------------------------- #
#                      Route - emissions map
# -------------------------------------------------------------------- #


@app.route("/api/v1.0/emissions_map")
def emissions_map():
    return render_template(
        'map_page.html'
    )


@app.route("/api/low_res_world")
def low_res_world():
    geo_json_path = './static/data/low_res_world.geo.json'
    f = open(geo_json_path, "r")
    # geo_json = f.readline()
    geo_json_dict = json.load(f)
    f.close()
    print(type(geo_json_dict))
    return jsonify(geo_json_dict)


@app.route("/api/v1.0/get_global_emissions")
def get_global_emissions():
    """Get emissions data as json"""
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute(
        """select  emission_value, country_id from co2_emission where year = 2020"""
    )
    results = cursor.fetchall()
    cursor.close()

    close_connection(conn)
    return jsonify(results)



def main():
    #----------Create DB------#
    print("Creating Database")
    create_db(DB_USER, DB_KEY, DB_NAME)
    print("Database Created")
    '''Run the Flask app.'''
    app.run(debug=True)


if __name__ == "__main__":
    main()
