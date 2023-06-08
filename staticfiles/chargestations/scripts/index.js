/* chargestations/static/scripts/index.js */

// Initialize the map
var map = L.map('map').setView([52.5, 4.95], 15);

// add openstreetmap layer
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);