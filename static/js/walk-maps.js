
let maps;

function initMap() {

    // Haymarket Maps //

    haymarket_park_map = new google.maps.Map(document.getElementById("haymarket_park_map"), {
        center: { lat: 55.94182203172515, lng: -3.1961244593145115 },
        zoom: 15,
    });
    haymarket_city_map = new google.maps.Map(document.getElementById("haymarket_city_map"), {
        center: { lat: 55.95038584310472, lng: -3.227426190397426 },
        zoom: 15,
    });

    // Leith Maps // 

    leith_park_map = new google.maps.Map(document.getElementById("leith_park_map"), {
        center: { lat: 55.97518293123383, lng: -3.193479546274399 },
        zoom: 15,
    });
    leith_city_map = new google.maps.Map(document.getElementById("leith_city_map"), {
        center: { lat: 55.972418581703884, lng: -3.1993879089088795 },
        zoom: 15,
    });
    leith_beach_map = new google.maps.Map(document.getElementById("leith_beach_map"), {
        center: { lat: 55.979918904200666, lng: -3.2818102128858313 },
        zoom: 15,
    });

    // Morningside Maps // 

    morningside_park_map = new google.maps.Map(document.getElementById("morningside_park_map"), {
        center: { lat: 55.934184655162674, lng: -3.225700635388955 },
        zoom: 15,
    });
    morningside_city_map = new google.maps.Map(document.getElementById("morningside_city_map"), {
        center: { lat: 55.93051200385491, lng: -3.2099003053588286 },
        zoom: 15,
    });

    // New Town Maps // 

    new_town_park_map = new google.maps.Map(document.getElementById("new_town_park_map"), {
        center: { lat: 55.955137465193744, lng: -3.199761587950736 },
        zoom: 15,
    });
    new_town_city_map = new google.maps.Map(document.getElementById("new_town_city_map"), {
        center: { lat: 55.956220269174814, lng: -3.190570628836145 },
        zoom: 15,
    });

    // Stockbridge Maps // 

    stockbridge_park_map = new google.maps.Map(document.getElementById("stockbridge_park_map"), {
        center: { lat: 55.96339313049672, lng: -3.217796504437263 },
        zoom: 15,
    });
    stockbridge_city_map = new google.maps.Map(document.getElementById("stockbridge_city_map"), {
        center: { lat: 55.95925791642962, lng: -3.2127291423277105 },
        zoom: 15,
    });
    stockbridge_beach_map = new google.maps.Map(document.getElementById("stockbridge_beach_map"), {
        center: { lat: 55.981145109325006, lng: -3.1960934400215373 },
        zoom: 15,
    });

}

var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  var locations = [
    { lat: 55.981145109325006, lng: -3.1960934400215373 }];

    var markers = locations.map(function (location, i) {
    return new google.maps.Marker({
      position: location,
      label: labels[i % labels.length],
    });
  });

  var markerCluster = new MarkerClusterer(stockbridge_beach_map, markers, {
    imagePath:
      "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m",
  });
