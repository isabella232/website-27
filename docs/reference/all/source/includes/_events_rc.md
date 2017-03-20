<!-- rc-receiver_state-->
### <a name="rc-receiver_state">State of drone RC receiver</a><br/>
> State of drone RC receiver:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_RC_RECEIVERSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_RECEIVERSTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_RC_RECEIVER_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_RECEIVERSTATE_PROTOCOL, arg);
            if (arg != NULL)
            {
                char * protocol = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_RECEIVERSTATE_ENABLED, arg);
            if (arg != NULL)
            {
                uint8_t enabled = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_RC_RECEIVERSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_RECEIVERSTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_RC_RECEIVER_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_RECEIVERSTATE_PROTOCOL, arg);
            if (arg != NULL)
            {
                char * protocol = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_RECEIVERSTATE_ENABLED, arg);
            if (arg != NULL)
            {
                uint8_t enabled = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_RC_RECEIVERSTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_RC_RECEIVER_STATE_ENUM state = ARCOMMANDS_RC_RECEIVER_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_RECEIVERSTATE_STATE));
            String protocol = (String)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_RECEIVERSTATE_PROTOCOL);
            byte enabled = (byte)((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_RECEIVERSTATE_ENABLED)).intValue();
        }
    }
}
```

State of drone RC receiver<br/>


* state (enum): RC Receiver state.<br/>
   * connected: RC drone receiver connected to a RC.<br/>
   * disconnected: RC drone receiver not connected to a RC.<br/>
* protocol (string): Protocol used by RC.<br/>
* enabled (u8): 1 if enabled, 0 otherwise.<br/>
If enabled, drone will apply values sent by RC receiver.<br/>
<br/>

<!-- rc-channels_monitor_state-->
### <a name="rc-channels_monitor_state">RC channels monitor state</a><br/>
> RC channels monitor state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELSMONITORSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELSMONITORSTATE_STATE, arg);
            if (arg != NULL)
            {
                uint8_t state = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELSMONITORSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELSMONITORSTATE_STATE, arg);
            if (arg != NULL)
            {
                uint8_t state = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELSMONITORSTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte state = (byte)((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELSMONITORSTATE_STATE)).intValue();
        }
    }
}
```

RC Channel monitor state sent by drone<br/>


* state (u8): 1 if enabled, 0 if disabled<br/>
<br/>

<!-- rc-channel_value-->
### <a name="rc-channel_value">RC channels value</a><br/>
> RC channels value:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELVALUE)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELVALUE_ID, arg);
                if (arg != NULL)
                {
                    uint8_t id = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELVALUE_ACTION, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_RC_CHANNEL_ACTION action = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELVALUE_VALUE, arg);
                if (arg != NULL)
                {
                    int16_t value = arg->value.I16;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELVALUE)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELVALUE_ID, arg);
                if (arg != NULL)
                {
                    uint8_t id = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELVALUE_ACTION, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_RC_CHANNEL_ACTION action = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELVALUE_VALUE, arg);
                if (arg != NULL)
                {
                    int16_t value = arg->value.I16;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELVALUE){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    byte id = (byte)((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELVALUE_ID)).intValue();
                    ARCOMMANDS_RC_CHANNEL_ACTION_ENUM action = ARCOMMANDS_RC_CHANNEL_ACTION_ENUM.getFromValue((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELVALUE_ACTION));
                    short value = (short)((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELVALUE_VALUE)).intValue();
                }
            }
        } else {
            // list is empty
        }
    }
}
```

RC Channel value sent by drone<br/>


* id (u8): RC channel id.<br/>
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
* value (i16): RC channel value.<br/>
* list_flags (bitfield as u8): Flags use by maps and lists<br/>
   * First: indicate it's the first element of the list.<br/>
   * Last: indicate it's the last element of the list.<br/>
   * Empty: indicate the list is empty (implies First/Last). All other arguments should be ignored.<br/>
   * Remove: This value should be removed from the existing list.<br/>
<br/>

<!-- rc-calibration_state-->
### <a name="rc-calibration_state">Channels calibration state</a><br/>
> Channels calibration state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_CALIBRATION_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_RC_CALIBRATION_TYPE calibration_type = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_CHANNEL_ACTION, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_RC_CHANNEL_ACTION channel_action = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_REQUIRED, arg);
            if (arg != NULL)
            {
                uint32_t required = arg->value.U32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_CALIBRATED, arg);
            if (arg != NULL)
            {
                uint32_t calibrated = arg->value.U32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_NEUTRAL_CALIBRATED, arg);
            if (arg != NULL)
            {
                uint8_t neutral_calibrated = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_CALIBRATION_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_RC_CALIBRATION_TYPE calibration_type = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_CHANNEL_ACTION, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_RC_CHANNEL_ACTION channel_action = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_REQUIRED, arg);
            if (arg != NULL)
            {
                uint32_t required = arg->value.U32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_CALIBRATED, arg);
            if (arg != NULL)
            {
                uint32_t calibrated = arg->value.U32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_NEUTRAL_CALIBRATED, arg);
            if (arg != NULL)
            {
                uint8_t neutral_calibrated = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_RC_CALIBRATION_TYPE_ENUM calibration_type = ARCOMMANDS_RC_CALIBRATION_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_CALIBRATION_TYPE));
            ARCOMMANDS_RC_CHANNEL_ACTION_ENUM channel_action = ARCOMMANDS_RC_CHANNEL_ACTION_ENUM.getFromValue((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_CHANNEL_ACTION));
            int required = (int)((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_REQUIRED)).intValue();
            int calibrated = (int)((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_CALIBRATED)).intValue();
            byte neutral_calibrated = (byte)((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_CALIBRATIONSTATE_NEUTRAL_CALIBRATED)).intValue();
        }
    }
}
```

