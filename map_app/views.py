from django.shortcuts import render
def map_view(request):
    markers = Marker.objects.all()
    return render(request, 'map.html', {'markers': markers})

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
# Create your views here.
