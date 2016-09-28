<!-- generic-default-->
### <a name="generic-default">default</a><br/>
> default:

```c
deviceController->generic->sendDefault(deviceController->generic);
```

```objective_c
deviceController->generic->sendDefault(deviceController->generic);
```

```java
deviceController.getFeatureGeneric().sendDefault();
```

default<br/>




Result:<br/>
default<br/>


*Supported by <br/>*

- *no product*<br/>


<br/>

<!-- generic-SetDroneSettings-->
### <a name="generic-SetDroneSettings">SetDroneSettings</a><br/>
> SetDroneSettings:

```c
deviceController->generic->sendSetDroneSettings(deviceController->generic, (ARCOMMANDS_Generic_DroneSettings_t)settings);
```

```objective_c
deviceController->generic->sendSetDroneSettings(deviceController->generic, (ARCOMMANDS_Generic_DroneSettings_t)settings);
```

```java
deviceController.getFeatureGeneric().sendSetDroneSettings((ARCommandsGenericDroneSettings)settings);
```

Set several drone settings in only one command.<br/>


* settings (multi setting): Drone settings<br/>
   * [ARDrone3-PilotingSettings-MaxAltitude](#ARDrone3-PilotingSettings-MaxAltitude): Set max altitude<br/>
   * [ARDrone3-PilotingSettings-MaxTilt](#ARDrone3-PilotingSettings-MaxTilt): Set max pitch/roll<br/>
   * [ARDrone3-PilotingSettings-MaxDistance](#ARDrone3-PilotingSettings-MaxDistance): Set max distance<br/>
   * [ARDrone3-PilotingSettings-NoFlyOverMaxDistance](#ARDrone3-PilotingSettings-NoFlyOverMaxDistance): Enable geofence<br/>
   * [ARDrone3-SpeedSettings-MaxVerticalSpeed](#ARDrone3-SpeedSettings-MaxVerticalSpeed): Set max vertical speed<br/>
   * [ARDrone3-SpeedSettings-MaxRotationSpeed](#ARDrone3-SpeedSettings-MaxRotationSpeed): Set max rotation speed<br/>
   * [ARDrone3-SpeedSettings-MaxPitchRollRotationSpeed](#ARDrone3-SpeedSettings-MaxPitchRollRotationSpeed): Set max pitch/roll rotation speed<br/>
   * [ARDrone3-GPSSettings-ReturnHomeDelay](#ARDrone3-GPSSettings-ReturnHomeDelay): Set the return home delay<br/>
   * [ARDrone3-GPSSettings-HomeType](#ARDrone3-GPSSettings-HomeType): Set the preferred home type<br/>
   * [ARDrone3-PictureSettings-VideoStabilizationMode](#ARDrone3-PictureSettings-VideoStabilizationMode): Set video stabilization mode<br/>
   * [ARDrone3-PilotingSettings-BankedTurn](#ARDrone3-PilotingSettings-BankedTurn): Set banked turn mode<br/>


Result:<br/>
Drone settings are set.<br/>
Then, event [DroneSettingsChanged](#generic-DroneSettingsChanged) is triggered.<br/>


*Supported by <br/>*

- *no product*<br/>


<br/>