RC Channels calibration state sent by drone.<br/>


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
* required (bitfield as u32): Channel action.<br/>
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
* calibrated (bitfield as u32): Channel action.<br/>
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
* neutral_calibrated (u8): 1 if neutral channels are calibrated, 0 otherwise.<br/>
<br/>

<!-- rc-channel_action_item-->
### <a name="rc-channel_action_item">Channel action item</a><br/>
> Channel action item:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM_ACTION, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_RC_CHANNEL_ACTION action = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM_SUPPORTED_TYPE, arg);
                if (arg != NULL)
                {
                    uint32_t supported_type = arg->value.U32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM_CALIBRATED_TYPE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_RC_CHANNEL_TYPE calibrated_type = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM_INVERTED, arg);
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM_ACTION, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_RC_CHANNEL_ACTION action = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM_SUPPORTED_TYPE, arg);
                if (arg != NULL)
                {
                    uint32_t supported_type = arg->value.U32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM_CALIBRATED_TYPE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_RC_CHANNEL_TYPE calibrated_type = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM_INVERTED, arg);
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    ARCOMMANDS_RC_CHANNEL_ACTION_ENUM action = ARCOMMANDS_RC_CHANNEL_ACTION_ENUM.getFromValue((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM_ACTION));
                    int supported_type = (int)((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM_SUPPORTED_TYPE)).intValue();
                    ARCOMMANDS_RC_CHANNEL_TYPE_ENUM calibrated_type = ARCOMMANDS_RC_CHANNEL_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM_CALIBRATED_TYPE));
                    byte inverted = (byte)((Integer)args.get(ARFeatureRc.ARCONTROLLER_DICTIONARY_KEY_RC_CHANNELACTIONITEM_INVERTED)).intValue();
                }
            }
        } else {
            // list is empty
        }
    }
}
```

Channel action supported by drone.<br/>


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
* supported_type (bitfield as u32): Channel physical type.<br/>
   * invalid: Invalid channel physical type.<br/>
   * signed_axis: Signed axis type.<br/>
   * unsigned_axis: Unsigned axis type.<br/>
   * monostable_button: Monostable button type.<br/>
   * bistable_button: Bistable button type.<br/>
   * tristate_button: Tristate button type.<br/>
   * rotary_button: Rotary button type.<br/>
* calibrated_type (enum): Channel physical type.<br/>
   * invalid: Invalid channel physical type.<br/>
   * signed_axis: Signed axis type.<br/>
   * unsigned_axis: Unsigned axis type.<br/>
   * monostable_button: Monostable button type.<br/>
   * bistable_button: Bistable button type.<br/>
   * tristate_button: Tristate button type.<br/>
   * rotary_button: Rotary button type.<br/>
* inverted (u8): 1 if inverted, 0 otherwise.<br/>
<br/>

