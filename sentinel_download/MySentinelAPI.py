
from sentinelsat.sentinel import SentinelAPI
from sentinelsat import read_geojson, geojson_to_wkt
from datetime import datetime
import pdb
class MySentinelAPI(SentinelAPI):
    def __init__(self, *args, **kwargs):
        super(MySentinelAPI, self).__init__(*args, **kwargs)

    def get_area(self, latmin, latmax, lonmin, lonmax):
        assert latmin <= latmax, 'ERROR: invalid lat'
        assert lonmin <= lonmax, 'ERROR: invalid lon'
        return '%.13f %.13f,%.13f %.13f,%.13f %.13f,%.13f %.13f,%.13f %.13f' % (lonmin, latmin, lonmax, latmin, lonmax, latmax, lonmin, latmax, lonmin, latmin)


def all_in_one(user, password, area, api_url='https://scihub.copernicus.eu/apihub/', show_progressbars=True, path='./', download='no', date=('NOW-1DAY', 'NOW'),  **keywords):

    ### login information Copernicus Open Access Hub (https://scihub.copernicus.eu/dhus/#/home)
    api=MySentinelAPI(user, password, api_url, show_progressbars)

    ### read area information
    try:
        geojson=geojson_to_wkt(read_geojson(area))
    except IOError:
        area=area.split(',')
        area=api.get_area(float(area[0]),float(area[1]),float(area[2]),float(area[3]))
        geojson=area

    ### Sentinel data search
    products = api.query(geojson, date, **keywords)
    # products_df = api.to_dataframe(products)
    print(api._last_query)

    print('{} product results for your query. The products need {} Gb disk space'.format(len(products), api.get_products_size(products)))
    print([i['title'] for i in products if 'title' in i])

    ## check if query results already downloaded to given path
    check_dic = api.check_files(ids=products, directory=path)
    # print(check_dic)

    ### download all query products
    if download == 'yes':
        result = api.download_all(products, directory_path=path, max_attempts=10, checksum=True)
        # print('Downloaded files:')
        # print(result.viewkeys())
        check_files = api.check_files(products)

        return result, check_files, check_dic
    # print(products_df.index.values)
    # return products_df
    # print([i['title'] for i in products if 'title' in i])

    return products, None, check_dic





