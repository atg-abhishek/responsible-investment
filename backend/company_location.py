import urllib.parse, json, urllib.request, urllib
def company_locations(company_name):
    locations = []
    # compnay_name = urllib.quote(company_name)
    # print(company_name)
    params = {'key': 'AIzaSyAfi34BQ1OEkIn0W-kzDl__Php_aVxnb38', 'query': company_name}
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?{}".format(urllib.parse.urlencode(params))
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
        for i in range(len(data['results'])):
            location = data["results"][i]["formatted_address"]
            locations.append(location)
    return locations





