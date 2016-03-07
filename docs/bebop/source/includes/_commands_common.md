<!-- common-Network-Disconnect-->
### <a name="common-Network-Disconnect">Signal the remote that the controller will disconnect</a><br/>
> Signal the remote that the controller will disconnect (deprecated):

```c
deviceController->common->sendNetworkDisconnect(deviceController->common);
```

```objective_c
deviceController->common->sendNetworkDisconnect(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendNetworkDisconnect();
```

This command is deprecated, please don't use it.

<br/>

<!-- common-Settings-AllSettings-->
### <a name="common-Settings-AllSettings">Get all product settings</a><br/>
> Get all product settings:

```c
deviceController->common->sendSettingsAllSettings(deviceController->common);
```

```objective_c
deviceController->common->sendSettingsAllSettings(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendSettingsAllSettings();
```

Get all product settings<br/>

Result:<br/>
The product will trigger all settings events. Such as [CameraSettings](#common-CameraSettingsState-CameraSettingsChanged), or product specific settings (such as the MaxAltitude for the Bebop.<br/>
Then, it will trigger [AllSettingsChangedEnd](#common-SettingsState-AllSettingsChanged).

*Supported by all products<br/>*

**Please note that you should not send this command if you are using the libARController API as this library is handling the connection process for you.**

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

Reset all settings<br/>

Result:<br/>
All the new settings will be triggered. Such as [CameraSettings](#common-CameraSettingsState-CameraSettingsChanged), or product specific settings (such as the MaxAltitude for the Bebop.<br/>
Then, it will trigger [ResetChanged](#common-SettingsState-ResetChanged).

*Supported by all products<br/>*

<br/>

<!-- common-Settings-ProductName-->
### <a name="common-Settings-ProductName">Set Product name</a><br/>
> Set Product name:

```c
deviceController->common->sendSettingsProductName(deviceController->common, (char *)name);
```

```objective_c
deviceController->common->sendSettingsProductName(deviceController->common, (char *)name);
```

```java
deviceController.getFeatureCommon().sendSettingsProductName((String)name);
```

Set Product name.<br/>
Please note that the product name is also the SSID for the Wifi products. This SSID will only be changed after a reboot of the product.

* name (string): Product name<br/>
<br/>

Result:<br/>
The name of the product is changed.<br/>
Then, it will trigger [ProductNameChanged](#common-SettingsState-ProductNameChanged).

*Supported by all products<br/>*

<!-- common-Settings-Country-->
### <a name="common-Settings-Country">Set country of controller</a><br/>
> Set country of controller:

```c
deviceController->common->sendSettingsCountry(deviceController->common, (char *)code);
```

```objective_c
deviceController->common->sendSettingsCountry(deviceController->common, (char *)code);
```

```java
deviceController.getFeatureCommon().sendSettingsCountry((String)code);
```

Set country of controller<br/>

* code (string): Country code with ISO 3166 format<br/>

Result:<br/>
The country of the product is changed.<br/>
Then, it will trigger [CountryChanged](#common-SettingsState-CountryChanged).

*Supported by all products<br/>*

<br/>

<!-- common-Settings-AutoCountry-->
### <a name="common-Settings-AutoCountry">Set Auto Country Settings</a><br/>
> Set Auto Country Settings:

```c
deviceController->common->sendSettingsAutoCountry(deviceController->common, (uint8_t)automatic);
```

```objective_c
deviceController->common->sendSettingsAutoCountry(deviceController->common, (uint8_t)automatic);
```

```java
deviceController.getFeatureCommon().sendSettingsAutoCountry((byte)automatic);
```

Set Auto Country Setting.<br/>
If auto-country is set, the drone will guess its Wifi country by itself by checking other Wifi country around it.

* automatic (u8): Boolean : 0 : Manual / 1 : Auto<br/>

Result:<br/>
The auto-country of the product is changed.<br/>
Then, it will trigger [AutoCountryChanged](#common-SettingsState-AutoCountryChanged).

*Supported by all products<br/>*

<br/>

<!-- common-Common-AllStates-->
### <a name="common-Common-AllStates">Get all product states</a><br/>
> Get all product states:

```c
deviceController->common->sendCommonAllStates(deviceController->common);
```

```objective_c
deviceController->common->sendCommonAllStates(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendCommonAllStates();
```

Get all product states.<br/>

Result:<br/>
The product will trigger all its current states. Such as [BatteryState](#common-CommonState-BatteryStateChanged), or product specific states (such as the flying state for the Bebop.<br/>
Then, it will trigger [AllStatesChangedEnd](#common-CommonState-AllStatesChanged).

*Supported by all products<br/>*

**Please note that you should not send this command if you are using the libARController API as this library is handling the connection process for you.**

<br/>

<!-- common-Common-CurrentDate-->
### <a name="common-Common-CurrentDate">Set current date of controller</a><br/>
> Set current date of controller:

```c
deviceController->common->sendCommonCurrentDate(deviceController->common, (char *)date);
```

```objective_c
deviceController->common->sendCommonCurrentDate(deviceController->common, (char *)date);
```

```java
deviceController.getFeatureCommon().sendCommonCurrentDate((String)date);
```

Set current date of controller.<br/>
This date is taken by the drone as its own date. So medias and other files will be dated from this date.

* date (string): Date with ISO-8601 format<br/>

Result:<br/>
The date of the product is set.<br/>
Then, it will trigger [CurrentDateChanged](#common-CommonState-CurrentDateChanged).

*Supported by all products<br/>*

**Please note that you should not send this command if you are using the libARController API as this library is handling the connection process for you.**
<br/>

<!-- common-Common-CurrentTime-->
### <a name="common-Common-CurrentTime">Set current time of controller</a><br/>
> Set current time of controller:

```c
deviceController->common->sendCommonCurrentTime(deviceController->common, (char *)time);
```

```objective_c
deviceController->common->sendCommonCurrentTime(deviceController->common, (char *)time);
```

```java
deviceController.getFeatureCommon().sendCommonCurrentTime((String)time);
```

Set current time of controller.<br/>
This time is taken by the drone as its own time. So medias and other files will be dated from this time.

* time (string): Time with ISO-8601 format<br/>

Result:<br/>
The time of the product is set.<br/>
Then, it will trigger [CurrentTimeChanged](#common-CommonState-CurrentTimeChanged).

*Supported by all products<br/>*

**Please note that you should not send this command if you are using the libARController API as this library is handling the connection process for you.**
<br/>

<!-- common-Common-Reboot-->
### <a name="common-Common-Reboot">Reboot the drone</a><br/>
> Reboot the drone:

```c
deviceController->common->sendCommonReboot(deviceController->common);
```

```objective_c
deviceController->common->sendCommonReboot(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendCommonReboot();
```

Reboot the drone.<br/>

Result:<br/>
The drone will reboot.

*Supported by all products<br/>*

<br/>

<!-- common-OverHeat-SwitchOff-->
### <a name="common-OverHeat-SwitchOff">Switch off the drone when a overheat appeared</a><br/>
> Switch off the drone when a overheat appeared (deprecated):

```c
deviceController->common->sendOverHeatSwitchOff(deviceController->common);
```

```objective_c
deviceController->common->sendOverHeatSwitchOff(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendOverHeatSwitchOff();
```

This command is deprecated, please don't use it.

<br/>

<!-- common-OverHeat-Ventilate-->
### <a name="common-OverHeat-Ventilate">Ventilate the drone when a overheat appeared</a><br/>
> Ventilate the drone when a overheat appeared (deprecated):

```c
deviceController->common->sendOverHeatVentilate(deviceController->common);
```

```objective_c
deviceController->common->sendOverHeatVentilate(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendOverHeatVentilate();
```

This command is deprecated, please don't use it.<br/>

<br/>

<!-- common-Controller-isPiloting-->
### <a name="common-Controller-isPiloting">Tell the drone that the controller enters/leaves the piloting HUD</a><br/>
> Tell the drone that the controller enters/leaves the piloting HUD:

```c
deviceController->common->sendControllerIsPiloting(deviceController->common, (uint8_t)piloting);
```

```objective_c
deviceController->common->sendControllerIsPiloting(deviceController->common, (uint8_t)piloting);
```

```java
deviceController.getFeatureCommon().sendControllerIsPiloting((byte)piloting);
```


Tell the drone that the controller enters/leaves the piloting HUD<br/>

* piloting (u8): 0 when the application is not in the piloting HUD, 1 when it enters the HUD.<br/>

Result:<br/>
If yes, the product will begin a new session (so it should send a new [runId](#common-RunState-RunIdChanged).<br/> 
Also, on the JumpingSumos, if the video is in autorecord mode, it will start recording.

*Supported by all products<br/>*

<br/>


<!-- common-WifiSettings-OutdoorSetting-->
### <a name="common-WifiSettings-OutdoorSetting">Set indoor or outdoor wifi settings</a><br/>
> Set indoor or outdoor wifi settings:

```c
deviceController->common->sendWifiSettingsOutdoorSetting(deviceController->common, (uint8_t)outdoor);
```

```objective_c
deviceController->common->sendWifiSettingsOutdoorSetting(deviceController->common, (uint8_t)outdoor);
```

```java
deviceController.getFeatureCommon().sendWifiSettingsOutdoorSetting((byte)outdoor);
```

Set indoor or outdoor wifi settings.<br/>

* outdoor (u8): 1 if it should use outdoor wifi settings, 0 otherwise<br/>

Result:<br/>
The product change its indoor/outdoor wifi settings.<br/> 
Then, it will trigger [OutdoorChanged](#common-WifiSettingsState-OutdoorChanged).<br/>
According to the country (defined by [SetAutoCountry](#common-Settings-AutoCountry) or [SetCountry](#common-Settings-Country)) laws the drone might change its wifi band and channel. So a disconnection might appear.

*Supported by all wifi products<br/>*

<br/>

<!-- common-Mavlink-Start-->
### <a name="common-Mavlink-Start">Start an autonomous flight</a><br/>
> Start an autonomous flight:

```c
deviceController->common->sendMavlinkStart(deviceController->common, (char *)filepath, (eARCOMMANDS_COMMON_MAVLINK_START_TYPE)type);
```

```objective_c
deviceController->common->sendMavlinkStart(deviceController->common, (char *)filepath, (eARCOMMANDS_COMMON_MAVLINK_START_TYPE)type);
```

```java
deviceController.getFeatureCommon().sendMavlinkStart((String)filepath, (ARCOMMANDS_COMMON_MAVLINK_START_TYPE_ENUM)type);
```

Start an autonomous flight<br/>

* filepath (string): autonomous flight file path from the mavlink ftp root<br/>
* type (enum): type of the played mavlink file<br/>
   * flightPlan: Mavlink file for FlightPlan<br/>
   * mapMyHouse: Mavlink file for MapMyHouse (not used)<br/>

Result:<br/>
The autonomous flight will be started if all requirements are met. Requirements are :

* Product is calibrated
* Product should be in outdoor mode
* Product has fixed its GPS

If autonomous flight has been started, event [MavlinkFilePlayingStateChanged](#common-MavlinkState-MavlinkFilePlayingStateChanged) is triggered with param state set to playing.<br/>
Otherwise, event [MavlinkFilePlayingStateChanged](#common-MavlinkState-MavlinkFilePlayingStateChanged) is triggered with param state set to stopped and event [MavlinkPlayErrorStateChanged](#common-MavlinkState-MavlinkPlayErrorStateChanged) is triggered with an explanation of the error.

*Supported by <br/>*   

- *Bebop since 2.0.29<br/>*
- *Bebop 2<br/>*

<br/>

<!-- common-Mavlink-Pause-->
### <a name="common-Mavlink-Pause">Pause an autonomous flight</a><br/>
> Pause an autonomous flight:

```c
deviceController->common->sendMavlinkPause(deviceController->common);
```

```objective_c
deviceController->common->sendMavlinkPause(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendMavlinkPause();
```

Pause an autonomous flight (can be restarted with a start).<br/>

Result:<br/>
The currently playing autonomous flight will be paused.
Then, event [MavlinkFilePlayingStateChanged](#common-MavlinkState-MavlinkFilePlayingStateChanged) is triggered with param state set to the current state of the autonomous flight (should be *paused* if everything went well).<br/>

*Supported by <br/>*   

- *Bebop since 2.0.29<br/>*
- *Bebop 2<br/>*

<br/>

<!-- common-Mavlink-Stop-->
### <a name="common-Mavlink-Stop">Stop an autonomous flight</a><br/>
> Stop an autonomous flight:

```c
deviceController->common->sendMavlinkStop(deviceController->common);
```

```objective_c
deviceController->common->sendMavlinkStop(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendMavlinkStop();
```

Stop an autonomous flight<br/>

Result:<br/>
The currently playing autonomous flight will be stopped.
Then, event [MavlinkFilePlayingStateChanged](#common-MavlinkState-MavlinkFilePlayingStateChanged) is triggered with param state set to the current state of the autonomous flight (should be *stopped* if everything went well).<br/>

*Supported by <br/>*   

- *Bebop since 2.0.29<br/>*
- *Bebop 2<br/>*

<br/>

<!-- common-Calibration-MagnetoCalibration-->
### <a name="common-Calibration-MagnetoCalibration">Start or abort magnetometer calibration</a><br/>
> Start or abort magnetometer calibration:

```c
deviceController->common->sendCalibrationMagnetoCalibration(deviceController->common, (uint8_t)calibrate);
```

```objective_c
deviceController->common->sendCalibrationMagnetoCalibration(deviceController->common, (uint8_t)calibrate);
```

```java
deviceController.getFeatureCommon().sendCalibrationMagnetoCalibration((byte)calibrate);
```

Start or abort magnetometer calibration.<br/>

* calibrate (u8): 1 if the calibration should be started, 0 if it should be aborted<br/>

Result:<br/>
The magnetometer calibration process is started or aborted.
Then, event [MagnetoCalibrationStartedChanged](#common-CalibrationState-MagnetoCalibrationStartedChanged) is triggered.<br/>
If started, event [MagnetoCalibrationStateChanged](#common-CalibrationState-MagnetoCalibrationStateChanged) is triggered with the current calibration state: a list of all axis and their calibration states. It will also trigger [MagnetoCalibrationAxisToCalibrateChanged](#common-CalibrationState-MagnetoCalibrationAxisToCalibrateChanged), that will inform the controller about the current axis to calibrate.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- common-GPS-ControllerPositionForRun-->
### <a name="common-GPS-ControllerPositionForRun">Set the controller position for a run</a><br/>
> Set the controller position for a run:

```c
deviceController->common->sendGPSControllerPositionForRun(deviceController->common, (double)latitude, (double)longitude);
```

```objective_c
deviceController->common->sendGPSControllerPositionForRun(deviceController->common, (double)latitude, (double)longitude);
```

```java
deviceController.getFeatureCommon().sendGPSControllerPositionForRun((double)latitude, (double)longitude);
```

Set the controller position for a run. This command is used by all non gps products. Watch out, this command cannot be used with BLE products<br/>
This will let the product know the controller location for the flight/run. The location is typically used to geotag medias.

* latitude (double): Controller latitude in decimal degrees<br/>
* longitude (double): Controller longitude in decimal degrees<br/>


*Supported by all Wifi products without GPS (such as the JumpingSumo)<br/>*


<br/>

<!-- common-Audio-ControllerReadyForStreaming-->
### <a name="common-Audio-ControllerReadyForStreaming">Tell the product whether the controller is ready to start audio streaming.</a><br/>
> Tell the product whether the controller is ready to start audio streaming.:

```c
deviceController->common->sendAudioControllerReadyForStreaming(deviceController->common, (uint8_t)ready);
```

```objective_c
deviceController->common->sendAudioControllerReadyForStreaming(deviceController->common, (uint8_t)ready);
```

```java
deviceController.getFeatureCommon().sendAudioControllerReadyForStreaming((byte)ready);
```

Tell the product whether the controller is ready to start audio streaming.<br/>

* ready (u8): Bit field for TX and RX ready.<br/>
bit 0 is 1 if controller is ready and wants to receive sound (Drone TX)<br/>
bit 1 is 1 if controller is ready and wants to send sound (Drone RX)<br/>

*Supported by <br/>*   

- *Jumping Sumo Evo Race<br/>*
- *Jumping Sumo Evo Brick<br/>*

<br/>

<!-- common-Headlights-intensity-->
### <a name="common-Headlights-intensity">Set instensity of lighting LEDs.</a><br/>
> Set instensity of lighting LEDs.:

```c
deviceController->common->sendHeadlightsIntensity(deviceController->common, (uint8_t)left, (uint8_t)right);
```

```objective_c
deviceController->common->sendHeadlightsIntensity(deviceController->common, (uint8_t)left, (uint8_t)right);
```

```java
deviceController.getFeatureCommon().sendHeadlightsIntensity((byte)left, (byte)right);
```

Set instensity of lighting LEDs.<br/>

* left (u8): Set the left LED intensity value (0 through 255).<br/>
* right (u8): Set the right LED intensity value (0 through 255).<br/>

Result:<br/>
Intensity of the LEDs is changed.
Then, event [HeadlightsStateIntensityChanged](#common-HeadlightsState-intensityChanged) is triggered.<br/>

*Supported by <br/>*   

- *Jumping Sumo Evo Race<br/>*
- *Jumping Sumo Evo Brick<br/>*
- *Airborne Night<br/>*

<br/>

<!-- common-Animations-StartAnimation-->
### <a name="common-Animations-StartAnimation">Start a paramaterless animation.</a><br/>
> Start a paramaterless animation.:

```c
deviceController->common->sendAnimationsStartAnimation(deviceController->common, (eARCOMMANDS_COMMON_ANIMATIONS_STARTANIMATION_ANIM)anim);
```

```objective_c
deviceController->common->sendAnimationsStartAnimation(deviceController->common, (eARCOMMANDS_COMMON_ANIMATIONS_STARTANIMATION_ANIM)anim);
```

```java
deviceController.getFeatureCommon().sendAnimationsStartAnimation((ARCOMMANDS_COMMON_ANIMATIONS_STARTANIMATION_ANIM_ENUM)anim);
```

Start a paramaterless animation.<br/>

* anim (enum): Animation to start.<br/>
   * HEADLIGHTS_FLASH: Flash headlights.<br/>
   * HEADLIGHTS_BLINK: Blink headlights.<br/>
   * HEADLIGHTS_OSCILLATION: Oscillating headlights.<br/>
   * SPIN: Spin animation.<br/>
   * TAP: Tap animation.<br/>
   * SLOW_SHAKE: Slow shake animation.<br/>
   * METRONOME: Metronome animation.<br/>
   * ONDULATION: Standing dance animation.<br/>
   * SPIN_JUMP: Spin jump animation.<br/>
   * SPIN_TO_POSTURE: Spin that end in standing posture, or in jumper if it was standing animation.<br/>
   * SPIRAL: Spiral animation.<br/>
   * SLALOM: Slalom animation.<br/>
   * BOOST: Boost animation.<br/>

Result:<br/>
If possible, the product starts the requested animation.
Then, event [AnimationsStateList](#common-AnimationsState-List) is triggered.<br/>

*Supported by <br/>*   

- *Jumping Sumo<br/>*
- *Jumping Sumo Evo Race<br/>*
- *Jumping Sumo Evo Brick<br/>*
- *Airborne Night<br/>*
- *Airborne Cargo<br/>*
<br/>

<!-- common-Animations-StopAnimation-->
### <a name="common-Animations-StopAnimation">Stop a running animation</a><br/>
> Stop a running animation:

```c
deviceController->common->sendAnimationsStopAnimation(deviceController->common, (eARCOMMANDS_COMMON_ANIMATIONS_STOPANIMATION_ANIM)anim);
```

```objective_c
deviceController->common->sendAnimationsStopAnimation(deviceController->common, (eARCOMMANDS_COMMON_ANIMATIONS_STOPANIMATION_ANIM)anim);
```

```java
deviceController.getFeatureCommon().sendAnimationsStopAnimation((ARCOMMANDS_COMMON_ANIMATIONS_STOPANIMATION_ANIM_ENUM)anim);
```

Stop a running animation.<br/>

* anim (enum): Animation to stop.<br/>
   * HEADLIGHTS_FLASH: Flash headlights.<br/>
   * HEADLIGHTS_BLINK: Blink headlights.<br/>
   * HEADLIGHTS_OSCILLATION: Oscillating headlights.<br/>
   * SPIN: Spin animation.<br/>
   * TAP: Tap animation.<br/>
   * SLOW_SHAKE: Slow shake animation.<br/>
   * METRONOME: Metronome animation.<br/>
   * ONDULATION: Standing dance animation.<br/>
   * SPIN_JUMP: Spin jump animation.<br/>
   * SPIN_TO_POSTURE: Spin that end in standing posture, or in jumper if it was standing animation.<br/>
   * SPIRAL: Spiral animation.<br/>
   * SLALOM: Slalom animation.<br/>
   * BOOST: Boost animation.<br/>

Result:<br/>
If the requested animation was running, the product stops it.
Then, event [AnimationsStateList](#common-AnimationsState-List) is triggered.<br/>

*Supported by <br/>*   

- *Jumping Sumo<br/>*
- *Jumping Sumo Evo Race<br/>*
- *Jumping Sumo Evo Brick<br/>* 
- *Airborne Night<br/>*
- *Airborne Cargo<br/>*  

<br/>

<!-- common-Animations-StopAllAnimations-->
### <a name="common-Animations-StopAllAnimations">Stop all running animations</a><br/>
> Stop all running animations:

```c
deviceController->common->sendAnimationsStopAllAnimations(deviceController->common);
```

```objective_c
deviceController->common->sendAnimationsStopAllAnimations(deviceController->common);
```

```java
deviceController.getFeatureCommon().sendAnimationsStopAllAnimations();
```

Stop all running animations.<br/>
You can get the list of the animations with [AnimationsStateList](#common-AnimationsState-List).

Result:<br/>
All running animations are stopped.
Then, event [AnimationsStateList](#common-AnimationsState-List) is triggered.<br/>

*Supported by <br/>*   

- *Jumping Sumo<br/>*
- *Jumping Sumo Evo Race<br/>*
- *Jumping Sumo Evo Brick<br/>* 
- *Airborne Night<br/>*
- *Airborne Cargo<br/>*

<br/>

<!-- common-Accessory-Config-->
### <a name="common-Accessory-Config">Set the current accessory configuration</a><br/>
> Set the current accessory configuration:

```c
deviceController->common->sendAccessoryConfig(deviceController->common, (eARCOMMANDS_COMMON_ACCESSORY_CONFIG_ACCESSORY)accessory);
```

```objective_c
deviceController->common->sendAccessoryConfig(deviceController->common, (eARCOMMANDS_COMMON_ACCESSORY_CONFIG_ACCESSORY)accessory);
```

```java
deviceController.getFeatureCommon().sendAccessoryConfig((ARCOMMANDS_COMMON_ACCESSORY_CONFIG_ACCESSORY_ENUM)accessory);
```

Set the current accessory configuration.<br/>

* accessory (enum): Accessory configuration to set.<br/>
   * NO_ACCESSORY: No accessory.<br/>
   * STD_WHEELS: Standard wheels<br/>
   * TRUCK_WHEELS: Truck wheels<br/>
   * HULL: Hull<br/>
   * HYDROFOIL: Hydrofoil<br/>

You can choose the accessory between all accessible for this product. You can get this list through event [SupportedAccessoriesListChanged](#common-AccessoryState-SupportedAccessoriesListChanged).<br/>
You can only set the accessory when the modification is enabled. You can know if it possible with the event [AccessoryConfigModificationEnabled](#common-AccessoryState-AccessoryConfigModificationEnabled).

Result:<br/>
The product knows which accessory it is wearing.
Then, event [AccessoryConfigChanged](#common-AccessoryState-AccessoryConfigChanged) is triggered.<br/>

*Supported by <br/>*   

- *Jumping Sumo<br/>*
- *Jumping Sumo Evo Race<br/>*
- *Jumping Sumo Evo Brick<br/>* 
- *Airborne Night<br/>*
- *Airborne Cargo<br/>*
- *Hydrofoil<br/>*

<br/>

<!-- common-Charger-SetMaxChargeRate-->
### <a name="common-Charger-SetMaxChargeRate">Set the max charge rate</a><br/>

> Set the max charge rate (deprecated):

```c
deviceController->common->sendChargerSetMaxChargeRate(deviceController->common, (eARCOMMANDS_COMMON_CHARGER_SETMAXCHARGERATE_RATE)rate);
```

```objective_c
deviceController->common->sendChargerSetMaxChargeRate(deviceController->common, (eARCOMMANDS_COMMON_CHARGER_SETMAXCHARGERATE_RATE)rate);
```

```java
deviceController.getFeatureCommon().sendChargerSetMaxChargeRate((ARCOMMANDS_COMMON_CHARGER_SETMAXCHARGERATE_RATE_ENUM)rate);
```

This command is deprecated, please don't use it.<br/>
The product will inform itself the controller about its charging type (see [ChargingInfoChanged](#common-ChargerState-ChargingInfo)).

<br/>
