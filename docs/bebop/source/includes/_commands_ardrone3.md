<!-- ARDrone3-Piloting-FlatTrim-->
### <a name="ARDrone3-Piloting-FlatTrim">Do a flat trim</a><br/>
> Do a flat trim:

```c
deviceController->aRDrone3->sendPilotingFlatTrim(deviceController->aRDrone3);
```

```objective_c
deviceController->aRDrone3->sendPilotingFlatTrim(deviceController->aRDrone3);
```

```java
deviceController.getFeatureARDrone3().sendPilotingFlatTrim();
```

Do a flat trim of the accelerometer/gyro. Could be useful when the drone is sliding in hover mode.<br/>

Result:<br/>
Accelero/Gyro are re-calibrated.<br/>
Then, event [FlatTrimChanged](#ARDrone3-PilotingState-FlatTrimChanged) is triggered.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-Piloting-TakeOff-->
### <a name="ARDrone3-Piloting-TakeOff">Take off</a><br/>
> Take off:

```c
deviceController->aRDrone3->sendPilotingTakeOff(deviceController->aRDrone3);
```

```objective_c
deviceController->aRDrone3->sendPilotingTakeOff(deviceController->aRDrone3);
```

```java
deviceController.getFeatureARDrone3().sendPilotingTakeOff();
```

Ask the drone to take off<br/>

Result:<br/>
The drone takes off.<br/>
Then, event[FlyingStateChanged](#ARDrone3-PilotingState-FlyingStateChanged) is triggered.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-Piloting-PCMD-->
### <a name="ARDrone3-Piloting-PCMD">Move the drone</a><br/>
> Ask the drone to move around.:

```c
deviceController->aRDrone3->sendPilotingPCMD(deviceController->aRDrone3, (uint8_t)flag, (int8_t)roll, (int8_t)pitch, (int8_t)yaw, (int8_t)gaz, (uint32_t)timestampAndSeqNum);
```

```objective_c
deviceController->aRDrone3->sendPilotingPCMD(deviceController->aRDrone3, (uint8_t)flag, (int8_t)roll, (int8_t)pitch, (int8_t)yaw, (int8_t)gaz, (uint32_t)timestampAndSeqNum);
```

```java
deviceController.getFeatureARDrone3().sendPilotingPCMD((byte)flag, (byte)roll, (byte)pitch, (byte)yaw, (byte)gaz, (int)timestampAndSeqNum);
```

Ask the drone to move around.<br/>

* flag (u8): Boolean flag to activate roll/pitch movement<br/>
* roll (i8): Roll consign for the drone [-100;100]<br/>
* pitch (i8): Pitch consign for the drone [-100;100]<br/>
* yaw (i8): Yaw consign for the drone [-100;100]<br/>
* gaz (i8): Gaz consign for the drone [-100;100]<br/>
* psi (float): [NOT USED] - Magnetic north heading of the controlling device (deg) [-180;180]<br/>

This command should be sent on the non-acknowledged buffer as it is sent periodically (already done by the libARController). <br/>
The libARController is sending the command each 50ms. 

**Please note that you should call setPilotingPCMD and not sendPilotingPCMD because the libARController is handling the periodicity and the buffer on which it is sent.**

Result:<br/>
The drone moves! Yaaaaay!<br/>
Event [SpeedChanged](#ARDrone3-PilotingState-SpeedChanged), [AttitudeChanged](#ARDrone3-PilotingState-AttitudeChanged) and [PositionChanged](#ARDrone3-PilotingState-PositionChanged) (only if gps of the drone has fixed) are triggered.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-Piloting-Landing-->
### <a name="ARDrone3-Piloting-Landing">Ask the drone to land</a><br/>
> Ask the drone to land:

```c
deviceController->aRDrone3->sendPilotingLanding(deviceController->aRDrone3);
```

```objective_c
deviceController->aRDrone3->sendPilotingLanding(deviceController->aRDrone3);
```

```java
deviceController.getFeatureARDrone3().sendPilotingLanding();
```

Ask the drone to land<br/>
Please note that if you put some positive gaz (in the [PilotingCommand](#ARDrone3-Piloting-PCMD)) during the landing, it will cancel it.

Result:<br/>
The drone lands.<br/>
Then, event[FlyingStateChanged](#ARDrone3-PilotingState-FlyingStateChanged) is triggered.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-Piloting-Emergency-->
### <a name="ARDrone3-Piloting-Emergency">Put drone in emergency user state</a><br/>
> Put drone in emergency user state:

```c
deviceController->aRDrone3->sendPilotingEmergency(deviceController->aRDrone3);
```

```objective_c
deviceController->aRDrone3->sendPilotingEmergency(deviceController->aRDrone3);
```

```java
deviceController.getFeatureARDrone3().sendPilotingEmergency();
```

Put drone in emergency user state<br/>
This command is sent on a dedicated high priority buffer which will infinitely retry to send it if the command is not delivered.

Result:<br/>
The drone immediatly switches off its motors.<br/>
Then, event[FlyingStateChanged](#ARDrone3-PilotingState-FlyingStateChanged) is triggered.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-Piloting-NavigateHome-->
### <a name="ARDrone3-Piloting-NavigateHome">Ask the drone to fly to home</a><br/>
> Ask the drone to fly to home:

```c
deviceController->aRDrone3->sendPilotingNavigateHome(deviceController->aRDrone3, (uint8_t)start);
```

```objective_c
deviceController->aRDrone3->sendPilotingNavigateHome(deviceController->aRDrone3, (uint8_t)start);
```

```java
deviceController.getFeatureARDrone3().sendPilotingNavigateHome((byte)start);
```

Ask the drone to fly to home to its home position (you can get it from [HomeChanged](#ARDrone3-GPSSettingsState-HomeChanged))<br/>
The availability of the navigate home can be get from [NavigateHomeStateChanged](#ARDrone3-PilotingState-NavigateHomeStateChanged).

* start (u8): 1 to start the navigate home, 0 to stop it<br/>

Result:<br/>
The drone will fly back to its home position.<br/>
Then, event[NavigateHomeStateChanged](#ARDrone3-PilotingState-NavigateHomeStateChanged) is triggered. You can get a state *pending* if the drone is not ready to start its return home process but will do it as soon as it is possible.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-Piloting-AutoTakeOffMode-->
### <a name="ARDrone3-Piloting-AutoTakeOffMode">Set automatic take off mode</a><br/>

This command is deprecated, please don't use it.
<br/>

<!-- ARDrone3-Piloting-moveBy-->
### <a name="ARDrone3-Piloting-moveBy">Move the drone to a relative position</a><br/>
> Move the drone to a relative position (not implemented):

```c
deviceController->aRDrone3->sendPilotingMoveBy(deviceController->aRDrone3, (float)dX, (float)dY, (float)dZ, (float)dPsi);
```

```objective_c
deviceController->aRDrone3->sendPilotingMoveBy(deviceController->aRDrone3, (float)dX, (float)dY, (float)dZ, (float)dPsi);
```

```java
deviceController.getFeatureARDrone3().sendPilotingMoveBy((float)dX, (float)dY, (float)dZ, (float)dPsi);
```

**Draft: this command is not implemented yet by the firmware**<br/>

Move the drone to a relative position and rotate heading by a given angle<br/>

The frame is horizontal and relative to the current drone orientation:<br/>

- X is front<br/>

- Y is right<br/>

- Z is down<br/>

The movement settings of the device are those set for the autonomous flight.<br/>

* dX (float): Wanted displacement along the front axis [m]<br/>
* dY (float): Wanted displacement along the right axis [m]<br/>
* dZ (float): Wanted displacement along the down axis [m]<br/>
* dPsi (float): Wanted rotation of heading  [rad]<br/>

Result:<br/>
The drone will move of the given offsets.<br/>
Then, event [MoveByEnd](#ARDrone3-PilotingEvent-moveByEnd) is triggered.<br/>
If you send a second command [MoveBy](#ARDrone3-Piloting-moveBy), the drone will trigger a [MoveByEnd](#ARDrone3-PilotingEvent-moveByEnd) with the offsets it managed to do before this command and the value of error set to *interrupted*.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-Animations-Flip-->
### <a name="ARDrone3-Animations-Flip">Make a flip</a><br/>
> Make a flip:

```c
deviceController->aRDrone3->sendAnimationsFlip(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_ANIMATIONS_FLIP_DIRECTION)direction);
```

```objective_c
deviceController->aRDrone3->sendAnimationsFlip(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_ANIMATIONS_FLIP_DIRECTION)direction);
```

```java
deviceController.getFeatureARDrone3().sendAnimationsFlip((ARCOMMANDS_ARDRONE3_ANIMATIONS_FLIP_DIRECTION_ENUM)direction);
```

Make a flip<br/>

* direction (enum): Direction for the flip<br/>
   * front: Flip direction front<br/>
   * back: Flip direction back<br/>
   * right: Flip direction right<br/>
   * left: Flip direction left<br/>

Result:<br/>
The drone will make a flip if it has enough battery.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*
   
<br/>

<!-- ARDrone3-Camera-Orientation-->
### <a name="ARDrone3-Camera-Orientation">Ask the drone to move camera.</a><br/>
> Ask the drone to move camera.:

```c
deviceController->aRDrone3->sendCameraOrientation(deviceController->aRDrone3, (int8_t)tilt, (int8_t)pan);
```

```objective_c
deviceController->aRDrone3->sendCameraOrientation(deviceController->aRDrone3, (int8_t)tilt, (int8_t)pan);
```

```java
deviceController.getFeatureARDrone3().sendCameraOrientation((byte)tilt, (byte)pan);
```

Ask the drone to move camera.<br/>

* tilt (i8): Tilt camera consign for the drone (in degree)<br/>
The value is saturated by the drone.<br/>
Saturation value is sent by thre drone through CameraSettingsChanged command.<br/>
* pan (i8): Pan camera consign for the drone (in degree)<br/>
The value is saturated by the drone.<br/>
Saturation value is sent by thre drone through CameraSettingsChanged command.<br/>

You can get min and max values for tilt and pan using [CameraSettingsChanged](#common-CameraSettingsState-CameraSettingsChanged).

Result:<br/>
The drone will move its camera.<br/>
Then, event [CameraOrientationState](#ARDrone3-CameraState-Orientation) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-MediaRecord-Picture-->
### <a name="ARDrone3-MediaRecord-Picture">Record picture v1</a><br/>
> Record picture v1:

```c
deviceController->aRDrone3->sendMediaRecordPicture(deviceController->aRDrone3, (uint8_t)mass_storage_id);
```

```objective_c
deviceController->aRDrone3->sendMediaRecordPicture(deviceController->aRDrone3, (uint8_t)mass_storage_id);
```

```java
deviceController.getFeatureARDrone3().sendMediaRecordPicture((byte)mass_storage_id);
```

This command is deprecated, please don't use it.

<br/>

<!-- ARDrone3-MediaRecord-Video-->
### <a name="ARDrone3-MediaRecord-Video">Record video v1</a><br/>
> Record video v1 (deprecated):

```c
deviceController->aRDrone3->sendMediaRecordVideo(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_MEDIARECORD_VIDEO_RECORD)record, (uint8_t)mass_storage_id);
```

```objective_c
deviceController->aRDrone3->sendMediaRecordVideo(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_MEDIARECORD_VIDEO_RECORD)record, (uint8_t)mass_storage_id);
```

```java
deviceController.getFeatureARDrone3().sendMediaRecordVideo((ARCOMMANDS_ARDRONE3_MEDIARECORD_VIDEO_RECORD_ENUM)record, (byte)mass_storage_id);
```

This command is deprecated, please don't use it.
<br/>

<!-- ARDrone3-MediaRecord-PictureV2-->
### <a name="ARDrone3-MediaRecord-PictureV2">Take picture</a><br/>
> Take picture:

```c
deviceController->aRDrone3->sendMediaRecordPictureV2(deviceController->aRDrone3);
```

```objective_c
deviceController->aRDrone3->sendMediaRecordPictureV2(deviceController->aRDrone3);
```

```java
deviceController.getFeatureARDrone3().sendMediaRecordPictureV2();
```

Take picture<br/>

The type of picture taken is related to the picture setting.<br/>
You can set the picture format by sending the command [SetPictureFormat](#ARDrone3-PictureSettings-PictureFormatSelection). You can also get the current picture format with [PictureFormatChanged](#ARDrone3-PictureSettingsState-PictureFormatChanged).<br/>
Please note that the time required to take the picture is highly related to this format.

You can check if the picture taking is available with [PictureStateChanged](#ARDrone3-MediaRecordState-PictureStateChangedV2).<br/>
Also, please note that if your picture format is different from *snapshot*, picture taking will stop video recording (it will restart after the picture has been taken).


Result:<br/>
Event [PictureStateChanged](#ARDrone3-MediaRecordState-PictureStateChangedV2) will be triggered with a state *busy*.<br/>
The drone will take a picture.<br/>
Then, when picture has been taken, event [PictureEventChanged](#ARDrone3-MediaRecordEvent-PictureEventChanged) is triggered. <br/>
And normally [PictureStateChanged](#ARDrone3-MediaRecordState-PictureStateChangedV2) will be triggered with a state *ready*.

*Supported by <br/>*   

- *Bebop since 2.0.1<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-MediaRecord-VideoV2-->
### <a name="ARDrone3-MediaRecord-VideoV2">Video record</a><br/>
> Video record:

```c
deviceController->aRDrone3->sendMediaRecordVideoV2(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_MEDIARECORD_VIDEOV2_RECORD)record);
```

```objective_c
deviceController->aRDrone3->sendMediaRecordVideoV2(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_MEDIARECORD_VIDEOV2_RECORD)record);
```

```java
deviceController.getFeatureARDrone3().sendMediaRecordVideoV2((ARCOMMANDS_ARDRONE3_MEDIARECORD_VIDEOV2_RECORD_ENUM)record);
```

Video record<br/>

* record (enum): Command to record video (or timelapse)<br/>
   * stop: Stop the video recording<br/>
   * start: Start the video recording<br/>

You can check if the video recording is available with [VideoStateChanged](#ARDrone3-MediaRecordState-VideoStateChangedV2).<br/>
This command can start a video (obvious huh?), but also a timelapse if the timelapse mode is set. You can check if the timelapse mode is set with the event [TimelapseChanged](#ARDrone3-PictureSettingsState-TimelapseChanged).<br/>
Also, please note that if your picture format is different from *snapshot*, picture taking will stop video recording (it will restart after the picture has been taken).


Result:<br/>
The drone will begin or stop to record the video (or timelapse).<br/>
Then, event [VideoStateChanged](#ARDrone3-MediaRecordState-VideoStateChangedV2) will be triggered.
Also, [VideoEventChanged](#ARDrone3-MediaRecordEvent-VideoEventChanged) is triggered. 

*Supported by <br/>*   

- *Bebop since 2.0.1<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-Network-WifiScan-->
### <a name="ARDrone3-Network-WifiScan">Scan wifi network</a><br/>
> Scan wifi network:

```c
deviceController->aRDrone3->sendNetworkWifiScan(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_NETWORK_WIFISCAN_BAND)band);
```

```objective_c
deviceController->aRDrone3->sendNetworkWifiScan(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_NETWORK_WIFISCAN_BAND)band);
```

```java
deviceController.getFeatureARDrone3().sendNetworkWifiScan((ARCOMMANDS_ARDRONE3_NETWORK_WIFISCAN_BAND_ENUM)band);
```

Scan wifi network to get a list of all wifi networks found by the drone.<br/>

* band (enum): The band(s) : 2.4 Ghz, 5 Ghz, or both<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
   * all: Both 2.4 and 5 GHz bands<br/>

Result:<br/>
Event [WifiScanListChanged](#ARDrone3-NetworkState-WifiScanListChanged) is triggered with all networks found. When all networks have been sent, event [AllWifiScanChanged](#ARDrone3-NetworkState-AllWifiScanChanged) is triggered.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-Network-WifiAuthChannel-->
### <a name="ARDrone3-Network-WifiAuthChannel">Get all available Wifi channels</a><br/>
> Get all available Wifi channels:

```c
deviceController->aRDrone3->sendNetworkWifiAuthChannel(deviceController->aRDrone3);
```

```objective_c
deviceController->aRDrone3->sendNetworkWifiAuthChannel(deviceController->aRDrone3);
```

```java
deviceController.getFeatureARDrone3().sendNetworkWifiAuthChannel();
```

Get all available Wifi channels.<br/>
The list of available Wifi channels is related to the country of the drone. You can get this country with the event [CountryChanged](#common-SettingsState-CountryChanged).

Result:<br/>
Event [WifiAuthChannelListChanged](#ARDrone3-NetworkState-WifiAuthChannelListChanged) is triggered with all authorized channels. When all channels have been sent, event [AllWifiAuthChannelChanged](#ARDrone3-NetworkState-AllWifiAuthChannelChanged) is triggered.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingSettings-MaxAltitude-->
### <a name="ARDrone3-PilotingSettings-MaxAltitude">Set Max Altitude</a><br/>
> Set Max Altitude:

```c
deviceController->aRDrone3->sendPilotingSettingsMaxAltitude(deviceController->aRDrone3, (float)current);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsMaxAltitude(deviceController->aRDrone3, (float)current);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsMaxAltitude((float)current);
```

Set Max Altitude. <br/>

* current (float): Current altitude max in m<br/>

The drone will not fly over this max altitude when it is in manual piloting. Please note that if you set a max altitude which is below the current drone altitude, the drone will no go to the max altitude.
You can get the bounds in the event [MaxAltitudeChanged](#ARDrone3-PilotingSettingsState-MaxAltitudeChanged).
 
Result:<br/>
The max altitude is set.<br/>
Then, event [MaxAltitudeChanged](#ARDrone3-PilotingSettingsState-MaxAltitudeChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingSettings-MaxTilt-->
### <a name="ARDrone3-PilotingSettings-MaxTilt">Set Max Tilt</a><br/>
> Set Max Tilt:

```c
deviceController->aRDrone3->sendPilotingSettingsMaxTilt(deviceController->aRDrone3, (float)current);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsMaxTilt(deviceController->aRDrone3, (float)current);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsMaxTilt((float)current);
```

Set Max Tilt<br/>

* current (float): Current tilt max in degree<br/>

This represent the max inclination allowed by the drone. You can get the bounds with the commands [MaxAltitudeChanged](#ARDrone3-PilotingSettingsState-MaxTiltChanged).
 
Result:<br/>
The max tilt is set.<br/>
Then, event [MaxTiltChanged](#ARDrone3-PilotingSettingsState-MaxTiltChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingSettings-AbsolutControl-->
### <a name="ARDrone3-PilotingSettings-AbsolutControl">Enable/Disable absolut control</a><br/>
> Enable/Disable absolut control (deprecated):

```c
deviceController->aRDrone3->sendPilotingSettingsAbsolutControl(deviceController->aRDrone3, (uint8_t)on);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsAbsolutControl(deviceController->aRDrone3, (uint8_t)on);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsAbsolutControl((byte)on);
```

This command is deprecated, please don't use it.

<!-- ARDrone3-PilotingSettings-MaxDistance-->
### <a name="ARDrone3-PilotingSettings-MaxDistance">Set the distance max of the drone</a><br/>
> Set the distance max of the drone:

```c
deviceController->aRDrone3->sendPilotingSettingsMaxDistance(deviceController->aRDrone3, (float)value);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsMaxDistance(deviceController->aRDrone3, (float)value);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsMaxDistance((float)value);
```

Set the distance max of the drone<br/>

* value (float): Current max distance in meter<br/>

You can get the bounds with the event [MaxDistanceChanged](#ARDrone3-PilotingSettingsState-MaxDistanceChanged).

If NoFlyOverMaxDistance is set to 1, the drone won't fly over the given max distance. You can get this value through the event [MaxDistanceLimitationBehaviourChanged](#ARDrone3-PilotingSettingsState-NoFlyOverMaxDistanceChanged). 

Result:<br/>
The max distance is set.<br/>
Then, event [MaxDistanceChanged](#ARDrone3-PilotingSettingsState-MaxDistanceChanged) is triggered. 

**Draft: this command is not implemented yet by the firmware**<br/>

*Supported by no products<br/>*

<br/>

<!-- ARDrone3-PilotingSettings-NoFlyOverMaxDistance-->
### <a name="ARDrone3-PilotingSettings-NoFlyOverMaxDistance">Set the max distance limitation behaviour</a><br/>
> Set the max distance limitation behaviour (not implemented):

```c
deviceController->aRDrone3->sendPilotingSettingsNoFlyOverMaxDistance(deviceController->aRDrone3, (uint8_t)shouldNotFlyOver);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsNoFlyOverMaxDistance(deviceController->aRDrone3, (uint8_t)shouldNotFlyOver);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsNoFlyOverMaxDistance((byte)shouldNotFlyOver);
```

Set the max distance limitation behaviour<br/>

* shouldNotFlyOver (u8): 1 if the drone can't fly further than max distance, 0 if no limitation on the drone should be done<br/>

You can get the current max distance with the event [MaxDistanceChanged](#ARDrone3-PilotingSettingsState-MaxDistanceChanged).

**Draft: this command is not implemented yet by the firmware**<br/>

Result:<br/>
The given behaviour is set on the drone. If it shouldn't fly over the max distance, the drone won't fly further the max distance.<br/>
Then, event [MaxDistanceLimitationBehaviourChanged](#ARDrone3-PilotingSettingsState-NoFlyOverMaxDistanceChanged) is triggered. 

*Supported by no products<br/>*

<br/>

<!-- ARDrone3-PilotingSettings-setAutonomousFlightMaxHorizontalSpeed-->
### <a name="ARDrone3-PilotingSettings-setAutonomousFlightMaxHorizontalSpeed">Set the maximum horizontal speed used during autonomous flights</a><br/>
> Set the maximum horizontal speed used during autonomous flights (not implemented):

```c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxHorizontalSpeed(deviceController->aRDrone3, (float)value);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxHorizontalSpeed(deviceController->aRDrone3, (float)value);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsSetAutonomousFlightMaxHorizontalSpeed((float)value);
```

Set the maximum horizontal speed used during autonomous flights.<br/>

**Draft: this command is not implemented yet by the firmware**<br/>

* value (float): maximum horizontal speed [m/s]<br/>

Result:<br/>
The max horizontal speed for autonomous flights is set.<br/>
Then, event [AutonomousFlightMaxHorizontalSpeedChanged](#ARDrone3-PilotingSettingsState-AutonomousFlightMaxHorizontalSpeed) is triggered. 

*Supported by no products<br/>* 

<br/>

<!-- ARDrone3-PilotingSettings-setAutonomousFlightMaxVerticalSpeed-->
### <a name="ARDrone3-PilotingSettings-setAutonomousFlightMaxVerticalSpeed">Set the maximum vertical speed used by autonomous flights</a><br/>
> Set the maximum vertical speed used by autonomous flights (not implemented):

```c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxVerticalSpeed(deviceController->aRDrone3, (float)value);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxVerticalSpeed(deviceController->aRDrone3, (float)value);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsSetAutonomousFlightMaxVerticalSpeed((float)value);
```

Set the maximum vertical speed used by autonomous flights.<br/>

**Draft: this command is not implemented yet by the firmware**<br/>

* value (float): maximum vertical speed [m/s]<br/>

Result:<br/>
The max vertical speed for autonomous flights is set.<br/>
Then, event [AutonomousFlightMaxVerticalSpeedChanged](#ARDrone3-PilotingSettingsState-AutonomousFlightMaxVerticalSpeed) is triggered. 

*Supported by no products<br/>* 

<br/>

<!-- ARDrone3-PilotingSettings-setAutonomousFlightMaxHorizontalAcceleration-->
### <a name="ARDrone3-PilotingSettings-setAutonomousFlightMaxHorizontalAcceleration">Set the maximum horizontal acceleration used by autonomous flights</a><br/>
> Set the maximum horizontal acceleration used by autonomous flights (not implemented):

```c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxHorizontalAcceleration(deviceController->aRDrone3, (float)value);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxHorizontalAcceleration(deviceController->aRDrone3, (float)value);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsSetAutonomousFlightMaxHorizontalAcceleration((float)value);
```

Set the maximum horizontal acceleration used by autonomous flights.<br/>

**Draft: this command is not implemented yet by the firmware**<br/>

* value (float): maximum horizontal acceleration [m/s2]<br/>

Result:<br/>
The max horizontal acceleration for autonomous flights is set.<br/>
Then, event [AutonomousFlightMaxHorizontalAccelerationChanged](#ARDrone3-PilotingSettingsState-AutonomousFlightMaxHorizontalAcceleration) is triggered. 

*Supported by no products<br/>* 

<br/>

<!-- ARDrone3-PilotingSettings-setAutonomousFlightMaxVerticalAcceleration-->
### <a name="ARDrone3-PilotingSettings-setAutonomousFlightMaxVerticalAcceleration">Set the maximum vertical acceleration used during autonomous flights</a><br/>
> Set the maximum vertical acceleration used during autonomous flights (not implemented):

```c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxVerticalAcceleration(deviceController->aRDrone3, (float)value);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxVerticalAcceleration(deviceController->aRDrone3, (float)value);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsSetAutonomousFlightMaxVerticalAcceleration((float)value);
```

Set the maximum vertical acceleration used during autonomous flights.<br/>

**Draft: this command is not implemented yet by the firmware**<br/>

* value (float): maximum vertical acceleration [m/s2]<br/>

Result:<br/>
The max vertical acceleration for autonomous flights is set.<br/>
Then, event [AutonomousFlightMaxVerticalAccelerationChanged](#ARDrone3-PilotingSettingsState-AutonomousFlightMaxVerticalAcceleration) is triggered. 

*Supported by no products<br/>* 

<br/>

<!-- ARDrone3-PilotingSettings-setAutonomousFlightMaxRotationSpeed-->
### <a name="ARDrone3-PilotingSettings-setAutonomousFlightMaxRotationSpeed">Set the maximum yaw rotation speed used during autonomous flights</a><br/>
> Set the maximum yaw rotation speed used during autonomous flights (not implemented):

```c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxRotationSpeed(deviceController->aRDrone3, (float)value);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxRotationSpeed(deviceController->aRDrone3, (float)value);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsSetAutonomousFlightMaxRotationSpeed((float)value);
```

Set the maximum yaw rotation speed used during autonomous flights.<br/>

**Draft: this command is not implemented yet by the firmware**<br/>

* value (float): maximum yaw rotation speed [rad/s]<br/>

Result:<br/>
The max rotation speed for autonomous flights is set.<br/>
Then, event [AutonomousFlightMaxRotationSpeedChanged](#ARDrone3-PilotingSettingsState-AutonomousFlightMaxRotationSpeed) is triggered. 

*Supported by no products<br/>* 

<br/>

<!-- ARDrone3-SpeedSettings-MaxVerticalSpeed-->
### <a name="ARDrone3-SpeedSettings-MaxVerticalSpeed">Set Max Vertical speed</a><br/>
> Set Max Vertical speed:

```c
deviceController->aRDrone3->sendSpeedSettingsMaxVerticalSpeed(deviceController->aRDrone3, (float)current);
```

```objective_c
deviceController->aRDrone3->sendSpeedSettingsMaxVerticalSpeed(deviceController->aRDrone3, (float)current);
```

```java
deviceController.getFeatureARDrone3().sendSpeedSettingsMaxVerticalSpeed((float)current);
```

Set Max Vertical speed<br/>

* current (float): Current max vertical speed in m/s<br/>

You can get bounds with event [MaxVerticalSpeedChanged](#ARDrone3-SpeedSettingsState-MaxVerticalSpeedChanged).

Result:<br/>
The max vertical speed is set.<br/>
Then, event [MaxVerticalSpeedChanged](#ARDrone3-SpeedSettingsState-MaxVerticalSpeedChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-SpeedSettings-MaxRotationSpeed-->
### <a name="ARDrone3-SpeedSettings-MaxRotationSpeed">Set Max Rotation speed</a><br/>
> Set Max Rotation speed:

```c
deviceController->aRDrone3->sendSpeedSettingsMaxRotationSpeed(deviceController->aRDrone3, (float)current);
```

```objective_c
deviceController->aRDrone3->sendSpeedSettingsMaxRotationSpeed(deviceController->aRDrone3, (float)current);
```

```java
deviceController.getFeatureARDrone3().sendSpeedSettingsMaxRotationSpeed((float)current);
```

Set Max Rotation speed<br/>

* current (float): Current max rotation speed in degree/s<br/>

You can get bounds with event [MaxRotationSpeedChanged](#ARDrone3-SpeedSettingsState-MaxRotationSpeedChanged).

Result:<br/>
The max rotation speed is set.<br/>
Then, event [MaxRotationSpeedChanged](#ARDrone3-SpeedSettingsState-MaxRotationSpeedChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*


<br/>

<!-- ARDrone3-SpeedSettings-HullProtection-->
### <a name="ARDrone3-SpeedSettings-HullProtection">Presence of hull protection</a><br/>
> Presence of hull protection:

```c
deviceController->aRDrone3->sendSpeedSettingsHullProtection(deviceController->aRDrone3, (uint8_t)present);
```

```objective_c
deviceController->aRDrone3->sendSpeedSettingsHullProtection(deviceController->aRDrone3, (uint8_t)present);
```

```java
deviceController.getFeatureARDrone3().sendSpeedSettingsHullProtection((byte)present);
```

Presence of hull protection<br/>

* present (u8): 1 if present, 0 if not present<br/>

Sending this command is not mandatory, it just helps the drone to modify its wind resistance and adapt its battery decrease model.

Result:<br/>
The presence of the hull is set.<br/>
Then, event [HullProtectionChanged](#ARDrone3-SpeedSettingsState-HullProtectionChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-SpeedSettings-Outdoor-->
### <a name="ARDrone3-SpeedSettings-Outdoor">Outdoor property</a><br/>
> Outdoor property (deprecated):

```c
deviceController->aRDrone3->sendSpeedSettingsOutdoor(deviceController->aRDrone3, (uint8_t)outdoor);
```

```objective_c
deviceController->aRDrone3->sendSpeedSettingsOutdoor(deviceController->aRDrone3, (uint8_t)outdoor);
```

```java
deviceController.getFeatureARDrone3().sendSpeedSettingsOutdoor((byte)outdoor);
```

This command is deprecated, please don't use it.

<!-- ARDrone3-NetworkSettings-WifiSelection-->
### <a name="ARDrone3-NetworkSettings-WifiSelection">Wifi selection</a><br/>
> Wifi selection:

```c
deviceController->aRDrone3->sendNetworkSettingsWifiSelection(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISELECTION_TYPE)type, (eARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISELECTION_BAND)band, (uint8_t)channel);
```

```objective_c
deviceController->aRDrone3->sendNetworkSettingsWifiSelection(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISELECTION_TYPE)type, (eARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISELECTION_BAND)band, (uint8_t)channel);
```

```java
deviceController.getFeatureARDrone3().sendNetworkSettingsWifiSelection((ARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISELECTION_TYPE_ENUM)type, (ARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISELECTION_BAND_ENUM)band, (byte)channel);
```

Select or auto-select channel of choosen band.<br/>

* type (enum): The type of wifi selection (auto, manual)<br/>
   * auto: Auto selection<br/>
   * manual: Manual selection<br/>
* band (enum): The allowed band(s) : 2.4 Ghz, 5 Ghz, or all<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
   * all: Both 2.4 and 5 GHz bands<br/>
* channel (u8): The channel (not used in auto mode)<br/>

Result:<br/>
The wifi channel changes according to given parameters. Watch out, a disconnection might appear.<br/>
Then, event [WifiSelectionChanged](#ARDrone3-NetworkSettingsState-WifiSelectionChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-NetworkSettings-wifiSecurity-->
### <a name="ARDrone3-NetworkSettings-wifiSecurity">Set the wifi security</a><br/>
> Set the wifi security:

```c
deviceController->aRDrone3->sendNetworkSettingsWifiSecurity(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISECURITY_TYPE)type, (char *)key, (eARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISECURITY_KEYTYPE)keyType);
```

```objective_c
deviceController->aRDrone3->sendNetworkSettingsWifiSecurity(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISECURITY_TYPE)type, (char *)key, (eARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISECURITY_KEYTYPE)keyType);
```

```java
deviceController.getFeatureARDrone3().sendNetworkSettingsWifiSecurity((ARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISECURITY_TYPE_ENUM)type, (String)key, (ARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISECURITY_KEYTYPE_ENUM)keyType);
```

Set the wifi security<br/>

* type (enum): The type of wifi security (open, wpa2)<br/>
   * open: Wifi is not protected by any security (default)<br/>
   * wpa2: Wifi is protected by wpa2<br/>
* key (string): The key to secure the network (empty if type is open)<br/>
* keyType (enum): Type of the key<br/>
   * plain: Key is plain text, not encrypted<br/>

The security is changed on the next boot.

Result:<br/>
The wifi security is set.<br/>
Then, event [WifiSecurityChanged](#ARDrone3-NetworkSettingsState-wifiSecurityChanged) is triggered. 

*Not supported by any product for the moment.*

<br/>


<!-- ARDrone3-PictureSettings-PictureFormatSelection-->
### <a name="ARDrone3-PictureSettings-PictureFormatSelection">The format of the photo</a><br/>
> The format of the photo:

```c
deviceController->aRDrone3->sendPictureSettingsPictureFormatSelection(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_PICTUREFORMATSELECTION_TYPE)type);
```

```objective_c
deviceController->aRDrone3->sendPictureSettingsPictureFormatSelection(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_PICTUREFORMATSELECTION_TYPE)type);
```

```java
deviceController.getFeatureARDrone3().sendPictureSettingsPictureFormatSelection((ARCOMMANDS_ARDRONE3_PICTURESETTINGS_PICTUREFORMATSELECTION_TYPE_ENUM)type);
```

The format of the photo<br/>

* type (enum): The type of photo format<br/>
   * raw: Take raw image<br/>
   * jpeg: Take a 4:3 jpeg photo<br/>
   * snapshot: Take a 16:9 snapshot from camera<br/>
   * jpeg_fisheye: Take jpeg fisheye image only<br/>

Please note that the time required to take the picture is highly related to this format.<br/>
Also, please note that if your picture format is different from *snapshot*, picture taking will stop video recording (it will restart after the picture has been taken).

Result:<br/>
The picture format is set.<br/>
Then, event [PictureFormatChanged](#ARDrone3-PictureSettingsState-PictureFormatChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PictureSettings-AutoWhiteBalanceSelection-->
### <a name="ARDrone3-PictureSettings-AutoWhiteBalanceSelection">Set the white balance mode</a><br/>
> Set the white balance mode:

```c
deviceController->aRDrone3->sendPictureSettingsAutoWhiteBalanceSelection(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_AUTOWHITEBALANCESELECTION_TYPE)type);
```

```objective_c
deviceController->aRDrone3->sendPictureSettingsAutoWhiteBalanceSelection(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_AUTOWHITEBALANCESELECTION_TYPE)type);
```

```java
deviceController.getFeatureARDrone3().sendPictureSettingsAutoWhiteBalanceSelection((ARCOMMANDS_ARDRONE3_PICTURESETTINGS_AUTOWHITEBALANCESELECTION_TYPE_ENUM)type);
```

Set the white balance mode.<br/>

* type (enum): The type auto white balance<br/>
   * auto: Auto guess of best white balance params<br/>
   * tungsten: Tungsten white balance<br/>
   * daylight: Daylight white balance<br/>
   * cloudy: Cloudy white balance<br/>
   * cool_white: White balance for a flash<br/>

Result:<br/>
The balance is set.<br/>
Then, event [WhiteBalanceModeChanged](#ARDrone3-PictureSettingsState-AutoWhiteBalanceChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PictureSettings-ExpositionSelection-->
### <a name="ARDrone3-PictureSettings-ExpositionSelection">Set image exposure</a><br/>
> Set image exposure:

```c
deviceController->aRDrone3->sendPictureSettingsExpositionSelection(deviceController->aRDrone3, (float)value);
```

```objective_c
deviceController->aRDrone3->sendPictureSettingsExpositionSelection(deviceController->aRDrone3, (float)value);
```

```java
deviceController.getFeatureARDrone3().sendPictureSettingsExpositionSelection((float)value);
```

Set image exposure.<br/>

* value (float): exposure value (bounds given by ExposureChanged arg min and max, by default [-3:3])<br/>

Bounds can be get with commands [ExposureChanged](#ARDrone3-PictureSettingsState-ExpositionChanged).

Result:<br/>
The exposure is set.<br/>
Then, event [ExposureChanged](#ARDrone3-PictureSettingsState-ExpositionChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PictureSettings-SaturationSelection-->
### <a name="ARDrone3-PictureSettings-SaturationSelection">Set image saturation</a><br/>
> Set image saturation:

```c
deviceController->aRDrone3->sendPictureSettingsSaturationSelection(deviceController->aRDrone3, (float)value);
```

```objective_c
deviceController->aRDrone3->sendPictureSettingsSaturationSelection(deviceController->aRDrone3, (float)value);
```

```java
deviceController.getFeatureARDrone3().sendPictureSettingsSaturationSelection((float)value);
```

Set image saturation.<br/>

* value (float): Saturation value (bounds given by SaturationChanged arg min and max, by default [-100:100])<br/>

Bounds can be get with commands [SaturationChanged](#ARDrone3-PictureSettingsState-SaturationChanged).

Result:<br/>
The saturation is set.<br/>
Then, event [SaturationChanged](#ARDrone3-PictureSettingsState-SaturationChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PictureSettings-TimelapseSelection-->
### <a name="ARDrone3-PictureSettings-TimelapseSelection">Configure timelapse mode</a><br/>
> Configure timelapse mode:

```c
deviceController->aRDrone3->sendPictureSettingsTimelapseSelection(deviceController->aRDrone3, (uint8_t)enabled, (float)interval);
```

```objective_c
deviceController->aRDrone3->sendPictureSettingsTimelapseSelection(deviceController->aRDrone3, (uint8_t)enabled, (float)interval);
```

```java
deviceController.getFeatureARDrone3().sendPictureSettingsTimelapseSelection((byte)enabled, (float)interval);
```

Configure timelapse mode.<br/>

* enabled (u8): 1 if timelapse is enabled, 0 otherwise<br/>
* interval (float): interval in seconds for taking pictures<br/>

Watch out, this command only configure the timelapse mode. Once it is configured, you can start/stop the timelapse with the [RecordVideo](#ARDrone3-MediaRecord-VideoV2) command.

Result:<br/>
The timelapse mode is configured (but not started).<br/>
Then, event [TimelapseModeConfigurationChanged](#ARDrone3-PictureSettingsState-TimelapseChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PictureSettings-VideoAutorecordSelection-->
### <a name="ARDrone3-PictureSettings-VideoAutorecordSelection">Set video autorecord</a><br/>
> Set video autorecord:

```c
deviceController->aRDrone3->sendPictureSettingsVideoAutorecordSelection(deviceController->aRDrone3, (uint8_t)enabled, (uint8_t)mass_storage_id);
```

```objective_c
deviceController->aRDrone3->sendPictureSettingsVideoAutorecordSelection(deviceController->aRDrone3, (uint8_t)enabled, (uint8_t)mass_storage_id);
```

```java
deviceController.getFeatureARDrone3().sendPictureSettingsVideoAutorecordSelection((byte)enabled, (byte)mass_storage_id);
```

Set video autorecord.<br/>

* enabled (u8): 1 if video autorecord is enabled, 0 otherwise<br/>
* mass_storage_id (u8): Mass storage id to take video<br/>

If autorecord is set, video record will be automatically started when the drone takes off and stopped slightly after landing.

Result:<br/>
The autorecord mode is configured.<br/>
Then, event [VideoAutorecordChanged](#ARDrone3-PictureSettingsState-VideoAutorecordChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-MediaStreaming-VideoEnable-->
### <a name="ARDrone3-MediaStreaming-VideoEnable">Enable/disable video streaming.</a><br/>
> Enable/disable video streaming.:

```c
deviceController->aRDrone3->sendMediaStreamingVideoEnable(deviceController->aRDrone3, (uint8_t)enable);
```

```objective_c
deviceController->aRDrone3->sendMediaStreamingVideoEnable(deviceController->aRDrone3, (uint8_t)enable);
```

```java
deviceController.getFeatureARDrone3().sendMediaStreamingVideoEnable((byte)enable);
```

Enable/disable video streaming.<br/>

* enable (u8): 1 to enable, 0 to disable.<br/>

Please note that on Bebop version less that 2.0.57 and Bebop 2 version less that 3.0.6 this command is not needed as the drone starts automatically the stream. To be fully compatible with future versions, you should in any cases send this command if you want to get the video stream.

Result:<br/>
The video stream is started or stopped.<br/>
Then, event [VideoEnableChanged](#ARDrone3-MediaStreamingState-VideoEnableChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-GPSSettings-SetHome-->
### <a name="ARDrone3-GPSSettings-SetHome">Set home location</a><br/>
> Set home location (deprecated):

```c
deviceController->aRDrone3->sendGPSSettingsSetHome(deviceController->aRDrone3, (double)latitude, (double)longitude, (double)altitude);
```

```objective_c
deviceController->aRDrone3->sendGPSSettingsSetHome(deviceController->aRDrone3, (double)latitude, (double)longitude, (double)altitude);
```

```java
deviceController.getFeatureARDrone3().sendGPSSettingsSetHome((double)latitude, (double)longitude, (double)altitude);
```

This command is deprecated, please don't use it.
<br/>

<!-- ARDrone3-GPSSettings-ResetHome-->
### <a name="ARDrone3-GPSSettings-ResetHome">Reset home location</a><br/>
> Reset home location:

```c
deviceController->aRDrone3->sendGPSSettingsResetHome(deviceController->aRDrone3);
```

```objective_c
deviceController->aRDrone3->sendGPSSettingsResetHome(deviceController->aRDrone3);
```

```java
deviceController.getFeatureARDrone3().sendGPSSettingsResetHome();
```

Reset home location. The drone will choose its own home.<br/>

Result:<br/>
The home location is reset.<br/>
Then, event [HomeLocationReset](#ARDrone3-GPSSettingsState-ResetHomeChanged) is triggered with the new home location. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-GPSSettings-SendControllerGPS-->
### <a name="ARDrone3-GPSSettings-SendControllerGPS">Send controller GPS location</a><br/>
> Send controller GPS location:

```c
deviceController->aRDrone3->sendGPSSettingsSendControllerGPS(deviceController->aRDrone3, (double)latitude, (double)longitude, (double)altitude, (double)horizontalAccuracy, (double)verticalAccuracy);
```

```objective_c
deviceController->aRDrone3->sendGPSSettingsSendControllerGPS(deviceController->aRDrone3, (double)latitude, (double)longitude, (double)altitude, (double)horizontalAccuracy, (double)verticalAccuracy);
```

```java
deviceController.getFeatureARDrone3().sendGPSSettingsSendControllerGPS((double)latitude, (double)longitude, (double)altitude, (double)horizontalAccuracy, (double)verticalAccuracy);
```

Send controller GPS location<br/>

* latitude (double): GPS latitude in decimal degrees<br/>
* longitude (double): GPS longitude in decimal degrees<br/>
* altitude (double): GPS altitude in meters<br/>
* horizontalAccuracy (double): Horizontal Accuracy in meter ; equal -1 if no horizontal Accuracy<br/>
* verticalAccuracy (double): Vertical Accuracy in meter ; equal -1 if no vertical Accuracy<br/>

The user location might be used in case of return home, according to the home type and the accuracy of the given position. You can get the current home type with the event [HomeTypeChosenChanged](#ARDrone3-GPSState-HomeTypeChosenChanged).

Result:<br/>
The user position is known by the drone.<br/>
Then, event [HomeChanged](#ARDrone3-GPSSettingsState-HomeChanged) is triggered with the new home location. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*
<br/>

<!-- ARDrone3-GPSSettings-HomeType-->
### <a name="ARDrone3-GPSSettings-HomeType">Set preferred home type</a><br/>
> Set user preference for the type of the home position:

```c
deviceController->aRDrone3->sendGPSSettingsHomeType(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_GPSSETTINGS_HOMETYPE_TYPE)type);
```

```objective_c
deviceController->aRDrone3->sendGPSSettingsHomeType(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_GPSSETTINGS_HOMETYPE_TYPE)type);
```

```java
deviceController.getFeatureARDrone3().sendGPSSettingsHomeType((ARCOMMANDS_ARDRONE3_GPSSETTINGS_HOMETYPE_TYPE_ENUM)type);
```

Set user preference for the type of the home position.<br/>

* type (enum): The type of the home position<br/>
   * TAKEOFF: The drone will try to return to the take off position<br/>
   * PILOT: The drone will try to return to the pilot position<br/>

Please note that this is only a preference. The actual type chosen is given by the event [HomeTypeChosenChanged](#ARDrone3-GPSState-HomeTypeChosenChanged).<br/>
The availability of the choices can be given by the event [HomeTypeAvailabilityChanged](#ARDrone3-GPSState-HomeTypeAvailabilityChanged).

Result:<br/>
The user choice is known by the drone.<br/>
Then, event [HomeTypeChanged](#ARDrone3-GPSSettingsState-HomeTypeChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-GPSSettings-ReturnHomeDelay-->
### <a name="ARDrone3-GPSSettings-ReturnHomeDelay">Set the delay of the return home</a><br/>
> Set the delay of the return home:

```c
deviceController->aRDrone3->sendGPSSettingsReturnHomeDelay(deviceController->aRDrone3, (uint16_t)delay);
```

```objective_c
deviceController->aRDrone3->sendGPSSettingsReturnHomeDelay(deviceController->aRDrone3, (uint16_t)delay);
```

```java
deviceController.getFeatureARDrone3().sendGPSSettingsReturnHomeDelay((short)delay);
```

Set the delay after which the drone will automatically try to return home after a disconnection.<br/>

* delay (u16): Delay in second<br/>

<!--TODO see if used by firmware-->

Result:<br/>
The delay of the return home is set.<br/>
Then, event [ReturnHomeDelayChanged](#ARDrone3-GPSSettingsState-ReturnHomeDelayChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-Antiflickering-electricFrequency-->
### <a name="ARDrone3-Antiflickering-electricFrequency">Set the electric frequency</a><br/>
> Set the electric frequency:

```c
deviceController->aRDrone3->sendAntiflickeringElectricFrequency(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_ANTIFLICKERING_ELECTRICFREQUENCY_FREQUENCY)frequency);
```

```objective_c
deviceController->aRDrone3->sendAntiflickeringElectricFrequency(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_ANTIFLICKERING_ELECTRICFREQUENCY_FREQUENCY)frequency);
```

```java
deviceController.getFeatureARDrone3().sendAntiflickeringElectricFrequency((ARCOMMANDS_ARDRONE3_ANTIFLICKERING_ELECTRICFREQUENCY_FREQUENCY_ENUM)frequency);
```

Set the electric frequency of the country determined by the position of the controller. <br/>
This is used to avoid the video flickering in auto mode. You can get the current antiflickering mode with the event [AntiflickeringModeChanged](#ARDrone3-AntiflickeringState-modeChanged).<br/>

* frequency (enum): Type of the electric frequency<br/>
   * fiftyHertz: Electric frequency of the country is 50hz<br/>
   * sixtyHertz: Electric frequency of the country is 60hz<br/>

Result:<br/>
The electric frequency is set.<br/>
Then, event [ElectricFrequencyChanged](#ARDrone3-AntiflickeringState-electricFrequencyChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-Antiflickering-setMode-->
### <a name="ARDrone3-Antiflickering-setMode">Set the anti flickering mode</a><br/>
> Set the anti flickering mode:

```c
deviceController->aRDrone3->sendAntiflickeringSetMode(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_ANTIFLICKERING_SETMODE_MODE)mode);
```

```objective_c
deviceController->aRDrone3->sendAntiflickeringSetMode(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_ANTIFLICKERING_SETMODE_MODE)mode);
```

```java
deviceController.getFeatureARDrone3().sendAntiflickeringSetMode((ARCOMMANDS_ARDRONE3_ANTIFLICKERING_SETMODE_MODE_ENUM)mode);
```

Set the anti flickering mode<br/>

* mode (enum): Mode of the anti flickering functionnality<br/>
   * auto: Anti flickering based on the electric frequency previously sent<br/>
   * FixedFiftyHertz: Anti flickering based on a fixed frequency of 50Hz<br/>
   * FixedFiftyHertz: Anti flickering based on a fixed frequency of 60Hz<br/>

If auto, the frequency taken in account is the one sent by [SetElectricFrequency](#ARDrone3-Antiflickering-electricFrequency). You can get the current electric frequency with the event [ElectricFrequencyChanged](#ARDrone3-AntiflickeringState-electricFrequencyChanged).<br/>
If auto, the drone will detect when flickers appears on the video and trigger the antiflickering.<br/>
Forcing the antiflickering (*FixedFiftyHertz* or *FixedFiftyHertz*) can reduce luminosity of the video.

Result:<br/>
The antiflickering mode is set.<br/>
Then, event [AntiflickeringModeChanged](#ARDrone3-AntiflickeringState-modeChanged) is triggered. 

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

