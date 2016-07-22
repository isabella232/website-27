# PTP (Picture Transfer Protocol)

The Picture Transfer Protocol is a transport independent system to communicate
with camera-like devices.

PTP allows fine-grained control of Sequoia. Including all band-specific
properties and helper modules such as Sunshine.

Extended information is available and configurable programmatically:

* WiFi station name and password.
* Internal thermometers.
* Live Inertial Measurement Unit (IMU) data.
* Irradiance data from connected Sunshine.

Consult the Parrot PTP Extension for extensive documentation on supported
modes, operations and properties.

Use cases include:

* intelligent auto-exposure algorithms
* reference matching (e.g. luxmeter vs Sequoia)
* advanced automation (coordinating several Sequoia)
* extended acquisition system incorporating many PTP compatible cameras.
* synchronising acquisition from many different sources

## Transports

Sequoia is a fully multiclient camera. It supports simultaneous sessions
through IP and USB.

### PTPIP - Picture Transfer Protocol over Internet Protocol
By means of the standard PTP port `15740` over IP,
all the PTP properties, operations and modes are available.

Sequoia does not support any discovery protocols,
so the fixed IP `192.168.47.1` allows static access.

### PTP over USB

The most common type of PTP transport and also the fastest. Full-sized, live
image download is possible.

## PTPy
A library in pure Python to communicate with PTP-compliant cameras. PTPy
currently supports USB as a transport only.

To discover camera functionality one issues a `get_device_info` command, which
allows all operations, properties and functional modes to be listed.

PTPy fully supports the Parrot Extension and is compatible with others.

> All basic PTP operations are fully implemented. A general description can be
> obtained with:

```python
import ptpy

camera = ptpy.PTPy()
print(camera.get_device_info())
```

Dealing with PTP sessions is straightforward.

> Most PTP commands require an open session.
> Sessions can be managed automatically using standard context managers:

```python
import ptpy

camera = ptpy.PTPy
with camera.session():
    info = camera.get_device_info()
    for property in info.DevicePropertiesSupported:
        print(camera.get_device_prop_desc(property))
```

> Behind the scenes, PTPy opens a session with the camera and using that
> session sends the required commands.

It is possible to build knowledge of encountered property descriptions to
automatically parse and build PTP messages into Python values that can be used
directly.

```python
import ptpy

camera = ptpy.PTPy()
camera._obtain_the_knowledge()

with camera.session():
    print camera.get_device_prop_value('ImageSize')
    camera.set_device_prop_value('ImageSize', '4000 x 3000')
    print camera.get_device_prop_value('ImageSize')
```

## gphoto2

`gphoto2` is a standard library and CLI interface to deal with PTP cameras.

However more detailed control of Sequoia is difficult.
It is impossible to select which bands are active, for instance.

> Usage is straightforward with a single Sequoia camera connected:

```bash
gphoto2 --capture-image
```

> It is also easy to start captude over WiFi:

```bash
gphoto2 --port ptpip:192.168.47.1 --capture-image
```
