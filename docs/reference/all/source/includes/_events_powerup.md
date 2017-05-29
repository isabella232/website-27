<!-- powerup-PilotingState-AlertStateChanged-->
### <a name="powerup-PilotingState-AlertStateChanged">JS alert state changed</a><br/>
> JS alert state changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ALERTSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ALERTSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_PILOTINGSTATE_ALERTSTATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ALERTSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ALERTSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_PILOTINGSTATE_ALERTSTATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ALERTSTATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_POWERUP_PILOTINGSTATE_ALERTSTATECHANGED_STATE_ENUM state = ARCOMMANDS_POWERUP_PILOTINGSTATE_ALERTSTATECHANGED_STATE_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ALERTSTATECHANGED_STATE));
        }
    }
}
```

JS alert state changed<br/>


* state (enum): JS alert state<br/>
   * none: No alert<br/>
   * critical_battery: Critical battery alert<br/>
   * low_battery: Low battery alert<br/>
<br/>

<!-- powerup-PilotingState-FlyingStateChanged-->
### <a name="powerup-PilotingState-FlyingStateChanged">Drone flying state changed</a><br/>
> Drone flying state changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_FLYINGSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_FLYINGSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_PILOTINGSTATE_FLYINGSTATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_FLYINGSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_FLYINGSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_PILOTINGSTATE_FLYINGSTATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_FLYINGSTATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_POWERUP_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM state = ARCOMMANDS_POWERUP_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_FLYINGSTATECHANGED_STATE));
        }
    }
}
```

Drone flying state changed<br/>


* state (enum): Drone flying state<br/>
   * landed: Landed state<br/>
   * takingoff: Taking off state<br/>
   * flying: Flying state<br/>
   * recovery: Recovery state<br/>
   * emergency: Emergency state<br/>
   * usertakeoff: User take off state. Waiting for user action to take off.<br/>
   * init: Initializing state (user should let the drone steady for a while)<br/>
<br/>

<!-- powerup-PilotingState-MotorModeChanged-->
### <a name="powerup-PilotingState-MotorModeChanged">Motor mode changed</a><br/>
> Motor mode changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_MOTORMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_MOTORMODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_PILOTINGSTATE_MOTORMODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_MOTORMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_MOTORMODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_PILOTINGSTATE_MOTORMODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_MOTORMODECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_POWERUP_PILOTINGSTATE_MOTORMODECHANGED_MODE_ENUM mode = ARCOMMANDS_POWERUP_PILOTINGSTATE_MOTORMODECHANGED_MODE_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_MOTORMODECHANGED_MODE));
        }
    }
}
```

Motor mode changed<br/>


* mode (enum): <br/>
   * normal: The motors will only start on user action after being in state user take off<br/>
   * forced: Motors will use the current pcmd values without considering the flying state<br/>
<br/>

<!-- powerup-PilotingState-AttitudeChanged-->
### <a name="powerup-PilotingState-AttitudeChanged">Drone attitude changed</a><br/>
> Drone attitude changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ATTITUDECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ATTITUDECHANGED_ROLL, arg);
            if (arg != NULL)
            {
                float roll = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ATTITUDECHANGED_PITCH, arg);
            if (arg != NULL)
            {
                float pitch = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ATTITUDECHANGED_YAW, arg);
            if (arg != NULL)
            {
                float yaw = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ATTITUDECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ATTITUDECHANGED_ROLL, arg);
            if (arg != NULL)
            {
                float roll = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ATTITUDECHANGED_PITCH, arg);
            if (arg != NULL)
            {
                float pitch = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ATTITUDECHANGED_YAW, arg);
            if (arg != NULL)
            {
                float yaw = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ATTITUDECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float roll = (float)((Double)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ATTITUDECHANGED_ROLL)).doubleValue();
            float pitch = (float)((Double)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ATTITUDECHANGED_PITCH)).doubleValue();
            float yaw = (float)((Double)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ATTITUDECHANGED_YAW)).doubleValue();
        }
    }
}
```

Drone attitude changed<br/>


