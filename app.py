# flask imports
from flask import Flask, render_template

########################## Flask ##############################

app = Flask(__name__)

##################### Route - Home ############################


@app.route('/')
def index():
    heading: str = '''
    Fossil Fuel Consumption and 
    Greenhouse Gas Emission Dashboard
    '''
    heading2: str = 'Pages:'
    info: str = '/api/v1.0/consumption'
    info2: str = '/api/v1.0/emissions'
    return render_template('index.html', heading=heading, heading2=heading2, info=info, info2=info2)


############## Route - Fossil Fuel Consumption ##################


@app.route('/api/v1.0/consumption')
def consumption():
    heading: str = 'Fossil Fuel Consumption by Country'
    info: str = 'This is the consumption page.'
    return render_template("page1.html", heading=heading, info=info)

############## Route - Greenhouse Gas Emissions ##################
    @app.route('/api/v1.0/emissions')
    def emissions():

        return(
            f'<h1>Greenhouse Gas Emissions by Country</h1>'
        )


if __name__ == "__main__":
    app.run(debug=True)
