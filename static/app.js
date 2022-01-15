d3.json("http://127.0.0.1:5000/api/v1.0/countries").then((countries) => {

    console.log(countries)

    countries.forEach((country) => {
        d3.select("#selCountry").append("option").text(country);
    });
});

d3.json("http://127.0.0.1:5000/api/v1.0/countries2").then((countries2) => {

    console.log(countries2)

    countries2.forEach((country2) => {
        d3.select("#selCountry2").append("option").text(country2);
    });
});

d3.json("http://127.0.0.1:5000/api/v1.0/groupings").then((yearRanges) => {

    console.log(yearRanges)

    yearRanges.forEach((range) => {
        d3.select("#selYear").append("option").text(range);
    });
});

init();

function init(){
    
    // Set default values on inital load
    let countryVal = "Algeria";
    let yearRangeVal = "1965-1975"

    
    // Create the GDP line chart
    create_gdp_line_chart(countryVal, yearRangeVal);
    create_emission_line_chart(countryVal, yearRangeVal);
    create_allEmissions_line_chart(countryVal);
    create_allConsumption_line_chart(countryVal);

    // create the bar charts
    create_prod_bar_chart(countryVal, yearRangeVal);
    create_cons_bar_chart(countryVal, yearRangeVal);
}

function create_prod_bar_chart(countryVal, yearRangeVal){

    url = `http://127.0.0.1:5000/api/v1.0/production/${countryVal}/${yearRangeVal}`

    //Make an api call to get the GDP for the selected country
   
    d3.json(url).then((prod) => {

    var trace1 = {
        x: prod[0],
        y: prod[1],
        type: 'bar'
    };
    
    var data = [trace1];

    var layout = {
        // title: `GDP for ${countryVal} for the years ${yearRangeVal}`,
        title: `Fuel Production over 10 year period`,
        width: 600,
        xaxis: {
            title: 'Year',
            showgrid: false,
            zeroline: false
        },
        yaxis: {
            title: 'Exajoules',
            showline: false
        }
    };
    
    Plotly.newPlot('fuel-prod-bar', data, layout);
});

}

function create_cons_bar_chart(countryVal, yearRangeVal){

    url = `http://127.0.0.1:5000/api/v1.0/fuel_cons/${countryVal}/${yearRangeVal}`

    //Make an api call to get the GDP for the selected country
   
    d3.json(url).then((cons) => {

    var trace1 = {
        x: cons[0],
        y: cons[1],
        type: 'bar'
    };
    
    var data = [trace1];

    var layout = {
        // title: `GDP for ${countryVal} for the years ${yearRangeVal}`,
        title: `Fuel Consumption over 10 year period`,
        width: 600,
        xaxis: {
            title: 'Year',
            showgrid: false,
            zeroline: false
        },
        yaxis: {
            title: 'Exajoules',
            showline: false
        }
    };
    
    Plotly.newPlot('fuel-cons-bar', data, layout);
});

}

function create_gdp_line_chart(countryVal, yearRangeVal){

    url = `http://127.0.0.1:5000/api/v1.0/gdp/${countryVal}/${yearRangeVal}`

    //Make an api call to get the GDP for the selected country
   
    d3.json(url).then((gdp) => {
    var trace1 = {
        x: gdp[0],
        y: gdp[1],
        type: 'lines',
        ine: {
            color: 'rgb(55, 128, 191)',
            width: 2
        }
    };
    
    var data = [trace1];

    var layout = {
        // title: `GDP for ${countryVal} for the years ${yearRangeVal}`,
        title: `GDP over 10 year period`,
        width: 600,
        xaxis: {
            title: 'Year',
            showgrid: false,
            zeroline: false
        },
        yaxis: {
            title: 'Billions (US$)',
            showline: false
        }
    };
    
    Plotly.newPlot('gdp-line', data, layout);
});

}

function create_emission_line_chart(countryVal, yearRangeVal){

    url = `http://127.0.0.1:5000/api/v1.0/emissions/${countryVal}/${yearRangeVal}`

    //Make an api call to get the GDP for the selected country
   
    d3.json(url).then((emission) => {
    var trace1 = {
        x: emission[0],
        y: emission[1],
        type: 'lines',
        ine: {
            color: 'rgb(55, 128, 191)',
            width: 2
        }
    };
    
    var data = [trace1];

    var layout = {
        // title: `Emission for ${countryVal} for the years ${yearRangeVal}`,
        title: `CO2 Emissions over 10 year period`,
        width: 600,
        xaxis: {
            title: 'Year',
            showgrid: false,
            zeroline: false
        },
        yaxis: {
            title: 'Metric Tonnes',
            showline: false
        }
    };
    
    Plotly.newPlot('co2-line', data, layout);
});

}