* roll (float): roll value (in radian) (relative to horizontal)<br/>
* pitch (float): Pitch value (in radian) (relative to horizontal)<br/>
* yaw (float): Yaw value (in radian) (relative to North)<br/>
<br/>

<!-- powerup-PilotingState-AltitudeChanged-->
### <a name="powerup-PilotingState-AltitudeChanged">Drone altitude changed</a><br/>
> Drone altitude changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ALTITUDECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ALTITUDECHANGED_ALTITUDE, arg);
            if (arg != NULL)
            {
                float altitude = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ALTITUDECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ALTITUDECHANGED_ALTITUDE, arg);
            if (arg != NULL)
            {
                float altitude = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ALTITUDECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float altitude = (float)((Double)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSTATE_ALTITUDECHANGED_ALTITUDE)).doubleValue();
        }
    }
}
```

Drone altitude changed<br/>


* altitude (float): Altitude in meters relative to take off altitude<br/>
<br/>

<!-- powerup-PilotingSettingsState-settingChanged-->
### <a name="powerup-PilotingSettingsState-settingChanged">Fired when a setting has changed</a><br/>
> Fired when a setting has changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_SETTING, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_SETTING setting = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_CURRENT, arg);
                if (arg != NULL)
                {
                    float current = arg->value.Float;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_MIN, arg);
                if (arg != NULL)
                {
                    float min = arg->value.Float;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_MAX, arg);
                if (arg != NULL)
                {
                    float max = arg->value.Float;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_SETTING, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_SETTING setting = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_CURRENT, arg);
                if (arg != NULL)
                {
                    float current = arg->value.Float;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_MIN, arg);
                if (arg != NULL)
                {
                    float min = arg->value.Float;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_MAX, arg);
                if (arg != NULL)
                {
                    float max = arg->value.Float;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    ARCOMMANDS_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_SETTING_ENUM setting = ARCOMMANDS_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_SETTING_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_SETTING));
                    float current = (float)((Double)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_CURRENT)).doubleValue();
                    float min = (float)((Double)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_MIN)).doubleValue();
                    float max = (float)((Double)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_PILOTINGSETTINGSSTATE_SETTINGCHANGED_MAX)).doubleValue();
                }
            }
        } else {
            // list is empty
        }
    }
}
```

Fired when a setting has changed<br/>


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
   * WIND_SPEED: Wind speed in m/s.<br/>
   * PLANE_SPEED: Target plane speed in m/s.<br/>
* current (float): Current value of the given setting<br/>
* min (float): Minimal value of the given setting<br/>
* max (float): Max value of the given setting<br/>
<br/>

<!-- powerup-MediaRecordState-PictureStateChangedV2-->
### <a name="powerup-MediaRecordState-PictureStateChangedV2">State of device picture recording changed</a><br/>
> State of device picture recording changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE_ENUM state = ARCOMMANDS_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE));
            ARCOMMANDS_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR_ENUM error = ARCOMMANDS_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR));
        }
    }
}
```

State of device picture recording changed<br/>


* state (enum): State of device picture recording<br/>
   * ready: The picture recording is ready<br/>
   * busy: The picture recording is busy<br/>
   * notAvailable: The picture recording is not available<br/>
* error (enum): Error to explain the state<br/>
   * ok: No Error<br/>
   * unknown: Unknown generic error<br/>
   * camera_ko: Picture camera is out of order<br/>
   * memoryFull: Memory full ; cannot save one additional picture<br/>
   * lowBattery: Battery is too low to start/keep recording.<br/>
<br/>

<!-- powerup-MediaRecordState-VideoStateChangedV2-->
### <a name="powerup-MediaRecordState-VideoStateChangedV2">State of device video recording changed</a><br/>
> State of device video recording changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_STATE_ENUM state = ARCOMMANDS_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_STATE_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_STATE));
            ARCOMMANDS_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_ERROR_ENUM error = ARCOMMANDS_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_ERROR_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_ERROR));
        }
    }
}
```

State of device video recording changed<br/>


* state (enum): State of device video recording<br/>
   * stopped: Video is stopped<br/>
   * started: Video is started<br/>
   * notAvailable: The video recording is not available<br/>
