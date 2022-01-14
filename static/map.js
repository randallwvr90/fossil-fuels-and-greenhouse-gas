init();

function init() {

    d3.json("http://127.0.0.1:5000/api/v1.0/getMappingYears").then((countries) => {

        console.log(countries)

        countries.forEach((country) => {
            d3.select("#selectYear").append("option").text(country);
        });
    });    
    var params = new URLSearchParams(window.location.search);
    var year = params.get("year");

    console.log(year);
    d3.select('#selectYear').node().value = year;

    // let element = document.getElementById('#selectYear');
    // element.value = year;

    load_map(year);

}

function load_map(yr){
    var myGeoJSONPath = '/api/low_res_world';
    
    var emissionsJSONPath = `/api/v1.0/get_global_emissions/${yr}`;
    console.log(emissionsJSONPath);

    $.getJSON(myGeoJSONPath,function(data){
        var map = L.map('map').setView([30, 0], 2);
        // Getting our GeoJSON data
        d3.json(emissionsJSONPath).then(function(data2) {
            // Creating a GeoJSON layer with the retrieved data
            L.geoJson(data, {
                style: function(feature) {
                    return {
                        color: "white",
                        // Call the chooseColor() function to decide which color to color our neighborhood. (The color is based on the borough.)
                        fillColor: chooseColor(data2, feature.properties.iso_n3),
                        fillOpacity: 0.5,
                        weight: 1.5
                    };
                },
            }).addTo(map);
        });
    }); 
}


function yearChanged(selYear){
    var url = `/api/v1.0/emissions_map?year=${selYear}`;
    location.href = url;
    // document.getElementById('emissionsMap').innerHTML = "<div id='map' style='width: 100%; height: 100%;'></div>";
    // load_map(selYear);
}

// The function that will determine the color of a neighborhood based on the borough that it belongs to
function chooseColor(data2, countryCode) {
    emissions = getEmissions(data2, countryCode);
    if (emissions > 5000) return "#a60202";
    else if (emissions > 4000) return "#FC0303";
    else if (emissions > 3500) return "#FA6800";
    else if (emissions > 3000) return "#FAB700";
    else if (emissions > 2500) return "#FAED00";
    else if (emissions > 2000) return "#ABFA00";
    else if (emissions > 1500) return "#00FA0C";
    else if (emissions > 1000) return "#00FACC";
    else if (emissions > 500) return "#00CCFA";
    else if (emissions >= 0) return "#0008fa";
    else return "white";
}
function getEmissions(data2, countryCode) {
    for (let i=0; i<data2.length; i++) {
        if (data2[i][1] == countryCode) {
            return data2[i][0]
        }
    }
}
