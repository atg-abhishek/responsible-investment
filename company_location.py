from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'AIzaSyAfi34BQ1OEkIn0W-kzDl__Php_aVxnb38'

google_places = GooglePlaces(YOUR_API_KEY)

# import pudb; pu.db

query_result = google_places.nearby_search(
        location='London, England', keyword='Fish and Chips',
        radius=20000, types=[types.TYPE_FOOD])


