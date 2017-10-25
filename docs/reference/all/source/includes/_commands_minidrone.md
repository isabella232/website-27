<!-- MiniDrone-Piloting-FlatTrim-->
### <a name="MiniDrone-Piloting-FlatTrim">Do a flat trim</a><br/>
> Do a flat trim:

```c
deviceController->miniDrone->sendPilotingFlatTrim(deviceController->miniDrone);
```

```objective_c
deviceController->miniDrone->sendPilotingFlatTrim(deviceController->miniDrone);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingFlatTrim();
```

Do a flat trim<br/>


<br/>

<!-- MiniDrone-Piloting-TakeOff-->
### <a name="MiniDrone-Piloting-TakeOff">Ask the drone to take off</a><br/>
> Ask the drone to take off:

```c
deviceController->miniDrone->sendPilotingTakeOff(deviceController->miniDrone);
```

```objective_c
deviceController->miniDrone->sendPilotingTakeOff(deviceController->miniDrone);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingTakeOff();
```

Ask the drone to take off<br/>


<br/>

<!-- MiniDrone-Piloting-PCMD-->
### <a name="MiniDrone-Piloting-PCMD">Ask the drone to move around.</a><br/>
> Ask the drone to move around.:

```c
deviceController->miniDrone->sendPilotingPCMD(deviceController->miniDrone, (uint8_t)flag, (int8_t)roll, (int8_t)pitch, (int8_t)yaw, (int8_t)gaz, (uint32_t)timestamp);
```

```objective_c
deviceController->miniDrone->sendPilotingPCMD(deviceController->miniDrone, (uint8_t)flag, (int8_t)roll, (int8_t)pitch, (int8_t)yaw, (int8_t)gaz, (uint32_t)timestamp);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingPCMD((byte)flag, (byte)roll, (byte)pitch, (byte)yaw, (byte)gaz, (int)timestamp);
```

Ask the drone to move around.<br/>


* flag (u8): Boolean flag to activate roll/pitch movement<br/>
* roll (i8): Roll consign for the MiniDrone [-100;100]<br/>
* pitch (i8): Pitch consign for the MiniDrone [-100;100]<br/>
* yaw (i8): Yaw consign for the MiniDrone [-100;100]<br/>
* gaz (i8): Gaz consign for the MiniDrone [-100;100]<br/>
* timestamp (u32): Timestamp in miliseconds. Not an absolute time. (Typically 0 = time of connexion).<br/>
<br/>

<!-- MiniDrone-Piloting-Landing-->
### <a name="MiniDrone-Piloting-Landing">Ask the MiniDrone to land</a><br/>
> Ask the MiniDrone to land:

```c
deviceController->miniDrone->sendPilotingLanding(deviceController->miniDrone);
```

```objective_c
deviceController->miniDrone->sendPilotingLanding(deviceController->miniDrone);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingLanding();
```

Ask the MiniDrone to land<br/>


<br/>

<!-- MiniDrone-Piloting-Emergency-->
### <a name="MiniDrone-Piloting-Emergency">Put drone in emergency state</a><br/>
> Put drone in emergency state:

```c
deviceController->miniDrone->sendPilotingEmergency(deviceController->miniDrone);
```

```objective_c
deviceController->miniDrone->sendPilotingEmergency(deviceController->miniDrone);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingEmergency();
```

Put drone in emergency state<br/>


<br/>

<!-- MiniDrone-Piloting-AutoTakeOffMode-->
### <a name="MiniDrone-Piloting-AutoTakeOffMode">Set MiniDrone automatic take off mode</a><br/>
> Set MiniDrone automatic take off mode:

```c
deviceController->miniDrone->sendPilotingAutoTakeOffMode(deviceController->miniDrone, (uint8_t)state);
```

```objective_c
deviceController->miniDrone->sendPilotingAutoTakeOffMode(deviceController->miniDrone, (uint8_t)state);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingAutoTakeOffMode((byte)state);
```

Set MiniDrone automatic take off mode<br/>


* state (u8): State of automatic take off mode<br/>
<br/>

<!-- MiniDrone-Piloting-FlyingMode-->
### <a name="MiniDrone-Piloting-FlyingMode">Set drone FlyingMode. Only supported by WingX</a><br/>
> Set drone FlyingMode. Only supported by WingX:

