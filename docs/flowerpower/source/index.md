---
title: Flower Power API Reference

language_tabs:
  - python: Python
  - shell: nodeJS

toc_footers:
  - <a href='https://apiflowerpower.parrot.com/api_access/signup'>Sign Up for a Developer Key</a>
  - <a href='http://github.com/tripit/slate'>Documentation Powered by Slate</a>

includes:
  - errors

search: true
---

#  Flower Power Cloud API

Welcome to the Flower Power Cloud API !

You can use our API to connect to the Flower Power Cloud, and retrieve your sensors' data from it. 

You can also receive alerts like those in the Flower Power mobile app.

we advise you to use requests package, it can be installed using pip :
pip install requests

```python
  _          _ _             
 | |__   ___| | | ___        
 | 	_ \ / _ \ | |/ _ \       
 | | | |  __/ | | (_) |      
 |_| |_|\___|_|_|\___/     _ 
 __      _____  _ __| | __| |
 \ \ /\ / / _ \|  __| |/ _  |
  \ V  V / (_) | |  | | (_| |
   \_/\_/ \___/|_|  |_|\__,_|
```

```shell
see github repo : 
https://github.com/Parrot-Developers/node-flower-power
https://github.com/Parrot-Developers/node-flower-power-cloud
```

# Authentication

```python
import requests
from pprint import pformat  # here only for aesthetic 

# First we set our credentials
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'

#from the developer portal
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_SECRET'

req = requests.get('https://apiflowerpower.parrot.com/user/v1/authenticate',
                   data={'grant_type': 'password',
                         'username': username,
                         'password': password,
                         'client_id': client_id,
                         'client_secret': client_secret,
                        })
response = req.json()
print('Server response: \n {0}'.format(pformat(response)))

# Get authorization token from response
access_token = response['access_token']
auth_header = {'Authorization': 'Bearer {token}'.format(token=access_token)}

# From now on, we won't need initial credentials: access_token and auth_header will be enough.

```

> This should returns JSON structure:

```json
{
    "access_token": "YOUR_ACCESS_TOKEN_", 
    "expires_in": 2592000, 
    "refresh_token": "YOUR_REFRESH_TOKEN" 
}
```


Flower Power Cloud  uses API keys to allow access to the API. You can register a new API key at our [developer portal](https://apiflowerpower.parrot.com/api_access/signup).


Flower Power Cloud API expects for the 'access_token' and 'auth_header' to be included in all API requests to the server.

### HTTP Request

`GET https://apiflowerpower.parrot.com/user/v1/authenticate`

### Query Parameters

Parameter | Description
--------- | ----------
grant_type  | should be set to ‘password’
username | replace with your username
password | replace with your password
client_id | replace with your client_id from credentials
client_secret | replace with your client_secret from credentials



<aside class="notice">
Be sure to replace values with your own credentials :)
</aside>

# User API

## Get profile

```python

import requests
from pprint import pformat  # here only for aesthetic

# Set your own authentication token
req = requests.get('https://apiflowerpower.parrot.com/user/v4/profile',
                   headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN_'})


response = req.json()
print('Server response: \n {0}'.format(pformat(response)))

```

> This should returns JSON structure:

```json
{
 "errors": [],
 "server_identifier": "YOURS",
 "user_config_version": "YOURS",
 "user_profile": { "dob": "",
                   "email": "YOURS",
                   "ip_address_on_create": "YOURS",
                   "language_iso639": "YOURS",
                   "notification_curfew_end": "YOURS",
                   "notification_curfew_start": "YOURS",
                   "pictures_public": "YOURS",
                   "tmz_offset": "YOURS",
                   "use_fahrenheit": "YOURS",
                   "use_feet_inches": "YOURS",
                   "username": "YOURS"
                  }
}

```

### HTTP Request

`GET https://apiflowerpower.parrot.com/user/v4/profile`

### Query Parameters

No parameters.

## Obtain version info

```python

import requests
from pprint import pformat  # here only for aesthetic

# Set your own authentication token
req = requests.get('https://apiflowerpower.parrot.com/user/v1/versions',
                   headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN_'})


response = req.json()
print('Server response: \n {0}'.format(pformat(response)))
```

> This should returns JSON structure:

```json
{
 "errors": [],
 "garden_status_version": "YOURS",
 "server_identifier": "YOURS",
 "user_config_version": "YOURS"
 }
 ```

### HTTP Request

`GET https://apiflowerpower.parrot.com/user/v1/versions`

### Query Parameters

No parameters.

# Sensor Data API

## Get Samples for Location

```python


import requests
from pprint import pformat  # here only for aesthetic

location_identifier = 'eg9dnEtyHy589153XXX'

# Set your own authentication token
req = requests.get('https://apiflowerpower.parrot.com/sensor_data/v4/sample/location/' + location_identifier, 
    headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN_'},
    params={'from_datetime_utc': '2014-03-01T14:42:42Z',
            'to_datetime_utc': '2014-04-13T06:30:00Z'})

response = req.json()
print('Server response: \n {0}'.format(pformat(response)))
```

> This should returns JSON structure:

```json
 {"errors": [],
  "events": [],
  "fertilizer": [{"fertilizer_level": "YOURS",
                  "id": "YOURS",
                  "watering_cycle_end_date_time_utc": "YOURS",
                  "watering_cycle_start_date_time_utc": "YOURS"}],
 "samples": [{"air_temperature_celsius": "YOURS",
               "capture_ts": "YOURS",
               "par_umole_m2s": "YOURS",
               "vwc_percent": "YOURS"}],
 "server_identifier": "YOURS",
 "user_data_version": "YOURS"
 }
 ```
 
