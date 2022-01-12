
d3.json("http://127.0.0.1:5000/api/v1.0/countries").then((countries) => {

    console.log(countries)

    countries.forEach((country) => {
        d3.select("#selCountry").append("option").text(country);
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
    create_gdp_line_chart(countryVal, yearRangeVal)

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
// }