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

Do a flat trim of the accelerometer/gyro.<br/>
Could be useful when the drone is sliding in hover mode.<br/>




Result:<br/>
Accelerometer and gyroscope are calibrated then event [FlatTrimChanged](#ARDrone3-PilotingState-FlatTrimChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


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

Ask the drone to take off.<br/>
On the fixed wings (such as Disco): not used except to cancel a land.<br/>




Result:<br/>
On the quadcopters: the drone takes off if its [FlyingState](#ARDrone3-PilotingState-FlyingStateChanged) was landed.<br/>
On the fixed wings, the landing process is aborted if the [FlyingState](#ARDrone3-PilotingState-FlyingStateChanged) was landing.<br/>
Then, event [FlyingState](#ARDrone3-PilotingState-FlyingStateChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-Piloting-PCMD-->
### <a name="ARDrone3-Piloting-PCMD">Move the drone</a><br/>
> Move the drone:

```c
deviceController->aRDrone3->sendPilotingPCMD(deviceController->aRDrone3, (uint8_t)flag, (int8_t)roll, (int8_t)pitch, (int8_t)yaw, (int8_t)gaz, (uint32_t)timestampAndSeqNum);
```

```objective_c
deviceController->aRDrone3->sendPilotingPCMD(deviceController->aRDrone3, (uint8_t)flag, (int8_t)roll, (int8_t)pitch, (int8_t)yaw, (int8_t)gaz, (uint32_t)timestampAndSeqNum);
```

```java
deviceController.getFeatureARDrone3().sendPilotingPCMD((byte)flag, (byte)roll, (byte)pitch, (byte)yaw, (byte)gaz, (int)timestampAndSeqNum);
```

Move the drone.<br/>
The libARController is sending the command each 50ms.<br/>
<br/>
**Please note that you should call setPilotingPCMD and not sendPilotingPCMD because the libARController is handling the periodicity and the buffer on which it is sent.**<br/>


* flag (u8): Boolean flag: 1 if the roll and pitch values should be taken in consideration. 0 otherwise<br/>
* roll (i8): Roll angle as signed percentage.<br/>
On copters:<br/>
Roll angle expressed as signed percentage of the max pitch/roll setting, in range [-100, 100]<br/>
-100 corresponds to a roll angle of max pitch/roll to the left (drone will fly left)<br/>
100 corresponds to a roll angle of max pitch/roll to the right (drone will fly right)<br/>
This value may be clamped if necessary, in order to respect the maximum supported physical tilt of the copter.<br/>
<br/>
On fixed wings:<br/>
Roll angle expressed as signed percentage of the physical max roll of the wing, in range [-100, 100]<br/>
Negative value makes the plane fly to the left<br/>
Positive value makes the plane fly to the right<br/>
* pitch (i8): Pitch angle as signed percentage.<br/>
On copters:<br/>
Expressed as signed percentage of the max pitch/roll setting, in range [-100, 100]<br/>
-100 corresponds to a pitch angle of max pitch/roll towards sky (drone will fly backward)<br/>
100 corresponds to a pitch angle of max pitch/roll towards ground (drone will fly forward)<br/>
This value may be clamped if necessary, in order to respect the maximum supported physical tilt of the copter.<br/>
<br/>
On fixed wings:<br/>
Expressed as signed percentage of the physical max pitch of the wing, in range [-100, 100]<br/>
Negative value makes the plane fly in direction of the sky<br/>
Positive value makes the plane fly in direction of the ground<br/>
* yaw (i8): Yaw rotation speed as signed percentage.<br/>
On copters:<br/>
Expressed as signed percentage of the max yaw rotation speed setting, in range [-100, 100].<br/>
-100 corresponds to a counter-clockwise rotation of max yaw rotation speed<br/>
100 corresponds to a clockwise rotation of max yaw rotation speed<br/>
This value may be clamped if necessary, in order to respect the maximum supported physical tilt of the copter.<br/>
<br/>
On fixed wings:<br/>
Giving more than a fixed value (75% for the moment) triggers a circle.<br/>
Positive value will trigger a clockwise circling<br/>
Negative value will trigger a counter-clockwise circling<br/>
* gaz (i8): Throttle as signed percentage.<br/>
On copters:<br/>
Expressed as signed percentage of the max vertical speed setting, in range [-100, 100]<br/>
-100 corresponds to a max vertical speed towards ground<br/>
100 corresponds to a max vertical speed towards sky<br/>
This value may be clamped if necessary, in order to respect the maximum supported physical tilt of the copter.<br/>
During the landing phase, putting some positive gaz will cancel the land.<br/>
<br/>
On fixed wings:<br/>
Expressed as signed percentage of the physical max throttle, in range [-100, 100]<br/>
Negative value makes the plane fly slower<br/>
Positive value makes the plane fly faster<br/>
* timestampAndSeqNum (u32): Command timestamp in milliseconds (low 24 bits) + command sequence number (high 8 bits) [0;255].<br/>


Result:<br/>
The drone moves! Yaaaaay!<br/>
Event [SpeedChanged](#ARDrone3-PilotingState-SpeedChanged), [AttitudeChanged](#ARDrone3-PilotingState-AttitudeChanged) and [PositionChanged](#ARDrone3-PilotingState-PositionChanged) (only if gps of the drone has fixed) are triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-Piloting-Landing-->
### <a name="ARDrone3-Piloting-Landing">Land</a><br/>
> Land:

```c
deviceController->aRDrone3->sendPilotingLanding(deviceController->aRDrone3);
```

```objective_c
deviceController->aRDrone3->sendPilotingLanding(deviceController->aRDrone3);
```

```java
deviceController.getFeatureARDrone3().sendPilotingLanding();
```

Land.<br/>
Please note that on copters, if you put some positive gaz (in the [PilotingCommand](#ARDrone3-Piloting-PCMD)) during the landing, it will cancel it.<br/>




Result:<br/>
On the copters, the drone lands if its [FlyingState](#ARDrone3-PilotingState-FlyingStateChanged) was taking off, hovering or flying.<br/>
On the fixed wings, the drone lands if its [FlyingState](#ARDrone3-PilotingState-FlyingStateChanged) was hovering or flying.<br/>
Then, event [FlyingState](#ARDrone3-PilotingState-FlyingStateChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-Piloting-Emergency-->
### <a name="ARDrone3-Piloting-Emergency">Cut out the motors</a><br/>
> Cut out the motors:

```c
deviceController->aRDrone3->sendPilotingEmergency(deviceController->aRDrone3);
```

```objective_c
deviceController->aRDrone3->sendPilotingEmergency(deviceController->aRDrone3);
```

```java
deviceController.getFeatureARDrone3().sendPilotingEmergency();
```

Cut out the motors.<br/>
This cuts immediatly the motors. The drone will fall.<br/>
This command is sent on a dedicated high priority buffer which will infinitely retry to send it if the command is not delivered.<br/>




Result:<br/>
The drone immediatly cuts off its motors.<br/>
Then, event [FlyingState](#ARDrone3-PilotingState-FlyingStateChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-Piloting-NavigateHome-->
### <a name="ARDrone3-Piloting-NavigateHome">Return home</a><br/>
> Return home:

```c
deviceController->aRDrone3->sendPilotingNavigateHome(deviceController->aRDrone3, (uint8_t)start);
```

```objective_c
deviceController->aRDrone3->sendPilotingNavigateHome(deviceController->aRDrone3, (uint8_t)start);
```

```java
deviceController.getFeatureARDrone3().sendPilotingNavigateHome((byte)start);
```

Return home.<br/>
Ask the drone to fly to its [HomePosition](#ARDrone3-GPSSettingsState-HomeChanged).<br/>
The availability of the return home can be get from [ReturnHomeState](#ARDrone3-PilotingState-NavigateHomeStateChanged).<br/>
Please note that the drone will wait to be hovering to start its return home. This means that it will wait to have a [flag](#ARDrone3-Piloting-PCMD) set at 0.<br/>


* start (u8): 1 to start the navigate home, 0 to stop it<br/>


Result:<br/>
The drone will fly back to its home position.<br/>
Then, event [ReturnHomeState](#ARDrone3-PilotingState-NavigateHomeStateChanged) is triggered.<br/>
You can get a state pending if the drone is not ready to start its return home process but will do it as soon as it is possible.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-Piloting-moveBy-->
### <a name="ARDrone3-Piloting-moveBy">Move the drone to a relative position</a><br/>
> Move the drone to a relative position:

```c
deviceController->aRDrone3->sendPilotingMoveBy(deviceController->aRDrone3, (float)dX, (float)dY, (float)dZ, (float)dPsi);
```

```objective_c
deviceController->aRDrone3->sendPilotingMoveBy(deviceController->aRDrone3, (float)dX, (float)dY, (float)dZ, (float)dPsi);
```

```java
deviceController.getFeatureARDrone3().sendPilotingMoveBy((float)dX, (float)dY, (float)dZ, (float)dPsi);
```

Move the drone to a relative position and rotate heading by a given angle.<br/>
Moves are relative to the current drone orientation, (drone's reference).<br/>
Also note that the given rotation will not modify the move (i.e. moves are always rectilinear).<br/>


* dX (float): Wanted displacement along the front axis [m]<br/>
* dY (float): Wanted displacement along the right axis [m]<br/>
* dZ (float): Wanted displacement along the down axis [m]<br/>
* dPsi (float): Wanted rotation of heading [rad]<br/>


Result:<br/>
The drone will move of the given offsets.<br/>
Then, event [RelativeMoveEnded](#ARDrone3-PilotingEvent-moveByEnd) is triggered.<br/>
If you send a second relative move command, the drone will trigger a [RelativeMoveEnded](#ARDrone3-PilotingEvent-moveByEnd) with the offsets it managed to do before this new command and the value of error set to interrupted.<br/>


*Supported by <br/>*

- *Bebop since 3.3.0*<br/>
- *Bebop 2 since 3.3.0*<br/>


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

Make a flip.<br/>


* direction (enum): Direction for the flip<br/>
   * front: Flip direction front<br/>
   * back: Flip direction back<br/>
   * right: Flip direction right<br/>
   * left: Flip direction left<br/>


Result:<br/>
The drone will make a flip if it has enough battery.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>


<br/>

<!-- ARDrone3-Camera-Orientation-->
### <a name="ARDrone3-Camera-Orientation">Move the camera (deprecated)</a><br/>
> Move the camera (deprecated):

```c
deviceController->aRDrone3->sendCameraOrientation(deviceController->aRDrone3, (int8_t)tilt, (int8_t)pan);
```

```objective_c
deviceController->aRDrone3->sendCameraOrientation(deviceController->aRDrone3, (int8_t)tilt, (int8_t)pan);
```

```java
deviceController.getFeatureARDrone3().sendCameraOrientation((byte)tilt, (byte)pan);
```

*This message is deprecated.*<br/>

Move the camera.<br/>
You can get min and max values for tilt and pan using [CameraInfo](#common-CameraSettingsState-CameraSettingsChanged).<br/>


* tilt (i8): Tilt camera consign for the drone (in degree)<br/>
The value is saturated by the drone.<br/>
Saturation value is sent by thre drone through CameraSettingsChanged command.<br/>
* pan (i8): Pan camera consign for the drone (in degree)<br/>
The value is saturated by the drone.<br/>
Saturation value is sent by thre drone through CameraSettingsChanged command.<br/>


Result:<br/>
The drone moves its camera.<br/>
Then, event [CameraOrientation](#ARDrone3-CameraState-Orientation) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-Camera-OrientationV2-->
### <a name="ARDrone3-Camera-OrientationV2">Move the camera</a><br/>
> Move the camera:

```c
deviceController->aRDrone3->sendCameraOrientationV2(deviceController->aRDrone3, (float)tilt, (float)pan);
```

```objective_c
deviceController->aRDrone3->sendCameraOrientationV2(deviceController->aRDrone3, (float)tilt, (float)pan);
```

```java
deviceController.getFeatureARDrone3().sendCameraOrientationV2((float)tilt, (float)pan);
```

Move the camera.<br/>
You can get min and max values for tilt and pan using [CameraInfo](#common-CameraSettingsState-CameraSettingsChanged).<br/>


* tilt (float): Tilt camera consign for the drone (in degree)<br/>
The value is saturated by the drone.<br/>
Saturation value is sent by thre drone through CameraSettingsChanged command.<br/>
* pan (float): Pan camera consign for the drone (in degree)<br/>
The value is saturated by the drone.<br/>
Saturation value is sent by thre drone through CameraSettingsChanged command.<br/>


Result:<br/>
The drone moves its camera.<br/>
Then, event [CameraOrientationV2](#ARDrone3-CameraState-OrientationV2) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-Camera-Velocity-->
### <a name="ARDrone3-Camera-Velocity">Move the camera using velocity</a><br/>
> Move the camera using velocity:

```c
deviceController->aRDrone3->sendCameraVelocity(deviceController->aRDrone3, (float)tilt, (float)pan);
```

```objective_c
deviceController->aRDrone3->sendCameraVelocity(deviceController->aRDrone3, (float)tilt, (float)pan);
```

```java
deviceController.getFeatureARDrone3().sendCameraVelocity((float)tilt, (float)pan);
```

Move the camera given velocity consign.<br/>
You can get min and max values for tilt and pan using [CameraVelocityRange](#ARDrone3-CameraState-VelocityRange).<br/>


* tilt (float): Tilt camera velocity consign [deg/s]<br/>
Negative tilt velocity move camera to bottom<br/>
Positive tilt velocity move camera to top<br/>
* pan (float): Pan camera velocity consign [deg/s]<br/>
Negative pan velocity move camera to left<br/>
Positive pan velocity move camera to right<br/>


Result:<br/>
The drone moves its camera.<br/>
Then, event [CameraOrientationV2](#ARDrone3-CameraState-OrientationV2) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-MediaRecord-PictureV2-->
### <a name="ARDrone3-MediaRecord-PictureV2">Take a picture</a><br/>
> Take a picture:

```c
deviceController->aRDrone3->sendMediaRecordPictureV2(deviceController->aRDrone3);
```

```objective_c
deviceController->aRDrone3->sendMediaRecordPictureV2(deviceController->aRDrone3);
```

```java
deviceController.getFeatureARDrone3().sendMediaRecordPictureV2();
```

Take a picture.<br/>
The type of picture taken is related to the picture setting.<br/>
You can set the picture format by sending the command [SetPictureFormat](#ARDrone3-PictureSettings-PictureFormatSelection). You can also get the current picture format with [PictureFormat](#ARDrone3-PictureSettingsState-PictureFormatChanged).<br/>
Please note that the time required to take the picture is highly related to this format.<br/>
<br/>
You can check if the picture taking is available with [PictureState](#ARDrone3-MediaRecordState-PictureStateChangedV2).<br/>
Also, please note that if your picture format is different from snapshot, picture taking will stop video recording (it will restart after that the picture has been taken).<br/>




Result:<br/>
Event [PictureState](#ARDrone3-MediaRecordState-PictureStateChangedV2) will be triggered with a state busy.<br/>
The drone will take a picture.<br/>
Then, when picture has been taken, notification [PictureEvent](#ARDrone3-MediaRecordEvent-PictureEventChanged) is triggered.<br/>
And normally [PictureState](#ARDrone3-MediaRecordState-PictureStateChangedV2) will be triggered with a state ready.<br/>


*Supported by <br/>*

- *Bebop since 2.0.1*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-MediaRecord-VideoV2-->
### <a name="ARDrone3-MediaRecord-VideoV2">Record a video</a><br/>
> Record a video:

```c
deviceController->aRDrone3->sendMediaRecordVideoV2(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_MEDIARECORD_VIDEOV2_RECORD)record);
```

```objective_c
deviceController->aRDrone3->sendMediaRecordVideoV2(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_MEDIARECORD_VIDEOV2_RECORD)record);
```

```java
deviceController.getFeatureARDrone3().sendMediaRecordVideoV2((ARCOMMANDS_ARDRONE3_MEDIARECORD_VIDEOV2_RECORD_ENUM)record);
```

Record a video (or start timelapse).<br/>
You can check if the video recording is available with [VideoState](#ARDrone3-MediaRecordState-VideoStateChangedV2).<br/>
This command can start a video (obvious huh?), but also a timelapse if the timelapse mode is set. You can check if the timelapse mode is set with the event [TimelapseMode](#ARDrone3-PictureSettingsState-TimelapseChanged).<br/>
Also, please note that if your picture format is different from snapshot, picture taking will stop video recording (it will restart after the picture has been taken).<br/>


* record (enum): Command to record video<br/>
   * stop: Stop the video recording<br/>
   * start: Start the video recording<br/>


Result:<br/>
The drone will begin or stop to record the video (or timelapse).<br/>
Then, event [VideoState](#ARDrone3-MediaRecordState-VideoStateChangedV2) will be triggered. Also, notification [VideoEvent](#ARDrone3-MediaRecordEvent-VideoEventChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop since 2.0.1*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


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

Scan wifi network to get a list of all networks found by the drone<br/>


* band (enum): The band(s) : 2.4 Ghz, 5 Ghz, or both<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
   * all: Both 2.4 and 5 GHz bands<br/>


Result:<br/>
Event [WifiScanResults](#ARDrone3-NetworkState-WifiScanListChanged) is triggered with all networks found.<br/>
When all networks have been sent, event [WifiScanEnded](#ARDrone3-NetworkState-AllWifiScanChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-Network-WifiAuthChannel-->
### <a name="ARDrone3-Network-WifiAuthChannel">Ask for available wifi channels</a><br/>
> Ask for available wifi channels:

```c
deviceController->aRDrone3->sendNetworkWifiAuthChannel(deviceController->aRDrone3);
```

```objective_c
deviceController->aRDrone3->sendNetworkWifiAuthChannel(deviceController->aRDrone3);
```

```java
deviceController.getFeatureARDrone3().sendNetworkWifiAuthChannel();
```

Ask for available wifi channels.<br/>
The list of available Wifi channels is related to the country of the drone. You can get this country from the event [CountryChanged](#common-SettingsState-CountryChanged).<br/>




Result:<br/>
Event [AvailableWifiChannels](#ARDrone3-NetworkState-WifiAuthChannelListChanged) is triggered with all available channels. When all channels have been sent, event [AvailableWifiChannelsCompleted](#ARDrone3-NetworkState-AllWifiAuthChannelChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-PilotingSettings-MaxAltitude-->
### <a name="ARDrone3-PilotingSettings-MaxAltitude">Set max altitude</a><br/>
> Set max altitude:

```c
deviceController->aRDrone3->sendPilotingSettingsMaxAltitude(deviceController->aRDrone3, (float)current);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsMaxAltitude(deviceController->aRDrone3, (float)current);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsMaxAltitude((float)current);
```

Set max altitude.<br/>
The drone will not fly over this max altitude when it is in manual piloting.<br/>
Please note that if you set a max altitude which is below the current drone altitude, the drone will not go to given max altitude.<br/>
You can get the bounds in the event [MaxAltitude](#ARDrone3-PilotingSettingsState-MaxAltitudeChanged).<br/>


* current (float): Current altitude max in m<br/>


Result:<br/>
The max altitude is set.<br/>
Then, event [MaxAltitude](#ARDrone3-PilotingSettingsState-MaxAltitudeChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-PilotingSettings-MaxTilt-->
### <a name="ARDrone3-PilotingSettings-MaxTilt">Set max pitch/roll</a><br/>
> Set max pitch/roll:

```c
deviceController->aRDrone3->sendPilotingSettingsMaxTilt(deviceController->aRDrone3, (float)current);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsMaxTilt(deviceController->aRDrone3, (float)current);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsMaxTilt((float)current);
```

Set max pitch/roll.<br/>
This represent the max inclination allowed by the drone.<br/>
You can get the bounds with the commands [MaxPitchRoll](#ARDrone3-PilotingSettingsState-MaxTiltChanged).<br/>


* current (float): Current tilt max in degree<br/>


Result:<br/>
The max pitch/roll is set.<br/>
Then, event [MaxPitchRoll](#ARDrone3-PilotingSettingsState-MaxTiltChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>


<br/>

<!-- ARDrone3-PilotingSettings-MaxDistance-->
### <a name="ARDrone3-PilotingSettings-MaxDistance">Set max distance</a><br/>
> Set max distance:

```c
deviceController->aRDrone3->sendPilotingSettingsMaxDistance(deviceController->aRDrone3, (float)value);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsMaxDistance(deviceController->aRDrone3, (float)value);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsMaxDistance((float)value);
```

Set max distance.<br/>
You can get the bounds from the event [MaxDistance](#ARDrone3-PilotingSettingsState-MaxDistanceChanged).<br/>
<br/>
If [Geofence](#ARDrone3-PilotingSettingsState-NoFlyOverMaxDistanceChanged) is activated, the drone won't fly over the given max distance.<br/>


* value (float): Current max distance in meter<br/>


Result:<br/>
The max distance is set.<br/>
Then, event [MaxDistance](#ARDrone3-PilotingSettingsState-MaxDistanceChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-PilotingSettings-NoFlyOverMaxDistance-->
### <a name="ARDrone3-PilotingSettings-NoFlyOverMaxDistance">Enable geofence</a><br/>
> Enable geofence:

```c
deviceController->aRDrone3->sendPilotingSettingsNoFlyOverMaxDistance(deviceController->aRDrone3, (uint8_t)shouldNotFlyOver);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsNoFlyOverMaxDistance(deviceController->aRDrone3, (uint8_t)shouldNotFlyOver);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsNoFlyOverMaxDistance((byte)shouldNotFlyOver);
```

Enable geofence.<br/>
If geofence is enabled, the drone won't fly over the given max distance.<br/>
You can get the max distance from the event [MaxDistance](#ARDrone3-PilotingSettingsState-MaxDistanceChanged).<br/>
For copters: the distance is computed from the controller position, if this position is not known, it will use the take off.<br/>
For fixed wings: the distance is computed from the take off position.<br/>


* shouldNotFlyOver (u8): 1 if the drone can't fly further than max distance, 0 if no limitation on the drone should be done<br/>


Result:<br/>
Geofencing is enabled or disabled.<br/>
Then, event [Geofencing](#ARDrone3-PilotingSettingsState-NoFlyOverMaxDistanceChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-PilotingSettings-setAutonomousFlightMaxHorizontalSpeed-->
### <a name="ARDrone3-PilotingSettings-setAutonomousFlightMaxHorizontalSpeed">Set autonomous flight max horizontal speed</a><br/>
> Set autonomous flight max horizontal speed:

```c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxHorizontalSpeed(deviceController->aRDrone3, (float)value);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxHorizontalSpeed(deviceController->aRDrone3, (float)value);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsSetAutonomousFlightMaxHorizontalSpeed((float)value);
```

Set autonomous flight max horizontal speed.<br/>
This will only be used during autonomous flights such as moveBy.<br/>


* value (float): maximum horizontal speed [m/s]<br/>


Result:<br/>
The max horizontal speed is set.<br/>
Then, event [AutonomousFlightMaxHorizontalSpeed](#ARDrone3-PilotingSettingsState-AutonomousFlightMaxHorizontalSpeed) is triggered.<br/>


*Supported by <br/>*

- *Bebop since 3.3.0*<br/>
- *Bebop 2 since 3.3.0*<br/>


<br/>

<!-- ARDrone3-PilotingSettings-setAutonomousFlightMaxVerticalSpeed-->
### <a name="ARDrone3-PilotingSettings-setAutonomousFlightMaxVerticalSpeed">Set autonomous flight max vertical speed</a><br/>
> Set autonomous flight max vertical speed:

```c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxVerticalSpeed(deviceController->aRDrone3, (float)value);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxVerticalSpeed(deviceController->aRDrone3, (float)value);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsSetAutonomousFlightMaxVerticalSpeed((float)value);
```

Set autonomous flight max vertical speed.<br/>
This will only be used during autonomous flights such as moveBy.<br/>


* value (float): maximum vertical speed [m/s]<br/>


Result:<br/>
The max vertical speed is set.<br/>
Then, event [AutonomousFlightMaxVerticalSpeed](#ARDrone3-PilotingSettingsState-AutonomousFlightMaxVerticalSpeed) is triggered.<br/>


*Supported by <br/>*

- *Bebop since 3.3.0*<br/>
- *Bebop 2 since 3.3.0*<br/>


<br/>

<!-- ARDrone3-PilotingSettings-setAutonomousFlightMaxHorizontalAcceleration-->
### <a name="ARDrone3-PilotingSettings-setAutonomousFlightMaxHorizontalAcceleration">Set autonomous flight max horizontal acceleration</a><br/>
> Set autonomous flight max horizontal acceleration:

```c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxHorizontalAcceleration(deviceController->aRDrone3, (float)value);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxHorizontalAcceleration(deviceController->aRDrone3, (float)value);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsSetAutonomousFlightMaxHorizontalAcceleration((float)value);
```

Set autonomous flight max horizontal acceleration.<br/>
This will only be used during autonomous flights such as moveBy.<br/>


* value (float): maximum horizontal acceleration [m/s2]<br/>


Result:<br/>
The max horizontal acceleration is set.<br/>
Then, event [AutonomousFlightMaxHorizontalAcceleration](#ARDrone3-PilotingSettingsState-AutonomousFlightMaxHorizontalAcceleration) is triggered.<br/>


*Supported by <br/>*

- *Bebop since 3.3.0*<br/>
- *Bebop 2 since 3.3.0*<br/>


<br/>

<!-- ARDrone3-PilotingSettings-setAutonomousFlightMaxVerticalAcceleration-->
### <a name="ARDrone3-PilotingSettings-setAutonomousFlightMaxVerticalAcceleration">Set autonomous flight max vertical acceleration</a><br/>
> Set autonomous flight max vertical acceleration:

```c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxVerticalAcceleration(deviceController->aRDrone3, (float)value);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxVerticalAcceleration(deviceController->aRDrone3, (float)value);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsSetAutonomousFlightMaxVerticalAcceleration((float)value);
```

Set autonomous flight max vertical acceleration.<br/>
This will only be used during autonomous flights such as moveBy.<br/>


* value (float): maximum vertical acceleration [m/s2]<br/>


Result:<br/>
The max vertical acceleration is set.<br/>
Then, event [AutonomousFlightMaxVerticalAcceleration](#ARDrone3-PilotingSettingsState-AutonomousFlightMaxVerticalAcceleration) is triggered.<br/>


*Supported by <br/>*

- *Bebop since 3.3.0*<br/>
- *Bebop 2 since 3.3.0*<br/>


<br/>

<!-- ARDrone3-PilotingSettings-setAutonomousFlightMaxRotationSpeed-->
### <a name="ARDrone3-PilotingSettings-setAutonomousFlightMaxRotationSpeed">Set autonomous flight max rotation speed</a><br/>
> Set autonomous flight max rotation speed:

```c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxRotationSpeed(deviceController->aRDrone3, (float)value);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsSetAutonomousFlightMaxRotationSpeed(deviceController->aRDrone3, (float)value);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsSetAutonomousFlightMaxRotationSpeed((float)value);
```

Set autonomous flight max rotation speed.<br/>
This will only be used during autonomous flights such as moveBy.<br/>


* value (float): maximum yaw rotation speed [deg/s]<br/>


Result:<br/>
The max rotation speed is set.<br/>
Then, event [AutonomousFlightMaxRotationSpeed](#ARDrone3-PilotingSettingsState-AutonomousFlightMaxRotationSpeed) is triggered.<br/>


*Supported by <br/>*

- *Bebop since 3.3.0*<br/>
- *Bebop 2 since 3.3.0*<br/>


<br/>

<!-- ARDrone3-PilotingSettings-BankedTurn-->
### <a name="ARDrone3-PilotingSettings-BankedTurn">Set banked turn mode</a><br/>
> Set banked turn mode:

```c
deviceController->aRDrone3->sendPilotingSettingsBankedTurn(deviceController->aRDrone3, (uint8_t)value);
```

```objective_c
deviceController->aRDrone3->sendPilotingSettingsBankedTurn(deviceController->aRDrone3, (uint8_t)value);
```

```java
deviceController.getFeatureARDrone3().sendPilotingSettingsBankedTurn((byte)value);
```

Set banked turn mode.<br/>
When banked turn mode is enabled, the drone will use yaw values from the piloting command to infer with roll and pitch on the drone when its horizontal speed is not null.<br/>


* value (u8): 1 to enable, 0 to disable<br/>


Result:<br/>
The banked turn mode is enabled or disabled.<br/>
Then, event [BankedTurnMode](#ARDrone3-PilotingSettingsState-BankedTurnChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop since 3.2.0*<br/>
- *Bebop 2 since 3.2.0*<br/>


<br/>

<!-- ARDrone3-SpeedSettings-MaxVerticalSpeed-->
### <a name="ARDrone3-SpeedSettings-MaxVerticalSpeed">Set max vertical speed</a><br/>
> Set max vertical speed:

```c
deviceController->aRDrone3->sendSpeedSettingsMaxVerticalSpeed(deviceController->aRDrone3, (float)current);
```

```objective_c
deviceController->aRDrone3->sendSpeedSettingsMaxVerticalSpeed(deviceController->aRDrone3, (float)current);
```

```java
deviceController.getFeatureARDrone3().sendSpeedSettingsMaxVerticalSpeed((float)current);
```

Set max vertical speed.<br/>


* current (float): Current max vertical speed in m/s<br/>


Result:<br/>
The max vertical speed is set.<br/>
Then, event [MaxVerticalSpeed](#ARDrone3-SpeedSettingsState-MaxVerticalSpeedChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>


<br/>

<!-- ARDrone3-SpeedSettings-MaxRotationSpeed-->
### <a name="ARDrone3-SpeedSettings-MaxRotationSpeed">Set max rotation speed</a><br/>
> Set max rotation speed:

```c
deviceController->aRDrone3->sendSpeedSettingsMaxRotationSpeed(deviceController->aRDrone3, (float)current);
```

```objective_c
deviceController->aRDrone3->sendSpeedSettingsMaxRotationSpeed(deviceController->aRDrone3, (float)current);
```

```java
deviceController.getFeatureARDrone3().sendSpeedSettingsMaxRotationSpeed((float)current);
```

Set max rotation speed.<br/>


* current (float): Current max yaw rotation speed in degree/s<br/>


Result:<br/>
The max rotation speed is set.<br/>
Then, event [MaxRotationSpeed](#ARDrone3-SpeedSettingsState-MaxRotationSpeedChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>


<br/>

<!-- ARDrone3-SpeedSettings-HullProtection-->
### <a name="ARDrone3-SpeedSettings-HullProtection">Set the presence of hull protection</a><br/>
> Set the presence of hull protection:

```c
deviceController->aRDrone3->sendSpeedSettingsHullProtection(deviceController->aRDrone3, (uint8_t)present);
```

```objective_c
deviceController->aRDrone3->sendSpeedSettingsHullProtection(deviceController->aRDrone3, (uint8_t)present);
```

```java
deviceController.getFeatureARDrone3().sendSpeedSettingsHullProtection((byte)present);
```

Set the presence of hull protection.<br/>


* present (u8): 1 if present, 0 if not present<br/>


Result:<br/>
The drone knows that it has a hull protection.<br/>
Then, event [HullProtection](#ARDrone3-SpeedSettingsState-HullProtectionChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>


<br/>

<!-- ARDrone3-SpeedSettings-MaxPitchRollRotationSpeed-->
### <a name="ARDrone3-SpeedSettings-MaxPitchRollRotationSpeed">Set max pitch/roll rotation speed</a><br/>
> Set max pitch/roll rotation speed:

```c
deviceController->aRDrone3->sendSpeedSettingsMaxPitchRollRotationSpeed(deviceController->aRDrone3, (float)current);
```

```objective_c
deviceController->aRDrone3->sendSpeedSettingsMaxPitchRollRotationSpeed(deviceController->aRDrone3, (float)current);
```

```java
deviceController.getFeatureARDrone3().sendSpeedSettingsMaxPitchRollRotationSpeed((float)current);
```

Set max pitch/roll rotation speed.<br/>


* current (float): Current max pitch/roll rotation speed in degree/s<br/>


Result:<br/>
The max pitch/roll rotation speed is set.<br/>
Then, event [MaxPitchRollRotationSpeed](#ARDrone3-SpeedSettingsState-MaxPitchRollRotationSpeedChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>


<br/>

<!-- ARDrone3-NetworkSettings-WifiSelection-->
### <a name="ARDrone3-NetworkSettings-WifiSelection">Select Wifi</a><br/>
> Select Wifi:

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
Then, event [WifiSelection](#ARDrone3-NetworkSettingsState-WifiSelectionChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-NetworkSettings-wifiSecurity-->
### <a name="ARDrone3-NetworkSettings-wifiSecurity">Set wifi security type</a><br/>
> Set wifi security type:

```c
deviceController->aRDrone3->sendNetworkSettingsWifiSecurity(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISECURITY_TYPE)type, (char *)key, (eARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISECURITY_KEYTYPE)keyType);
```

```objective_c
deviceController->aRDrone3->sendNetworkSettingsWifiSecurity(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISECURITY_TYPE)type, (char *)key, (eARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISECURITY_KEYTYPE)keyType);
```

```java
deviceController.getFeatureARDrone3().sendNetworkSettingsWifiSecurity((ARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISECURITY_TYPE_ENUM)type, (String)key, (ARCOMMANDS_ARDRONE3_NETWORKSETTINGS_WIFISECURITY_KEYTYPE_ENUM)keyType);
```

Set wifi security type.<br/>
The security will be changed on the next restart<br/>


* type (enum): The type of wifi security (open, wpa2)<br/>
   * open: Wifi is not protected by any security (default)<br/>
   * wpa2: Wifi is protected by wpa2<br/>
* key (string): The key to secure the network (empty if type is open)<br/>
* keyType (enum): Type of the key<br/>
   * plain: Key is plain text, not encrypted<br/>


Result:<br/>
The wifi security is set (but not applied until next restart).<br/>
Then, event [WifiSecurityType](#ARDrone3-NetworkSettingsState-wifiSecurity) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-PictureSettings-PictureFormatSelection-->
### <a name="ARDrone3-PictureSettings-PictureFormatSelection">Set picture format</a><br/>
> Set picture format:

```c
deviceController->aRDrone3->sendPictureSettingsPictureFormatSelection(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_PICTUREFORMATSELECTION_TYPE)type);
```

```objective_c
deviceController->aRDrone3->sendPictureSettingsPictureFormatSelection(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_PICTUREFORMATSELECTION_TYPE)type);
```

```java
deviceController.getFeatureARDrone3().sendPictureSettingsPictureFormatSelection((ARCOMMANDS_ARDRONE3_PICTURESETTINGS_PICTUREFORMATSELECTION_TYPE_ENUM)type);
```

Set picture format.<br/>
Please note that the time required to take the picture is highly related to this format.<br/>
Also, please note that if your picture format is different from snapshot, picture taking will stop video recording (it will restart after the picture has been taken).<br/>


* type (enum): The type of photo format<br/>
   * raw: Take raw image<br/>
   * jpeg: Take a 4:3 jpeg photo<br/>
   * snapshot: Take a 16:9 snapshot from camera<br/>
   * jpeg_fisheye: Take jpeg fisheye image only<br/>


Result:<br/>
The picture format is set.<br/>
Then, event [PictureFormat](#ARDrone3-PictureSettingsState-PictureFormatChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-PictureSettings-AutoWhiteBalanceSelection-->
### <a name="ARDrone3-PictureSettings-AutoWhiteBalanceSelection">Set White Balance mode</a><br/>
> Set White Balance mode:

```c
deviceController->aRDrone3->sendPictureSettingsAutoWhiteBalanceSelection(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_AUTOWHITEBALANCESELECTION_TYPE)type);
```

```objective_c
deviceController->aRDrone3->sendPictureSettingsAutoWhiteBalanceSelection(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_AUTOWHITEBALANCESELECTION_TYPE)type);
```

```java
deviceController.getFeatureARDrone3().sendPictureSettingsAutoWhiteBalanceSelection((ARCOMMANDS_ARDRONE3_PICTURESETTINGS_AUTOWHITEBALANCESELECTION_TYPE_ENUM)type);
```

Set White Balance mode.<br/>


* type (enum): The type auto white balance<br/>
   * auto: Auto guess of best white balance params<br/>
   * tungsten: Tungsten white balance<br/>
   * daylight: Daylight white balance<br/>
   * cloudy: Cloudy white balance<br/>
   * cool_white: White balance for a flash<br/>


Result:<br/>
The white balance mode is set.<br/>
Then, event [WhiteBalanceMode](#ARDrone3-PictureSettingsState-AutoWhiteBalanceChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


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


* value (float): Exposition value (bounds given by ExpositionChanged arg min and max, by default [-3:3])<br/>


Result:<br/>
The exposure is set.<br/>
Then, event [ImageExposure](#ARDrone3-PictureSettingsState-ExpositionChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


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


Result:<br/>
The saturation is set.<br/>
Then, event [ImageSaturation](#ARDrone3-PictureSettingsState-SaturationChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-PictureSettings-TimelapseSelection-->
### <a name="ARDrone3-PictureSettings-TimelapseSelection">Set timelapse mode</a><br/>
> Set timelapse mode:

```c
deviceController->aRDrone3->sendPictureSettingsTimelapseSelection(deviceController->aRDrone3, (uint8_t)enabled, (float)interval);
```

```objective_c
deviceController->aRDrone3->sendPictureSettingsTimelapseSelection(deviceController->aRDrone3, (uint8_t)enabled, (float)interval);
```

```java
deviceController.getFeatureARDrone3().sendPictureSettingsTimelapseSelection((byte)enabled, (float)interval);
```

Set timelapse mode.<br/>
If timelapse mode is set, instead of taking a video, the drone will take picture regularly.<br/>
Watch out, this command only configure the timelapse mode. Once it is configured, you can start/stop the timelapse with the [RecordVideo](#ARDrone3-MediaRecord-VideoV2) command.<br/>


* enabled (u8): 1 if timelapse is enabled, 0 otherwise<br/>
* interval (float): interval in seconds for taking pictures<br/>


Result:<br/>
The timelapse mode is set (but not started).<br/>
Then, event [TimelapseMode](#ARDrone3-PictureSettingsState-TimelapseChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-PictureSettings-VideoAutorecordSelection-->
### <a name="ARDrone3-PictureSettings-VideoAutorecordSelection">Set video autorecord mode</a><br/>
> Set video autorecord mode:

```c
deviceController->aRDrone3->sendPictureSettingsVideoAutorecordSelection(deviceController->aRDrone3, (uint8_t)enabled, (uint8_t)mass_storage_id);
```

```objective_c
deviceController->aRDrone3->sendPictureSettingsVideoAutorecordSelection(deviceController->aRDrone3, (uint8_t)enabled, (uint8_t)mass_storage_id);
```

```java
deviceController.getFeatureARDrone3().sendPictureSettingsVideoAutorecordSelection((byte)enabled, (byte)mass_storage_id);
```

Set video autorecord mode.<br/>
If autorecord is set, video record will be automatically started when the drone takes off and stopped slightly after landing.<br/>


* enabled (u8): 1 if video autorecord is enabled, 0 otherwise<br/>
* mass_storage_id (u8): Mass storage id to take video<br/>


Result:<br/>
The autorecord mode is set.<br/>
Then, event [AutorecordMode](#ARDrone3-PictureSettingsState-VideoAutorecordChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-PictureSettings-VideoStabilizationMode-->
### <a name="ARDrone3-PictureSettings-VideoStabilizationMode">Set video stabilization mode</a><br/>
> Set video stabilization mode:

```c
deviceController->aRDrone3->sendPictureSettingsVideoStabilizationMode(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_VIDEOSTABILIZATIONMODE_MODE)mode);
```

```objective_c
deviceController->aRDrone3->sendPictureSettingsVideoStabilizationMode(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_VIDEOSTABILIZATIONMODE_MODE)mode);
```

```java
deviceController.getFeatureARDrone3().sendPictureSettingsVideoStabilizationMode((ARCOMMANDS_ARDRONE3_PICTURESETTINGS_VIDEOSTABILIZATIONMODE_MODE_ENUM)mode);
```

Set video stabilization mode.<br/>


* mode (enum): Video stabilization mode<br/>
   * roll_pitch: Video flat on roll and pitch<br/>
   * pitch: Video flat on pitch only<br/>
   * roll: Video flat on roll only<br/>
   * none: Video follows drone angles<br/>


Result:<br/>
The video stabilization mode is set.<br/>
Then, event [VideoStabilizationMode](#ARDrone3-PictureSettingsState-VideoStabilizationModeChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop since 3.4.0*<br/>
- *Bebop 2 since 3.4.0*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-PictureSettings-VideoRecordingMode-->
### <a name="ARDrone3-PictureSettings-VideoRecordingMode">Set video recording mode</a><br/>
> Set video recording mode:

```c
deviceController->aRDrone3->sendPictureSettingsVideoRecordingMode(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_VIDEORECORDINGMODE_MODE)mode);
```

```objective_c
deviceController->aRDrone3->sendPictureSettingsVideoRecordingMode(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_VIDEORECORDINGMODE_MODE)mode);
```

```java
deviceController.getFeatureARDrone3().sendPictureSettingsVideoRecordingMode((ARCOMMANDS_ARDRONE3_PICTURESETTINGS_VIDEORECORDINGMODE_MODE_ENUM)mode);
```

Set video recording mode.<br/>


* mode (enum): Video recording mode<br/>
   * quality: Maximize recording quality.<br/>
   * time: Maximize recording time.<br/>


Result:<br/>
The video recording mode is set.<br/>
Then, event [VideoRecordingMode](#ARDrone3-PictureSettingsState-VideoRecordingModeChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop since 3.4.0*<br/>
- *Bebop 2 since 3.4.0*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-PictureSettings-VideoFramerate-->
### <a name="ARDrone3-PictureSettings-VideoFramerate">Set video framerate</a><br/>
> Set video framerate:

```c
deviceController->aRDrone3->sendPictureSettingsVideoFramerate(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_VIDEOFRAMERATE_FRAMERATE)framerate);
```

```objective_c
deviceController->aRDrone3->sendPictureSettingsVideoFramerate(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_VIDEOFRAMERATE_FRAMERATE)framerate);
```

```java
deviceController.getFeatureARDrone3().sendPictureSettingsVideoFramerate((ARCOMMANDS_ARDRONE3_PICTURESETTINGS_VIDEOFRAMERATE_FRAMERATE_ENUM)framerate);
```

Set video framerate.<br/>


* framerate (enum): Video framerate<br/>
   * 24_FPS: 23.976 frames per second.<br/>
   * 25_FPS: 25 frames per second.<br/>
   * 30_FPS: 29.97 frames per second.<br/>


Result:<br/>
The video framerate is set.<br/>
Then, event [VideoFramerate](#ARDrone3-PictureSettingsState-VideoFramerateChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop since 3.4.0*<br/>
- *Bebop 2 since 3.4.0*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-PictureSettings-VideoResolutions-->
### <a name="ARDrone3-PictureSettings-VideoResolutions">Set video resolutions</a><br/>
> Set video resolutions:

```c
deviceController->aRDrone3->sendPictureSettingsVideoResolutions(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_VIDEORESOLUTIONS_TYPE)type);
```

```objective_c
deviceController->aRDrone3->sendPictureSettingsVideoResolutions(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_PICTURESETTINGS_VIDEORESOLUTIONS_TYPE)type);
```

```java
deviceController.getFeatureARDrone3().sendPictureSettingsVideoResolutions((ARCOMMANDS_ARDRONE3_PICTURESETTINGS_VIDEORESOLUTIONS_TYPE_ENUM)type);
```

Set video streaming and recording resolutions.<br/>


* type (enum): Video streaming and recording resolutions<br/>
   * rec1080_stream480: 1080p recording, 480p streaming.<br/>
   * rec720_stream720: 720p recording, 720p streaming.<br/>


Result:<br/>
The video resolutions is set.<br/>
Then, event [VideoResolutions](#ARDrone3-PictureSettingsState-VideoResolutionsChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop since 3.4.0*<br/>
- *Bebop 2 since 3.4.0*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-MediaStreaming-VideoEnable-->
### <a name="ARDrone3-MediaStreaming-VideoEnable">Enable/disable video streaming</a><br/>
> Enable/disable video streaming:

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


Result:<br/>
The video stream is started or stopped.<br/>
Then, event [VideoStreamState](#ARDrone3-MediaStreamingState-VideoEnableChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-GPSSettings-ResetHome-->
### <a name="ARDrone3-GPSSettings-ResetHome">Reset home position</a><br/>
> Reset home position:

```c
deviceController->aRDrone3->sendGPSSettingsResetHome(deviceController->aRDrone3);
```

```objective_c
deviceController->aRDrone3->sendGPSSettingsResetHome(deviceController->aRDrone3);
```

```java
deviceController.getFeatureARDrone3().sendGPSSettingsResetHome();
```

Reset home position.<br/>




Result:<br/>
The home position is reset.<br/>
Then, event [HomeLocationReset](#ARDrone3-GPSSettingsState-ResetHomeChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-GPSSettings-SendControllerGPS-->
### <a name="ARDrone3-GPSSettings-SendControllerGPS">Set controller gps location</a><br/>
> Set controller gps location:

```c
deviceController->aRDrone3->sendGPSSettingsSendControllerGPS(deviceController->aRDrone3, (double)latitude, (double)longitude, (double)altitude, (double)horizontalAccuracy, (double)verticalAccuracy);
```

```objective_c
deviceController->aRDrone3->sendGPSSettingsSendControllerGPS(deviceController->aRDrone3, (double)latitude, (double)longitude, (double)altitude, (double)horizontalAccuracy, (double)verticalAccuracy);
```

```java
deviceController.getFeatureARDrone3().sendGPSSettingsSendControllerGPS((double)latitude, (double)longitude, (double)altitude, (double)horizontalAccuracy, (double)verticalAccuracy);
```

Set controller gps location.<br/>
The user location might be used in case of return home, according to the home type and the accuracy of the given position. You can get the current home type with the event [HomeType](#ARDrone3-GPSSettingsState-HomeTypeChanged).<br/>


* latitude (double): GPS latitude in decimal degrees<br/>
* longitude (double): GPS longitude in decimal degrees<br/>
* altitude (double): GPS altitude in meters<br/>
* horizontalAccuracy (double): Horizontal Accuracy in meter ; equal -1 if no horizontal Accuracy<br/>
* verticalAccuracy (double): Vertical Accuracy in meter ; equal -1 if no vertical Accuracy<br/>


Result:<br/>
The controller position is known by the drone.<br/>
Then, event [HomeLocation](#ARDrone3-GPSSettingsState-GPSFixStateChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-GPSSettings-HomeType-->
### <a name="ARDrone3-GPSSettings-HomeType">Set the preferred home type</a><br/>
> Set the preferred home type:

```c
deviceController->aRDrone3->sendGPSSettingsHomeType(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_GPSSETTINGS_HOMETYPE_TYPE)type);
```

```objective_c
deviceController->aRDrone3->sendGPSSettingsHomeType(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_GPSSETTINGS_HOMETYPE_TYPE)type);
```

```java
deviceController.getFeatureARDrone3().sendGPSSettingsHomeType((ARCOMMANDS_ARDRONE3_GPSSETTINGS_HOMETYPE_TYPE_ENUM)type);
```

Set the preferred home type.<br/>
Please note that this is only a preference. The actual type chosen is given by the event [HomeType](#ARDrone3-GPSState-HomeTypeChosenChanged).<br/>
You can get the currently available types with the event [HomeTypeAvailability](#ARDrone3-GPSState-HomeTypeAvailabilityChanged).<br/>


* type (enum): The type of the home position<br/>
   * TAKEOFF: The drone will try to return to the take off position<br/>
   * PILOT: The drone will try to return to the pilot position<br/>
   * FOLLOWEE: The drone will try to return to the target of the current (or last) follow me<br/>


Result:<br/>
The user choice is known by the drone.<br/>
Then, event [PreferredHomeType](#ARDrone3-GPSSettingsState-HomeTypeChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-GPSSettings-ReturnHomeDelay-->
### <a name="ARDrone3-GPSSettings-ReturnHomeDelay">Set the return home delay</a><br/>
> Set the return home delay:

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


Result:<br/>
The delay of the return home is set.<br/>
Then, event [ReturnHomeDelay](#ARDrone3-GPSSettingsState-ReturnHomeDelayChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


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

Set the electric frequency of the surrounding lights.<br/>
This is used to avoid the video flickering in auto mode. You can get the current antiflickering mode with the event [AntiflickeringModeChanged](#ARDrone3-AntiflickeringState-modeChanged).<br/>


* frequency (enum): Type of the electric frequency<br/>
   * fiftyHertz: Electric frequency of the country is 50hz<br/>
   * sixtyHertz: Electric frequency of the country is 60hz<br/>


Result:<br/>
The electric frequency is set.<br/>
Then, event [ElectricFrequency](#ARDrone3-AntiflickeringState-electricFrequencyChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

<!-- ARDrone3-Antiflickering-setMode-->
### <a name="ARDrone3-Antiflickering-setMode">Set the antiflickering mode</a><br/>
> Set the antiflickering mode:

```c
deviceController->aRDrone3->sendAntiflickeringSetMode(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_ANTIFLICKERING_SETMODE_MODE)mode);
```

```objective_c
deviceController->aRDrone3->sendAntiflickeringSetMode(deviceController->aRDrone3, (eARCOMMANDS_ARDRONE3_ANTIFLICKERING_SETMODE_MODE)mode);
```

```java
deviceController.getFeatureARDrone3().sendAntiflickeringSetMode((ARCOMMANDS_ARDRONE3_ANTIFLICKERING_SETMODE_MODE_ENUM)mode);
```

Set the antiflickering mode.<br/>
If auto, the drone will detect when flickers appears on the video and trigger the antiflickering.<br/>
In this case, this electric frequency it will use will be the one specified in the event [ElectricFrequency](#ARDrone3-Antiflickering-electricFrequency).<br/>
Forcing the antiflickering (FixedFiftyHertz or FixedFiftyHertz) can reduce luminosity of the video.<br/>


* mode (enum): Mode of the anti flickering functionnality<br/>
   * auto: Anti flickering based on the electric frequency previously sent<br/>
   * FixedFiftyHertz: Anti flickering based on a fixed frequency of 50Hz<br/>
   * FixedSixtyHertz: Anti flickering based on a fixed frequency of 60Hz<br/>


Result:<br/>
The antiflickering mode is set.<br/>
Then, event [AntiflickeringMode](#ARDrone3-AntiflickeringState-modeChanged) is triggered.<br/>


*Supported by <br/>*

- *Bebop*<br/>
- *Bebop 2*<br/>
- *Disco*<br/>


<br/>