```c
deviceController->miniDrone->sendPilotingFlyingMode(deviceController->miniDrone, (eARCOMMANDS_MINIDRONE_PILOTING_FLYINGMODE_MODE)mode);
```

```objective_c
deviceController->miniDrone->sendPilotingFlyingMode(deviceController->miniDrone, (eARCOMMANDS_MINIDRONE_PILOTING_FLYINGMODE_MODE)mode);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingFlyingMode((ARCOMMANDS_MINIDRONE_PILOTING_FLYINGMODE_MODE_ENUM)mode);
```

Set drone FlyingMode. Only supported by WingX<br/>


* mode (enum): Drone Flying Mode<br/>
   * quadricopter: Fly as a quadrictopter<br/>
   * plane_forward: Fly as a plane in forward mode<br/>
   * plane_backward: Fly as a plane in backward mode<br/>
<br/>

<!-- MiniDrone-Piloting-PlaneGearBox-->
### <a name="MiniDrone-Piloting-PlaneGearBox">Set Plane Gear Box. Only supported by WingX</a><br/>
> Set Plane Gear Box. Only supported by WingX:

```c
deviceController->miniDrone->sendPilotingPlaneGearBox(deviceController->miniDrone, (eARCOMMANDS_MINIDRONE_PILOTING_PLANEGEARBOX_STATE)state);
```

```objective_c
deviceController->miniDrone->sendPilotingPlaneGearBox(deviceController->miniDrone, (eARCOMMANDS_MINIDRONE_PILOTING_PLANEGEARBOX_STATE)state);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingPlaneGearBox((ARCOMMANDS_MINIDRONE_PILOTING_PLANEGEARBOX_STATE_ENUM)state);
```

Set Plane Gear Box. Only supported by WingX<br/>


* state (enum): Plane Gear Box<br/>
   * gear_1: Gear 1. Low speed<br/>
   * gear_2: Gear 2. Middle speed<br/>
   * gear_3: Gear 3. High speed<br/>
<br/>

<!-- MiniDrone-Piloting-TogglePilotingMode-->
### <a name="MiniDrone-Piloting-TogglePilotingMode">Command to toggle between "easy" piloting mode and "preferred" piloting mode.</a><br/>
> Command to toggle between "easy" piloting mode and "preferred" piloting mode.:

```c
deviceController->miniDrone->sendPilotingTogglePilotingMode(deviceController->miniDrone);
```

```objective_c
deviceController->miniDrone->sendPilotingTogglePilotingMode(deviceController->miniDrone);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingTogglePilotingMode();
```

Command to toggle between "easy" piloting mode and "preferred" piloting mode.<br/>
This command only works while the drone is flying.<br/>


<br/>

<!-- MiniDrone-Animations-Flip-->
### <a name="MiniDrone-Animations-Flip">Make a flip</a><br/>
> Make a flip:

```c
deviceController->miniDrone->sendAnimationsFlip(deviceController->miniDrone, (eARCOMMANDS_MINIDRONE_ANIMATIONS_FLIP_DIRECTION)direction);
```

```objective_c
deviceController->miniDrone->sendAnimationsFlip(deviceController->miniDrone, (eARCOMMANDS_MINIDRONE_ANIMATIONS_FLIP_DIRECTION)direction);
```

```java
deviceController.getFeatureMiniDrone().sendAnimationsFlip((ARCOMMANDS_MINIDRONE_ANIMATIONS_FLIP_DIRECTION_ENUM)direction);
```

Make a flip<br/>


* direction (enum): Direction for the flip<br/>
   * front: Flip direction front<br/>
   * back: Flip direction back<br/>
   * right: Flip direction right<br/>
   * left: Flip direction left<br/>
<br/>

<!-- MiniDrone-Animations-Cap-->
### <a name="MiniDrone-Animations-Cap">Change the product cap</a><br/>
> Change the product cap:

```c
deviceController->miniDrone->sendAnimationsCap(deviceController->miniDrone, (int16_t)offset);
```

```objective_c
deviceController->miniDrone->sendAnimationsCap(deviceController->miniDrone, (int16_t)offset);
```

