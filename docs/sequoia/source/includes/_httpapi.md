# HTTP Control API

All data are exchanged in JSON format.

The wifi IP address is 192.168.47.1

The main URLs are:

* **/capture**: to get the Sequoia capture state, start and stop a capture
* **/config**: to get and set the cameras configuration
* **/status**: to get all informations about the Seuqoia physical state
* **/calibration**: to get the calibration status, start and stop a calibration
* **/storage**: to get informations about memory
* **/file**: to get files and folders informations
* **/download**: to download files
* **/delete**: to delete files and folders
* **/version**: to get serial number and software version
* **/wifi**: to get the Sequoia SSID
* **/manualmode**: to get and set ISO and exposure manually
* **/websocket**: to use websocket notifications on asynchronous events

## /capture

```python
import requests
import json

sequoia_ip = '192.168.47.1'

r = requests.get('http://' + sequoia_ip + '/capture')

print json.dumps(r.json(), indent = 4)
```

> If no capture is running:

```json
{
    "request": "capture_status",
    "status": "Ready"
}
```

> If a capture is running:

```json
{
    "request": "capture_status",
    "status": "Snapshot running",
    "path": "/internal/0037"
}
```

### HTTP REQUEST

This URL returns the capture status of Sequoia

`GET http://192.168.47.1/capture`

URL            | Description
-------------- | -----------
/capture/start | Start a capture
/capture/stop  | Stop a capture

### QUERY PARAMETERS

Argument        | Type   | Description
--------------- | ------ | -----------
request         | string | 'capture_status'
status          | string | 'Ready' or 'Calibration running' or 'Snapshot running' or 'Timelapse running'
path (optional) | string | Path where pictures are saved if a capture is running

## /config

```python
import requests
import json

sequoia_ip = '192.168.47.1'

print "get:"
r = requests.get('http://' + sequoia_ip + '/config')
print json.dumps(r.json(), indent = 4)

print "post:"
payload = { "capture_mode": "single",
            "timelapse_param": 2.5,
            "gps_param": 25.0,
            "overlap_param": 80.0,
            "resolution_rgb": 12,
            "resolution_mono": 1.2,
            "bit_depth": 10,
            "sensors_mask": 31,
            "storage_selected": "internal",
            "auto_select": "off",
          }
r = requests.post('http://' + sequoia_ip + '/config', json = payload)
print json.dumps(r.json(), indent = 4)
```

> This should returns JSON structures for the GET:

```json
{
    "request": "get_config",
    "capture_mode": "single",
    "timelapse_param": 2.5,
    "gps_param": 25.0,
    "overlap_param": 80.0,
    "resolution_rgb": 16,
    "resolution_mono": 1.2,
    "bit_depth": 10,
    "sensors_mask": 31,
    "storage_selected": "internal",
    "auto_select": "off"
}
```
> This should returns JSON structures for the POST:

```json
{
    "request": "set_config",
    "capture_mode": "Ok",
    "timelapse_param": "Ok",
    "gps_param": "Ok",
    "overlap_param": "Ok",
    "resolution_rgb": "Ok",
    "resolution_mono": "Ok",
    "bit_depth": "Ok",
    "sensors_mask": "Ok",
    "storage_selected": "Ok",
    "auto_select": "Ok"
}
```

### HTTP REQUEST

`GET http://192.168.47.1/config`

`POST http://192.168.47.1/config`

### QUERY PARAMETERS

This URL allows you to get all informations about Sequoia capture configuration.
The following informations are provided:

Argument         | Type   | Description
---------------- | ------ | -----------
request          | string | 'get_config'
capture_mode     | string | Capture state or error message
timelapse_param  | double | Time interval
gps_param        | double | Distance interval
overlap_param    | double | Overlap parameter
resolution_rgb   | int    | 12 or 16
resolution_mono  | double | 0.3 or 1.2
bit_depth        | int    | 8 or 10
sensors_mask     | int    | Mask on 5 bits {nir, red-edge, red, green, rgb}
storage_selected | string | 'internal' or 'sd'
auto_select      | string | 'on' or 'off'

## /status

```python
import requests
import json

sequoia_ip = '192.168.47.1'

r = requests.get('http://' + sequoia_ip + '/status')

print json.dumps(r.json(), indent = 4)
```

