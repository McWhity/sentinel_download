
from sentinelsat.sentinel import SentinelAPI
from sentinelsat import read_geojson, geojson_to_wkt
from datetime import datetime

class MySentinelAPI(SentinelAPI):
    def __init__(self, *args, **kwargs):
        SentinelAPI.__init__(self, *args, **kwargs)
        # super(MySentinelAPI, self).__init__(*args, **kwargs)

    def get_area(self, latmin, latmax, lonmin, lonmax):
        assert latmin <= latmax, 'ERROR: invalid lat'
        assert lonmin <= lonmax, 'ERROR: invalid lon'
        return '%.13f %.13f,%.13f %.13f,%.13f %.13f,%.13f %.13f,%.13f %.13f' % (lonmin, latmin, lonmax, latmin, lonmax, latmax, lonmin, latmax, lonmin, latmin)


def all_in_one(user, password, area, api_url='https://scihub.copernicus.eu/apihub/', show_progressbars=True, path='./', download='no', check_if_already_downloaded='yes', date=('NOW-1DAY', 'NOW'),  **keywords):

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
    print(api._last_query)

    print('{} product results for your query. The products need {} Gb disk space'.format(len(products), api.get_products_size(products)))
    products_df = api.to_dataframe(products)
    print(products_df.title.values)

    ## check if query results already downloaded to given path
    if check_if_already_downloaded == 'yes':
        check_dic = api.check_files(ids=products, directory=path)
    else:
        check_dic = 'not applied'

    ### download all query products
    if download == 'yes':
        result = api.download_all(products, directory_path=path, max_attempts=10, checksum=True)

        check_files = api.check_files(products)

        successful_downloaded = api.to_dataframe(result[0])
        successful_triggered_retrieval = api.to_dataframe(result[1])

        return result, check_files, check_dic, successful_downloaded, successful_triggered_retrieval

    return products_df, None, check_dic





