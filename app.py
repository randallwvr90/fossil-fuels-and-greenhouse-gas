# flask imports
from flask import Flask, jsonify

########################## Flask ##############################

app = Flask(__name__)

##################### Route - Home ############################
@app.route('/')
def index():

    return (
        f'<h1>Fossil Fuel Consumption and Greenhouse Gass Emission Dashboard</h1><br>'
        f'<ul><li> /api/v1.0/consumption </li><br>'
        f'<li> /api/v1.0/emissions </li></ul>'
        )

############## Route - Fossil Fuel Consumption ##################
@app.route('/api/v1.0/consumption')
def consumption():

    return(
        f'<h1>Fossil Fuel Consumption by Country</h1>'
        )

############## Route - Greenhouse Gas Emissions ##################
    @app.route('/api/v1.0/emissions')
    def emissions():

        return(
                f'<h1>Greenhouse Gas Emissions by Country</h1>'
              )


if __name__ == "__main__":
    app.run(debug=True)