> This should returns JSON structures for the GET:

```json
{
    "request": "get_status",
    "sunshine": {
        "green_0": 13,
        "red_0": 40,
        "red_edge_0": 1,
        "near_infrared_0": 3,
        "green_1": 1,
        "red_1": 8,
        "red_edge_1": 0,
        "near_infrared_1": 1,
        "status": "Ok"
    },
    "temperature": {
        "body_p7": 44.0,
        "body_p7mu": 49.0,
        "body_ddr3": 35.0,
        "body_wifi": 40.0,
        "body_imu": 35.071175,
        "sunshine_imu": 45.435883,
        "status": "Ok"
    },
    "gps": {
        "satellite_number": 0,
        "precision": 0.0,
        "speed": 0.0,
        "fix": 0,
        "status": "No GPS coordinates available"
    },
    "instruments": {
        "body_yaw": 48.297066,
        "body_pitch": -46.946239,
        "body_roll": -136.494492,
        "sunshine_yaw": 102.461197,
        "sunshine_pitch": -2.24509,
        "sunshine_roll": -4.575416,
        "status": "Ok"
    }
}
```

### HTTP REQUEST

`GET http://192.168.47.1/status`

### QUERY PARAMETERS

This URL provides informations about the physical state of the Sequoia.
The following informations will be returned:

Argument         | Type        | Description
---------------- | ----------- | -----------
request          | string      | 'get_status'
gps              | JSON object | All informations about gps state
instruments      | JSON object | All informations about Sequoia and sunshine sensor angles
sunshine         | JSON object | All sunshine sensors values
temperature      | JSON object | All temperatures values

You can get each JSON object seperatly, for exemple for the 'sunshine' informations:

`GET http://192.168.47.1/status/sunshine`

## /calibration

```python
import requests
import json

sequoia_ip = '192.168.47.1'

r = requests.get('http://' + sequoia_ip + '/calibration')

print json.dumps(r.json(), indent = 4)
```

> This should returns JSON structures for the GET:

```json
{
    "body": "Psi pending",
    "sunshine": "Psi pending",
    "request": "get_calibration"
}
```

### HTTP REQUEST

`GET http://192.168.47.1/calibration`

URL                         | Description
--------------------------- | -----------
/calibration/start          | Start calibration of both devices
/calibration/stop           | Stop calibration of both devices
/calibration/body/start     | Start Sequoia calibration
/calibration/body/stop      | Stop Sequoia calibration
/calibration/sunshine/start | Start sunshine sensor calibration
/calibration/sunshine/stop  | Stop sunshine sensor calibration

### QUERY PARAMETERS

This URL provides the calibration status of Sequoia and sunshine sensor.

Argument     | Type        | Description
------------ | ----------- | -----------
request      | string      | 'get_calibration'
body         | string      | Sequoia calibration status
sunshine     | string      | Sunshine sensor calibration status

The calibration status should have those different states:

* **None**: device need a calibration
* **Ok**: No calibration is required
* **Running**: A calibration is running
* **Psi pending**: Psi (Yaw) rotation needed
* **Theta pending**: Theta (Pitch) rotation needed
* **Phi pending**: Phi (Roll) rotation needed
* **Failed**: Calibration failed
* **Abort**: Calibration aborted

## /storage

```python
import requests
import json

sequoia_ip = '192.168.47.1'

r = requests.get('http://' + sequoia_ip + '/storage')

print json.dumps(r.json(), indent = 4)
```

> This should returns JSON structures for the GET:

```json
{
    "request": "get_storage",
    "storage_selected": "internal",
    "internal": {
        "total": 59272328.0,
        "free": 55453700.0,
        "path": "/internal",
        "read_only": "no",
        "corrupted": "no"
    },
    "sd": {
        "total": 7630848.0,
        "free": 7443364.0,
        "path": "/sd",
        "read_only": "no",
        "corrupted": "no"
    }
}
```

### HTTP REQUEST

`GET http://192.168.47.1/storage`

### QUERY PARAMETERS

This URL provides informations about Sequoia memories.
The following informations will be returned:

Argument         | Type        | Description
---------------- | ----------- | -----------
request          | string      | 'get_storage'
storage_selected | string      | 'internal' or 'sd'
internal         | JSON object | All informations about internal memory
sd               | JSON object | All informations about sd memory

