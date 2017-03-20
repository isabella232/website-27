<!-- mapper-grab_state-->
### <a name="mapper-grab_state">Grabbed controls</a><br/>
> Grabbed controls:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABSTATE_BUTTONS, arg);
            if (arg != NULL)
            {
                uint32_t buttons = arg->value.U32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABSTATE_AXES, arg);
            if (arg != NULL)
            {
                uint32_t axes = arg->value.U32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABSTATE_BUTTONS_STATE, arg);
            if (arg != NULL)
            {
                uint32_t buttons_state = arg->value.U32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABSTATE_BUTTONS, arg);
            if (arg != NULL)
            {
                uint32_t buttons = arg->value.U32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABSTATE_AXES, arg);
            if (arg != NULL)
            {
                uint32_t axes = arg->value.U32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABSTATE_BUTTONS_STATE, arg);
            if (arg != NULL)
            {
                uint32_t buttons_state = arg->value.U32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABSTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            int buttons = (int)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABSTATE_BUTTONS);
            int axes = (int)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABSTATE_AXES);
            int buttons_state = (int)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABSTATE_BUTTONS_STATE);
        }
    }
}
```

Grabbed buttons are sent to the app and are not handled by the mapper<br/>


* buttons (u32): Grabbed buttons (bitfield)<br/>
* axes (u32): Grabbed axes (bitfield)<br/>
* buttons_state (u32): For grabbed buttons only.<br/>
State of the button when the grab starts (bitfield)<br/>


Triggered by a [grab](#mapper-grab) command<br/>



*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- mapper-grab_button_event-->
### <a name="mapper-grab_button_event">Event on a grabbed button</a><br/>
> Event on a grabbed button:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABBUTTONEVENT) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABBUTTONEVENT_BUTTON, arg);
            if (arg != NULL)
            {
                uint32_t button = arg->value.U32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABBUTTONEVENT_EVENT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MAPPER_BUTTON_EVENT event = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABBUTTONEVENT) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABBUTTONEVENT_BUTTON, arg);
            if (arg != NULL)
            {
                uint32_t button = arg->value.U32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABBUTTONEVENT_EVENT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MAPPER_BUTTON_EVENT event = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABBUTTONEVENT) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            int button = (int)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABBUTTONEVENT_BUTTON);
            ARCOMMANDS_MAPPER_BUTTON_EVENT_ENUM event = ARCOMMANDS_MAPPER_BUTTON_EVENT_ENUM.getFromValue((Integer)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABBUTTONEVENT_EVENT));
        }
    }
}
```

The state of a grabbed button changes<br/>


* button (u32): Button id<br/>
* event (enum): Button event<br/>
   * release: button released<br/>
   * press: button pressed<br/>


Triggered when a grabbed button is pressed/released<br/>



