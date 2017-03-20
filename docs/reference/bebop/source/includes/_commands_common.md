<!-- common-Settings-AllSettings-->
### <a name="common-Settings-AllSettings">Ask for all settings</a><br/>
> Ask for all settings:

```c
deviceController->common->sendSettingsAllSettings(deviceController->common);
```

```objective_c
deviceController->common->sendSettingsAllSettings(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendSettingsAllSettings();
```

Ask for all settings.<br/>
<br/>
**Please note that you should not send this command if you are using the<br/>
libARController API as this library is handling the connection process for you.**<br/>




Result:<br/>
The product will trigger all settings events (such as [CameraSettings](#common-CameraSettingsState-CameraSettingsChanged), or product specific settings as the [MaxAltitude](#ARDrone3-PilotingSettingsState-MaxAltitudeChanged) for the Bebop).<br/>
Then, it will trigger [AllSettingsEnd](#common-SettingsState-AllSettingsChanged).<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-Settings-Reset-->
### <a name="common-Settings-Reset">Reset all settings</a><br/>
> Reset all settings:

```c
deviceController->common->sendSettingsReset(deviceController->common);
```

```objective_c
deviceController->common->sendSettingsReset(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendSettingsReset();
```

Reset all settings.<br/>




Result:<br/>
It will trigger [ResetChanged](#common-SettingsState-ResetChanged).<br/>
Then, the product will trigger all settings events (such as [CameraSettings](#common-CameraSettingsState-CameraSettingsChanged), or product specific settings as the [MaxAltitude](#ARDrone3-PilotingSettingsState-MaxAltitudeChanged) for the Bebop) with factory values.<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-Settings-ProductName-->
### <a name="common-Settings-ProductName">Set product name</a><br/>
> Set product name:

```c
deviceController->common->sendSettingsProductName(deviceController->common, (char *)name);
```

```objective_c
deviceController->common->sendSettingsProductName(deviceController->common, (char *)name);
```

```java
deviceController.getFeatureCommon().sendSettingsProductName((String)name);
```

Set the product name.<br/>
It also sets the name of the SSID for Wifi products and advertisement name for BLE products (changed after a reboot of the product).<br/>


* name (string): Product name<br/>


Result:<br/>
Name is changed.<br/>
Then, it will trigger [NameChanged](#common-SettingsState-ProductNameChanged).<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-Settings-Country-->
### <a name="common-Settings-Country">Set the country</a><br/>
> Set the country:

```c
deviceController->common->sendSettingsCountry(deviceController->common, (char *)code);
```

```objective_c
deviceController->common->sendSettingsCountry(deviceController->common, (char *)code);
```

```java
deviceController.getFeatureCommon().sendSettingsCountry((String)code);
```

Set the country for Wifi products.<br/>
This can modify Wifi band and/or channel.<br/>
**Please note that you might be disconnected from the product after changing the country as it changes Wifi parameters.**<br/>


* code (string): Country code with ISO 3166 format<br/>


Result:<br/>
The country is set.<br/>
Then, it will trigger [CountryChanged](#common-SettingsState-CountryChanged).<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- common-Settings-AutoCountry-->
### <a name="common-Settings-AutoCountry">Enable auto-country</a><br/>
> Enable auto-country:

```c
deviceController->common->sendSettingsAutoCountry(deviceController->common, (uint8_t)automatic);
```

```objective_c
deviceController->common->sendSettingsAutoCountry(deviceController->common, (uint8_t)automatic);
```

```java
deviceController.getFeatureCommon().sendSettingsAutoCountry((byte)automatic);
```

Enable auto-country.<br/>
If auto-country is set, the drone will guess its Wifi country by itself by checking other Wifi country around it.<br/>
**Please note that you might be disconnected from the product after changing the country as it changes Wifi parameters.**<br/>


* automatic (u8): Boolean : 0 : Manual / 1 : Auto<br/>


Result:<br/>
The auto-country of the product is changed.<br/>
Then, it will trigger [AutoCountryChanged](#common-SettingsState-AutoCountryChanged) and [CountryChanged](#common-SettingsState-CountryChanged).<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- common-Common-AllStates-->
### <a name="common-Common-AllStates">Ask for all states</a><br/>
> Ask for all states:

```c
deviceController->common->sendCommonAllStates(deviceController->common);
```

```objective_c
deviceController->common->sendCommonAllStates(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendCommonAllStates();
```

Ask for all states.<br/>
<br/>
**Please note that you should not send this command if you are using the<br/>
libARController API as this library is handling the connection process for you.**<br/>




Result:<br/>
The product will trigger all states events (such as [FlyingState](#ARDrone3-PilotingState-FlyingStateChanged) for the Bebop).<br/>
Then, it will trigger [AllStatesEnd](#common-CommonState-AllStatesChanged).<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-Common-CurrentDate-->
### <a name="common-Common-CurrentDate">Set the date</a><br/>
> Set the date:

```c
deviceController->common->sendCommonCurrentDate(deviceController->common, (char *)date);
```

```objective_c
deviceController->common->sendCommonCurrentDate(deviceController->common, (char *)date);
```

```java
deviceController.getFeatureCommon().sendCommonCurrentDate((String)date);
```

Set the date.<br/>
This date is taken by the drone as its own date.<br/>
So medias and other files will be dated from this date<br/>
<br/>
**Please note that you should not send this command if you are using the<br/>
libARController API as this library is handling the connection process for you.**<br/>


* date (string): Date with ISO-8601 format<br/>


Result:<br/>
The date of the product is set.<br/>
Then, it will trigger [DateChanged](#common-CommonState-CurrentDateChanged).<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-Common-CurrentTime-->
### <a name="common-Common-CurrentTime">Set the time</a><br/>
> Set the time:

```c
deviceController->common->sendCommonCurrentTime(deviceController->common, (char *)time);
```

```objective_c
deviceController->common->sendCommonCurrentTime(deviceController->common, (char *)time);
```

```java
deviceController.getFeatureCommon().sendCommonCurrentTime((String)time);
```

Set the time.<br/>
This time is taken by the drone as its own time.<br/>
So medias and other files will be dated from this time<br/>
<br/>
**Please note that you should not send this command if you are using the<br/>
libARController API as this library is handling the connection process for you.**<br/>


* time (string): Time with ISO-8601 format<br/>


Result:<br/>
The time of the product is set.<br/>
Then, it will trigger [TimeChanged](#common-CommonState-CurrentTimeChanged).<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-Common-Reboot-->
### <a name="common-Common-Reboot">Reboot</a><br/>
> Reboot:

```c
deviceController->common->sendCommonReboot(deviceController->common);
```

```objective_c
deviceController->common->sendCommonReboot(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendCommonReboot();
```

Reboot the product.<br/>
The product will accept this command only if is not flying.<br/>




Result:<br/>
The product will reboot if it can.<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-Controller-isPiloting-->
### <a name="common-Controller-isPiloting">Inform about hud entering</a><br/>
> Inform about hud entering:

```c
deviceController->common->sendControllerIsPiloting(deviceController->common, (uint8_t)piloting);
```

```objective_c
deviceController->common->sendControllerIsPiloting(deviceController->common, (uint8_t)piloting);
```

```java
deviceController.getFeatureCommon().sendControllerIsPiloting((byte)piloting);
```

Inform about hud entering.<br/>
Tell the drone that the controller enters/leaves the piloting hud.<br/>
On a non-flying products it is used to know when a run begins.<br/>


* piloting (u8): 0 when the application is not in the piloting HUD, 1 when it enters the HUD.<br/>


Result:<br/>
If yes, the product will begin a new session (so it should send a new [runId](#common-RunState-RunIdChanged)).<br/>
Also, on the JumpingSumos, if the video is in autorecord mode, it will start recording.<br/>


*Supported by <br/>*

- *all drones*<br/>


<br/>

<!-- common-WifiSettings-OutdoorSetting-->
### <a name="common-WifiSettings-OutdoorSetting">Set wifi outdoor mode</a><br/>
> Set wifi outdoor mode:

```c
deviceController->common->sendWifiSettingsOutdoorSetting(deviceController->common, (uint8_t)outdoor);
```

```objective_c
deviceController->common->sendWifiSettingsOutdoorSetting(deviceController->common, (uint8_t)outdoor);
```

```java
deviceController.getFeatureCommon().sendWifiSettingsOutdoorSetting((byte)outdoor);
```

Set wifi indoor/outdoor mode.<br/>
**Please note that you might be disconnected from the product after changing the indoor/outdoor setting as it changes Wifi parameters.**<br/>


* outdoor (u8): 1 if it should use outdoor wifi settings, 0 otherwise<br/>


Result:<br/>
The product change its indoor/outdoor wifi settings.<br/>
Then, it will trigger [WifiOutdoorMode](#common-WifiSettingsState-outdoorSettingsChanged).<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- common-Mavlink-Start-->
### <a name="common-Mavlink-Start">Start a FlightPlan</a><br/>
> Start a FlightPlan:

```c
deviceController->common->sendMavlinkStart(deviceController->common, (char *)filepath, (eARCOMMANDS_COMMON_MAVLINK_START_TYPE)type);
```

```objective_c
deviceController->common->sendMavlinkStart(deviceController->common, (char *)filepath, (eARCOMMANDS_COMMON_MAVLINK_START_TYPE)type);
```

```java
deviceController.getFeatureCommon().sendMavlinkStart((String)filepath, (ARCOMMANDS_COMMON_MAVLINK_START_TYPE_ENUM)type);
```

Start a FlightPlan based on a mavlink file existing on the drone.<br/>
<br/>
Requirements are:<br/>
* Product is calibrated<br/>
* Product should be in outdoor mode<br/>
* Product has fixed its GPS<br/>
<br/>


* filepath (string): flight plan file path from the mavlink ftp root<br/>
* type (enum): type of the played mavlink file<br/>
   * flightPlan: Mavlink file for FlightPlan<br/>
   * mapMyHouse: Mavlink file for MapMyHouse<br/>


Result:<br/>
If the FlightPlan has been started, event [FlightPlanPlayingStateChanged](#common-MavlinkState-MavlinkFilePlayingStateChanged) is triggered with param state set to *playing*.<br/>
Otherwise, event [FlightPlanPlayingStateChanged](#common-MavlinkState-MavlinkFilePlayingStateChanged) is triggered with param state set to stopped and event [MavlinkPlayErrorStateChanged](#common-MavlinkState-MavlinkPlayErrorStateChanged) is triggered with an explanation of the error.<br/>


*Supported by <br/>*

- *Bebop since 2.0.29*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- common-Mavlink-Pause-->
### <a name="common-Mavlink-Pause">Pause a FlightPlan</a><br/>
> Pause a FlightPlan:

```c
deviceController->common->sendMavlinkPause(deviceController->common);
```

```objective_c
deviceController->common->sendMavlinkPause(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendMavlinkPause();
```

Pause a FlightPlan that was playing.<br/>
To unpause a FlightPlan, see [StartFlightPlan](#common-Mavlink-Start)<br/>
<br/>




Result:<br/>
The currently playing FlightPlan will be paused. Then, event [FlightPlanPlayingStateChanged](#common-MavlinkState-MavlinkFilePlayingStateChanged) is triggered with param state set to the current state of the FlightPlan (should be *paused* if everything went well).<br/>


*Supported by <br/>*

- *Bebop since 2.0.29*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- common-Mavlink-Stop-->
### <a name="common-Mavlink-Stop">Stop a FlightPlan</a><br/>
> Stop a FlightPlan:

```c
deviceController->common->sendMavlinkStop(deviceController->common);
```

```objective_c
deviceController->common->sendMavlinkStop(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendMavlinkStop();
```

Stop a FlightPlan that was playing.<br/>
<br/>




Result:<br/>
The currently playing FlightPlan will be stopped. Then, event [FlightPlanPlayingStateChanged](#common-MavlinkState-MavlinkFilePlayingStateChanged) is triggered with param state set to the current state of the FlightPlan (should be *stopped* if everything went well).<br/>


*Supported by <br/>*

- *Bebop since 2.0.29*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- common-FlightPlanSettings-ReturnHomeOnDisconnect-->
### <a name="common-FlightPlanSettings-ReturnHomeOnDisconnect">Set ReturnHome behavior during FlightPlan</a><br/>
> Set ReturnHome behavior during FlightPlan:

```c
deviceController->common->sendFlightPlanSettingsReturnHomeOnDisconnect(deviceController->common, (uint8_t)value);
```

```objective_c
deviceController->common->sendFlightPlanSettingsReturnHomeOnDisconnect(deviceController->common, (uint8_t)value);
```

```java
deviceController.getFeatureCommon().sendFlightPlanSettingsReturnHomeOnDisconnect((byte)value);
```

Set ReturnHome behavior during FlightPlan<br/>
When set, drone will return home, after return home delay, if a disconnection occurs during execution of FlightPlan<br/>


* value (u8): 1 to enable, 0 to disable<br/>


Result:<br/>
The return home mode is enabled or disabled.<br/>
Then, event [ReturnHomeOnDisconnectionChanged](#common-FlightPlanSettingsState-ReturnHomeOnDisconnectChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop since 4.1.0*<br/>
- *Bebop 2 since 4.1.0*<br/>
- *Disco since 1.4.0*<br/>


<br/>

<!-- common-Calibration-MagnetoCalibration-->
### <a name="common-Calibration-MagnetoCalibration">Start/Abort magnetometer calibration</a><br/>
> Start/Abort magnetometer calibration:

```c
deviceController->common->sendCalibrationMagnetoCalibration(deviceController->common, (uint8_t)calibrate);
```

```objective_c
deviceController->common->sendCalibrationMagnetoCalibration(deviceController->common, (uint8_t)calibrate);
```

```java
deviceController.getFeatureCommon().sendCalibrationMagnetoCalibration((byte)calibrate);
```

Start or abort magnetometer calibration process.<br/>
<br/>


* calibrate (u8): 1 if the calibration should be started, 0 if it should be aborted<br/>


Result:<br/>
The magnetometer calibration process is started or aborted. Then, event [MagnetoCalibrationStartedChanged](#common-CalibrationState-MagnetoCalibrationStartedChanged) is triggered.<br/>
If started, event [MagnetoCalibrationStateChanged](#common-CalibrationState-MagnetoCalibrationStartedChanged) is triggered with the current calibration state: a list of all axis and their calibration states.<br/>
It will also trigger [MagnetoCalibrationAxisToCalibrateChanged](#common-CalibrationState-MagnetoCalibrationAxisToCalibrateChanged), that will inform the controller about the current axis to calibrate.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