For 'internal' and 'sd' JSON objects are:

Argument         | Type        | Description
---------------- | ----------- | -----------
total            | double      | Total memory
free             | double      | Free memory
path             | string      | Path of the root directory
read_only        | string      | 'yes' or 'no'
corrupted        | string      | 'yes' or 'no'

## /file

```python
import requests
import json

sequoia_ip = '192.168.47.1'

print "/file:"
r = requests.get('http://' + sequoia_ip + '/file')
print json.dumps(r.json(), indent = 4)

print "/file/internal:"
r = requests.get('http://' + sequoia_ip + '/file/internal')
print json.dumps(r.json(), indent = 4)

print "/file/internal:"
r = requests.get('http://' + sequoia_ip + '/file/internal/0002')
print json.dumps(r.json(), indent = 4)
```

> This should returns JSON structures for the GET /file:

```json
{
    "request": "file_info",
    "/internal": 5.685868,
    "/sd": 2.668143
}
```

> This should returns JSON structures for the GET /file/internal:

```json
{
    "request": "file_info",
    "/internal/0001": 5,
    "/internal/0000": 5,
    "/internal/0002": 5
}
```

> This should returns JSON structures for the GET /file/internal/0002:

```json
{
    "request": "file_info",
    "/internal/0002/IMG_160629_123655_0000_RGB.JPG": 1246414,
    "/internal/0002/IMG_160629_123656_0000_GRE.TIF": 2486514,
    "/internal/0002/IMG_160629_123656_0000_REG.TIF": 2486514,
    "/internal/0002/IMG_160629_123656_0000_RED.TIF": 2486514,
    "/internal/0002/IMG_160629_123656_0000_NIR.TIF": 2486514
}
```

### HTTP REQUEST

This URL returns Sequoia file informations

`GET http://192.168.47.1/file`

URL                          | Description
---------------------------- | -----------
/file                        | Storage usage for both medias 'internal' and 'sd'
/file/internal               | List 'internal'memory content
/file/sd                     | List 'sd' memory content
/file/internal/<folder name> | List 'folder name' content

You can list a specific directory content, for example:

`GET http://192.168.47.1/file/internal/0003`

### QUERY PARAMETERS

For '/file' requests:

Argument | Type        | Description
-------- | ----------- | -----------
request  | string      | 'file_info'
internal | double      | internal memory usage in GB
sd       | double      | internal memory usage in GB

For '/file/internal' or '/file/sd' requests:

Argument          | Type        | Description
----------------- | ----------- | -----------
request           | string      | 'file_info'
\<folder path 1\> | int         | number of pictures in folder 1

For '/file/internal/<folder name>' requests:

Argument           | Type        | Description
------------------ | ----------- | -----------
request            | string      | 'file_info'
\<picture path 1\> | int         | size of picture 1 in octet

## /download

```python
import requests
import shutil
import os.path

sequoia_ip = '192.168.47.1'

# To download a single file
img = "internal/0000/IMG_160704_133619_0000_GRE.TIF"

r = requests.get('http://' + sequoia_ip + '/download/' + img, stream=True)

if r.status_code == 200:
    with open(os.path.basename(img), 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

# To download an entire directory
directory = "internal/0000"

r = requests.get('http://' + sequoia_ip + '/download/' + directory, stream=True)

if r.status_code == 200:
    with open(os.path.basename(directory) + '.zip', 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
```

### HTTP REQUEST

This URL downloads the Sequoia files.

`GET http://192.168.47.1/download/internal/0000/IMG_160704_133619_0000_GRE.TIF"`

You can download an entire directory into a zip file:

`GET http://192.168.47.1/download/internal/0000"`

## /delete

```python
import requests

sequoia_ip = '192.168.47.1'

# To delete a single file
img = "internal/0000/IMG_160704_133619_0000_GRE.TIF"

r = requests.get('http://' + sequoia_ip + '/delete/' + img)

# To delete an entire directory
directory = "internal/0000"

r = requests.get('http://' + sequoia_ip + '/delete/' + directory)
```

### HTTP REQUEST

This URL deletes the Sequoia files.

`GET http://192.168.47.1/delete/internal/0000/IMG_160704_133619_0000_GRE.TIF"`

You can delete an entire directory:

`GET http://192.168.47.1/delete/internal/0000"`

