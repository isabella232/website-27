<!-- mapper-grab-->
### <a name="mapper-grab">Grab (or ungrab) controls</a><br/>
> Grab (or ungrab) controls:

```c
deviceController->mapper->sendGrab(deviceController->mapper, (uint32_t)buttons, (uint32_t)axes);
```

```objective_c
deviceController->mapper->sendGrab(deviceController->mapper, (uint32_t)buttons, (uint32_t)axes);
```

```java
deviceController.getFeatureMapper().sendGrab((int)buttons, (int)axes);
```

Grabbed buttons are sent to the app and are not handled by the mapper<br/>


* buttons (u32): Buttons to grab/ungrab (bitfield)<br/>
* axes (u32): Axes to grab/ungrab (bitfield)<br/>


Result:<br/>
The mapper will send a [grab_state](#mapper-grab_state) command<br/>


*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- mapper-map_button_action-->
### <a name="mapper-map_button_action">Map a button action on one or more buttons</a><br/>
> Map a button action on one or more buttons:

```c
deviceController->mapper->sendMapButtonAction(deviceController->mapper, (uint16_t)product, (eARCOMMANDS_MAPPER_BUTTON_ACTION)action, (uint32_t)buttons);
```

```objective_c
deviceController->mapper->sendMapButtonAction(deviceController->mapper, (uint16_t)product, (eARCOMMANDS_MAPPER_BUTTON_ACTION)action, (uint32_t)buttons);
```

```java
deviceController.getFeatureMapper().sendMapButtonAction((short)product, (ARCOMMANDS_MAPPER_BUTTON_ACTION_ENUM)action, (int)buttons);
```

An action can only be mapped to one button set.<br/>
Each action can be mapped to different buttons for different products.<br/>


* product (u16): Product (see libARDiscovery for list)<br/>
* action (enum): The action (mapped on a button)<br/>
   * app_0: Action handled by the application<br/>
   * app_1: Action handled by the application<br/>
   * app_2: Action handled by the application<br/>
   * app_3: Action handled by the application<br/>
   * app_4: Action handled by the application<br/>
   * app_5: Action handled by the application<br/>
   * app_6: Action handled by the application<br/>
   * app_7: Action handled by the application<br/>
   * app_8: Action handled by the application<br/>
   * app_9: Action handled by the application<br/>
   * app_10: Action handled by the application<br/>
   * app_11: Action handled by the application<br/>
   * app_12: Action handled by the application<br/>
   * app_13: Action handled by the application<br/>
   * app_14: Action handled by the application<br/>
   * app_15: Action handled by the application<br/>
   * return_home: Return to home<br/>
   * takeoff_land: Take off or land<br/>
   * video_record: Start/stop video record<br/>
   * take_picture: Take a picture<br/>
   * camera_exposition_inc: Increment camera exposition<br/>
   * camera_exposition_dec: Decrement camera exposition<br/>
   * flip_left: Flip left<br/>
   * flip_right: Flip right<br/>
   * flip_front: Flip front<br/>
   * flip_back: Flip back<br/>
   * emergency: Emergency motors shutdown<br/>
   * center_camera: Reset camera to its default position<br/>
   * cycle_hud: Cycle between different hud configurations on HDMI<br/>
(Skycontroller 1 only)<br/>
* buttons (u32): Buttons combination mapped to the action (bitfield).<br/>
Set 0 (no button) to unmap an action<br/>


Result:<br/>
The mapper will send [button_mapping_item](#mapper-button_mapping_item) and [axis_mapping_item](#mapper-axis_mapping_item) according to the request.<br/>


*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- mapper-map_axis_action-->
### <a name="mapper-map_axis_action">Map an axis action to one axis and zero or more buttons</a><br/>
> Map an axis action to one axis and zero or more buttons:

```c
deviceController->mapper->sendMapAxisAction(deviceController->mapper, (uint16_t)product, (eARCOMMANDS_MAPPER_AXIS_ACTION)action, (int32_t)axis, (uint32_t)buttons);
```

```objective_c
deviceController->mapper->sendMapAxisAction(deviceController->mapper, (uint16_t)product, (eARCOMMANDS_MAPPER_AXIS_ACTION)action, (int32_t)axis, (uint32_t)buttons);
```

```java
deviceController.getFeatureMapper().sendMapAxisAction((short)product, (ARCOMMANDS_MAPPER_AXIS_ACTION_ENUM)action, (int)axis, (int)buttons);
```

An action can only be mapped to one axis/button set.<br/>
Each action can be mapped to different axes/buttons for different products.<br/>


* product (u16): Product (see libARDiscovery for list)<br/>
* action (enum): The action (mapped on an axis)<br/>
   * app_0: Action handled by the application<br/>
   * app_1: Action handled by the application<br/>
   * app_2: Action handled by the application<br/>
   * app_3: Action handled by the application<br/>
   * app_4: Action handled by the application<br/>
   * app_5: Action handled by the application<br/>
   * app_6: Action handled by the application<br/>
   * app_7: Action handled by the application<br/>
   * app_8: Action handled by the application<br/>
   * app_9: Action handled by the application<br/>
   * app_10: Action handled by the application<br/>
   * app_11: Action handled by the application<br/>
   * app_12: Action handled by the application<br/>
   * app_13: Action handled by the application<br/>
   * app_14: Action handled by the application<br/>
   * app_15: Action handled by the application<br/>
   * roll: roll<br/>
   * pitch: pitch<br/>
   * yaw: yaw<br/>
   * gaz: gaz<br/>
   * camera_pan: camera pan<br/>
   * camera_tilt: camera tilt<br/>
* axis (i32): The axis number on which the action will be mapped.<br/>
Set a negative value to unmap the action.<br/>
* buttons (u32): Buttons combination mapped to the action (bitfield).<br/>
Can be zero if no buttons are required.<br/>


Result:<br/>
The mapper will send [button_mapping_item](#mapper-button_mapping_item) and [axis_mapping_item](#mapper-axis_mapping_item) according to the request.<br/>


*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- mapper-reset_mapping-->
### <a name="mapper-reset_mapping">Reset mapping to default values</a><br/>
> Reset mapping to default values:

```c
deviceController->mapper->sendResetMapping(deviceController->mapper, (uint16_t)product);
```

```objective_c
deviceController->mapper->sendResetMapping(deviceController->mapper, (uint16_t)product);
```

```java
deviceController.getFeatureMapper().sendResetMapping((short)product);
```

Resets the mappings, axis exponential parameters, and axis inversion for the given product.<br/>
If the product is given as 0 (zero), the all products are reset.<br/>


* product (u16): The product to reset, or 0 to reset all products.<br/>


Result:<br/>
The mapper will send [button_mapping_item](#mapper-button_mapping_item), [axis_mapping_item](#mapper-axis_mapping_item), [expo_map_item](#mapper-expo_map_item) and [inverted_map_item](#mapper-inverted_map_item) according to the request.<br/>


*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- mapper-set_expo-->
### <a name="mapper-set_expo">Set exponential type for the given axis, for the given product</a><br/>
> Set exponential type for the given axis, for the given product:

```c
deviceController->mapper->sendSetExpo(deviceController->mapper, (uint16_t)product, (int32_t)axis, (eARCOMMANDS_MAPPER_EXPO_TYPE)expo);
```

```objective_c
deviceController->mapper->sendSetExpo(deviceController->mapper, (uint16_t)product, (int32_t)axis, (eARCOMMANDS_MAPPER_EXPO_TYPE)expo);
```

```java
deviceController.getFeatureMapper().sendSetExpo((short)product, (int)axis, (ARCOMMANDS_MAPPER_EXPO_TYPE_ENUM)expo);
```

By default, each axis can have a different expo value.<br/>
For some products/mappings configuration, the expo values of two axes belonging to the same physical joystick can be locked to the same value. In this case, setting the value for one axis will automatically change both values.<br/>


* product (u16): Product (see libARDiscovery for list).<br/>
Set to 0 to apply to all products<br/>
* axis (i32): Axis number. Set to -1 to apply to all axes.<br/>
* expo (enum): Expo type<br/>
   * linear: No expo applied, axis is linear<br/>
   * expo_0: Light exponential curve<br/>
   * expo_1: Medium exponential curve<br/>
   * expo_2: Heavy exponential curve<br/>
   * expo_4: Maximum exponential curve<br/>


Result:<br/>
The mapper will send [expo_map_item](#mapper-expo_map_item)<br/>


*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- mapper-set_inverted-->
### <a name="mapper-set_inverted">Set/unset inverted state for a physical axis</a><br/>
> Set/unset inverted state for a physical axis:

```c
deviceController->mapper->sendSetInverted(deviceController->mapper, (uint16_t)product, (int32_t)axis, (uint8_t)inverted);
```

```objective_c
deviceController->mapper->sendSetInverted(deviceController->mapper, (uint16_t)product, (int32_t)axis, (uint8_t)inverted);
```

```java
deviceController.getFeatureMapper().sendSetInverted((short)product, (int)axis, (byte)inverted);
```

Axis inversion has no effect on grabbed axes, nor on virtual buttons that might be generated from axes.<br/>


* product (u16): Product (see libARDiscovery for list).<br/>
Set to 0 to apply to all products<br/>
* axis (i32): Axis number<br/>
* inverted (u8): 0 : Axis not inverted.<br/>
1 : Axis inverted<br/>


Result:<br/>
The mapper will send [inverted_map_item](#mapper-inverted_map_item)<br/>


*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