### HTTP Request

`GET https://apiflowerpower.parrot.com/sensor_data/v4/sample/location/:location_identifier`

### Query Parameters

Parameter | Description
--------- | ----------
from_datetime_utc  | UTC datetime start, optional
to_datetime_utc | UTC datetime end, optional
include_acknowledged | returns all open and closed events, optional
resolution | DAILY. from/to mandatory when resolution present. Time components of from/to ignored when resolution present


<aside class="success">
Remember — you need to send access_token’ and ‘auth_header’ withh each Api call.</aside>
<aside class="notice">
The from/to should not exceed 10 days.</aside>

## Obtain Sync Data

```python
import requests
from pprint import pformat  # here only for aesthetic

# Set your own authentication token
req = requests.get('https://apiflowerpower.parrot.com/sensor_data/v3/sync'
                   headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN_'})

response = req.json()
print('Server response: \n {0}'.format(pformat(response)))
```

> This should returns JSON structure:

```json
{
 "errors": [],
 "locations": [{ "avatar_url": "YOURS",
                 "display_order": "YOURS",
                 "ignore_fertilizer_alert": "YOURS",
                 "ignore_light_alert": "YOURS",
                 "ignore_moisture_alert": "YOURS",
                 "ignore_temperature_alert": "YOURS",
                 "images": "YOURS",
                 "in_pot": "YOURS",
                 "is_indoor": "YOURS",
                 "latitude": "YOURS",
                 "location_identifier": "YOURS",
                 "longitude": "YOURS",
                 "plant_assigned_date": "YOURS",
                 "plant_nickname": "YOURS",
                 "sensor_serial": "YOURS"}],
 "sensors": [{ "color": "YOURS",
               "firmware_version": "YOURS",
               "nickname": "YOURS",
               "sensor_serial": "YOURS"}],
 "server_identifier": "YOURS",
 "user_config_version": "YOURS"
 }
 ```
 
### HTTP Request

`GET https://apiflowerpower.parrot.com/sensor_data/v3/sync`

### Query Parameters

Parameter | Description
--------- | ----------
include_s3_urls | Return the locations image urls rather than the "id", optional

## Obtain garden location statuses

```python
import requests
from pprint import pformat  # here only for aesthetic

# Set your own authentication token
req = requests.get('https://apiflowerpower.parrot.com/sensor_data/v4/garden_locations_status',
                   headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN_'})
                   
response = req.json()
print('Server response: \n {0}'.format(pformat(response)))
```

> This should returns JSON structure:

```json
{
 "errors": [],
 "garden_status_version": "YOURS",
 "locations": [{"air_temperature": {"done_action_timedate_utc": "YOURS",
                                      "gauge_values": { "current_value": "YOURS",
                                                        "max_threshold": "YOURS",
                                                        "min_threshold": "YOURS"},
                                      "instruction_key": "YOURS",
                                      "next_analysis_timedate_utc": "YOURS",
                                      "predicted_action_timedate_utc": "YOURS",
                                      "status_key": "YOURS"},
                 "fertilizer": { "done_action_timedate_utc": "YOURS",
                                 "gauge_values": { "current_value": "YOURS",
                                                   "max_threshold": "YOURS",
                                                   "min_threshold": "YOURS"},
                                 "instruction_key": "YOURS",
                                 "next_analysis_timedate_utc": "YOURS",
                                 "predicted_action_timedate_utc": "YOURS",
                                 "status_key": "YOURS"},
                 "first_sample_utc": "YOURS",
                 "global_validity_timedate_utc": "YOURS",
                 "last_processed_upload_timedate_utc": "YOURS",
                 "last_sample_upload": "YOURS",
                 "last_sample_utc": "YOURS",
                 "light": { "done_action_timedate_utc": "YOURS",
                            "gauge_values": { "current_value": "YOURS",
                                              "max_threshold": "YOURS",
                                              "min_threshold": "YOURS"},
                            "instruction_key": "YOURS",
                            "next_analysis_timedate_utc": "YOURS",
                            "predicted_action_timedate_utc": "YOURS",
                            "status_key": "YOURS"},
                 "location_identifier": "YOURS",
                 "processing_uploads": "YOURS",
                 "soil_moisture": { "done_action_timedate_utc": "YOURS",
                                    "gauge_values": { "current_value": "YOURS",
                                                      "max_threshold": "YOURS",
                                                      "min_threshold": "YOURS"},
                                    "instruction_key": "YOURS",
                                    "next_analysis_timedate_utc": "YOURS",
                                    "predicted_action_timedate_utc": "YOURS",
                                    "status_key": "YOURS"},
                 "total_sample_count": "YOURS",
                 "user_sharing": {"first_all_green": {"sharing_status": "YOURS"}}}],
 "sensors": [{"battery_level": {"battery_end_of_life_date_utc": "YOURS",
                                  "level_percent": "YOURS"},
               "current_history_index": "YOURS",
               "last_upload_datetime_utc": "YOURS",
               "processing_uploads": "YOURS",
               "sensor_serial": "YOURS",
               "total_uploaded_samples": "YOURS"}],
 "server_identifier": "YOURS",
 "user_config_version": "YOURS"
 }
 ```
 
### HTTP Request

`GET https://apiflowerpower.parrot.com/v4/gardenlocation_status`

### Query Parameters

No parameters.
