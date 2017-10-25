<!-- controller_info-gps-->
### <a name="controller_info-gps">Controller gps info</a><br/>
> Controller gps info:

```c
deviceController->controller_info->sendGps(deviceController->controller_info, (double)latitude, (double)longitude, (float)altitude, (float)horizontal_accuracy, (float)vertical_accuracy, (float)north_speed, (float)east_speed, (float)down_speed, (double)timestamp);
```

```objective_c
deviceController->controller_info->sendGps(deviceController->controller_info, (double)latitude, (double)longitude, (float)altitude, (float)horizontal_accuracy, (float)vertical_accuracy, (float)north_speed, (float)east_speed, (float)down_speed, (double)timestamp);
```

```java
deviceController.getFeatureControllerInfo().sendGps((double)latitude, (double)longitude, (float)altitude, (float)horizontal_accuracy, (float)vertical_accuracy, (float)north_speed, (float)east_speed, (float)down_speed, (double)timestamp);
```

Controller gps info.<br/>
This command is not acknowledged by the drone.<br/>


* latitude (double): Latitude of the controller (in deg)<br/>
* longitude (double): Longitude of the controller (in deg)<br/>
* altitude (float): Altitude of the controller (in meters, according to sea level)<br/>
* horizontal_accuracy (float): Horizontal accuracy (in meter)<br/>
* vertical_accuracy (float): Vertical accuracy (in meter)<br/>
* north_speed (float): North speed (in meter per second)<br/>
* east_speed (float): East speed (in meter per second)<br/>
* down_speed (float): Vertical speed (in meter per second) (down is positive)<br/>
* timestamp (double): Timestamp of the gps info<br/>


Result:<br/>
The position of the controller is known by the drone.<br/>
It can be used for RTH or FollowMe.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- controller_info-barometer-->
### <a name="controller_info-barometer">Controller barometer info</a><br/>
> Controller barometer info:

```c
deviceController->controller_info->sendBarometer(deviceController->controller_info, (float)pressure, (double)timestamp);
```

```objective_c
deviceController->controller_info->sendBarometer(deviceController->controller_info, (float)pressure, (double)timestamp);
```

```java
deviceController.getFeatureControllerInfo().sendBarometer((float)pressure, (double)timestamp);
```

<br/>


* pressure (float): Atmospheric pressure in Pa<br/>
* timestamp (double): Timestamp of the barometer info<br/>


Result:<br/>
The altitude of the controller is known by the drone.<br/>
This command is not acknowledged by the drone.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

