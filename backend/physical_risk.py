import company_location as locate
import urllib.parse, json, urllib.request, urllib

def physical_risk_query(location):

    # find the data by location, Query the server
    try:
        params={'text':location, 'maxLocations':'1', 'outSR' :'102100', 'f':'json'}
        url = "http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find?{}".format(urllib.parse.urlencode(params))
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
            # print(data)

    except:
        print('Error in getting data')
        return 0.0

    geometry = data['locations'][0]['feature']['geometry']
    risk_params = {'f': 'json', 'where': '1=1', 'returnGeometry': 'false', 'spatialRel': 'esriSpatialRelIntersects',
              'geometry': geometry, 'geometryType':'esriGeometryPoint', 'inSR': '102100', 'outFields': '*',
              'outSR': '102100'}

    risk_url = "https://gis.wri.org/server/rest/services/Aqueduct/aqueduct_global_2014/MapServer/2/query?{}".format(urllib.parse.urlencode(risk_params))
    print(risk_url)

    try:
        with urllib.request.urlopen(risk_url) as risk_url:
            risk_data = json.loads(risk_url.read().decode())
            # print(risk_data['features'][0])

    except:
        print('Error in getting data')
        return 0.0

    return risk_data['features'][0]['attributes']['BWS_cat']


def get_water_risk(company_name):
    loc_list = locate.company_locations(company_name)
    risk_list = ["1. Low (<10%)", "2. Low to medium (10-20%)", "3. Medium to high (20-40%)", "4. High (40-80%)", "5. Extremely high (>80%)"]
    risks = []
    avg_risk = 0
    for location in loc_list:
        risk = physical_risk_query(location)
        risk_level = risk_list.index(risk)
        avg_risk += risk_level


    return risk_list[int(avg_risk/len(loc_list))]

if __name__ == "__main__":
    print(get_water_risk('Agrium Inc'))

