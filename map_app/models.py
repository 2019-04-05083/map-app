from django.db import models
class Marker(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    note = models.TextField()

    def __str__(self):
        return f"Marker ({self.latitude}, {self.longitude})"

Run the following commands to create the necessary database tables:

shell

python manage.py makemigrations
python manage.py migrate

Step 4: Create views and templates
Create a new file map_app/views.py and define the necessary view functions:

python

from django.shortcuts import render

def map_view(request):
    return render(request, 'map.html')

def add_marker(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        note = request.POST.get('note')

        Marker.objects.create(latitude=latitude, longitude=longitude, note=note)
    
    return HttpResponse()

def get_markers(request):
    markers = Marker.objects.all()
    data = [{'latitude': marker.latitude, 'longitude': marker.longitude, 'note': marker.note} for marker in markers]
    return JsonResponse(data, safe=False)

def delete_marker(request, marker_id):
    marker = Marker.objects.get(id=marker_id)
    marker.delete()
    return HttpResponse()

Create HTML templates in the map_app/templates directory for each view. For example, create a map.html template:

html

<!DOCTYPE html>
<html>
<head>
    <title>Map Display</title>
    <!-- Include necessary CSS and JavaScript libraries -->
</head>
<body>
    <div id="map"></div>
    <script>
        // Include JavaScript code for map interaction and AJAX requests
    </script>
</body>
</html>

Step 5: Set up URLs and routing
Open the map_display/urls.py file and add URL patterns for the map app views:

python

from django.urls import include, path

urlpatterns = [
    ...
    path('', include('map_app.urls')),
]

Create a new file map_app/urls.py and define the URLs and corresponding view functions:

python

from django.urls import path
from map_app import views

app_name = 'map_app'

urlpatterns = [
    path('', views.map_view, name='map_view'),
    path('add_marker/', views.add_marker, name='add_marker'),
    path('get_markers/', views.get_markers, name='get_markers'),
    path('delete_marker/<int:marker_id>/', views.delete_marker, name='delete_marker'),
]

Step 6: Implement the frontend
#Add the necessary CSS and JavaScript libraries to the map.html template. You can use Leaflet.js as an example. Here's a simplified version of the JavaScript code:

html

<!DOCTYPE html>
<html>
<head>
    <title>Map Display</title>
    <!-- Include necessary CSS and JavaScript libraries -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
</head>
<body>
    <div id="map" style="height: 500px;"></div>
    <script>
        // Create the map
        var map = L.map('map').setView([0, 0], 2);

        // Add a tile layer (e.g., OpenStreetMap)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Handle marker placement
        map.on('click', function (event) {
            var latitude = event.latlng.lat.toFixed(6);
            var longitude = event.latlng.lng.toFixed(6);
            var note = prompt('Enter a note for this marker:');
            
            // Send AJAX request to add the marker
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/add_marker/', true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    // Marker added successfully
                    // Refresh the markers on the map
                    refreshMarkers();
                }
            };
            xhr.send('latitude=' + latitude + '&longitude=' + longitude + '&note=' + note);
        });

        // Function to refresh markers on the map
        function refreshMarkers() {
            // Remove existing markers from the map
            // ...

            // Fetch markers from the server
            var xhr = new XMLHttpRequest();
            xhr.open('GET', '/get_markers/', true);
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    var markers = JSON.parse(xhr.responseText);
                    // Iterate over markers and add them to the map
                    // ...
                }
            };
            xhr.send();
        }

        // Call the refreshMarkers function initially to load existing markers
        refreshMarkers();
    </script>
</body>
</html>

Step 7: Integrate local storage or a backend service
To store markers and notes in the database, we have already implemented the necessary view functions (add_marker, get_markers, delete_marker). The Marker model takes care of the database storage.

Step 8: Ensure persistence
In the map_app/views.py file, modify the map_view function to fetch existing markers and pass them to the template:

python

def map_view(request):
    markers = Marker.objects.all()
    return render(request, 'map.html', {'markers': markers})

Update the map.html template to display the existing markers on the map using JavaScript:

javascript

// ...

// Function to refresh markers on the map
function refreshMarkers() {
    // Remove existing markers from the map
    map.eachLayer(function (layer) {
        if (layer instanceof L.Marker) {
            map.removeLayer(layer);
        }
    });

    // Fetch markers from the server
    // ...
    
    // Iterate over markers and add them to the map
    markers.forEach(function (marker) {
        var latitude = marker.latitude;
        var longitude = marker.longitude;
        var note = marker.note;
        
        var marker = L.marker([latitude, longitude]).addTo(map);
       


# Create your models here.