```java
deviceController.getFeatureMiniDrone().sendAnimationsCap((short)offset);
```

Change the product cap<br/>


* offset (i16): Change the cap with offset angle [-180;180]<br/>
<br/>

<!-- MiniDrone-MediaRecord-Picture-->
### <a name="MiniDrone-MediaRecord-Picture">@deprecated</a><br/>
> @deprecated:

```c
deviceController->miniDrone->sendMediaRecordPicture(deviceController->miniDrone, (uint8_t)mass_storage_id);
```

```objective_c
deviceController->miniDrone->sendMediaRecordPicture(deviceController->miniDrone, (uint8_t)mass_storage_id);
```

```java
deviceController.getFeatureMiniDrone().sendMediaRecordPicture((byte)mass_storage_id);
```

@deprecated<br/>
Take picture<br/>


* mass_storage_id (u8): Mass storage id to take picture<br/>
<br/>

<!-- MiniDrone-MediaRecord-PictureV2-->
### <a name="MiniDrone-MediaRecord-PictureV2">Take picture</a><br/>
> Take picture:

```c
deviceController->miniDrone->sendMediaRecordPictureV2(deviceController->miniDrone);
```

```objective_c
deviceController->miniDrone->sendMediaRecordPictureV2(deviceController->miniDrone);
```

```java
deviceController.getFeatureMiniDrone().sendMediaRecordPictureV2();
```

Take picture<br/>


<br/>

<!-- MiniDrone-PilotingSettings-MaxAltitude-->
### <a name="MiniDrone-PilotingSettings-MaxAltitude">Set Max Altitude</a><br/>
> Set Max Altitude:

```c
deviceController->miniDrone->sendPilotingSettingsMaxAltitude(deviceController->miniDrone, (float)current);
```

```objective_c
deviceController->miniDrone->sendPilotingSettingsMaxAltitude(deviceController->miniDrone, (float)current);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingSettingsMaxAltitude((float)current);
```

Set Max Altitude<br/>


* current (float): Current altitude max in m<br/>
<br/>

<!-- MiniDrone-PilotingSettings-MaxTilt-->
### <a name="MiniDrone-PilotingSettings-MaxTilt">Set Max Tilt</a><br/>
> Set Max Tilt:

```c
deviceController->miniDrone->sendPilotingSettingsMaxTilt(deviceController->miniDrone, (float)current);
```

```objective_c
deviceController->miniDrone->sendPilotingSettingsMaxTilt(deviceController->miniDrone, (float)current);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingSettingsMaxTilt((float)current);
```

Set Max Tilt<br/>


* current (float): Current tilt max in degree<br/>
<br/>

<!-- MiniDrone-PilotingSettings-BankedTurn-->
### <a name="MiniDrone-PilotingSettings-BankedTurn">Set banked turn mode</a><br/>
> Set banked turn mode:

```c
deviceController->miniDrone->sendPilotingSettingsBankedTurn(deviceController->miniDrone, (uint8_t)value);
```

```objective_c
deviceController->miniDrone->sendPilotingSettingsBankedTurn(deviceController->miniDrone, (uint8_t)value);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingSettingsBankedTurn((byte)value);
```

Set banked turn mode.<br/>
When banked turn mode is enabled, the drone will use yaw values from the piloting command to infer with roll and pitch on the drone when its horizontal speed is not null.<br/>


* value (u8): 1 to enable, 0 to disable<br/>


