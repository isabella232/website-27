<!-- rc-monitor_channels-->
### <a name="rc-monitor_channels">Monitor RC channels</a><br/>
> Monitor RC channels:

```c
deviceController->rc->sendMonitorChannels(deviceController->rc, (uint8_t)enable);
```

```objective_c
deviceController->rc->sendMonitorChannels(deviceController->rc, (uint8_t)enable);
```

```java
deviceController.getFeatureRc().sendMonitorChannels((byte)enable);
```

Enable or Disable RC channels monitoring.<br/>
If enable, drone will send periodically rc channel value<br/>
events.<br/>


* enable (u8): 1 for enable / 0 to disable<br/>
<br/>

<!-- rc-start_calibration-->
### <a name="rc-start_calibration">Start a calibration</a><br/>
> Start a calibration:

```c
deviceController->rc->sendStartCalibration(deviceController->rc, (eARCOMMANDS_RC_CALIBRATION_TYPE)calibration_type, (eARCOMMANDS_RC_CHANNEL_ACTION)channel_action, (eARCOMMANDS_RC_CHANNEL_TYPE)channel_type);
```

```objective_c
deviceController->rc->sendStartCalibration(deviceController->rc, (eARCOMMANDS_RC_CALIBRATION_TYPE)calibration_type, (eARCOMMANDS_RC_CHANNEL_ACTION)channel_action, (eARCOMMANDS_RC_CHANNEL_TYPE)channel_type);
```

```java
deviceController.getFeatureRc().sendStartCalibration((ARCOMMANDS_RC_CALIBRATION_TYPE_ENUM)calibration_type, (ARCOMMANDS_RC_CHANNEL_ACTION_ENUM)channel_action, (ARCOMMANDS_RC_CHANNEL_TYPE_ENUM)channel_type);
```

Start a calibration.<br/>


* calibration_type (enum): Calibration type.<br/>
   * none: No calibration.<br/>
   * neutral: All neutral channels calibration.<br/>
   * min_max: Min/Max specific channel calibration.<br/>
* channel_action (enum): Channel action.<br/>
   * invalid: Invalid/Unused channel.<br/>
   * roll: Roll axis channel.<br/>
   * pitch: Pitch axis channel.<br/>
   * yaw: Yaw axis channel.<br/>
   * gaz: Gaz / Throttle / Altitude axis channel.<br/>
   * takeoff_land: Takeoff / Land channel.<br/>
   * emergency: Emergency channel.<br/>
   * return_home: Return Home channel.<br/>
   * piloting_mode: RC Piloting mode.<br/>
Auto mode: used for doing flightplans and for assisted flying<br/>
with a non-RC controller.<br/>
Easy manual mode: used for assisted flying with a RC controller.<br/>
Manual mode: used for non-assisted flying with a RC controller and<br/>
for directly controlling the servomotors.<br/>
   * take_control: RC take control.<br/>
When take control is activated the RC controller, if<br/>
available, becomes the main controller.<br/>
* channel_type (enum): Channel physical type.<br/>
   * invalid: Invalid channel physical type.<br/>
   * signed_axis: Signed axis type.<br/>
   * unsigned_axis: Unsigned axis type.<br/>
   * monostable_button: Monostable button type.<br/>
   * bistable_button: Bistable button type.<br/>
   * tristate_button: Tristate button type.<br/>
   * rotary_button: Rotary button type.<br/>
<br/>

<!-- rc-invert_channel-->
### <a name="rc-invert_channel">Invert a RC channel values</a><br/>
> Invert a RC channel values:

```c
deviceController->rc->sendInvertChannel(deviceController->rc, (eARCOMMANDS_RC_CHANNEL_ACTION)action, (uint8_t)flag);
```

```objective_c
deviceController->rc->sendInvertChannel(deviceController->rc, (eARCOMMANDS_RC_CHANNEL_ACTION)action, (uint8_t)flag);
```

```java
deviceController.getFeatureRc().sendInvertChannel((ARCOMMANDS_RC_CHANNEL_ACTION_ENUM)action, (byte)flag);
```

Invert a RC channel values<br/>


* action (enum): Channel action.<br/>
   * invalid: Invalid/Unused channel.<br/>
   * roll: Roll axis channel.<br/>
   * pitch: Pitch axis channel.<br/>
   * yaw: Yaw axis channel.<br/>
   * gaz: Gaz / Throttle / Altitude axis channel.<br/>
   * takeoff_land: Takeoff / Land channel.<br/>
   * emergency: Emergency channel.<br/>
   * return_home: Return Home channel.<br/>
   * piloting_mode: RC Piloting mode.<br/>
Auto mode: used for doing flightplans and for assisted flying<br/>
with a non-RC controller.<br/>
Easy manual mode: used for assisted flying with a RC controller.<br/>
Manual mode: used for non-assisted flying with a RC controller and<br/>
for directly controlling the servomotors.<br/>
   * take_control: RC take control.<br/>
When take control is activated the RC controller, if<br/>
available, becomes the main controller.<br/>
* flag (u8): 1 to invert channel 0 to restore channel.<br/>
<br/>

<!-- rc-abort_calibration-->
### <a name="rc-abort_calibration">Abort current calibration</a><br/>
> Abort current calibration:

```c
deviceController->rc->sendAbortCalibration(deviceController->rc);
```

```objective_c
deviceController->rc->sendAbortCalibration(deviceController->rc);
```

```java
deviceController.getFeatureRc().sendAbortCalibration();
```

Abort current calibration.<br/>


<br/>

<!-- rc-reset_calibration-->
### <a name="rc-reset_calibration">Reset calibration to default values</a><br/>
> Reset calibration to default values:

```c
deviceController->rc->sendResetCalibration(deviceController->rc);
```

```objective_c
deviceController->rc->sendResetCalibration(deviceController->rc);
```

```java
deviceController.getFeatureRc().sendResetCalibration();
```

Reset calibration to default values.<br/>


<br/>

<!-- rc-enable_receiver-->
### <a name="rc-enable_receiver">Enable RC receiver</a><br/>
> Enable RC receiver:

```c
deviceController->rc->sendEnableReceiver(deviceController->rc, (uint8_t)enable);
```

```objective_c
deviceController->rc->sendEnableReceiver(deviceController->rc, (uint8_t)enable);
```

```java
deviceController.getFeatureRc().sendEnableReceiver((byte)enable);
```

Enable or disable RC receiver.<br/>
If enable, drone will apply values sent by RC receiver.<br/>


* enable (u8): 1 for enable / 0 to disable<br/>
<br/>

