# flask imports
from flask import Flask, render_template,jsonify
import psycopg2

from postgres_key import DB_USER,DB_KEY,DB_NAME

# -------------------------------------------------------------------- #
#                               Flask
# -------------------------------------------------------------------- #
app = Flask(__name__)

# -------------------------------------------------------------------- #
#                           Route - Home
# -------------------------------------------------------------------- #


@app.route('/')
def index():
    #Connect to the database to get the list of countries

    heading: str = '''
    Fossil Fuel Consumption and 
    Greenhouse Gas Emission Dashboard
    '''
    heading2: str = 'Pages:'
    content_1_title: str = 'Fossil Fuel Consumption'
    content_1_location: str = '/api/v1.0/consumption'
    content_2_title: str = 'CO2 Emissions'
    content_2_location: str = '/api/v1.0/emissions'
    return render_template(
        'index.html',
        heading=heading, heading2=heading2,
        content_1_title=content_1_title, content_1_location=content_1_location,
        content_2_title=content_2_title, content_2_location=content_2_location
    )

@app.route("/api/v1.0/countries")
def get_countries():
    """Return the justice league data as json"""
    conn = open_connection()
    cursor  = conn.cursor()
    cursor.execute("""Select country from country_master""")
    results = cursor.fetchall()
    cursor.close()

    close_connection(conn)
    return jsonify(results)

@app.route("/api/v1.0/groupings")
def get_year_groupings():
    """Return the justice league data as json"""
    conn = open_connection()
    cursor  = conn.cursor()
    cursor.execute("""select distinct year_range from fuel_consumption""")
    results = cursor.fetchall()
    cursor.close()

    close_connection(conn)
    return jsonify(results)

@app.route("/api/v1.0/gdp/<country>/<year_range>")
def get_gdp(country, year_range):
    """Return the justice league data as json"""
    conn = open_connection()

    years  = year_range.split('-')

    fromYear = int(years[0])
    toYear = int(years[1])

    print("***********************")
    print(years)
    print(country)


    cursor  = conn.cursor()
    cursor.execute("""select year, gdp from gdp where country = (%s) and year between (%s) and (%s) """, (country, fromYear, toYear, ))
    results = cursor.fetchall()
    print(results)
    cursor.close()
    close_connection(conn)

    years = []
    gdpValue = []
    returnValue = []
    for result in results:
        years.append(result[0])
        gdpValue.append(result[1])

    returnValue.append(years)
    returnValue.append(gdpValue)

    print(returnValue)
    return jsonify(returnValue)


def open_connection():
    conn = psycopg2.connect(host="localhost", port = 5432, database=DB_NAME, user=DB_USER, password=DB_KEY)
    return conn

def close_connection(conn):
    conn.close()
    

# -------------------------------------------------------------------- #
#                  Route - Fossil Fuel Consumption
# -------------------------------------------------------------------- #


@app.route('/api/v1.0/consumption')
def consumption():
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


@app.route('/api/v1.0/emissions')
def emissions():

    return(
        f'<h1>Greenhouse Gas Emissions by Country</h1>'
    )

# -------------------------------------------------------------------- #
#                  Route - Map 1
# -------------------------------------------------------------------- #


@app.route('/api/v1.0/map_page')
def map_page():

    title: str = 'World Map'
    heading: str = 'World Map'
    info: str = 'This is the world map page.'
    # TODO Is there a better way to structure this? Global variables?
    # TODO convert all hardcoded page info to variables that can be stored here
    content_1_title: str = 'Fossil Fuel Consumption'
    content_1_location: str = '/api/v1.0/consumption'
    content_2_title: str = 'CO2 Emissions'
    content_2_location: str = '/api/v1.0/emissions'
    return render_template(
        "map_page.html", title=title,
        heading=heading, info=info,
        content_1_title=content_1_title, content_1_location=content_1_location,
        content_2_title=content_2_title, content_2_location=content_2_location
    )


def main():
    '''Run the Flask app.'''

    app.run(debug=True)


if __name__ == "__main__":
    main()