Result:<br/>
The banked turn mode is enabled or disabled.<br/>
Then, event [BankedTurnMode](#MiniDrone-PilotingSettingsState-BankedTurnChanged) is triggered.<br/>


*Supported by <br/>*

- *Mambo since 3.0.6*<br/>


<br/>

<!-- MiniDrone-PilotingSettings-MaxThrottle-->
### <a name="MiniDrone-PilotingSettings-MaxThrottle">This setting represents the vertical acceleration command that will be sent to the drone when piloting in gaz mode.</a><br/>
> This setting represents the vertical acceleration command that will be sent to the drone when piloting in gaz mode.:

```c
deviceController->miniDrone->sendPilotingSettingsMaxThrottle(deviceController->miniDrone, (float)max);
```

```objective_c
deviceController->miniDrone->sendPilotingSettingsMaxThrottle(deviceController->miniDrone, (float)max);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingSettingsMaxThrottle((float)max);
```

This setting represents the vertical acceleration command that will be sent to the drone when piloting in gaz mode.<br/>
In this case, closed loop height control is no longer performed; an open loop vertical acceleration command is generated instead.<br/>
This command results from multiplying the user command coming from the joystick (float value between 0 and 1) by the MaxThrottle setting (also a value between 0 and 1) and by the gravity constant.<br/>
Thus, we obtain the corresponding value in [m/s²] that will then be mixed with the attitude commands and translated into rotation speeds.<br/>
As an example, if the value of this setting is 0.5, the maximal acceleration command that can be generated when the user command equals 1 is :<br/>
acc_cmd_max = 1 * 0.5 * 9.81 m/s² = 4.905 m/s².<br/>


* max (float): Max throttle, between 0 and 1.<br/>
<br/>

<!-- MiniDrone-PilotingSettings-PreferredPilotingMode-->
### <a name="MiniDrone-PilotingSettings-PreferredPilotingMode">The flight envelope of Mambo FPV has been divided in three piloting modes.</a><br/>
> The flight envelope of Mambo FPV has been divided in three piloting modes.:

```c
deviceController->miniDrone->sendPilotingSettingsPreferredPilotingMode(deviceController->miniDrone, (eARCOMMANDS_MINIDRONE_PILOTINGSETTINGS_PREFERREDPILOTINGMODE_MODE)mode);
```

```objective_c
deviceController->miniDrone->sendPilotingSettingsPreferredPilotingMode(deviceController->miniDrone, (eARCOMMANDS_MINIDRONE_PILOTINGSETTINGS_PREFERREDPILOTINGMODE_MODE)mode);
```

```java
deviceController.getFeatureMiniDrone().sendPilotingSettingsPreferredPilotingMode((ARCOMMANDS_MINIDRONE_PILOTINGSETTINGS_PREFERREDPILOTINGMODE_MODE_ENUM)mode);
```

The flight envelope of Mambo FPV has been divided in three piloting modes.<br/>


* mode (enum): Piloting modes.<br/>
   * easy: The flight envelope of Mambo FPV has been divided in three piloting modes.<br/>
The first one corresponds to the well-known flying mode currently used for<br/>
Mambo, which is based in an horizontal stabilisation (performed via the<br/>
vertical camera and the acceleration information) and a vertical acceleration<br/>
(by means of the ultrasound, the barometer and the vertical accelerometer) in<br/>
order for the drone to stay in fixed point position when no piloting commands<br/>
are sent by the user.<br/>
   * medium: The second piloting mode consists of deactivating the horizontal stabilisation.<br/>
Thus, in this flying mode, when no piloting command is received, the drone will<br/>
try to stay at 0° tilt angle instead of responding to a 0 m/s horizontal speed<br/>
reference. This behaviour will result in a slight horizontal drift.<br/>
   * difficult: The third piloting mode also adds the vertical stabilisation deactivation and,<br/>
therefore, a slight vertical drift. When flying in the third mode, a closed<br/>
loop height control is no longer performed in order for the drone to keep a<br/>
certain height and vertical speed. Instead, the vertical command coming from<br/>
the user will directly generate an open loop acceleration command.<br/>
<br/>

<!-- MiniDrone-SpeedSettings-MaxVerticalSpeed-->
### <a name="MiniDrone-SpeedSettings-MaxVerticalSpeed">Set Max Vertical speed</a><br/>
> Set Max Vertical speed:

```c
deviceController->miniDrone->sendSpeedSettingsMaxVerticalSpeed(deviceController->miniDrone, (float)current);
```

```objective_c
deviceController->miniDrone->sendSpeedSettingsMaxVerticalSpeed(deviceController->miniDrone, (float)current);
```

```java
deviceController.getFeatureMiniDrone().sendSpeedSettingsMaxVerticalSpeed((float)current);
```

Set Max Vertical speed<br/>


* current (float): Current max vertical speed in m/s<br/>
<br/>

<!-- MiniDrone-SpeedSettings-MaxRotationSpeed-->
### <a name="MiniDrone-SpeedSettings-MaxRotationSpeed">Set Max Rotation speed</a><br/>
> Set Max Rotation speed:

```c
deviceController->miniDrone->sendSpeedSettingsMaxRotationSpeed(deviceController->miniDrone, (float)current);
```

```objective_c
deviceController->miniDrone->sendSpeedSettingsMaxRotationSpeed(deviceController->miniDrone, (float)current);
```

```java
deviceController.getFeatureMiniDrone().sendSpeedSettingsMaxRotationSpeed((float)current);
```

Set Max Rotation speed<br/>


* current (float): Current max rotation speed in degree/s<br/>
<br/>

<!-- MiniDrone-SpeedSettings-Wheels-->
### <a name="MiniDrone-SpeedSettings-Wheels">Presence of wheels</a><br/>
> Presence of wheels:

```c
deviceController->miniDrone->sendSpeedSettingsWheels(deviceController->miniDrone, (uint8_t)present);
```

```objective_c
deviceController->miniDrone->sendSpeedSettingsWheels(deviceController->miniDrone, (uint8_t)present);
```

```java
deviceController.getFeatureMiniDrone().sendSpeedSettingsWheels((byte)present);
```

Presence of wheels<br/>


* present (u8): 1 if present, 0 if not present<br/>
<br/>

<!-- MiniDrone-SpeedSettings-MaxHorizontalSpeed-->
### <a name="MiniDrone-SpeedSettings-MaxHorizontalSpeed">Set Max Horizontal speed (only used in case where PilotingSettings_MaxTilt is not used like in hydrofoil mode)</a><br/>
> Set Max Horizontal speed (only used in case where PilotingSettings_MaxTilt is not used like in hydrofoil mode):

```c
deviceController->miniDrone->sendSpeedSettingsMaxHorizontalSpeed(deviceController->miniDrone, (float)current);
```

```objective_c
deviceController->miniDrone->sendSpeedSettingsMaxHorizontalSpeed(deviceController->miniDrone, (float)current);
```

```java
deviceController.getFeatureMiniDrone().sendSpeedSettingsMaxHorizontalSpeed((float)current);
```

Set Max Horizontal speed (only used in case where PilotingSettings_MaxTilt is not used like in hydrofoil mode)<br/>


* current (float): Current max Horizontal speed in m/s<br/>
<br/>

<!-- MiniDrone-SpeedSettings-MaxPlaneModeRotationSpeed-->
### <a name="MiniDrone-SpeedSettings-MaxPlaneModeRotationSpeed">Set max plane mode rotation speed (only available for wing x)</a><br/>
> Set max plane mode rotation speed (only available for wing x):

```c
deviceController->miniDrone->sendSpeedSettingsMaxPlaneModeRotationSpeed(deviceController->miniDrone, (float)current);
```

```objective_c
deviceController->miniDrone->sendSpeedSettingsMaxPlaneModeRotationSpeed(deviceController->miniDrone, (float)current);
```

```java
deviceController.getFeatureMiniDrone().sendSpeedSettingsMaxPlaneModeRotationSpeed((float)current);
```

Set max plane mode rotation speed (only available for wing x)<br/>


* current (float): Current max plane mode rotation speed in degree/s<br/>
<br/>

<!-- MiniDrone-Settings-CutOutMode-->
### <a name="MiniDrone-Settings-CutOutMode">Set MiniDrone cut out mode</a><br/>
> Set MiniDrone cut out mode:

```c
deviceController->miniDrone->sendSettingsCutOutMode(deviceController->miniDrone, (uint8_t)enable);
```

```objective_c
deviceController->miniDrone->sendSettingsCutOutMode(deviceController->miniDrone, (uint8_t)enable);
```

```java
deviceController.getFeatureMiniDrone().sendSettingsCutOutMode((byte)enable);
```

Set MiniDrone cut out mode<br/>


* enable (u8): Enable cut out mode (1 if is activate, 0 otherwise)<br/>
<br/>

<!-- MiniDrone-GPS-ControllerLatitudeForRun-->
### <a name="MiniDrone-GPS-ControllerLatitudeForRun">Set the controller latitude for a run.</a><br/>
> Set the controller latitude for a run.:

```c
deviceController->miniDrone->sendGPSControllerLatitudeForRun(deviceController->miniDrone, (double)latitude);
```

```objective_c
deviceController->miniDrone->sendGPSControllerLatitudeForRun(deviceController->miniDrone, (double)latitude);
```

```java
deviceController.getFeatureMiniDrone().sendGPSControllerLatitudeForRun((double)latitude);
```

Set the controller latitude for a run.<br/>


* latitude (double): Controller latitude in decimal degrees<br/>
<br/>

<!-- MiniDrone-GPS-ControllerLongitudeForRun-->
### <a name="MiniDrone-GPS-ControllerLongitudeForRun">Set the controller longitude for a run.</a><br/>
> Set the controller longitude for a run.:

```c
deviceController->miniDrone->sendGPSControllerLongitudeForRun(deviceController->miniDrone, (double)longitude);
```

```objective_c
deviceController->miniDrone->sendGPSControllerLongitudeForRun(deviceController->miniDrone, (double)longitude);
```

```java
deviceController.getFeatureMiniDrone().sendGPSControllerLongitudeForRun((double)longitude);
```

Set the controller longitude for a run.<br/>


* longitude (double): Controller longitude in decimal degrees<br/>
<br/>

<!-- MiniDrone-Configuration-ControllerType-->
### <a name="MiniDrone-Configuration-ControllerType">Set the controller type.</a><br/>
> Set the controller type.:

```c
deviceController->miniDrone->sendConfigurationControllerType(deviceController->miniDrone, (char *)type);
```

```objective_c
deviceController->miniDrone->sendConfigurationControllerType(deviceController->miniDrone, (char *)type);
```

```java
deviceController.getFeatureMiniDrone().sendConfigurationControllerType((String)type);
```

Set the controller type.<br/>


* type (string): Controller type like iOS or Android<br/>
<br/>

<!-- MiniDrone-Configuration-ControllerName-->
### <a name="MiniDrone-Configuration-ControllerName">Set the controller name.</a><br/>
> Set the controller name.:

```c
deviceController->miniDrone->sendConfigurationControllerName(deviceController->miniDrone, (char *)name);
```

```objective_c
deviceController->miniDrone->sendConfigurationControllerName(deviceController->miniDrone, (char *)name);
```

```java
deviceController.getFeatureMiniDrone().sendConfigurationControllerName((String)name);
```

Set the controller name.<br/>


* name (string): Controller name like com.parrot.freeflight3<br/>
<br/>

<!-- MiniDrone-UsbAccessory-LightControl-->
### <a name="MiniDrone-UsbAccessory-LightControl">USB Light control cmd.</a><br/>
> USB Light control cmd.:

```c
deviceController->miniDrone->sendUsbAccessoryLightControl(deviceController->miniDrone, (uint8_t)id, (eARCOMMANDS_MINIDRONE_USBACCESSORY_LIGHTCONTROL_MODE)mode, (uint8_t)intensity);
```

```objective_c
deviceController->miniDrone->sendUsbAccessoryLightControl(deviceController->miniDrone, (uint8_t)id, (eARCOMMANDS_MINIDRONE_USBACCESSORY_LIGHTCONTROL_MODE)mode, (uint8_t)intensity);
```

```java
deviceController.getFeatureMiniDrone().sendUsbAccessoryLightControl((byte)id, (ARCOMMANDS_MINIDRONE_USBACCESSORY_LIGHTCONTROL_MODE_ENUM)mode, (byte)intensity);
```

USB Light control cmd.<br/>


* id (u8): Usb accessory id<br/>
* mode (enum): Usb Light mode.<br/>
   * FIXED: Turn light in fixed state at a given intensity.<br/>
   * BLINKED: Turn light in blinked state.<br/>
   * OSCILLATED: Turn light in oscillated state.<br/>
* intensity (u8): Light intensity from 0 (OFF) to 100 (Max intensity).<br/>
Only used in FIXED mode.<br/>
<br/>

<!-- MiniDrone-UsbAccessory-ClawControl-->
### <a name="MiniDrone-UsbAccessory-ClawControl">USB Claw control cmd.</a><br/>
> USB Claw control cmd.:

```c
deviceController->miniDrone->sendUsbAccessoryClawControl(deviceController->miniDrone, (uint8_t)id, (eARCOMMANDS_MINIDRONE_USBACCESSORY_CLAWCONTROL_ACTION)action);
```

```objective_c
deviceController->miniDrone->sendUsbAccessoryClawControl(deviceController->miniDrone, (uint8_t)id, (eARCOMMANDS_MINIDRONE_USBACCESSORY_CLAWCONTROL_ACTION)action);
```

```java
deviceController.getFeatureMiniDrone().sendUsbAccessoryClawControl((byte)id, (ARCOMMANDS_MINIDRONE_USBACCESSORY_CLAWCONTROL_ACTION_ENUM)action);
```

USB Claw control cmd.<br/>


* id (u8): Usb accessory id.<br/>
* action (enum): USB Claw action.<br/>
   * OPEN: Open Claw.<br/>
   * CLOSE: Close Claw.<br/>
<br/>

<!-- MiniDrone-UsbAccessory-GunControl-->
### <a name="MiniDrone-UsbAccessory-GunControl">USB Gun control cmd.</a><br/>
> USB Gun control cmd.:

```c
deviceController->miniDrone->sendUsbAccessoryGunControl(deviceController->miniDrone, (uint8_t)id, (eARCOMMANDS_MINIDRONE_USBACCESSORY_GUNCONTROL_ACTION)action);
```

```objective_c
deviceController->miniDrone->sendUsbAccessoryGunControl(deviceController->miniDrone, (uint8_t)id, (eARCOMMANDS_MINIDRONE_USBACCESSORY_GUNCONTROL_ACTION)action);
```

```java
deviceController.getFeatureMiniDrone().sendUsbAccessoryGunControl((byte)id, (ARCOMMANDS_MINIDRONE_USBACCESSORY_GUNCONTROL_ACTION_ENUM)action);
```

USB Gun control cmd.<br/>


* id (u8): Usb accessory id<br/>
* action (enum): USB Gun action.<br/>
   * FIRE: Fire.<br/>
<br/>

<!-- MiniDrone-RemoteController-SetPairedRemote-->
### <a name="MiniDrone-RemoteController-SetPairedRemote">Send the address of the remote controller on which the drone should be paired</a><br/>
> Send the address of the remote controller on which the drone should be paired:

```c
deviceController->miniDrone->sendRemoteControllerSetPairedRemote(deviceController->miniDrone, (uint16_t)msb_mac, (uint16_t)mid_mac, (uint16_t)lsb_mac);
```

```objective_c
deviceController->miniDrone->sendRemoteControllerSetPairedRemote(deviceController->miniDrone, (uint16_t)msb_mac, (uint16_t)mid_mac, (uint16_t)lsb_mac);
```

```java
deviceController.getFeatureMiniDrone().sendRemoteControllerSetPairedRemote((short)msb_mac, (short)mid_mac, (short)lsb_mac);
```

Send the address of the remote controller on which the drone should be paired<br/>
This is used to pair a Tinos controller<br/>
Where mac address: MSB-MID-LSB.<br/>


* msb_mac (u16): 2 most significant bytes of mac address<br/>
* mid_mac (u16): 2 middle bytes of mac address<br/>
* lsb_mac (u16): 2 least significant bytes of mac address<br/>
<br/>

<!-- MiniDrone-VideoSettings-Autorecord-->
### <a name="MiniDrone-VideoSettings-Autorecord">Set video automatic recording state.</a><br/>
> Set video automatic recording state.:

```c
deviceController->miniDrone->sendVideoSettingsAutorecord(deviceController->miniDrone, (uint8_t)enable);
```

```objective_c
deviceController->miniDrone->sendVideoSettingsAutorecord(deviceController->miniDrone, (uint8_t)enable);
```

```java
deviceController.getFeatureMiniDrone().sendVideoSettingsAutorecord((byte)enable);
```

Set video automatic recording state.<br/>


* enable (u8): 0: disabled<br/>
1: enabled<br/>
<br/>

<!-- MiniDrone-VideoSettings-ElectricFrequency-->
### <a name="MiniDrone-VideoSettings-ElectricFrequency">Set the electric frequency (Anti-flickering).</a><br/>
> Set the electric frequency (Anti-flickering).:

```c
deviceController->miniDrone->sendVideoSettingsElectricFrequency(deviceController->miniDrone, (eARCOMMANDS_MINIDRONE_VIDEOSETTINGS_ELECTRICFREQUENCY_FREQUENCY)frequency);
```

```objective_c
deviceController->miniDrone->sendVideoSettingsElectricFrequency(deviceController->miniDrone, (eARCOMMANDS_MINIDRONE_VIDEOSETTINGS_ELECTRICFREQUENCY_FREQUENCY)frequency);
```

```java
deviceController.getFeatureMiniDrone().sendVideoSettingsElectricFrequency((ARCOMMANDS_MINIDRONE_VIDEOSETTINGS_ELECTRICFREQUENCY_FREQUENCY_ENUM)frequency);
```

Set the electric frequency (Anti-flickering).<br/>


* frequency (enum): Type of the electric frequency.<br/>
   * fifty_hertz: Electric frequency of the country is 50hz.<br/>
   * sixty_hertz: Electric frequency of the country is 60hz.<br/>
<br/>

<!-- MiniDrone-VideoSettings-VideoResolution-->
### <a name="MiniDrone-VideoSettings-VideoResolution">Set video streaming and recording resolution.</a><br/>
> Set video streaming and recording resolution.:

```c
deviceController->miniDrone->sendVideoSettingsVideoResolution(deviceController->miniDrone, (eARCOMMANDS_MINIDRONE_VIDEOSETTINGS_VIDEORESOLUTION_TYPE)type);
```

```objective_c
deviceController->miniDrone->sendVideoSettingsVideoResolution(deviceController->miniDrone, (eARCOMMANDS_MINIDRONE_VIDEOSETTINGS_VIDEORESOLUTION_TYPE)type);
```

```java
deviceController.getFeatureMiniDrone().sendVideoSettingsVideoResolution((ARCOMMANDS_MINIDRONE_VIDEOSETTINGS_VIDEORESOLUTION_TYPE_ENUM)type);
```

Set video streaming and recording resolution.<br/>


* type (enum): Video resolution type.<br/>
   * vga: 16/9 VGA streaming (640 x 360).<br/>
   * hd: HD streaming (1280 x 720).<br/>
<br/>

<!-- MiniDrone-Minicam-Picture-->
### <a name="MiniDrone-Minicam-Picture">Take picture.</a><br/>
> Take picture.:

```c
deviceController->miniDrone->sendMinicamPicture(deviceController->miniDrone);
```

```objective_c
deviceController->miniDrone->sendMinicamPicture(deviceController->miniDrone);
```

```java
deviceController.getFeatureMiniDrone().sendMinicamPicture();
```

Take picture.<br/>


<br/>

<!-- MiniDrone-Minicam-Video-->
### <a name="MiniDrone-Minicam-Video">Start/Stop video recording.</a><br/>
> Start/Stop video recording.:

```c
deviceController->miniDrone->sendMinicamVideo(deviceController->miniDrone, (eARCOMMANDS_MINIDRONE_MINICAM_VIDEO_RECORD)record);
```

```objective_c
deviceController->miniDrone->sendMinicamVideo(deviceController->miniDrone, (eARCOMMANDS_MINIDRONE_MINICAM_VIDEO_RECORD)record);
```

```java
deviceController.getFeatureMiniDrone().sendMinicamVideo((ARCOMMANDS_MINIDRONE_MINICAM_VIDEO_RECORD_ENUM)record);
```

Start/Stop video recording.<br/>


* record (enum): Command to record video<br/>
   * stop: Stop the video recording.<br/>
   * start: Start the video recording.<br/>
<br/>

<!-- MiniDrone-Minicam-MassStorageFormat-->
### <a name="MiniDrone-Minicam-MassStorageFormat">Format mass storage.</a><br/>
> Format mass storage.:

```c
deviceController->miniDrone->sendMinicamMassStorageFormat(deviceController->miniDrone);
```

```objective_c
deviceController->miniDrone->sendMinicamMassStorageFormat(deviceController->miniDrone);
```

```java
deviceController.getFeatureMiniDrone().sendMinicamMassStorageFormat();
```

Format mass storage.<br/>


<br/>