*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- mapper-grab_axis_event-->
### <a name="mapper-grab_axis_event">Event on a grabbed axis</a><br/>
> Event on a grabbed axis:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABAXISEVENT) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABAXISEVENT_AXIS, arg);
            if (arg != NULL)
            {
                uint32_t axis = arg->value.U32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABAXISEVENT_VALUE, arg);
            if (arg != NULL)
            {
                int8_t value = arg->value.I8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABAXISEVENT) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABAXISEVENT_AXIS, arg);
            if (arg != NULL)
            {
                uint32_t axis = arg->value.U32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABAXISEVENT_VALUE, arg);
            if (arg != NULL)
            {
                int8_t value = arg->value.I8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABAXISEVENT) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            int axis = (int)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABAXISEVENT_AXIS);
            byte value = (byte)((Integer)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_GRABAXISEVENT_VALUE)).intValue();
        }
    }
}
```

The state of a grabbed axis changes<br/>


* axis (u32): Axis id<br/>
* value (i8): Value in range [-100; 100].<br/>


Triggered when the value of a grabbed axis changes<br/>



*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- mapper-button_mapping_item-->
### <a name="mapper-button_mapping_item">Item of the button_actions mapping list</a><br/>
> Item of the button_actions mapping list:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM_UID, arg);
                if (arg != NULL)
                {
                    uint32_t uid = arg->value.U32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM_PRODUCT, arg);
                if (arg != NULL)
                {
                    uint16_t product = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM_ACTION, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MAPPER_BUTTON_ACTION action = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM_BUTTONS, arg);
                if (arg != NULL)
                {
                    uint32_t buttons = arg->value.U32;
                }
            }
        }
        else
        {
            // list is empty
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM_UID, arg);
                if (arg != NULL)
                {
                    uint32_t uid = arg->value.U32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM_PRODUCT, arg);
                if (arg != NULL)
                {
                    uint16_t product = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM_ACTION, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MAPPER_BUTTON_ACTION action = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM_BUTTONS, arg);
                if (arg != NULL)
                {
                    uint32_t buttons = arg->value.U32;
                }
            }
        }
        else
        {
            // list is empty
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    int uid = (int)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM_UID);
                    short product = (short)((Integer)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM_PRODUCT)).intValue();
                    ARCOMMANDS_MAPPER_BUTTON_ACTION_ENUM action = ARCOMMANDS_MAPPER_BUTTON_ACTION_ENUM.getFromValue((Integer)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM_ACTION));
                    int buttons = (int)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_BUTTONMAPPINGITEM_BUTTONS);
                }
            }
        } else {
            // list is empty
        }
    }
}
```

The resulting map describes all active button mappings of the mapper.<br/>
Each action can only be mapped once per product.<br/>


* uid (u32): Unique ID of the mapping.<br/>
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
* list_flags (bitfield as u8): Flags use by maps and lists<br/>
   * First: indicate it's the first element of the list.<br/>
   * Last: indicate it's the last element of the list.<br/>
   * Empty: indicate the list is empty (implies First/Last). All other arguments should be ignored.<br/>
   * Remove: This value should be removed from the existing list.<br/>


Triggered by a [map_button_action](#mapper-map_button_action) or a [map_axis_action](#mapper-map_axis_action) command<br/>



*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- mapper-axis_mapping_item-->
### <a name="mapper-axis_mapping_item">Item of the axis_actions mapping list</a><br/>
> Item of the axis_actions mapping list:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_UID, arg);
                if (arg != NULL)
                {
                    uint32_t uid = arg->value.U32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_PRODUCT, arg);
                if (arg != NULL)
                {
                    uint16_t product = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_ACTION, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MAPPER_AXIS_ACTION action = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_AXIS, arg);
                if (arg != NULL)
                {
                    int32_t axis = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_BUTTONS, arg);
                if (arg != NULL)
                {
                    uint32_t buttons = arg->value.U32;
                }
            }
        }
        else
        {
            // list is empty
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_UID, arg);
                if (arg != NULL)
                {
                    uint32_t uid = arg->value.U32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_PRODUCT, arg);
                if (arg != NULL)
                {
                    uint16_t product = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_ACTION, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MAPPER_AXIS_ACTION action = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_AXIS, arg);
                if (arg != NULL)
                {
                    int32_t axis = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_BUTTONS, arg);
                if (arg != NULL)
                {
                    uint32_t buttons = arg->value.U32;
                }
            }
        }
        else
        {
            // list is empty
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    int uid = (int)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_UID);
                    short product = (short)((Integer)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_PRODUCT)).intValue();
                    ARCOMMANDS_MAPPER_AXIS_ACTION_ENUM action = ARCOMMANDS_MAPPER_AXIS_ACTION_ENUM.getFromValue((Integer)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_ACTION));
                    int axis = (int)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_AXIS);
                    int buttons = (int)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_AXISMAPPINGITEM_BUTTONS);
                }
            }
        } else {
            // list is empty
        }
    }
}
```

The resulting map describes all active axis mappings of the mapper.<br/>
Each action can only be mapped once per product.<br/>


* uid (u32): Unique ID of the mapping.<br/>
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
* axis (i32): The axis number on which the action is mapped.<br/>
* buttons (u32): Buttons combination mapped to the action (bitfield).<br/>
* list_flags (bitfield as u8): Flags use by maps and lists<br/>
   * First: indicate it's the first element of the list.<br/>
   * Last: indicate it's the last element of the list.<br/>
   * Empty: indicate the list is empty (implies First/Last). All other arguments should be ignored.<br/>
   * Remove: This value should be removed from the existing list.<br/>


Triggered by a [map_button_action](#mapper-map_button_action) or a [map_axis_action](#mapper-map_axis_action) command<br/>



*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- mapper-application_axis_event-->
### <a name="mapper-application_axis_event">Application specific event</a><br/>
> Application specific event:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONAXISEVENT) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONAXISEVENT_ACTION, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MAPPER_AXIS_ACTION action = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONAXISEVENT_VALUE, arg);
            if (arg != NULL)
            {
                int8_t value = arg->value.I8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONAXISEVENT) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONAXISEVENT_ACTION, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MAPPER_AXIS_ACTION action = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONAXISEVENT_VALUE, arg);
            if (arg != NULL)
            {
                int8_t value = arg->value.I8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONAXISEVENT) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MAPPER_AXIS_ACTION_ENUM action = ARCOMMANDS_MAPPER_AXIS_ACTION_ENUM.getFromValue((Integer)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONAXISEVENT_ACTION));
            byte value = (byte)((Integer)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONAXISEVENT_VALUE)).intValue();
        }
    }
}
```

