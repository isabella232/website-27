<!-- follow_me-start-->
### <a name="follow_me-start">Start followMe mode</a><br/>
> Start followMe mode:

```c
deviceController->follow_me->sendStart(deviceController->follow_me, (eARCOMMANDS_FOLLOW_ME_MODE)mode);
```

```objective_c
deviceController->follow_me->sendStart(deviceController->follow_me, (eARCOMMANDS_FOLLOW_ME_MODE)mode);
```

```java
deviceController.getFeatureFollowMe().sendStart((ARCOMMANDS_FOLLOW_ME_MODE_ENUM)mode);
```

Start a FollowMe with all its params set to the default params.<br/>
Sending this command will stop other running followMe.<br/>


* mode (enum): FollowMe mode<br/>
   * none: No follow me<br/>
   * look_at: Look at the target without moving automatically<br/>
   * geographic: Follow the target keeping the same vector<br/>
   * relative: Follow the target keeping the same orientation to its direction<br/>


Result:<br/>
Event [state](#follow_me-state) is triggered.<br/>
Also triggers the event that informs about the current<br/>
configuration (if there is one) like event<br/>
[Geographic configuration](#follow_me-mode_info) or [Relative configuration](#follow_me-configure_geographic)<br/>


*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-stop-->
### <a name="follow_me-stop">Stop current followMe</a><br/>
> Stop current followMe:

```c
deviceController->follow_me->sendStop(deviceController->follow_me);
```

```objective_c
deviceController->follow_me->sendStop(deviceController->follow_me);
```

```java
deviceController.getFeatureFollowMe().sendStop();
```

Stop current followMe.<br/>




Result:<br/>
Event [state](#follow_me-state) is triggered with mode equals to none.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-configure_geographic-->
### <a name="follow_me-configure_geographic">Configure the geographic follow me</a><br/>
> Configure the geographic follow me:

```c
deviceController->follow_me->sendConfigureGeographic(deviceController->follow_me, (uint8_t)use_default, (float)distance, (float)elevation, (float)azimuth);
```

```objective_c
deviceController->follow_me->sendConfigureGeographic(deviceController->follow_me, (uint8_t)use_default, (float)distance, (float)elevation, (float)azimuth);
```

```java
deviceController.getFeatureFollowMe().sendConfigureGeographic((byte)use_default, (float)distance, (float)elevation, (float)azimuth);
```

Configure the geographic FollowMe.<br/>
This should only be taken in account if arg behavior in [state](#follow_me-state) is equal to Follow.<br/>


* use_default (bitfield as u8): Geographic and Relative follow me configuration parameters<br/>
   * distance: Distance configuration<br/>
   * elevation: Elevation configuration<br/>
   * azimuth: Azimuth configuration<br/>
* distance (float): The distance leader-follower in meter<br/>
Not used when arg start is at 0<br/>
* elevation (float): The elevation leader-follower in rad (not used when arg start is at 0)<br/>
* azimuth (float): The azimuth north-leader-follower in rad (not used when arg start is at 0)<br/>


Result:<br/>
Event [Geographic config](#follow_me-configure_geographic) is sent and drone will move to respect the configuration.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-configure_relative-->
### <a name="follow_me-configure_relative">Configure the relative follow me</a><br/>
> Configure the relative follow me:

```c
deviceController->follow_me->sendConfigureRelative(deviceController->follow_me, (uint8_t)use_default, (float)distance, (float)elevation, (float)azimuth);
```

```objective_c
deviceController->follow_me->sendConfigureRelative(deviceController->follow_me, (uint8_t)use_default, (float)distance, (float)elevation, (float)azimuth);
```

```java
deviceController.getFeatureFollowMe().sendConfigureRelative((byte)use_default, (float)distance, (float)elevation, (float)azimuth);
```

Configure the relative FollowMe.<br/>
This should only be taken in account if arg behavior in [state](#follow_me-state) is equal to Follow<br/>


* use_default (bitfield as u8): Geographic and Relative follow me configuration parameters<br/>
   * distance: Distance configuration<br/>
   * elevation: Elevation configuration<br/>
   * azimuth: Azimuth configuration<br/>
* distance (float): The distance leader-follower in meter<br/>
* elevation (float): The elevation leader-follower in rad<br/>
* azimuth (float): The azimuth north-leader-follower in rad<br/>


Result:<br/>
Event [Relative config](#follow_me-configure_geographic) is sent and drone will move to respect the configuration.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-stop_animation-->
### <a name="follow_me-stop_animation">Stop current followMe animation</a><br/>
> Stop current followMe animation:

```c
deviceController->follow_me->sendStopAnimation(deviceController->follow_me);
```

```objective_c
deviceController->follow_me->sendStopAnimation(deviceController->follow_me);
```

```java
deviceController.getFeatureFollowMe().sendStopAnimation();
```

Stop current followMe animation.<br/>
This message has been deprecated. Please use the animation feature.<br/>




Result:<br/>
FollowMe animation will stop. Event [state](#follow_me-stop) is triggered.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-start_helicoid_anim-->
### <a name="follow_me-start_helicoid_anim">Start a helicoid animation</a><br/>
> Start a helicoid animation:

```c
deviceController->follow_me->sendStartHelicoidAnim(deviceController->follow_me, (uint8_t)use_default, (float)speed, (float)revolution_number, (float)vertical_distance);
```

```objective_c
deviceController->follow_me->sendStartHelicoidAnim(deviceController->follow_me, (uint8_t)use_default, (float)speed, (float)revolution_number, (float)vertical_distance);
```

```java
deviceController.getFeatureFollowMe().sendStartHelicoidAnim((byte)use_default, (float)speed, (float)revolution_number, (float)vertical_distance);
```

Start a helicoid animation.<br/>
The helicoid animation allows the drone to revolve around the target while going up, with a fixed radius.<br/>
This message has been deprecated. Please use the animation feature.<br/>


* use_default (bitfield as u8): Helicoid animation configuration parameters.<br/>
   * speed: Speed parameter<br/>
   * revolution_nb: Number of turn<br/>
   * vertical_distance: Vertical distance<br/>
* speed (float): The desired speed of the anim in m/s<br/>
Not used when speed_is_default is 1<br/>
* revolution_number (float): The number of revolution (in turn)<br/>
Negative value is infinite<br/>
Example: 1.5 makes an entire turn plus half of a turn<br/>
Not used when revolutionNb_is_default is 1<br/>
* vertical_distance (float): Distance that should be made by the product to reach the top of the helicoid in m<br/>
Not used when verticalDistance_is_default is 1<br/>


Result:<br/>
Animation is started and event [state](#follow_me-stop) is triggered.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-start_swing_anim-->
### <a name="follow_me-start_swing_anim">Start a swing animation</a><br/>
> Start a swing animation:

```c
deviceController->follow_me->sendStartSwingAnim(deviceController->follow_me, (uint8_t)use_default, (float)speed, (float)vertical_distance);
```

```objective_c
deviceController->follow_me->sendStartSwingAnim(deviceController->follow_me, (uint8_t)use_default, (float)speed, (float)vertical_distance);
```

```java
deviceController.getFeatureFollowMe().sendStartSwingAnim((byte)use_default, (float)speed, (float)vertical_distance);
```

Start a swing animation.<br/>
The swing animation enables a vertical point of view while the drone passes over the target.<br/>
This message has been deprecated. Please use the animation feature.<br/>


* use_default (bitfield as u8): Swing configure parameters.<br/>
   * speed: Speed parameter<br/>
   * vertical_distance: Vertical distance<br/>
* speed (float): The desired speed of the anim in m/s<br/>
Not used when speed_is_default is 1<br/>
Not used when start is 0<br/>
* vertical_distance (float): Distance that should be made by the product to reach the top of the swing in m<br/>
Not used when verticalDistance_is_default is 1<br/>
Not used when start is 0<br/>


Result:<br/>
Animation is started and event [state](#follow_me-stop) is triggered.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-start_boomerang_anim-->
### <a name="follow_me-start_boomerang_anim">Start a boomerang animation</a><br/>
> Start a boomerang animation:

```c
deviceController->follow_me->sendStartBoomerangAnim(deviceController->follow_me, (uint8_t)use_default, (float)speed, (float)distance);
```

```objective_c
deviceController->follow_me->sendStartBoomerangAnim(deviceController->follow_me, (uint8_t)use_default, (float)speed, (float)distance);
```

```java
deviceController.getFeatureFollowMe().sendStartBoomerangAnim((byte)use_default, (float)speed, (float)distance);
```

Start a boomerang animation.<br/>
The boomerang animation enables a zoom-out/zoom-in trajectory while preserving the framing chosen by the user.<br/>
This message has been deprecated. Please use the animation feature.<br/>


* use_default (bitfield as u8): Boomerang animation configure parameters.<br/>
   * speed: Speed parameter<br/>
   * distance: Distance<br/>
* speed (float): The desired speed of the anim in m/s<br/>
Not used when speed_is_default is 1<br/>
Not used when start is 0<br/>
* distance (float): Distance that should be made by the product to reach its return point in m<br/>
Not used when distance_is_default is 1<br/>
Not used when start is 0<br/>


Result:<br/>
Animation is started and event [state](#follow_me-stop) is triggered.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-start_candle_anim-->
### <a name="follow_me-start_candle_anim">Start a candle animation</a><br/>
> Start a candle animation:

```c
deviceController->follow_me->sendStartCandleAnim(deviceController->follow_me, (uint8_t)use_default, (float)speed, (float)vertical_distance);
```

```objective_c
deviceController->follow_me->sendStartCandleAnim(deviceController->follow_me, (uint8_t)use_default, (float)speed, (float)vertical_distance);
```

```java
deviceController.getFeatureFollowMe().sendStartCandleAnim((byte)use_default, (float)speed, (float)vertical_distance);
```

Start a candle animation.<br/>
The candle animation enables a zoom-in directly on the target followed by a vertical zoom-out.<br/>
This message has been deprecated. Please use the animation feature.<br/>


* use_default (bitfield as u8): Candle animation configure parameters.<br/>
   * speed: Speed parameter<br/>
   * vertical_distance: Follow the target keeping the same vector<br/>
* speed (float): The desired speed of the anim in m/s<br/>
Not used when speed_is_default is 1<br/>
Not used when start is 0<br/>
* vertical_distance (float): Distance that should be made by the product to reach the top of the vertical zoom-out in m<br/>
Not used when verticalDistance_is_default is 1<br/>
Not used when start is 0<br/>


Result:<br/>
Animation is started and event [state](#follow_me-stop) is triggered.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-start_dolly_slide_anim-->
### <a name="follow_me-start_dolly_slide_anim">Start a dolly slide animation</a><br/>
> Start a dolly slide animation:

```c
deviceController->follow_me->sendStartDollySlideAnim(deviceController->follow_me, (uint8_t)use_default, (float)speed, (float)angle, (float)horizontal_distance);
```

```objective_c
deviceController->follow_me->sendStartDollySlideAnim(deviceController->follow_me, (uint8_t)use_default, (float)speed, (float)angle, (float)horizontal_distance);
```

```java
deviceController.getFeatureFollowMe().sendStartDollySlideAnim((byte)use_default, (float)speed, (float)angle, (float)horizontal_distance);
```

Start a dolly slide animation.<br/>
Allows the drone to catch up to the target before flying past it, creating a zoom-in/zoom_out effect without a curved path.<br/>
This message has been deprecated. Please use the animation feature.<br/>


* use_default (bitfield as u8): Dolly slide animation configure parameters.<br/>
   * speed: Speed parameter<br/>
   * angle: Angle<br/>
   * horizontal_distance: Horizontal distance<br/>
* speed (float): The desired speed of the anim in m/s<br/>
Not used when speed_is_default is 1<br/>
Not used when start is 0<br/>
* angle (float): Desired angle Product-User-Target in rad<br/>
Not used when angle_is_default is 1<br/>
Not used when start is 0<br/>
* horizontal_distance (float): Distance that should be made by the product to reach its target in m<br/>
Not used when horizontalDistance_is_default is 1<br/>
Not used when start is 0<br/>


Result:<br/>
Animation is started and event [state](#follow_me-stop) is triggered.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-target_framing_position-->
### <a name="follow_me-target_framing_position">Set the target framing</a><br/>
> Set the target framing:

```c
deviceController->follow_me->sendTargetFramingPosition(deviceController->follow_me, (int8_t)horizontal, (int8_t)vertical);
```

```objective_c
deviceController->follow_me->sendTargetFramingPosition(deviceController->follow_me, (int8_t)horizontal, (int8_t)vertical);
```

```java
deviceController.getFeatureFollowMe().sendTargetFramingPosition((byte)horizontal, (byte)vertical);
```

Set the desired target framing in the video.<br/>


* horizontal (i8): Horizontal position in the video (in %, from left to right)<br/>
* vertical (i8): Vertical position in the video (in %, from bottom to top)<br/>


Result:<br/>
Event [target framing position](#follow_me-start_dolly_slide_anim) is triggered.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-target_image_detection-->
### <a name="follow_me-target_image_detection">Send vision detection results</a><br/>
> Send vision detection results:

```c
deviceController->follow_me->sendTargetImageDetection(deviceController->follow_me, (float)target_azimuth, (float)target_elevation, (float)change_of_scale, (uint8_t)confidence_index, (uint8_t)is_new_selection, (uint64_t)timestamp);
```

```objective_c
deviceController->follow_me->sendTargetImageDetection(deviceController->follow_me, (float)target_azimuth, (float)target_elevation, (float)change_of_scale, (uint8_t)confidence_index, (uint8_t)is_new_selection, (uint64_t)timestamp);
```

```java
deviceController.getFeatureFollowMe().sendTargetImageDetection((float)target_azimuth, (float)target_elevation, (float)change_of_scale, (byte)confidence_index, (byte)is_new_selection, (long)timestamp);
```

Send vision detection results.<br/>


* target_azimuth (float): Horizontal north-drone-target angle in radian<br/>
* target_elevation (float): Vertical angle horizon-drone-target in radian<br/>
* change_of_scale (float): Normalized relative radial speed in 1/second<br/>
* confidence_index (u8): Confidence index of the detection (from 0 to 255, the highest is the best)<br/>
* is_new_selection (u8): Boolean. 1 if the selection is new, 0 otherwise<br/>
* timestamp (u64): Acquisition time of processed picture in millisecond<br/>


Result:<br/>
If drone is in FollowMe, is will look at the target according to<br/>
the chosen [framing position](#follow_me-start_dolly_slide_anim).<br/>


*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

