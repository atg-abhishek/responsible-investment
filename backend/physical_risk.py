
import urllib.parse, json, urllib.request, urllib

def physical_risk_query(location):

    # find the data by location, Query the server
    try:
        params={'text':location, 'maxLocations':'1', 'outSR' :'102100', 'f':'json'}
        url = "http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find?{}".format(urllib.parse.urlencode(params))
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
            print(data)

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
            print(risk_data['features'][0])

    except:
        print('Error in getting data')
        return 0.0

    print(risk_data['features'][0]['attributes']['BWS_cat'])
    return risk_data['features'][0]['attributes']['BWS_cat']

if __name__ == "__main__":
    physical_risk_query('Sherbrooke, Quebec, CAN')


