# Please install python packages pycurl, homora and sentinelsat
# The download from Scihub will fail if the server certificate cannot be verified because no default CA bundle is defined, as on Windows, or when the CA bundle is outdated. In most cases the easiest solution is to install or update `certifi <https: pypi.python.org="" pypi="" certifi="">`_: for example with 'pip install -U certifi'

from MySentinelAPI import MySentinelAPI, all_in_one
from datetime import datetime, date

"""
default settings
-------------------------
all_in_one(user, password, area, api_url='https://scihub.copernicus.eu/dhus', path='.', download='no', initial_date=None, end_date=datetime.now(),**keywords)

Wildcards for restricting search query (keywords)
-----------------------------------------------------------------
* = any sequence of zero or more characters
? = any one character

needed keywords
------------------------
user : username of Sentinel Scientific Data Hub account (e.g. 'mustermann')
password : password of Sentinel Scientific Data Hub account (e.g. '12345')
area : area of interest
    input of coordinates (e.g. 'latmin, latmax, lonmin, lonmax') or
    input of geojson-file with coordinates of a polygon (e.g. 'coordinates.geojson')
api_url: url of Sentinel Scientific Data Hub
path: path where to store the data
initial_date (date when data was taken): start date of the query (e.g. '20160101'; datetime(2016, 1, 1, 12, 5); date(2016,1,1))
end_date (date when data was taken): end date of the query (e.g. '20160102'; datetime(2016, 1, 2, 12, 5); date(2016,1,2))
download :
    'no' only query but no download of the data (default setting)
    'yes' query and download all results of the query

additional keywords Sentinel 1 and 2
--------------------------------------------------
platformname: e.g. 'Sentinel-1'; 'Sentinel-2'; 'Sentinel-1 OR Sentinel-2'
filename: e.g 'S1A_EW*'; 'S1A_EW_GRDH_1SDH_20141003T003840_20141003T003920_002658_002F54_4DD1'; '*1SD?_20141003T003840*'
orbitnumber: e.g. '20'; '[1020 TO 1021]'
orbitdirection: e.g. 'ascending'; 'decending'
producttype: e.g. 'SLC'; 'GRD'; 'OCN'; 'RAW'; 'SLC OR GRD'; ...
relativeorbitnumber: e.g. '20'; '[1020 TO 1021]'
sensoroperationalmode: e.g. 'SM'; 'IW'; 'EW'; 'SM OR IW'; ...

additional keywords Sentinel 1 only
-----------------------------------------------
lastorbitnumber: e.g. '20'; '[1020 TO 1021]'
polarisationmode: e.g. 'HH'; 'VV'; 'HV'; 'VH'; 'HH HV'; 'VV VH'; 'HH OR VV VH'; ...
lastrelativeorbitnumber: e.g. '20'; '[1020 TO 1021]'
swathidentifier: e.g. 'S1', 'IW1', 'EW4', 'S1 OR S2 OR S3', 'S? NOT S1'

additional keywords Sentinel 2 only
-----------------------------------------------
cloudcoverpercentage: e.g. '[0 TO 40]'

for possible values and probably more parameters please visit
https://scihub.copernicus.eu/twiki/do/view/SciHubUserGuide/3FullTextSearch#Search_Keywords
"""

print(datetime.now())

# needed keywords
user = 'xxx'
password = 'xxx'
area = '../coordinates_test_sites/capitanata.geojson'
api_url = 'https://scihub.copernicus.eu/apihub/'
path = '/media/nas_data/Thomas/Sentinel_1_data/foggia_italy'
date = ('20170101', '20171231')
download = 'yes'

# additional keywords Sentinel 1 and 2
platformname = 'Sentinel-1'
filename = '*'
orbitnumber = '*'
orbitdirection = '*'
producttype = 'SLC'
relativeorbitnumber = '*'
sensoroperationalmode = '*'

# additional keywords Sentinel 1 only
lastorbitnumber = '*'
polarisationmode = '*'
lastrelativeorbitnumber = '*'
swathidentifier = '*'

# additional keywords Sentinel 2 only
cloudcoverpercentage = '*'

# other additional keywords
show_progressbars = True

result_sentinel1, check_files, check_dic = all_in_one(user, password, area=area, api_url=api_url, show_progressbars=show_progressbars, path=path, date=date, download=download, platformname=platformname, filename=filename, orbitnumber=orbitnumber, lastorbitnumber=lastorbitnumber, orbitdirection=orbitdirection, polarisationmode=polarisationmode, producttype=producttype, relativeorbitnumber=relativeorbitnumber, lastrelativeorbitnumber=lastrelativeorbitnumber, sensoroperationalmode=sensoroperationalmode, swathidentifier=swathidentifier)

# result_sentinel2, check_files2 = all_in_one(user, password, area=area, api_url=api_url, show_progressbars=show_progressbars, path=path, date=date, download=download, platformname=platformname, filename=filename, orbitnumber=orbitnumber, orbitdirection=orbitdirection, producttype=producttype, relativeorbitnumber=relativeorbitnumber, sensoroperationalmode=sensoroperationalmode, cloudcoverpercentage=cloudcoverpercentage)

print(datetime.now())





