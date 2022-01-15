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
    // Get the selected country from the drop down
    // let selCountry = document.getElementById("selCountry");
    // let countryVal  = selCountry.options[selCountry.selectedIndex].value;

    // // Get the selected Year range from the drop down
    // let selYear = document.getElementById("selYear");
    // let yearRageVal  = selYear.options[selYear.selectedIndex].value;

    
    // Set default values on inital load
    let countryVal = "Algeria";
    let yearRangeVal = "1965-1975"

    
    // Create the GDP line chart
    create_gdp_line_chart(countryVal, yearRangeVal);
    create_emission_line_chart(countryVal, yearRangeVal);
    create_allEmissions_line_chart(countryVal);
    create_allConsumption_line_chart(countryVal);
    create_consumption_bar_chart(countryVal, yearRangeVal);
    create_production_bar_chart(countryVal, yearRangeVal);
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

function create_consumption_bar_chart(countryVal, yearRangeVal){

    url = `http://127.0.0.1:5000/api/v1.0/consumptions/${countryVal}/${yearRangeVal}`

    //Make an api call to get the GDP for the selected country
   
    d3.json(url).then((consumption) => {
        //console.log(consumption)
        //barcolor=['#a86632','#a88332','#a8a232','#FAED00','#00FACC','#FA6800']
    var trace1 = {
        x: consumption[0],
        y: consumption[1],
        //orientation: 'h',
        /*marker :{
            color:['#a86632','#a88332','#a8a232','#FAED00','#00FACC','#FA6800']
        },*/
        type: 'bar',
            };
    
    var data = [trace1];

    var layout = {
        // title: `Emission for ${countryVal} for the years ${yearRangeVal}`,
        title: `Fuel Consumption over 10 year period`,
        //width: 600,
        yaxis:{title:'Exajoules'}
       };
    
    Plotly.newPlot('fuel-cons-bar', data, layout);
});

}


function create_production_bar_chart(countryVal, yearRangeVal){

    url = `http://127.0.0.1:5000/api/v1.0/production/${countryVal}/${yearRangeVal}`

    //Make an api call to get the GDP for the selected country
   
    d3.json(url).then((production) => {
        //console.log(consumption)
        //barcolor=['#a86632','#a88332','#a8a232','#FAED00','#00FACC','#FA6800']
    var trace1 = {
        x: production[0],
        y: production[1],
        //orientation: 'h',
        /*marker :{
            color:['#a86632','#a88332','#a8a232','#FAED00','#00FACC','#FA6800']
        },*/
        type: 'bar',
            };
    
    var data = [trace1];

    var layout = {
        // title: `Emission for ${countryVal} for the years ${yearRangeVal}`,
        title: `Fuel Production over 10 year period`,
        //width: 600,
        yaxis:{title:'Exajoules'}
       };
    
    Plotly.newPlot('fuel-prod-bar', data, layout);
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
    url = `http://127.0.0.1:5000/api/v1.0/gdp/${countrySelected}/${yearRangeVal}`
    
    //Make an api call to get the GDP for the selected country
    d3.json(url).then((gdp) => {
        Plotly.restyle("gdp-line", "x", [gdp[0]])
        Plotly.restyle("gdp-line", "y", [gdp[1]])
        Plotly.restyle("gdp-line", "text", [`GDP for ${countrySelected} for the years ${yearRangeVal}`])
    });   

    create_emission_line_chart(countrySelected,yearRangeVal);
    create_consumption_bar_chart(countrySelected,yearRangeVal);
    create_production_bar_chart(countrySelected,yearRangeVal);
}

function countryOptionChanged2(countrySelected2){
    create_allEmissions_line_chart(countrySelected2); 
    create_allConsumption_line_chart(countrySelected2);   
}

function yearsOptionChanged(yearRangeVal){
    // Get the year range
    let selCountry = document.getElementById("selCountry");
    let countrySelected  = selCountry.options[selCountry.selectedIndex].value;
    url = `http://127.0.0.1:5000/api/v1.0/gdp/${countrySelected}/${yearRangeVal}`
    
    //Make an api call to get the GDP for the selected country
    d3.json(url).then((gdp) => {
        Plotly.restyle("gdp-line", "x", [gdp[0]])
        Plotly.restyle("gdp-line", "y", [gdp[1]])
        Plotly.restyle("gdp-line", "text", [`GDP for ${countrySelected} for the years ${yearRangeVal}`])
    }); 
    
    create_emission_line_chart(countrySelected,yearRangeVal);
    create_consumption_bar_chart(countrySelected,yearRangeVal);
    create_production_bar_chart(countrySelected,yearRangeVal);
  
}


// function get_gdp_data(countryVal, yearRangeVal){

//     url = `http://127.0.0.1:5000/api/v1.0/gdp/${countryVal}/${yearRangeVal}`
//     var data = [];
//     console.log(countryVal);

//     //Make an api call to get the GDP for the selected country
//     d3.json(url).then((gdp) => {
//         console.log(gdp);
//         data = gdp;
//         return data;
//     });