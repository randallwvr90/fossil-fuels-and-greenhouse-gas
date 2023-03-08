# flask imports
from flask import Flask, render_template, jsonify
import json
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

from postgres_key import DB_USER, DB_KEY, DB_NAME
from createDatabase import create_db

# global variables for web routes
# web route - any route function that uses "render_template"
content_1_title: str = 'Map - Emissions by Country'
content_1_location: str = '/api/v1.0/emissions_map?year=2020'
content_2_title: str = 'Consumption and Emissions by Country'
content_2_location: str = '/api/v1.0/allYears'


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
    return render_template(
        'index.html',
        heading=heading,
        content_1_title=content_1_title, content_1_location=content_1_location,
        content_2_title=content_2_title, content_2_location=content_2_location
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
#                  Route - Conusmptions Barchart
# -------------------------------------------------------------------- #

@app.route("/api/v1.0/fuel_cons/<country>/<year>")
def fuel_cons(country, year):
    conn = open_connection()
    years  = year.split('-')

    fromYear = int(years[0])
    toYear = int(years[1])
    cursor  = conn.cursor()
   
    cursor.execute(""" select sum(consumption_value), year from fuel_consumption where country = (%s) and year between (%s) and (%s) group by year """, (country, fromYear, toYear))
    results = cursor.fetchall()
    cursor.close()

    close_connection(conn)
    years = []
    consumptionValue = []
    returnValue = []
    for result in results:
        years.append(result[1])
        consumptionValue.append(result[0])

    returnValue.append(years)
    returnValue.append(consumptionValue)
    print(returnValue)
    return jsonify(returnValue) 

# -------------------------------------------------------------------- #
#                  Route - Fuel Production
# -------------------------------------------------------------------- #
@app.route("/api/v1.0/production/<country>/<year>")
def production(country, year):
    conn = open_connection()
    years  = year.split('-')

    fromYear = int(years[0])
    toYear = int(years[1])
    cursor  = conn.cursor()
   
    cursor.execute(""" select sum(production_value), year from fuel_production where country = (%s) and year between (%s) and (%s) group by year """, (country, fromYear, toYear))
    results = cursor.fetchall()
    cursor.close()

    close_connection(conn)
    years = []
    productionValue = []
    returnValue = []
    for result in results:
        years.append(result[1])
        productionValue.append(result[0])

    returnValue.append(years)
    returnValue.append(productionValue)
    print(returnValue)
    return jsonify(returnValue) 


# -------------------------------------------------------------------- #
#                      Route - emissions map
# -------------------------------------------------------------------- #


@app.route("/api/v1.0/emissions_map")
def emissions_map():
    return render_template(
        'map_page.html',
        content_1_title=content_1_title, content_1_location=content_1_location,
        content_2_title=content_2_title, content_2_location=content_2_location
    )

@app.route("/api/v1.0/getMappingYears")
def get_years_for_map():
    """Get emissions data as json"""
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute(
        """select distinct year from co2_emission order by year asc"""
    )
    results = cursor.fetchall()
    cursor.close()

    close_connection(conn)
    return jsonify(results)

# -------------------------------------------------------------------- #
#                      Route - get geojson
# -------------------------------------------------------------------- #


@app.route("/api/low_res_world")
def low_res_world():
    geo_json_path = './static/data/low_res_world.geo.json'
    f = open(geo_json_path, "r")
    # geo_json = f.readline()
    geo_json_dict = json.load(f)
    f.close()
    print(type(geo_json_dict))
    return jsonify(geo_json_dict)


# -------------------------------------------------------------------- #
#                      Route - get global emissions
# -------------------------------------------------------------------- #


@app.route("/api/v1.0/get_global_emissions/<year>")
def get_global_emissions(year):
    """Get emissions data as json"""
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute(
        """select  emission_value, country_id from co2_emission where year = (%s)""", (year,)
    )
    results = cursor.fetchall()
    cursor.close()
    print(results);
    close_connection(conn)
    return jsonify(results)

# -------------------------------------------------------------------- #
#                           Route - allYears
# -------------------------------------------------------------------- #


@app.route('/api/v1.0/allYears')
def allYears():

    heading: str = '''
    Fossil Fuel Consumption and 
    Greenhouse Gas Emission Dashboard
    '''
    heading2: str = 'Pages:'
    return render_template(
        'allYears3.html',
        heading=heading, heading2=heading2,
        content_1_title=content_1_title, content_1_location=content_1_location,
        content_2_title=content_2_title, content_2_location=content_2_location
    )


# -------------------------------------------------------------------- #
#                           Route - "countries2"
# -------------------------------------------------------------------- #


@app.route("/api/v1.0/countries2")
def get_countries2():
    """Return Countries data as json"""
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute("""Select country from country_master order by 1""")
    results = cursor.fetchall()
    cursor.close()

    close_connection(conn)
    return jsonify(results)


# -------------------------------------------------------------------- #
#                 Route - "allYears/emissions/<country>"
# -------------------------------------------------------------------- #


@app.route("/api/v1.0/allYears/emissions/<country>")
def get_allEmissions(country):

    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute(
        """select year, emission_value from co2_emission where country = (%s) """, (country,))
    results = cursor.fetchall()
    cursor.close()
    close_connection(conn)

    years = []
    co2 = []
    returnValue = []
    for result in results:
        years.append(result[0])
        co2.append(result[1])

    returnValue.append(years)
    returnValue.append(co2)

    return jsonify(returnValue)


# -------------------------------------------------------------------- #
#                 Route - "allYears/consumption/<country>"
# -------------------------------------------------------------------- #


@app.route("/api/v1.0/allYears/consumption/<country>")
def get_Consumption(country):

    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute(
        """select year, consumption_value from fuel_consumption where country = (%s) and fuel_type = 'oilcons_ej' """, (country,))
    results1 = cursor.fetchall()
    cursor.execute(
        """select year, consumption_value from fuel_consumption where country = (%s) and fuel_type = 'gascons_ej' """, (country,))
    results2 = cursor.fetchall()
    cursor.execute(
        """select year, consumption_value from fuel_consumption where country = (%s) and fuel_type = 'coalcons_ej' """, (country,))
    results3 = cursor.fetchall()
    cursor.execute(
        """select year, consumption_value from fuel_consumption where country = (%s) and fuel_type = 'ethanol_cons_ej' """, (country,))
    results4 = cursor.fetchall()
    cursor.execute(
        """select year, consumption_value from fuel_consumption where country = (%s) and fuel_type = 'biofuels_cons_ej' """, (country,))
    results5 = cursor.fetchall()
    cursor.execute(
        """select year, consumption_value from fuel_consumption where country = (%s) and fuel_type = 'biodiesel_cons_ej' """, (country,))
    results6 = cursor.fetchall()
    cursor.close()
    close_connection(conn)

    years1 = []
    fuel1 = []
    for result in results1:
        years1.append(result[0])
        fuel1.append(result[1])

    years2 = []
    fuel2 = []
    for result in results2:
        years2.append(result[0])
        fuel2.append(result[1])

    years3 = []
    fuel3 = []
    for result in results3:
        years3.append(result[0])
        fuel3.append(result[1])

    years4 = []
    fuel4 = []
    for result in results4:
        years4.append(result[0])
        fuel4.append(result[1])

    years5 = []
    fuel5 = []
    for result in results5:
        years5.append(result[0])
        fuel5.append(result[1])

    years6 = []
    fuel6 = []
    for result in results6:
        years6.append(result[0])
        fuel6.append(result[1])

    returnValue = []
    returnValue.append(years1)
    returnValue.append(fuel1)
    returnValue.append(years2)
    returnValue.append(fuel2)
    returnValue.append(years3)
    returnValue.append(fuel3)
    returnValue.append(years4)
    returnValue.append(fuel4)
    returnValue.append(years5)
    returnValue.append(fuel5)
    returnValue.append(years6)
    returnValue.append(fuel6)

    return jsonify(returnValue)


def main():
    '''Run the Flask app.'''
    app.run(debug=False)


if __name__ == "__main__":
    main()
