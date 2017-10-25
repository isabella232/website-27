<!-- mapper_mini-button_mapping_item-->
### <a name="mapper_mini-button_mapping_item">Item of the button_actions mapping list</a><br/>
> Item of the button_actions mapping list:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM_UID, arg);
                if (arg != NULL)
                {
                    uint16_t uid = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM_MODES, arg);
                if (arg != NULL)
                {
                    uint8_t modes = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM_ACTION, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MAPPER_MINI_BUTTON_ACTION action = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM_BUTTONS, arg);
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM_UID, arg);
                if (arg != NULL)
                {
                    uint16_t uid = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM_MODES, arg);
                if (arg != NULL)
                {
                    uint8_t modes = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM_ACTION, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MAPPER_MINI_BUTTON_ACTION action = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM_BUTTONS, arg);
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    short uid = (short)((Integer)args.get(ARFeatureMapperMini.ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM_UID)).intValue();
                    byte modes = (byte)((Integer)args.get(ARFeatureMapperMini.ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM_MODES)).intValue();
                    ARCOMMANDS_MAPPER_MINI_BUTTON_ACTION_ENUM action = ARCOMMANDS_MAPPER_MINI_BUTTON_ACTION_ENUM.getFromValue((Integer)args.get(ARFeatureMapperMini.ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM_ACTION));
                    int buttons = (int)args.get(ARFeatureMapperMini.ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_BUTTONMAPPINGITEM_BUTTONS);
                }
            }
        } else {
            // list is empty
        }
    }
}
```

The resulting map describes all active button mappings of the product.<br/>
A mapping can affect one or mode modes, but each action can only be mapped once per mode.<br/>


* uid (u16): Unique ID of the mapping.<br/>
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


Triggered by a [map_button_action](#mapper_mini-map_button_action) or a [map_axis_action](#mapper_mini-map_axis_action) command<br/>



*Supported by <br/>*

- *Mambo*<br/>
- *Swing*<br/>


<br/>

<!-- mapper_mini-axis_mapping_item-->
### <a name="mapper_mini-axis_mapping_item">Item of the axis_actions mapping list</a><br/>
> Item of the axis_actions mapping list:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_UID, arg);
                if (arg != NULL)
                {
                    uint16_t uid = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_MODES, arg);
                if (arg != NULL)
                {
                    uint8_t modes = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_ACTION, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MAPPER_MINI_AXIS_ACTION action = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_AXIS, arg);
                if (arg != NULL)
                {
                    int8_t axis = arg->value.I8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_BUTTONS, arg);
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_UID, arg);
                if (arg != NULL)
                {
                    uint16_t uid = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_MODES, arg);
                if (arg != NULL)
                {
                    uint8_t modes = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_ACTION, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MAPPER_MINI_AXIS_ACTION action = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_AXIS, arg);
                if (arg != NULL)
                {
                    int8_t axis = arg->value.I8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_BUTTONS, arg);
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    short uid = (short)((Integer)args.get(ARFeatureMapperMini.ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_UID)).intValue();
                    byte modes = (byte)((Integer)args.get(ARFeatureMapperMini.ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_MODES)).intValue();
                    ARCOMMANDS_MAPPER_MINI_AXIS_ACTION_ENUM action = ARCOMMANDS_MAPPER_MINI_AXIS_ACTION_ENUM.getFromValue((Integer)args.get(ARFeatureMapperMini.ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_ACTION));
                    byte axis = (byte)((Integer)args.get(ARFeatureMapperMini.ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_AXIS)).intValue();
                    int buttons = (int)args.get(ARFeatureMapperMini.ARCONTROLLER_DICTIONARY_KEY_MAPPER_MINI_AXISMAPPINGITEM_BUTTONS);
                }
            }
        } else {
            // list is empty
        }
    }
}
```

The resulting map describes all active axis mappings of the product.<br/>
A mapping can affect one or mode modes, but each action can only be mapped once per mode.<br/>


* uid (u16): Unique ID of the mapping.<br/>
* modes (bitfield as u8): The piloting mode of the product<br/>
   * quad: Quadricopter mode<br/>
   * plane: Plane mode<br/>
* action (enum): The action (mapped on an axis)<br/>
   * roll: roll<br/>
   * pitch: pitch<br/>
   * yaw: yaw<br/>
   * gaz: gaz<br/>
* axis (i8): The axis number on which the action is mapped.<br/>
* buttons (u32): Buttons combination mapped to the action (bitfield).<br/>


Triggered by a [map_button_action](#mapper_mini-map_button_action) or a [map_axis_action](#mapper_mini-map_axis_action) command<br/>



*Supported by <br/>*

- *Mambo*<br/>
- *Swing*<br/>


<br/>

