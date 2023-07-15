# Django Map Display

This is a web application built with Django that allows users to display an interactive map, place markers, and add notes to the markers.

## Features

- Interactive Map: Users can pan and zoom to different locations worldwide on the main page.
- Marker Placement: Users can place markers on the map by clicking on a location.
- Note Addition: Users can add notes to markers by entering text in a text box that pops up when a marker is placed or clicked.
- Marker and Note Persistence: Markers and their associated notes are saved and will still appear if the page is refreshed or visited later.
- Viewing Notes: Users can view the note associated with a marker by clicking on the marker.
- Marker Deletion: Users can delete markers, which will also delete the associated note.
- User-Friendly Interface: The application is designed to be intuitive and user-friendly.

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/your-username/django-map-display.git
   ```

2. Change to the project directory:

   ```shell
   cd django-map-display
   ```

3. Install the project dependencies using `pip`:

   ```shell
   pip install -r requirements.txt
   ```

4. Apply the database migrations:

   ```shell
   python manage.py migrate
   ```

## Usage

1. Run the Django development server:

   ```shell
   python manage.py runserver
   ```

2. Open a web browser and visit `http://127.0.0.1:8000/` or `http://localhost:8000/` to access the application.

3. Use the interactive map to pan and zoom to different locations worldwide.

4. To place a marker, click on the desired location on the map. A note text box will pop up. Enter a note and click "Save" to add the marker.

5. To view the note associated with a marker, click on the marker.

6. To delete a marker and its associated note, click on the marker and click the "Delete" button.