* error (enum): Error to explain the state<br/>
   * ok: No Error<br/>
   * unknown: Unknown generic error<br/>
   * camera_ko: Video camera is out of order<br/>
   * memoryFull: Memory full ; cannot save one additional video<br/>
   * lowBattery: Battery is too low to start/keep recording.<br/>
<br/>

<!-- powerup-MediaRecordEvent-PictureEventChanged-->
### <a name="powerup-MediaRecordEvent-PictureEventChanged">Event of picture recording</a><br/>
> Event of picture recording:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT event = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT event = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT_ENUM event = ARCOMMANDS_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT));
            ARCOMMANDS_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR_ENUM error = ARCOMMANDS_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR));
        }
    }
}
```

Event of picture recording<br/>


* event (enum): Last event of picture recording<br/>
   * taken: Picture taken and saved<br/>
   * failed: Picture failed<br/>
* error (enum): Error to explain the event<br/>
   * ok: No Error<br/>
   * unknown: Unknown generic error ; only when state is failed<br/>
   * busy: Picture recording is busy ; only when state is failed<br/>
   * notAvailable: Picture recording not available ; only when state is failed<br/>
   * memoryFull: Memory full ; only when state is failed<br/>
   * lowBattery: Battery is too low to record.<br/>
<br/>

<!-- powerup-MediaRecordEvent-VideoEventChanged-->
### <a name="powerup-MediaRecordEvent-VideoEventChanged">Event of video recording</a><br/>
> Event of video recording:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED_EVENT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED_EVENT event = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED_EVENT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED_EVENT event = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED_EVENT_ENUM event = ARCOMMANDS_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED_EVENT_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED_EVENT));
            ARCOMMANDS_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED_ERROR_ENUM error = ARCOMMANDS_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED_ERROR_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIARECORDEVENT_VIDEOEVENTCHANGED_ERROR));
        }
    }
}
```

Event of video recording<br/>


* event (enum): Event of video recording<br/>
   * start: Video start<br/>
   * stop: Video stop and saved<br/>
   * failed: Video failed<br/>
* error (enum): Error to explain the event<br/>
   * ok: No Error<br/>
   * unknown: Unknown generic error ; only when state is failed<br/>
   * busy: Video recording is busy ; only when state is failed<br/>
   * notAvailable: Video recording not available ; only when state is failed<br/>
   * memoryFull: Memory full<br/>
   * lowBattery: Battery is too low to record.<br/>
   * autoStopped: Video was auto stopped<br/>
<br/>

<!-- powerup-NetworkSettingsState-WifiSelectionChanged-->
### <a name="powerup-NetworkSettingsState-WifiSelectionChanged">Wifi selection from product</a><br/>
> Wifi selection from product:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_BAND, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_BAND band = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_CHANNEL, arg);
            if (arg != NULL)
            {
                uint8_t channel = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_BAND, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_BAND band = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_CHANNEL, arg);
            if (arg != NULL)
            {
                uint8_t channel = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE_ENUM type = ARCOMMANDS_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE));
            ARCOMMANDS_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_BAND_ENUM band = ARCOMMANDS_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_BAND_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_BAND));
            byte channel = (byte)((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_CHANNEL)).intValue();
        }
    }
}
```

Wifi selection from product<br/>


* type (enum): The type of wifi selection settings<br/>
   * auto_all: Auto selection<br/>
   * auto_2_4ghz: Auto selection 2.4ghz<br/>
   * auto_5ghz: Auto selection 5 ghz<br/>
   * manual: Manual selection<br/>
* band (enum): The actual wifi band state<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
   * all: Both 2.4 and 5 GHz bands<br/>
* channel (u8): The channel (depends of the band)<br/>
<br/>

<!-- powerup-NetworkState-WifiScanListChanged-->
### <a name="powerup-NetworkState-WifiScanListChanged">One scanning result found</a><br/>
> One scanning result found:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_SSID, arg);
                if (arg != NULL)
                {
                    char * ssid = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_RSSI, arg);
                if (arg != NULL)
                {
                    int16_t rssi = arg->value.I16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_BAND, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_BAND band = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_CHANNEL, arg);
                if (arg != NULL)
                {
                    uint8_t channel = arg->value.U8;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_SSID, arg);
                if (arg != NULL)
                {
                    char * ssid = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_RSSI, arg);
                if (arg != NULL)
                {
                    int16_t rssi = arg->value.I16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_BAND, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_BAND band = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_CHANNEL, arg);
                if (arg != NULL)
                {
                    uint8_t channel = arg->value.U8;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    String ssid = (String)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_SSID);
                    short rssi = (short)((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_RSSI)).intValue();
                    ARCOMMANDS_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_BAND_ENUM band = ARCOMMANDS_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_BAND_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_BAND));
                    byte channel = (byte)((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFISCANLISTCHANGED_CHANNEL)).intValue();
                }
            }
        } else {
            // list is empty
        }
    }
}
```

