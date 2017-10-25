<!-- animation-cancel-->
### <a name="animation-cancel">Cancel current animation</a><br/>
> Cancel current animation:

```c
deviceController->animation->sendCancel(deviceController->animation);
```

```objective_c
deviceController->animation->sendCancel(deviceController->animation);
```

```java
deviceController.getFeatureAnimation().sendCancel();
```

Cancel current animation.<br/>




Result:<br/>
The state of the current animation (for example [FlipState](#animation-flip_state)) changes to canceling. Then, as soon as possible, the current animation is stopped and [State](#animation-state) is triggered with type equals to none.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-start_flip-->
### <a name="animation-start_flip">Start flip animation</a><br/>
> Start flip animation:

```c
deviceController->animation->sendStartFlip(deviceController->animation, (eARCOMMANDS_ANIMATION_FLIP_TYPE)type);
```

```objective_c
deviceController->animation->sendStartFlip(deviceController->animation, (eARCOMMANDS_ANIMATION_FLIP_TYPE)type);
```

```java
deviceController.getFeatureAnimation().sendStartFlip((ARCOMMANDS_ANIMATION_FLIP_TYPE_ENUM)type);
```

Start a flip animation.<br/>
Starting this animation when another animation is started (or canceling), will cancel the current one to start this one.<br/>


* type (enum): Animation flip type.<br/>
   * front: The drone makes a front flip<br/>
   * back: The drone makes a back flip<br/>
   * left: The drone makes a left flip (its left side goes up)<br/>
   * right: The drone makes a right flip (its right side goes up)<br/>


Result:<br/>
If an animation was running, this animation is canceling, then canceled. Then, this animation is started, [FlipState](#animation-flip_state) is triggered with state equals to running and [State](#animation-state) is triggered with type equals to flip.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-start_horizontal_panorama-->
### <a name="animation-start_horizontal_panorama">Start horizontal panorama</a><br/>
> Start horizontal panorama:

```c
deviceController->animation->sendStartHorizontalPanorama(deviceController->animation, (uint8_t)provided_params, (float)rotation_angle, (float)rotation_speed);
```

```objective_c
deviceController->animation->sendStartHorizontalPanorama(deviceController->animation, (uint8_t)provided_params, (float)rotation_angle, (float)rotation_speed);
```

```java
deviceController.getFeatureAnimation().sendStartHorizontalPanorama((byte)provided_params, (float)rotation_angle, (float)rotation_speed);
```

Start an horizontal panorama animation.<br/>
Starting this animation when another animation is started (or canceling), will cancel the current one to start this one.<br/>
This animation will make the drone horizontaly rotates on itself.<br/>


* provided_params (bitfield as u8): Horizontal panorama configuration parameter.<br/>
   * rotation_angle: Rotation angle parameter.<br/>
   * rotation_speed: Rotation speed parameter.<br/>
* rotation_angle (float): Desired rotation angle in rad. Positive value makes a clockwise panorama, negative is anti-clockwise.<br/>
Not used when rotation angle of provided_params param is 0.<br/>
* rotation_speed (float): The desired rotation speed of the anim in rad/s<br/>
Not used when rotation speed of provided_params param is 0.<br/>


Result:<br/>
If an animation was running, this animation is canceling, then canceled. Then, this animation is started, [HorizontalPanoramaState](#animation-horizontal_panorama_state) is triggered with state equals to running and [State](#animation-state) is triggered with type equals to HorizontalPanorama.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-start_dronie-->
### <a name="animation-start_dronie">Start dronie</a><br/>
> Start dronie:

```c
deviceController->animation->sendStartDronie(deviceController->animation, (uint8_t)provided_params, (float)speed, (float)distance, (eARCOMMANDS_ANIMATION_PLAY_MODE)play_mode);
```

```objective_c
deviceController->animation->sendStartDronie(deviceController->animation, (uint8_t)provided_params, (float)speed, (float)distance, (eARCOMMANDS_ANIMATION_PLAY_MODE)play_mode);
```

```java
deviceController.getFeatureAnimation().sendStartDronie((byte)provided_params, (float)speed, (float)distance, (ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM)play_mode);
```

Start a dronie animation.<br/>
Starting this animation when another animation is started (or canceling), will cancel the current one to start this one.<br/>
This animation will make the drone flies away on a given distance with a computed angle.<br/>


* provided_params (bitfield as u8): Dronie animation configuration parameter.<br/>
   * speed: Speed parameter.<br/>
   * distance: Distance parameter.<br/>
   * play_mode: Play mode parameter.<br/>
* speed (float): Desired speed in m/s.<br/>
Not used when speed of provided_params param is 0.<br/>
* distance (float): Desired dronie distance in m (length of the hypotenuse).<br/>
Not used when distance of provided_params param is 0.<br/>
* play_mode (enum): Animation play mode.<br/>
   * normal: Animation is played once, normally.<br/>
   * once_then_mirrored: Animation is played once and then the animation is played mirrored.<br/>


Result:<br/>
If an animation was running, this animation is canceling, then canceled. Then, this animation is started, [DronieState](#animation-dronie_state) is triggered with state equals to running and [State](#animation-state) is triggered with type equals to Dronie.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-start_horizontal_reveal-->
### <a name="animation-start_horizontal_reveal">Start horizontal reveal</a><br/>
> Start horizontal reveal:

```c
deviceController->animation->sendStartHorizontalReveal(deviceController->animation, (uint8_t)provided_params, (float)speed, (float)distance, (eARCOMMANDS_ANIMATION_PLAY_MODE)play_mode);
```

```objective_c
deviceController->animation->sendStartHorizontalReveal(deviceController->animation, (uint8_t)provided_params, (float)speed, (float)distance, (eARCOMMANDS_ANIMATION_PLAY_MODE)play_mode);
```

```java
deviceController.getFeatureAnimation().sendStartHorizontalReveal((byte)provided_params, (float)speed, (float)distance, (ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM)play_mode);
```

Start an horizontal reveal animation.<br/>
Starting this animation when another animation is started (or canceling), will cancel the current one to start this one.<br/>
This animation will make the drone starts looking down, then moves forward while slowly looking at the horizon.<br/>


* provided_params (bitfield as u8): Horizontal reveal animation configuration parameter.<br/>
   * speed: Speed parameter.<br/>
   * distance: Distance parameter.<br/>
   * play_mode: Play mode parameter.<br/>
* speed (float): Desired speed in m/s.<br/>
Not used when speed of provided_params param is 0.<br/>
* distance (float): Desired distance in m.<br/>
Not used when distance of provided_params param is 0.<br/>
* play_mode (enum): Animation play mode.<br/>
   * normal: Animation is played once, normally.<br/>
   * once_then_mirrored: Animation is played once and then the animation is played mirrored.<br/>


Result:<br/>
If an animation was running, this animation is canceling, then canceled. Then, this animation is started, [HorizontalRevealState](#animation-horizontal_reveal_state) is triggered with state equals to running and [State](#animation-state) is triggered with type equals to HorizontalReveal.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-start_vertical_reveal-->
### <a name="animation-start_vertical_reveal">Start vertical reveal</a><br/>
> Start vertical reveal:

```c
deviceController->animation->sendStartVerticalReveal(deviceController->animation, (uint8_t)provided_params, (float)speed, (float)vertical_distance, (float)rotation_angle, (float)rotation_speed, (eARCOMMANDS_ANIMATION_PLAY_MODE)play_mode);
```

```objective_c
deviceController->animation->sendStartVerticalReveal(deviceController->animation, (uint8_t)provided_params, (float)speed, (float)vertical_distance, (float)rotation_angle, (float)rotation_speed, (eARCOMMANDS_ANIMATION_PLAY_MODE)play_mode);
```

```java
deviceController.getFeatureAnimation().sendStartVerticalReveal((byte)provided_params, (float)speed, (float)vertical_distance, (float)rotation_angle, (float)rotation_speed, (ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM)play_mode);
```

Start a vertical reveal animation.<br/>
Starting this animation when another animation is started (or canceling), will cancel the current one to start this one.<br/>
This animation will make the drone starts looking down, then moves up while slowly looking at the horizon. When it reaches its target altitude, it rotates on itself to do a panorama.<br/>


* provided_params (bitfield as u8): Vertical reveal animation configuration parameter.<br/>
   * speed: Speed parameter.<br/>
   * vertical_distance: Vertical distance parameter.<br/>
   * rotation_angle: Rotation angle parameter.<br/>
   * rotation_speed: Rotation speed parameter.<br/>
   * play_mode: Play mode parameter.<br/>
* speed (float): Desired speed in m/s.<br/>
Not used when speed of provided_params param is 0.<br/>
* vertical_distance (float): Desired vertical distance in m.<br/>
Not used when vertical distance of provided_params param is 0.<br/>
* rotation_angle (float): Desired rotation angle in rad. Positive value makes a clockwise panorama, negative is anti-clockwise.<br/>
Not used when rotation angle of provided_params param is 0.<br/>
* rotation_speed (float): The desired rotation speed of the anim in rad/s<br/>
Not used when rotation speed of provided_params param is 0.<br/>
* play_mode (enum): Animation play mode.<br/>
   * normal: Animation is played once, normally.<br/>
   * once_then_mirrored: Animation is played once and then the animation is played mirrored.<br/>


Result:<br/>
If an animation was running, this animation is canceling, then canceled. Then, this animation is started, [VerticalRevealState](#animation-vertical_reveal_state) is triggered with state equals to running and [State](#animation-state) is triggered with type equals to VerticalReveal.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-start_spiral-->
### <a name="animation-start_spiral">Start spiral</a><br/>
> Start spiral:

```c
deviceController->animation->sendStartSpiral(deviceController->animation, (uint8_t)provided_params, (float)speed, (float)radius_variation, (float)vertical_distance, (float)revolution_nb, (eARCOMMANDS_ANIMATION_PLAY_MODE)play_mode);
```

```objective_c
deviceController->animation->sendStartSpiral(deviceController->animation, (uint8_t)provided_params, (float)speed, (float)radius_variation, (float)vertical_distance, (float)revolution_nb, (eARCOMMANDS_ANIMATION_PLAY_MODE)play_mode);
```

```java
deviceController.getFeatureAnimation().sendStartSpiral((byte)provided_params, (float)speed, (float)radius_variation, (float)vertical_distance, (float)revolution_nb, (ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM)play_mode);
```

Start a spiral animation.<br/>
Starting this animation when another animation is started (or canceling), will cancel the current one to start this one.<br/>
This animation will make the drone circles around its target.<br/>


* provided_params (bitfield as u8): Spiral animation configuration parameter.<br/>
   * speed: Speed parameter.<br/>
   * radius_variation: Radius variation parameter.<br/>
   * vertical_distance: Vertical distance parameter.<br/>
   * revolution_nb: Revolution number parameter.<br/>
   * play_mode: Play mode parameter.<br/>
* speed (float): Desired speed in m/s.<br/>
Not used when speed of provided_params param is 0.<br/>
* radius_variation (float): Desired relative radius variation in m.<br/>
A value of 2 means that the ending radius will be twice as big as the starting radius.<br/>
A value of -2 means that the ending radius will half of the size of the starting radius.<br/>
A value of 1 means that the radius will not change during the animation.<br/>
Not used when radius variation of provided_params param is 0.<br/>
* vertical_distance (float): Desired vertical distance in m.<br/>
If negative, the spiral will be directed to the ground.<br/>
Not used when vertical distance of provided_params param is 0.<br/>
* revolution_nb (float): The number of revolution (in turn).<br/>
Positive value makes a clockwise spiral, negative is anti-clockwise.<br/>
Example: 1.5 makes an entire turn plus half of a turn<br/>
* play_mode (enum): Animation play mode.<br/>
   * normal: Animation is played once, normally.<br/>
   * once_then_mirrored: Animation is played once and then the animation is played mirrored.<br/>


Result:<br/>
If an animation was running, this animation is canceling, then canceled. Then, this animation is started, [SpiralState](#animation-spiral_state) is triggered with state equals to running and [State](#animation-state) is triggered with type equals to Spiral.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-start_parabola-->
### <a name="animation-start_parabola">Start parabola</a><br/>
> Start parabola:

```c
deviceController->animation->sendStartParabola(deviceController->animation, (uint8_t)provided_params, (float)speed, (float)vertical_distance, (eARCOMMANDS_ANIMATION_PLAY_MODE)play_mode);
```

```objective_c
deviceController->animation->sendStartParabola(deviceController->animation, (uint8_t)provided_params, (float)speed, (float)vertical_distance, (eARCOMMANDS_ANIMATION_PLAY_MODE)play_mode);
```

```java
deviceController.getFeatureAnimation().sendStartParabola((byte)provided_params, (float)speed, (float)vertical_distance, (ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM)play_mode);
```

Start a parabola animation.<br/>
Starting this animation when another animation is started (or canceling), will cancel the current one to start this one.<br/>
This animation will make the drone makes a parabola on top of its target and ends on the other side of it.<br/>


* provided_params (bitfield as u8): Parabola animation configuration parameter.<br/>
   * speed: Speed parameter.<br/>
   * vertical_distance: Vertical distance parameter.<br/>
   * play_mode: Play mode parameter.<br/>
* speed (float): Desired speed in m/s.<br/>
Not used when speed of provided_params param is 0.<br/>
* vertical_distance (float): Desired vertical distance in m.<br/>
Not used when vertical distance of provided_params param is 0.<br/>
* play_mode (enum): Animation play mode.<br/>
   * normal: Animation is played once, normally.<br/>
   * once_then_mirrored: Animation is played once and then the animation is played mirrored.<br/>


Result:<br/>
If an animation was running, this animation is canceling, then canceled. Then, this animation is started, [ParabolaState](#animation-parabola_state) is triggered with state equals to running and [State](#animation-state) is triggered with type equals to Parabola.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-start_candle-->
### <a name="animation-start_candle">Start candle</a><br/>
> Start candle:

```c
deviceController->animation->sendStartCandle(deviceController->animation, (uint8_t)provided_params, (float)speed, (float)vertical_distance, (eARCOMMANDS_ANIMATION_PLAY_MODE)play_mode);
```

```objective_c
deviceController->animation->sendStartCandle(deviceController->animation, (uint8_t)provided_params, (float)speed, (float)vertical_distance, (eARCOMMANDS_ANIMATION_PLAY_MODE)play_mode);
```

```java
deviceController.getFeatureAnimation().sendStartCandle((byte)provided_params, (float)speed, (float)vertical_distance, (ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM)play_mode);
```

Start a candle animation.<br/>
Starting this animation when another animation is started (or canceling), will cancel the current one to start this one.<br/>
This animation will make the drone flies horizontally in direction of the target then flies up.<br/>


* provided_params (bitfield as u8): Candle animation configuration parameter.<br/>
   * speed: Speed parameter.<br/>
   * vertical_distance: Vertical distance parameter.<br/>
   * play_mode: Play mode parameter.<br/>
* speed (float): Desired speed in m/s.<br/>
Not used when speed of provided_params param is 0.<br/>
* vertical_distance (float): Desired vertical distance in m.<br/>
Not used when vertical distance of provided_params param is 0.<br/>
* play_mode (enum): Animation play mode.<br/>
   * normal: Animation is played once, normally.<br/>
   * once_then_mirrored: Animation is played once and then the animation is played mirrored.<br/>


Result:<br/>
If an animation was running, this animation is canceling, then canceled. Then, this animation is started, [CandleState](#animation-candle_state) is triggered with state equals to running and [State](#animation-state) is triggered with type equals to Candle.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-start_dolly_slide-->
### <a name="animation-start_dolly_slide">Start a dolly slide</a><br/>
> Start a dolly slide:

```c
deviceController->animation->sendStartDollySlide(deviceController->animation, (uint8_t)provided_params, (float)speed, (float)angle, (float)horizontal_distance, (eARCOMMANDS_ANIMATION_PLAY_MODE)play_mode);
```

```objective_c
deviceController->animation->sendStartDollySlide(deviceController->animation, (uint8_t)provided_params, (float)speed, (float)angle, (float)horizontal_distance, (eARCOMMANDS_ANIMATION_PLAY_MODE)play_mode);
```

```java
deviceController.getFeatureAnimation().sendStartDollySlide((byte)provided_params, (float)speed, (float)angle, (float)horizontal_distance, (ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM)play_mode);
```

Start a dolly slide animation.<br/>
Starting this animation when another animation is started (or canceling), will cancel the current one to start this one.<br/>
This animation will make the drone slides horizontally.<br/>


* provided_params (bitfield as u8): Dolly slide animation configuration parameter.<br/>
   * speed: Speed parameter.<br/>
   * angle: Angle parameter.<br/>
   * horizontal_distance: Horizontal distance parameter.<br/>
   * play_mode: Play mode parameter.<br/>
* speed (float): Desired speed in m/s.<br/>
Not used when speed of provided_params param is 0.<br/>
* angle (float): Desired drone-target-destination angle in rad.<br/>
Not used when angle of provided_params param is 0.<br/>
* horizontal_distance (float): Desired horizontal distance in m..<br/>
Not used when angle of provided_params param is 0.<br/>
* play_mode (enum): Animation play mode.<br/>
   * normal: Animation is played once, normally.<br/>
   * once_then_mirrored: Animation is played once and then the animation is played mirrored.<br/>


Result:<br/>
If an animation was running, this animation is canceling, then canceled. Then, this animation is started, [DollySlideState](#animation-dolly_slide_state) is triggered with state equals to running and [State](#animation-state) is triggered with type equals to DollySlide.<br/>


*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

