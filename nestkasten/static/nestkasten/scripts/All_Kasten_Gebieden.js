/* nestkasten/static/scripts/All_Kasten_Gebieden.js */

// Initialize the map
var map = L.map('map').setView([52.5, 4.95], 15);

// add openstreetmap layer
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// add marker for each netkast
netkasten.forEach(netkast => {
  L.marker([netkast.latitude, netkast.longitude])
  .addTo(map)
  .bindPopup('Netkast<br>' + netkast.name)
})

// convert json text object to JSON dataobject to use data in javascript
let fourageergebieden = JSON.parse(document.getElementById('fourageergebieden_json').textContent)

// add area for each fourageergebied
fourageergebieden.forEach(fourageergebied => {
  L.polygon(latlngs, {color: 'red'}).addTo(map)
  .addTo(map)
  .bindPopup('Fourageergebied<br>' + fourageergbied.name)
})