One scanning result found<br/>


* ssid (string): SSID of the AP<br/>
* rssi (i16): RSSI of the AP in dbm (negative value)<br/>
* band (enum): The band : 2.4 GHz or 5 GHz<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
* channel (u8): Channel of the AP<br/>
<br/>

<!-- powerup-NetworkState-AllWifiScanChanged-->
### <a name="powerup-NetworkState-AllWifiScanChanged">State sent when all scanning result sent</a><br/>
> State sent when all scanning result sent:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_ALLWIFISCANCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_ALLWIFISCANCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_ALLWIFISCANCHANGED) && (elementDictionary != null)){

    }
}
```

State sent when all scanning result sent<br/>


<br/>

<!-- powerup-NetworkState-WifiAuthChannelListChanged-->
### <a name="powerup-NetworkState-WifiAuthChannelListChanged">Notify of an Authorized Channel.</a><br/>
> Notify of an Authorized Channel.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_BAND, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_BAND band = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_CHANNEL, arg);
                if (arg != NULL)
                {
                    uint8_t channel = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_IN_OR_OUT, arg);
                if (arg != NULL)
                {
                    uint8_t in_or_out = arg->value.U8;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_BAND, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_BAND band = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_CHANNEL, arg);
                if (arg != NULL)
                {
                    uint8_t channel = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_IN_OR_OUT, arg);
                if (arg != NULL)
                {
                    uint8_t in_or_out = arg->value.U8;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    ARCOMMANDS_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_BAND_ENUM band = ARCOMMANDS_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_BAND_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_BAND));
                    byte channel = (byte)((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_CHANNEL)).intValue();
                    byte in_or_out = (byte)((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_IN_OR_OUT)).intValue();
                }
            }
        } else {
            // list is empty
        }
    }
}
```

Notify of an Authorized Channel.<br/>


* band (enum): The band of this channel : 2.4 GHz or 5 GHz<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
* channel (u8): The authorized channel.<br/>
* in_or_out (u8): Bit 0 is 1 if channel is authorized outside (0 otherwise) ; Bit 1 is 1 if channel is authorized inside (0 otherwise)<br/>
<br/>

<!-- powerup-NetworkState-AllWifiAuthChannelChanged-->
### <a name="powerup-NetworkState-AllWifiAuthChannelChanged">Notify the end of the list of Authorized wifi Channel.</a><br/>
> Notify the end of the list of Authorized wifi Channel.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_ALLWIFIAUTHCHANNELCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_ALLWIFIAUTHCHANNELCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_ALLWIFIAUTHCHANNELCHANGED) && (elementDictionary != null)){

    }
}
```

Notify the end of the list of Authorized wifi Channel.<br/>


<br/>

<!-- powerup-NetworkState-LinkQualityChanged-->
### <a name="powerup-NetworkState-LinkQualityChanged">Notification sent by the firmware to give an indication of the WiFi link quality.</a><br/>
> Notification sent by the firmware to give an indication of the WiFi link quality.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_LINKQUALITYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_LINKQUALITYCHANGED_QUALITY, arg);
            if (arg != NULL)
            {
                uint8_t quality = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_LINKQUALITYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_LINKQUALITYCHANGED_QUALITY, arg);
            if (arg != NULL)
            {
                uint8_t quality = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_LINKQUALITYCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte quality = (byte)((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_NETWORKSTATE_LINKQUALITYCHANGED_QUALITY)).intValue();
        }
    }
}
```