This event signals the controller application when an application specific axis_event is triggered.<br/>
Application specific actions are typically used for UI interaction which does not involves the drone.<br/>


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
* value (i8): The current value of the axis.<br/>


Triggered when any axis action set to application_action is triggered.<br/>



*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- mapper-application_button_event-->
### <a name="mapper-application_button_event">Application specific event</a><br/>
> Application specific event:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONBUTTONEVENT) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONBUTTONEVENT_ACTION, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MAPPER_BUTTON_ACTION action = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONBUTTONEVENT) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONBUTTONEVENT_ACTION, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MAPPER_BUTTON_ACTION action = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONBUTTONEVENT) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MAPPER_BUTTON_ACTION_ENUM action = ARCOMMANDS_MAPPER_BUTTON_ACTION_ENUM.getFromValue((Integer)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_APPLICATIONBUTTONEVENT_ACTION));
        }
    }
}
```

This event signals the controller application when an application specific button_event is triggered.<br/>
Application specific actions are typically used for UI interaction which does not involves the drone.<br/>


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


Triggered when any button action set to application_action is triggered.<br/>



*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- mapper-expo_map_item-->
### <a name="mapper-expo_map_item">Item of the expo map</a><br/>
> Item of the expo map:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM_UID, arg);
                if (arg != NULL)
                {
                    uint32_t uid = arg->value.U32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM_PRODUCT, arg);
                if (arg != NULL)
                {
                    uint16_t product = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM_AXIS, arg);
                if (arg != NULL)
                {
                    int32_t axis = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM_EXPO, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MAPPER_EXPO_TYPE expo = arg->value.I32;
                }
            }
        }
        else
        {
            // list is empty
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM_UID, arg);
                if (arg != NULL)
                {
                    uint32_t uid = arg->value.U32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM_PRODUCT, arg);
                if (arg != NULL)
                {
                    uint16_t product = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM_AXIS, arg);
                if (arg != NULL)
                {
                    int32_t axis = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM_EXPO, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MAPPER_EXPO_TYPE expo = arg->value.I32;
                }
            }
        }
        else
        {
            // list is empty
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    int uid = (int)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM_UID);
                    short product = (short)((Integer)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM_PRODUCT)).intValue();
                    int axis = (int)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM_AXIS);
                    ARCOMMANDS_MAPPER_EXPO_TYPE_ENUM expo = ARCOMMANDS_MAPPER_EXPO_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_EXPOMAPITEM_EXPO));
                }
            }
        } else {
            // list is empty
        }
    }
}
```

By default, each axis can have a different expo value.<br/>
For some products/mappings configuration, the expo values of two axes belonging to the same physical joystick can be locked to the same value. In this case, setting the value for one axis will automatically change both values.<br/>


