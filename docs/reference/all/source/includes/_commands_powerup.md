<!-- powerup-Piloting-PCMD-->
### <a name="powerup-Piloting-PCMD">Ask the Power Up speed and turn ratio.</a><br/>
> Ask the Power Up speed and turn ratio.:

```c
deviceController->powerup->sendPilotingPCMD(deviceController->powerup, (uint8_t)flag, (uint8_t)throttle, (int8_t)roll);
```

```objective_c
deviceController->powerup->sendPilotingPCMD(deviceController->powerup, (uint8_t)flag, (uint8_t)throttle, (int8_t)roll);
```

```java
deviceController.getFeaturePowerup().sendPilotingPCMD((byte)flag, (byte)throttle, (byte)roll);
```

Ask the Power Up speed and turn ratio.<br/>


* flag (u8): Boolean for "touch screen".<br/>
* throttle (u8): Throttle value [0:100].<br/>
* roll (i8): Yaw-roll value. [-100:100]<br/>
<br/>

<!-- powerup-Piloting-UserTakeOff-->
### <a name="powerup-Piloting-UserTakeOff">Set drone in user take off state</a><br/>
> Set drone in user take off state:

```c
deviceController->powerup->sendPilotingUserTakeOff(deviceController->powerup, (uint8_t)state);
```

```objective_c
deviceController->powerup->sendPilotingUserTakeOff(deviceController->powerup, (uint8_t)state);
```

```java
deviceController.getFeaturePowerup().sendPilotingUserTakeOff((byte)state);
```

Set drone in user take off state<br/>


* state (u8): State of user take off mode<br/>
- 1 to enter in user take off.<br/>
- 0 to exit from user take off.<br/>
<br/>

<!-- powerup-Piloting-MotorMode-->
### <a name="powerup-Piloting-MotorMode">Motor mode</a><br/>
> Motor mode:

```c
deviceController->powerup->sendPilotingMotorMode(deviceController->powerup, (eARCOMMANDS_POWERUP_PILOTING_MOTORMODE_MODE)mode);
```

```objective_c
deviceController->powerup->sendPilotingMotorMode(deviceController->powerup, (eARCOMMANDS_POWERUP_PILOTING_MOTORMODE_MODE)mode);
```

```java
deviceController.getFeaturePowerup().sendPilotingMotorMode((ARCOMMANDS_POWERUP_PILOTING_MOTORMODE_MODE_ENUM)mode);
```

Motor mode<br/>


* mode (enum): <br/>
   * normal: The motors will only start on user action after being in state user take off<br/>
   * forced: Motors will use the current pcmd values without considering the flying state<br/>
<br/>

<!-- powerup-PilotingSettings-set-->
### <a name="powerup-PilotingSettings-set">Set the given setting</a><br/>
> Set the given setting:

```c
deviceController->powerup->sendPilotingSettingsSet(deviceController->powerup, (eARCOMMANDS_POWERUP_PILOTINGSETTINGS_SET_SETTING)setting, (float)value);
```

```objective_c
deviceController->powerup->sendPilotingSettingsSet(deviceController->powerup, (eARCOMMANDS_POWERUP_PILOTINGSETTINGS_SET_SETTING)setting, (float)value);
```

```java
deviceController.getFeaturePowerup().sendPilotingSettingsSet((ARCOMMANDS_POWERUP_PILOTINGSETTINGS_SET_SETTING_ENUM)setting, (float)value);
```

Set the given setting<br/>


* setting (enum): Variety of setting that can be customized<br/>
   * MAX_ROLL: Max roll value. In degree.<br/>
   * ROLL_KP: How fast the plane reaches the desired roll angle. No unit.<br/>
   * ROLL_RATE_KP: How fast the plane reaches the desired roll rate. No unit.<br/>
   * MAX_PITCH: Max pitch value. In degree.<br/>
   * MIN_PITCH: Min pitch value. In degree.<br/>
   * PITCH_KP: How fast the plane reaches the desired pitch angle. No unit.<br/>
   * PITCH_RATE_KP: How fast the plane reaches the desired pitch rate. No unit.<br/>
   * YAW_KP: How fast the plane reaches the desired yaw angle. No unit.<br/>
   * YAW_RATE_KP: How fast the plane reaches the desired yaw rate. No unit.<br/>
   * ROLL_TO_THROTTLE_RATE: Portion of thrust that is added to motors according to the roll/yaw<br/>