## /version

```python
import requests
import json

sequoia_ip = '192.168.47.1'

r = requests.get('http://' + sequoia_ip + '/version')

print json.dumps(r.json(), indent = 4)
```

> This should returns JSON structures for the GET:

```json
{
    "request": "get_version",
    "version": "1.1.0",
    "serial_number": "PI040378AA6A000109"
}
```

### HTTP REQUEST

`GET http://192.168.47.1/version`

### QUERY PARAMETERS

This URL provides informations about Sequoia software version and serial number.

Argument               | Type        | Description
---------------------- | ----------- | -----------
request                | string      | 'get_version'
version                | string      | Software version
serial_number          | string      | Sequoia serial number
sunshine_serial_number | string      | Sunshine sensor serial number

## /wifi

```python
import requests
import json

sequoia_ip = '192.168.47.1'

r = requests.get('http://' + sequoia_ip + '/wifi')

print json.dumps(r.json(), indent = 4)

# To change SSID:
r = requests.post('http://' + sequoia_ip + '/wifi', json = {"ssid": "new_ssid"})

print json.dumps(r.json(), indent = 4)
```

> This should returns JSON structures for the GET:

```json
{
    "request": "get_wifi",
    "ssid": "Sequoia_0109",
    "status": "on"
}
```

### HTTP REQUEST

`GET http://192.168.47.1/wifi`

`POST http://192.168.47.1/wifi`

### QUERY PARAMETERS

This URL provides informations about Sequoia wifi SSID

Argument     | Type        | Description
------------ | ----------- | -----------
request      | string      | 'get_wifi'
ssid         | string      | Sequoia SSID
status       | string      | 'on' or 'off'

SSID can be changed by sending a POST request with the new SSID.

## /manualmode

```python
import requests
import json

sequoia_ip = '192.168.47.1'

payload = { "monochrome": {
                "mode": "manual",
                "green": {
                    "exp_us": 12000,
                    "iso": 800,
                },
                "red": {
                    "exp_us": 13000,
                    "iso": 200,
                },
                "red_edge": {
                    "exp_us": 14000,
                    "iso": 400,
                },
                "near_infrared": {
                    "exp_us": 15000,
                    "iso": 100,
                },
            },
            "rgb": {
                "mode": "manual",
                "exp_us": 2530,
                "iso": 200,
            },
          }
r = requests.post('http://' + sequoia_ip + '/manualmode', json = payload)
print json.dumps(r.json(), indent=4)
print "----------------------------------"

r = requests.get('http://' + sequoia_ip + '/manualmode')
print json.dumps(r.json(), indent = 4)
```

> This should returns JSON structures for the POST:

```json
{
    "request": "set_manualmode",
    "monochrome": {
        "mode": "Ok",
        "green": {
            "exp_us": "Ok",
            "iso": "Ok"
        },
        "red": {
            "exp_us": "Ok",
            "iso": "Ok"
        },
        "red_edge": {
            "exp_us": "Ok",
            "iso": "Ok"
        },
        "near_infrared": {
            "exp_us": "Ok",
            "iso": "Ok"
        }
    },
    "rgb": {
        "mode": "Ok",
        "exp_us": "Ok",
        "iso": "Ok"
    }
}
```

> This should returns JSON structures for the GET:

```json
{
    "request": "get_manualmode",
    "monochrome": {
        "mode": "manual",
        "green": {
            "exp_us": 12000,
            "iso": 800
        },
        "red": {
            "exp_us": 13000,
            "iso": 300
        },
        "red_edge": {
            "exp_us": 14000,
            "iso": 405
        },
        "near_ir": {
            "exp_us": 800,
            "iso": 800
        }
    },
    "rgb": {
        "mode": "manual",
        "exp_us": 2530,
        "iso": 200
    }
}
```

### HTTP REQUEST

`GET http://192.168.47.1/manualmode`

`POST http://192.168.47.1/manualmode`

### QUERY PARAMETERS

Manual mode allows you to change the ISO and exposure of each camera.
The following informations are provided:

Argument          | Type        | Description
----------------- | ----------- | -----------
request           | string      | 'get_manualmode' or 'set_manualmode'
rgb               | JSON object | RGB camera parameters
monochrome        | JSON object | Capture state or error message