function create_allEmissions_line_chart(countryVal){

    url = `http://127.0.0.1:5000/api/v1.0/allYears/emissions/${countryVal}`

    //Make an api call to get the GDP for the selected country
   
    d3.json(url).then((allEmissions) => {
    var trace1 = {
        x: allEmissions[0],
        y: allEmissions[1],
        type: 'lines',
        line: {
            color: 'rgb(55, 128, 191)',
            width: 2
        }
    };
    
    var data = [trace1];

    var layout = {
        title: `Emissions for ${countryVal} since 1965`,
        autosize: false,
        width: 1200,
        height: 400,
        xaxis: {
            title: 'Year',
            showgrid: false,
            zeroline: false
        },
        yaxis: {
            title: 'Metric Tons',
            showline: false
        }
    };
    
    Plotly.newPlot('allEmissions-line', data, layout);
});

}

function create_allConsumption_line_chart(countryVal){

    url = `http://127.0.0.1:5000/api/v1.0/allYears/consumption/${countryVal}`

    //Make an api call to get the GDP for the selected country
   
    d3.json(url).then((Cons) => {
        var oil = {
            x: Cons[0],
            y: Cons[1],
            name: 'oil',
            type: 'lines',
            line: {width: 2}
        };

        var gas = {
            x: Cons[2],
            y: Cons[3],
            name: 'gas',
            type: 'lines',
            line: {width: 2}
        };

        var coal = {
            x: Cons[4],
            y: Cons[5],
            name: 'coal',
            type: 'lines',
            line: {width: 2}
        }; 

        var ethanol = {
            x: Cons[6],
            y: Cons[7],
            name: 'ethanol',
            type: 'lines',
            line: {width: 2}
        }; 

        var biofuels = {
            x: Cons[8],
            y: Cons[9],
            name: 'biofuels',
            type: 'lines',
            line: {width: 2}
        }; 

        var biodiesel = {
            x: Cons[10],
            y: Cons[11],
            name: 'biodiesel',
            type: 'lines',
            line: {width: 2}
        };        

    var data = [oil, gas, coal, ethanol, biofuels, biodiesel];

    var layout = {
        title: `Consumption for ${countryVal} since 1965`,
        autosize: false,
        width: 1200,
        height: 400,       
        xaxis: {
            title: 'Year',
            showgrid: false,
            zeroline: false
        },
        yaxis: {
            title: 'Exajoules',
            showline: false
        }
    };
    
    Plotly.newPlot('allConsumption-line', data, layout);
});

}

function countryOptionChanged(countrySelected){
    // Get the year range
    let selYear = document.getElementById("selYear");
    let yearRangeVal  = selYear.options[selYear.selectedIndex].value;
    restyle(countrySelected, yearRangeVal);

}

function countryOptionChanged2(countrySelected2){
    create_allEmissions_line_chart(countrySelected2); 
    create_allConsumption_line_chart(countrySelected2);   
}

function yearsOptionChanged(yearRangeVal){
    // Get the year range
    let selCountry = document.getElementById("selCountry");
    let countrySelected  = selCountry.options[selCountry.selectedIndex].value;
    restyle(countrySelected, yearRangeVal);
}

function restyle(countrySelected, yearRangeVal){
    let gdpUrl = `http://127.0.0.1:5000/api/v1.0/gdp/${countrySelected}/${yearRangeVal}`;
    let prodUrl = `http://127.0.0.1:5000/api/v1.0/production/${countrySelected}/${yearRangeVal}`;
    let consUrl = `http://127.0.0.1:5000/api/v1.0/fuel_cons/${countrySelected}/${yearRangeVal}`;
    let emUrl = `http://127.0.0.1:5000/api/v1.0/emissions/${countrySelected}/${yearRangeVal}`;
    
    //Make an api call to get the GDP for the selected country
    d3.json(gdpUrl).then((gdp) => {
        Plotly.restyle("gdp-line", "x", [gdp[0]])
        Plotly.restyle("gdp-line", "y", [gdp[1]])
    });   

    //Make an api call to get the GDP for the selected country
    d3.json(prodUrl).then((prod) => {
        Plotly.restyle("fuel-prod-bar", "x", [prod[0]])
        Plotly.restyle("fuel-prod-bar", "y", [prod[1]])
    });  

     //Make an api call to get the GDP for the selected country
     d3.json(consUrl).then((cons) => {
        Plotly.restyle("fuel-cons-bar", "x", [cons[0]])
        Plotly.restyle("fuel-cons-bar", "y", [cons[1]])
    });  
    
     //Make an api call to get the GDP for the selected country
     d3.json(emUrl).then((emission) => {
        Plotly.restyle("co2-line", "x", [emission[0]])
        Plotly.restyle("co2-line", "y", [emission[1]])
    });  

}