command to compensate a dive during turn. No unit.<br/>
   * ANGLE_OF_ATTACK: Angle of attack of a plane needed horizontal flight.<br/>
   * ALT_HOLD: Altitude hold during autopilot. 0 for false, other value for true.<br/>
   * ALT_HOLD_THROTTLE: Altitude hold throttle. Expressed in percentage divided by 100 (from 0 to 1).<br/>
   * DR_RSSI_EDGE: Rssi value that indicates that the airplane is close to the pilot.<br/>
   * RECOVERY_DURATION_LIMIT: Limit time for return home duration. In seconds.<br/>
   * WIND_SPEED: Wind speed in m/s. Should be sent before flight.<br/>
   * PLANE_SPEED: Target plane speed in m/s. Should be sent before flight.<br/>
* value (float): value of the given setting<br/>
<br/>

<!-- powerup-MediaRecord-PictureV2-->
### <a name="powerup-MediaRecord-PictureV2">Take picture</a><br/>
> Take picture:

```c
deviceController->powerup->sendMediaRecordPictureV2(deviceController->powerup);
```

```objective_c
deviceController->powerup->sendMediaRecordPictureV2(deviceController->powerup);
```

```java
deviceController.getFeaturePowerup().sendMediaRecordPictureV2();
```

Take picture<br/>


<br/>

<!-- powerup-MediaRecord-VideoV2-->
### <a name="powerup-MediaRecord-VideoV2">Video record</a><br/>
> Video record:

```c
deviceController->powerup->sendMediaRecordVideoV2(deviceController->powerup, (eARCOMMANDS_POWERUP_MEDIARECORD_VIDEOV2_RECORD)record);
```

```objective_c
deviceController->powerup->sendMediaRecordVideoV2(deviceController->powerup, (eARCOMMANDS_POWERUP_MEDIARECORD_VIDEOV2_RECORD)record);
```

```java
deviceController.getFeaturePowerup().sendMediaRecordVideoV2((ARCOMMANDS_POWERUP_MEDIARECORD_VIDEOV2_RECORD_ENUM)record);
```

Video record<br/>


* record (enum): Command to record video<br/>
   * stop: Stop the video recording<br/>
   * start: Start the video recording<br/>
<br/>

<!-- powerup-NetworkSettings-WifiSelection-->
### <a name="powerup-NetworkSettings-WifiSelection">Auto-select channel of choosen band</a><br/>
> Auto-select channel of choosen band:

```c
deviceController->powerup->sendNetworkSettingsWifiSelection(deviceController->powerup, (eARCOMMANDS_POWERUP_NETWORKSETTINGS_WIFISELECTION_TYPE)type, (eARCOMMANDS_POWERUP_NETWORKSETTINGS_WIFISELECTION_BAND)band, (uint8_t)channel);
```

```objective_c
deviceController->powerup->sendNetworkSettingsWifiSelection(deviceController->powerup, (eARCOMMANDS_POWERUP_NETWORKSETTINGS_WIFISELECTION_TYPE)type, (eARCOMMANDS_POWERUP_NETWORKSETTINGS_WIFISELECTION_BAND)band, (uint8_t)channel);
```

```java
deviceController.getFeaturePowerup().sendNetworkSettingsWifiSelection((ARCOMMANDS_POWERUP_NETWORKSETTINGS_WIFISELECTION_TYPE_ENUM)type, (ARCOMMANDS_POWERUP_NETWORKSETTINGS_WIFISELECTION_BAND_ENUM)band, (byte)channel);
```

Auto-select channel of choosen band<br/>


* type (enum): The type of wifi selection (auto, manual)<br/>
   * auto: Auto selection<br/>
   * manual: Manual selection<br/>
* band (enum): The allowed band(s) : 2.4 Ghz, 5 Ghz, or all<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
   * all: Both 2.4 and 5 GHz bands<br/>
* channel (u8): The channel (not used in auto mode)<br/>
<br/>

<!-- powerup-Network-WifiScan-->
### <a name="powerup-Network-WifiScan">Launches wifi network scan</a><br/>
> Launches wifi network scan:

```c
deviceController->powerup->sendNetworkWifiScan(deviceController->powerup, (eARCOMMANDS_POWERUP_NETWORK_WIFISCAN_BAND)band);
```

```objective_c
deviceController->powerup->sendNetworkWifiScan(deviceController->powerup, (eARCOMMANDS_POWERUP_NETWORK_WIFISCAN_BAND)band);
```

```java
deviceController.getFeaturePowerup().sendNetworkWifiScan((ARCOMMANDS_POWERUP_NETWORK_WIFISCAN_BAND_ENUM)band);
```

Launches wifi network scan<br/>


* band (enum): The band(s) : 2.4 Ghz, 5 Ghz, or both<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
   * all: Both 2.4 and 5 GHz bands<br/>
<br/>

<!-- powerup-Network-WifiAuthChannel-->
### <a name="powerup-Network-WifiAuthChannel">Controller inquire the list of authorized wifi channels.</a><br/>
> Controller inquire the list of authorized wifi channels.:

```c
deviceController->powerup->sendNetworkWifiAuthChannel(deviceController->powerup);
```

```objective_c
deviceController->powerup->sendNetworkWifiAuthChannel(deviceController->powerup);
```

```java
deviceController.getFeaturePowerup().sendNetworkWifiAuthChannel();
```

Controller inquire the list of authorized wifi channels.<br/>


<br/>

<!-- powerup-MediaStreaming-VideoEnable-->
### <a name="powerup-MediaStreaming-VideoEnable">Enable/disable video streaming.</a><br/>
> Enable/disable video streaming.:

```c
deviceController->powerup->sendMediaStreamingVideoEnable(deviceController->powerup, (uint8_t)enable);
```

```objective_c
deviceController->powerup->sendMediaStreamingVideoEnable(deviceController->powerup, (uint8_t)enable);
```

```java
deviceController.getFeaturePowerup().sendMediaStreamingVideoEnable((byte)enable);
```

Enable/disable video streaming.<br/>


* enable (u8): 1 to enable, 0 to disable.<br/>
<br/>

<!-- powerup-VideoSettings-Autorecord-->
### <a name="powerup-VideoSettings-Autorecord">Set video automatic recording state.</a><br/>
> Set video automatic recording state.:

```c
deviceController->powerup->sendVideoSettingsAutorecord(deviceController->powerup, (uint8_t)enable);
```

```objective_c
deviceController->powerup->sendVideoSettingsAutorecord(deviceController->powerup, (uint8_t)enable);
```

```java
deviceController.getFeaturePowerup().sendVideoSettingsAutorecord((byte)enable);
```

Set video automatic recording state.<br/>


* enable (u8): 0: Disabled 1: Enabled.<br/>
<br/>

<!-- powerup-VideoSettings-VideoMode-->
### <a name="powerup-VideoSettings-VideoMode">Set video mode</a><br/>
> Set video mode:

```c
deviceController->powerup->sendVideoSettingsVideoMode(deviceController->powerup, (eARCOMMANDS_POWERUP_VIDEOSETTINGS_VIDEOMODE_MODE)mode);
```

```objective_c
deviceController->powerup->sendVideoSettingsVideoMode(deviceController->powerup, (eARCOMMANDS_POWERUP_VIDEOSETTINGS_VIDEOMODE_MODE)mode);
```

```java
deviceController.getFeaturePowerup().sendVideoSettingsVideoMode((ARCOMMANDS_POWERUP_VIDEOSETTINGS_VIDEOMODE_MODE_ENUM)mode);
```

Set video mode<br/>


* mode (enum): Video mode<br/>
   * quality: Maximize video quality (VGA 30fps).<br/>
   * performance: Maximize video performance (QVGA 24fps).<br/>
<br/>

<!-- powerup-Sounds-buzz-->
### <a name="powerup-Sounds-buzz">Enable/disable the buzzer sound</a><br/>
> Enable/disable the buzzer sound:

```c
deviceController->powerup->sendSoundsBuzz(deviceController->powerup, (uint8_t)enable);
```

```objective_c
deviceController->powerup->sendSoundsBuzz(deviceController->powerup, (uint8_t)enable);
```

```java
deviceController.getFeaturePowerup().sendSoundsBuzz((byte)enable);
```

Enable/disable the buzzer sound<br/>


* enable (u8): 0: Disabled 1: Enabled.<br/>
<br/>

