/* chargestations/static/scripts/index.js */

// Initialize the map
var map = L.map('map').setView([41.51, -72.7], 8);

// add openstreetmap layer
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// convert json text object to JSON dataobject to use data in javascript
let stations = JSON.parse(document.getElementById('stations_json').textContent)

// add marker for each station
stations.forEach(station => {
  L.marker([station.latitude, station.longitude])
  .addTo(map)
  .bindPopup('I am a<br> Chargestation.')
})

// double click op the map
map.on('dblclick', (event) =>{
  //console.log(event.latlng)
  let lat = event.latlng.lat
  let lng = event.latlng.lng
  L.marker([lat, lng]).addTo(map)
  fetch(`/chargestations/get-nearest-station?latitude=${lat}&longitude=${lng}`).then(response => response.json()).then(result => {
    //console.log(result)
    station_coordinates = result.coordinates
    user_coordinates    = [lat, lng]
    // draw line between user location and nearest station
    let polyline = L.polyline([user_coordinates, station_coordinates]).addTo(map)
    // show popup at userlocation showing distance to nearest station
    var popup = L.popup()
    .setLatLng(user_coordinates)
    .setContent(`<p>Nearest station is ${result.distance.toFixed(2)} km away</p>`)
    .openOn(map);
  })
})