Notification sent by the firmware to give an indication of the WiFi link quality.<br/>


* quality (u8): The WiFi link quality in range 0-6, the higher the value, the higher the link quality.<br/>
<br/>

<!-- powerup-MediaStreamingState-VideoEnableChanged-->
### <a name="powerup-MediaStreamingState-VideoEnableChanged">Return video streaming status.</a><br/>
> Return video streaming status.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED_ENABLED, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED_ENABLED enabled = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED_ENABLED, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED_ENABLED enabled = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_POWERUP_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED_ENABLED_ENUM enabled = ARCOMMANDS_POWERUP_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED_ENABLED_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED_ENABLED));
        }
    }
}
```

Return video streaming status.<br/>


* enabled (enum): Current video streaming status.<br/>
   * enabled: Video streaming is enabled.<br/>
   * disabled: Video streaming is disabled.<br/>
   * error: Video streaming failed to start.<br/>
<br/>

<!-- powerup-VideoSettingsState-AutorecordChanged-->
### <a name="powerup-VideoSettingsState-AutorecordChanged">Get video automatic recording status.</a><br/>
> Get video automatic recording status.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_VIDEOSETTINGSSTATE_AUTORECORDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_VIDEOSETTINGSSTATE_AUTORECORDCHANGED_ENABLED, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_VIDEOSETTINGSSTATE_AUTORECORDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_VIDEOSETTINGSSTATE_AUTORECORDCHANGED_ENABLED, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_VIDEOSETTINGSSTATE_AUTORECORDCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte enabled = (byte)((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_VIDEOSETTINGSSTATE_AUTORECORDCHANGED_ENABLED)).intValue();
        }
    }
}
```

Get video automatic recording status.<br/>


* enabled (u8): 0: Disabled 1: Enabled.<br/>
<br/>

<!-- powerup-VideoSettingsState-VideoModeChanged-->
### <a name="powerup-VideoSettingsState-VideoModeChanged">Video mode</a><br/>
> Video mode:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_VIDEOSETTINGSSTATE_VIDEOMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_VIDEOSETTINGSSTATE_VIDEOMODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_VIDEOSETTINGSSTATE_VIDEOMODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_VIDEOSETTINGSSTATE_VIDEOMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_VIDEOSETTINGSSTATE_VIDEOMODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_POWERUP_VIDEOSETTINGSSTATE_VIDEOMODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_VIDEOSETTINGSSTATE_VIDEOMODECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_POWERUP_VIDEOSETTINGSSTATE_VIDEOMODECHANGED_MODE_ENUM mode = ARCOMMANDS_POWERUP_VIDEOSETTINGSSTATE_VIDEOMODECHANGED_MODE_ENUM.getFromValue((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_VIDEOSETTINGSSTATE_VIDEOMODECHANGED_MODE));
        }
    }
}
```

Video mode<br/>


* mode (enum): Video mode<br/>
   * quality: Maximize video quality (VGA 30fps).<br/>
   * performance: Maximize video performance (QVGA 24fps).<br/>
<br/>

<!-- powerup-SoundsState-buzzChanged-->
### <a name="powerup-SoundsState-buzzChanged">State of the buzzer</a><br/>
> State of the buzzer:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_SOUNDSSTATE_BUZZCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_SOUNDSSTATE_BUZZCHANGED_ENABLED, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_POWERUP_SOUNDSSTATE_BUZZCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_POWERUP_SOUNDSSTATE_BUZZCHANGED_ENABLED, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_POWERUP_SOUNDSSTATE_BUZZCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte enabled = (byte)((Integer)args.get(ARFeaturePowerup.ARCONTROLLER_DICTIONARY_KEY_POWERUP_SOUNDSSTATE_BUZZCHANGED_ENABLED)).intValue();
        }
    }
}
```

State of the buzzer<br/>


* enabled (u8): 0: Disabled 1: Enabled.<br/>
<br/>

