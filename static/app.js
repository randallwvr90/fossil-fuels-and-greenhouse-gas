
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

    let countryVal = "Algeria";
    let yearRangeVal = "2005-2015"

    // Build the url for the api

    url = `http://127.0.0.1:5000/api/v1.0/gdp/${countryVal}/${yearRangeVal}`

    //Make an api call to get the GDP for the selected country
    d3.json(url).then((gdp) => {

    plot_gdp_line_chart(gdp)

    });

}

function plot_gdp_line_chart(gdp){

    var trace1 = {
        x: gdp[0],
        y: gdp[1],
        type: 'scatter'
      };
      
      var data = [trace1];
      
      Plotly.newPlot('gdp-line', data);

}