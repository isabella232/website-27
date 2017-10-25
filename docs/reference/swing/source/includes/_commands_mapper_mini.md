<!-- mapper_mini-map_button_action-->
### <a name="mapper_mini-map_button_action">Map a button action on one or more buttons</a><br/>
> Map a button action on one or more buttons:

```c
deviceController->mapper_mini->sendMapButtonAction(deviceController->mapper_mini, (uint8_t)modes, (eARCOMMANDS_MAPPER_MINI_BUTTON_ACTION)action, (uint32_t)buttons);
```

```objective_c
deviceController->mapper_mini->sendMapButtonAction(deviceController->mapper_mini, (uint8_t)modes, (eARCOMMANDS_MAPPER_MINI_BUTTON_ACTION)action, (uint32_t)buttons);
```

```java
deviceController.getFeatureMapperMini().sendMapButtonAction((byte)modes, (ARCOMMANDS_MAPPER_MINI_BUTTON_ACTION_ENUM)action, (int)buttons);
```

An action can only be mapped to one button set.<br/>
Each action can be mapped to different buttons for different modes.<br/>


* modes (bitfield as u8): The piloting mode of the product<br/>
   * quad: Quadricopter mode<br/>
   * plane: Plane mode<br/>
* action (enum): The action (mapped on a button)<br/>
   * takeoff_land: Take off or land<br/>
   * take_picture: Take a picture<br/>
   * flip_left: Flip left<br/>
   * flip_right: Flip right<br/>
   * flip_front: Flip front<br/>
   * flip_back: Flip back<br/>
   * emergency: Emergency motors shutdown<br/>
   * accessory_gun: Launch USB accessory gun action (shoot)<br/>
   * thrown_takeoff: Thrown take off<br/>
   * cw_90_swipe: 90 deg clockwise swipe<br/>
   * ccw_90_swipe: 90 deg counter clockwise swipe<br/>
   * cw_180_swipe: 180 deg clockwise swipe<br/>
   * ccw_180_swipe: 180 deg counter clockwise swipe<br/>
   * gear_up: increase gear<br/>
   * gear_down: decrease gear<br/>
   * plane_mode_half_barel_roll_right: in plane mode make a 180 deg anticlockwise swipe on roll axis<br/>
   * plane_mode_half_barel_roll_left: in plane mode make a 180 deg clockwise swipe on roll axis<br/>
   * plane_mode_backswap: in plane mode make a 180 deg clockwise swipe on pitch axis<br/>
   * plane_mode_looping: vertical circular loop in plane mode<br/>
   * plane_mode_toggle: switch between plane mode and quad mode<br/>
   * accessory_claw: Launch USB accessory claw action (open/close)<br/>
   * light_continuous: switch continuous light (ON/OFF)<br/>
   * light_blink: switch blink light (ON/OFF)<br/>
   * light_sinus: switch sinus light (ON/OFF)<br/>
   * light_toggle: toggle between light animations (OFF-continuous-blink-sinus-OFF)<br/>
   * piloting_mode_toggle: toggle between easy and preferred piloting mode<br/>
   * video_record_toggle: start or stop video<br/>
* buttons (u32): Buttons combination mapped to the action (bitfield).<br/>
Set 0 (no button) to unmap an action<br/>


Result:<br/>
The drone will send [button_mapping_item](#mapper_mini-button_mapping_item) and [axis_mapping_item](#mapper_mini-axis_mapping_item) according to the request.<br/>


*Supported by <br/>*

- *Mambo*<br/>
- *Swing*<br/>


<br/>

<!-- mapper_mini-map_axis_action-->
### <a name="mapper_mini-map_axis_action">Map an axis action to one axis and zero or more buttons</a><br/>
> Map an axis action to one axis and zero or more buttons:

```c
deviceController->mapper_mini->sendMapAxisAction(deviceController->mapper_mini, (uint8_t)modes, (eARCOMMANDS_MAPPER_MINI_AXIS_ACTION)action, (int8_t)axis, (uint32_t)buttons);
```

```objective_c
deviceController->mapper_mini->sendMapAxisAction(deviceController->mapper_mini, (uint8_t)modes, (eARCOMMANDS_MAPPER_MINI_AXIS_ACTION)action, (int8_t)axis, (uint32_t)buttons);
```

```java
deviceController.getFeatureMapperMini().sendMapAxisAction((byte)modes, (ARCOMMANDS_MAPPER_MINI_AXIS_ACTION_ENUM)action, (byte)axis, (int)buttons);
```

An action can only be mapped to one axis/button set.<br/>
Each action can be mapped to different axes/buttons for different modes.<br/>


* modes (bitfield as u8): The piloting mode of the product<br/>
   * quad: Quadricopter mode<br/>
   * plane: Plane mode<br/>
* action (enum): The action (mapped on an axis)<br/>
   * roll: roll<br/>
   * pitch: pitch<br/>
   * yaw: yaw<br/>
   * gaz: gaz<br/>
* axis (i8): The axis number on which the action will be mapped.<br/>
Set a negative value to unmap the action.<br/>
* buttons (u32): Buttons combination mapped to the action (bitfield).<br/>
Can be zero if no buttons are required.<br/>


Result:<br/>
The drone will send [button_mapping_item](#mapper_mini-button_mapping_item) and [axis_mapping_item](#mapper_mini-axis_mapping_item) according to the request.<br/>


*Supported by <br/>*

- *Mambo*<br/>
- *Swing*<br/>


<br/>

<!-- mapper_mini-reset_mapping-->
### <a name="mapper_mini-reset_mapping">Reset mapping to default values</a><br/>
> Reset mapping to default values:

```c
deviceController->mapper_mini->sendResetMapping(deviceController->mapper_mini, (uint8_t)modes);
```

```objective_c
deviceController->mapper_mini->sendResetMapping(deviceController->mapper_mini, (uint8_t)modes);
```

```java
deviceController.getFeatureMapperMini().sendResetMapping((byte)modes);
```

Resets the mappings for the given mode(s) to their default value.<br/>


* modes (bitfield as u8): The piloting mode of the product<br/>
   * quad: Quadricopter mode<br/>
   * plane: Plane mode<br/>


Result:<br/>
The drone will send [button_mapping_item](#mapper_mini-button_mapping_item) and [axis_mapping_item](#mapper_mini-axis_mapping_item) according to the request.<br/>


*Supported by <br/>*

- *Mambo*<br/>
- *Swing*<br/>


<br/>