For 'rgb', JSON object is:

Argument | Type    | Description
-------- | ------- | -----------
mode     | string  | 'auto' or 'manual'
exp_us   | int     | Exposure time in us
iso      | int     | Gain value x 100

For 'monochrome', JSON object is:

Argument      | Type        | Description
------------- | ----------- | -----------
mode          | string      | 'auto' or 'manual'
green         | JSON object | Green camera parameters
red           | JSON object | Red camera parameters
red_edge      | JSON object | Red-Edge camera parameters
near_infrared | JSON object | Near Infrared camera parameters

For 'green', 'red', 'red_edge' and 'near_infrared', JSON object is:

Argument | Type  | Description
-------- | ----- | -----------
exp_us   | int   | Exposure time in us
iso      | int   | Gain value x 100

## /websocket

Websockets notifications allow you to receive asynchronous event from the Sequoia, such as change in camera configuration, insertion of sd card, etc...

> This is an example of how to connect to the Sequoia websocket, display received messages, and stay connected responding to the "ping" with "pong"

```python
import websocket
import json

sequoia_ip = '192.168.47.1'


def on_message(ws, message):
    data = json.loads(message)
    print json.dumps(data, indent = 4)

    if data['status'] == "ping":
        ws.send("pong")

def on_error(ws, error):
    print "error:" + error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    print "### opened ###"

ws = websocket.WebSocketApp('ws://' + sequoia_ip + '/websocket',
        on_open    = on_open,
        on_message = on_message,
        on_error   = on_error,
        on_close   = on_close)

ws.run_forever()
```

### HTTP REQUEST

Websocket notifications can be received by connecting to the following URL: `ws://192.168.47.1/websocket`

### PING

In order to stay connected to the websocket, you have to reply "pong" on each "ping" sent by the server.

### NOTIFICATIONS

Below is the list of JSON objects you could receive:

####Capture
Argument | Type  | Description
-------- | ----- | -----------
status   | string   | "change"
capture      | string   | Capture event: "ready" or "running"

####Sunshine
Argument | Type  | Description
-------- | ----- | -----------
status   | string   | "change"
sunshine      | string   | Sunshine event: "connected" or "disconnected"

####Stay still
Argument | Type  | Description
-------- | ----- | -----------
status   | string   | "change"
staystill      | string   | Stay still event: "yes" or "no"

####Storage select
Argument | Type  | Description
-------- | ----- | -----------
status   | string   | "change"
storage_select      | string   | Storage selected: "internal" or "sd"

####Storage status
Argument | Type  | Description
-------- | ----- | -----------
status   | string   | "change"
storage_status      | string   | Storage: "internal" or "sd"
state   | string    | Storage status event: "connected" , "disconnected", "full", "no_longer_full", "error"

####Calibration status
Argument | Type  | Description
-------- | ----- | -----------
status   | string   | "change"
calibration      | string   | Target: "body" or "sunshine"
state   | string    | Calibration event: "None", "Ok", "Running", "Phi pending", "Theta pending", "Psi pending", "Failed", "Aborted"

####Capture mode
Argument | Type  | Description
-------- | ----- | -----------
status   | string   | "change"
capture_mode      | string   | new capture mode: "single", "timelapse", "gps_position", "auto", "radiometric"

####Capture mode parameters
Argument | Type  | Description
-------- | ----- | -----------
status   | string   | "change"
timelapse_param      | double   | value of timelapse in second, for timelapse mode
gps_param   | double | value of gps distance in meters, for gps mode
overlap_param   | int     | Value of overlap in percent, for auto mode

####Sensors mask
Argument | Type  | Description
-------- | ----- | -----------
status   | string   | "change"
sensors_mask      | int   | Sensors mask of activated sensors on the camera

####Sensors resolution
Argument | Type  | Description
-------- | ----- | -----------
status   | string   | "change"
resolution_rgb      | int   | Resolution of  rgb sensor in Mpx
resolution_mono | double    | Resolution of  mono sensors in Mpx

####Bit depth
Argument | Type  | Description
-------- | ----- | -----------
status   | string   | "change"
bit_depth      | int   | Bit depth of mono sensors in bits

####GPS fix
Argument | Type  | Description
-------- | ----- | -----------
status   | string   | "change"
fix      | string   |  GPS fix state: "yes or "no"

