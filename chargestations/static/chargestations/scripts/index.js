/* chargestations/static/scripts/index.js */

/* set footer for contributors */
const copy       = "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
/* set url for background */
const tiles_url  = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
/* create baselayer from tiles url and contribution footer */
const base_layer = L.tileLayer(tiles_url, { attribution: copy });
/* define map */
const map        = L.map("map", { layers: [base_layer] });

/* set map center and zoom */
map.locate()
  /* centerlocation from ip */
  .on("locationfound", (e) => map.setView(e.latlng, 14))
  /* default centerlocation */
  .on("locationerror", () => map.setView([41.51, -72.7], 8));

// convert json text object to JSON dataobject to use data in javascript
let stations = JSON.parse(document.getElementById('stations_json').textContent)

// add marker for each station
stations.forEach(station => {
  L.marker([station.latitude, station.longitude])
  .addTo(map)
  .bindPopup('Station<br>' + station.station_name)
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