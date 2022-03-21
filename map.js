// Initialize and add the map
function initMap() {
   //The location of Uluru
  const uluru = { lat: 52.370216, lng: 4.895168 };
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 13,
      center: uluru,
  });

var directionsService = new google.maps.DirectionsService();

//create directions render object for displaying routes

var directionsDisplay = new google.maps.DirectionsRenderer();

// bind the directionsdisplay to map

directionsDisplay.setMap(map);

function calcRoute() {
  var request = {
      origin: document.getElementById("from").value,
      destination: document.getElementById("to").value,
      travelMode: google.maps.TravelMode.WALKING,
      unitSystem: google.maps.UnitSystem.IMPERIAL
  }
}

}