* uid (u32): Unique ID (for MAP_ITEM type)<br/>
* product (u16): Product (see libARDiscovery for list)<br/>
* axis (i32): Axis number<br/>
* expo (enum): Expo type<br/>
   * linear: No expo applied, axis is linear<br/>
   * expo_0: Light exponential curve<br/>
   * expo_1: Medium exponential curve<br/>
   * expo_2: Heavy exponential curve<br/>
   * expo_4: Maximum exponential curve<br/>
* list_flags (bitfield as u8): Flags use by maps and lists<br/>
   * First: indicate it's the first element of the list.<br/>
   * Last: indicate it's the last element of the list.<br/>
   * Empty: indicate the list is empty (implies First/Last). All other arguments should be ignored.<br/>
   * Remove: This value should be removed from the existing list.<br/>


Triggered by a [set_expo](#mapper-set_expo) command<br/>



*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- mapper-inverted_map_item-->
### <a name="mapper-inverted_map_item">Item of the inverted map</a><br/>
> Item of the inverted map:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM_UID, arg);
                if (arg != NULL)
                {
                    uint32_t uid = arg->value.U32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM_PRODUCT, arg);
                if (arg != NULL)
                {
                    uint16_t product = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM_AXIS, arg);
                if (arg != NULL)
                {
                    int32_t axis = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM_INVERTED, arg);
                if (arg != NULL)
                {
                    uint8_t inverted = arg->value.U8;
                }
            }
        }
        else
        {
            // list is empty
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM_UID, arg);
                if (arg != NULL)
                {
                    uint32_t uid = arg->value.U32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM_PRODUCT, arg);
                if (arg != NULL)
                {
                    uint16_t product = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM_AXIS, arg);
                if (arg != NULL)
                {
                    int32_t axis = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM_INVERTED, arg);
                if (arg != NULL)
                {
                    uint8_t inverted = arg->value.U8;
                }
            }
        }
        else
        {
            // list is empty
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    int uid = (int)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM_UID);
                    short product = (short)((Integer)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM_PRODUCT)).intValue();
                    int axis = (int)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM_AXIS);
                    byte inverted = (byte)((Integer)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_INVERTEDMAPITEM_INVERTED)).intValue();
                }
            }
        } else {
            // list is empty
        }
    }
}
```

Axis inversion has no effect on grabbed axes, nor on virtual buttons that might be generated from axes.<br/>


* uid (u32): Unique ID (for MAP_ITEM type)<br/>
* product (u16): Product (see libARDiscovery for list)<br/>
* axis (i32): Axis number<br/>
* inverted (u8): 0 : Axis not inverted.<br/>
1 : Axis inverted<br/>
* list_flags (bitfield as u8): Flags use by maps and lists<br/>
   * First: indicate it's the first element of the list.<br/>
   * Last: indicate it's the last element of the list.<br/>
   * Empty: indicate the list is empty (implies First/Last). All other arguments should be ignored.<br/>
   * Remove: This value should be removed from the existing list.<br/>


Triggered by a [set_inverted](#mapper-set_inverted) command<br/>



*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- mapper-active_product-->
### <a name="mapper-active_product">Active product for the mapper</a><br/>
> Active product for the mapper:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_ACTIVEPRODUCT) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_ACTIVEPRODUCT_PRODUCT, arg);
            if (arg != NULL)
            {
                uint16_t product = arg->value.U16;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_ACTIVEPRODUCT) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_ACTIVEPRODUCT_PRODUCT, arg);
            if (arg != NULL)
            {
                uint16_t product = arg->value.U16;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MAPPER_ACTIVEPRODUCT) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            short product = (short)((Integer)args.get(ARFeatureMapper.ARCONTROLLER_DICTIONARY_KEY_MAPPER_ACTIVEPRODUCT_PRODUCT)).intValue();
        }
    }
}
```

This event notifies the application about the currently active product, thus allowing the application to diplay and edit the current mapping without having to guess from other sources.<br/>


* product (u16): Product (see libARDiscovery for list)<br/>


Triggered when the active product changes<br/>



*Supported by <br/>*

- *SkyController 2 since 1.0.5*<br/>


<br/>

