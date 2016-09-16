---
title: Flower Power API Reference

language_tabs:
  - python: Python
  - shell: nodeJS

toc_footers:
  - <a href='https://api-flower-power-pot.parrot.com/api_access/signup'>Sign Up for a Developer Key</a>
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

# From the developer portal
client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'

req = requests.get('https://api-flower-power-pot.parrot.com/user/v1/authenticate',
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
    "expires_in": 172800,
    "import_status": "unavailable",
    "refresh_token": "YOUR_REFRESH_TOKEN"
}
```


Flower Power Cloud  uses API keys to allow access to the API. You can register a new API key at our [developer portal](https://api-flower-power-pot.parrot.com/api_access/signup)


Flower Power Cloud API expects for the 'access_token' and 'auth_header' to be included in all API requests to the server.

### HTTP Request

`GET https://api-flower-power-pot.parrot.com/user/v1/authenticate`

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
req = requests.get('https://api-flower-power-pot.parrot.com/user/v4/profile',
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
 "user_config_version": "YOURS",
 "user_profile": {"email": "YOURS",
                  "language_iso639": "YOURS",
                  "notification_curfew_end": "YOURS",
                  "notification_curfew_start": "YOURS",
                  "pictures_public": "YOURS",
                  "use_fahrenheit": "YOURS",
                  "use_feet_inches": "YOURS",
                  "use_ftc": "YOURS",
                  "use_liter": "YOURS",
                  "use_lux": "YOURS",
                  "use_mol": "YOURS",
                  "utc_timezone": "YOURS"}
}

```

### HTTP Request

`GET https://api-flower-power-pot.parrot.com/user/v4/profile`

### Query Parameters

No parameters.

## Obtain version info

```python

import requests
from pprint import pformat  # here only for aesthetic

# Set your own authentication token
req = requests.get('https://api-flower-power-pot.parrot.com/user/v1/versions',
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

`GET https://api-flower-power-pot.parrot.com/user/v1/versions`

### Query Parameters

No parameters.

# Sensor Data API

## Get Samples for Location

```python


import requests
from pprint import pformat  # here only for aesthetic

location_identifier = 'eg9dnEtyHy589153XXX'

# Set your own authentication token
req = requests.get('https://api-flower-power-pot.parrot.com/sensor_data/v6/sample/location/' + location_identifier, 
    headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN_'},
    params={'from_datetime_utc': '2014-03-01T14:42:42Z',
            'to_datetime_utc': '2014-04-13T06:30:00Z'})

response = req.json()
print('Server response: \n {0}'.format(pformat(response)))
```

> This should returns JSON structure:

```json
 {"samples":[{ "capture_datetime_utc": "YOURS",
               "light": "YOURS",
               "fertilizer_level": "YOURS",
               "air_temperature_celsius": "YOURS",
               "soil_moisture_percent": "YOURS",
               "battery_percent": "YOURS",
               "water_tank_level_percent": "YOURS"
             }],
 "watering_events": "YOURS",
 "first_not_definitive_value_datetime_utc": "YOURS",
 "user_config_version": "YOURS",
 "garden_status_version": "YOURS",
 "errors": "YOURS",
 "server_identifier": "YOURS"
 }
 ```

### HTTP Request

`GET https://api-flower-power-pot.parrot.com/sensor_data/v6/sample/location/:location_identifier`

### Query Parameters

Parameter | Description
--------- | ----------
from_datetime_utc  | UTC datetime start, optional
to_datetime_utc | UTC datetime end, optional


<aside class="success">
Remember — you need to send access_token’ and ‘auth_header’ withh each Api call.</aside>
<aside class="notice">
The from/to should not exceed 10 days.</aside>

## Obtain Sync Data

```python
import requests
from pprint import pformat  # here only for aesthetic

# Set your own authentication token
req = requests.get('https://api-flower-power-pot.parrot.com/garden/v2/configuration',
                   headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN_'})

response = req.json()
print('Server response: \n {0}'.format(pformat(response)))
```

> This should returns JSON structure:

```json
{
  "locations": [
    {
      "sensor": {
        "firmware_version": "YOURS",
        "system_id": "YOURS",
        "sensor_identifier": "YOURS",
        "color": "YOURS",
        "hardware_revision": "YOURS",
        "calibration_data": "YOURS",
        "sensor_type": "YOURS",
        "nickname": "YOURS",
        "assignment_datetime_utc": "YOURS",
        "autowatering_cfg": {
          "mode": "YOURS"
        }
      },
      "plant_nickname": "YOURS",
      "plant_ids": [
       "YOURS"
      ],
      "plant_assigned_datetime_utc": "YOURS",
      "ignored_alerts": { "watering": "YOURS" },
      "in_pot": "YOURS",
      "is_indoor": "YOURS",
      "location_identifier": "YOURS",
      "longitude": "YOURS",
      "latitude": "YOURS",
      "avatar_url": "YOURS",
      "pictures": [
        {
          "url": "YOURS",
          "location_identifier": "YOURS",
          "image_identifier": "YOURS",
          "expires": "YOURS"
        },
        {
          "url": "YOURS",
          "location_identifier": "YOURS",
          "image_identifier": "YOURS",
          "expires": "YOURS"
        }
      ]
    }
  ],
  "user_config_version": "YOURS",
  "garden_status_version": "YOURS",
  "errors": [],
  "server_identifier": "YOURS"
}
 ```

### HTTP Request

`GET https://api-flower-power-pot.parrot.com/garden/v2/configuration`

### Query Parameters

Parameter | Description
--------- | ----------
include_s3_urls | Return the locations image urls rather than the "id", optional

## Obtain garden location statuses

```python
import requests
from pprint import pformat  # here only for aesthetic

# Set your own authentication token
req = requests.get('https://api-flower-power-pot.parrot.com/garden/v1/status',
                   headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN_'})

response = req.json()
print('Server response: \n {0}'.format(pformat(response)))
```

> This should returns JSON structure:

```json
{
    "locations": [
      {
        "location_identifier": "YOURS",
        "last_processed_upload_datetime_utc": "YOURS",
        "total_sample_count": "YOURS",
        "last_sample_upload": "YOURS",
        "first_sample_utc": "YOURS",
        "last_sample_utc": "YOURS",
        "growth_day": "YOURS",
        "global_validity_datetime_utc": "YOURS",
        "air_temperature": {
          "status_key": "YOURS",
          "instruction_key": "YOURS",
          "next_analysis_datetime_utc": "YOURS",
          "predicted_action_datetime_utc": "YOURS",
          "done_action_datetime_utc": "YOURS",
          "gauge_values": {
            "min_threshold": "YOURS",
            "max_threshold": "YOURS",
            "current_value": "YOURS"
          }
        },
        "light": {
          "status_key": "YOURS",
          "instruction_key": "YOURS",
          "next_analysis_datetime_utc": "YOURS",
          "predicted_action_datetime_utc": "YOURS",
          "done_action_datetime_utc": "YOURS",
          "gauge_values": {
            "min_threshold": "YOURS",
            "max_threshold": "YOURS",
            "current_value": "YOURS"
          }
        },
        "fertilizer": {
          "status_key": "YOURS",
          "instruction_key": "YOURS",
          "next_analysis_datetime_utc": "YOURS",
          "predicted_action_datetime_utc": "YOURS",
          "done_action_datetime_utc": "YOURS",
          "gauge_values": {
            "min_threshold": "YOURS",
            "max_threshold": "YOURS",
            "current_value": "YOURS"
          }
        },
        "watering": {
          "status_key": "YOURS",
          "instruction_key": "YOURS",
          "automatic_watering": {
            "status_key": "YOURS",
            "instruction_key": "YOURS",
            "predicted_action_datetime_utc": "YOURS",
            "next_watering_datetime_utc": "YOURS",
            "full_autonomy_days": "YOURS",
            "gauge_values": {
              "min_threshold": "YOURS",
              "max_threshold": "YOURS",
              "current_value": "YOURS"
            }
          },
          "soil_moisture": {
            "status_key": "YOURS",
            "instruction_key": "YOURS",
            "predicted_action_datetime_utc": "YOURS",
            "predicted_action_vwc_value": "YOURS",
            "gauge_values": {
              "min_threshold": "YOURS",
              "max_threshold": "YOURS",
              "current_value": "YOURS"
            }
          }
        },
        "user_sharing": {
          "first_all_green": {
            "sharing_status": "YOURS"
          }
        },
        "sensor": {
          "sensor_type": "YOURS",
          "sensor_identifier": "YOURS",
          "current_history_index": "YOURS",
          "firmware_update": {
            "firmware_upgrade_available": "YOURS",
            "firmware_version": "YOURS",
            "firmware_update_url": "YOURS"
          }
        },
        "battery": {
          "gauge_values": {
            "min_threshold": "YOURS",
            "max_threshold": "YOURS",
            "current_value": "YOURS"
          }
        },
        "processing_uploads": "YOURS"
      }
    ],
    "user_config_version": "YOURS",
    "garden_status_version": "YOURS",
    "errors": [],
    "server_identifier": "YOURS"
  }
 ```

### HTTP Request

`GET https://api-flower-power-pot.parrot.com/garden/v1/status`

### Query Parameters

No parameters.
