<!-- MiniDrone-PilotingState-FlatTrimChanged-->
### <a name="MiniDrone-PilotingState-FlatTrimChanged">MiniDrone send flat trim was correctly processed</a><br/>
> MiniDrone send flat trim was correctly processed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLATTRIMCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLATTRIMCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLATTRIMCHANGED) && (elementDictionary != null)){

    }
}
```

MiniDrone send flat trim was correctly processed<br/>


<br/>

<!-- MiniDrone-PilotingState-FlyingStateChanged-->
### <a name="MiniDrone-PilotingState-FlyingStateChanged">Drone flying state changed</a><br/>
> Drone flying state changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLYINGSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLYINGSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_PILOTINGSTATE_FLYINGSTATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLYINGSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLYINGSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_PILOTINGSTATE_FLYINGSTATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLYINGSTATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MINIDRONE_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM state = ARCOMMANDS_MINIDRONE_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLYINGSTATECHANGED_STATE));
        }
    }
}
```

Drone flying state changed<br/>


* state (enum): Drone flying state<br/>
   * landed: Landed state<br/>
   * takingoff: Taking off state<br/>
   * hovering: Hovering state<br/>
   * flying: Flying state<br/>
   * landing: Landing state<br/>
   * emergency: Emergency state<br/>
   * rolling: Rolling state<br/>
   * init: Initializing state (user should let the drone steady for a while)<br/>
<br/>

<!-- MiniDrone-PilotingState-AlertStateChanged-->
### <a name="MiniDrone-PilotingState-AlertStateChanged">Drone alert state changed</a><br/>
> Drone alert state changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_ALERTSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_ALERTSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_PILOTINGSTATE_ALERTSTATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_ALERTSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_ALERTSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_PILOTINGSTATE_ALERTSTATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_ALERTSTATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MINIDRONE_PILOTINGSTATE_ALERTSTATECHANGED_STATE_ENUM state = ARCOMMANDS_MINIDRONE_PILOTINGSTATE_ALERTSTATECHANGED_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_ALERTSTATECHANGED_STATE));
        }
    }
}
```

Drone alert state changed<br/>


* state (enum): Drone alert state<br/>
   * none: No alert<br/>
   * user: User emergency alert<br/>
   * cut_out: Cut out alert<br/>
   * critical_battery: Critical battery alert<br/>
   * low_battery: Low battery alert<br/>
<br/>

<!-- MiniDrone-PilotingState-AutoTakeOffModeChanged-->
### <a name="MiniDrone-PilotingState-AutoTakeOffModeChanged">Set MiniDrone automatic take off mode</a><br/>
> Set MiniDrone automatic take off mode:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_AUTOTAKEOFFMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_AUTOTAKEOFFMODECHANGED_STATE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_AUTOTAKEOFFMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_AUTOTAKEOFFMODECHANGED_STATE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_AUTOTAKEOFFMODECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte state = (byte)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_AUTOTAKEOFFMODECHANGED_STATE)).intValue();
        }
    }
}
```

Set MiniDrone automatic take off mode<br/>


* state (u8): State of automatic take off mode<br/>
<br/>

<!-- MiniDrone-PilotingState-FlyingModeChanged-->
### <a name="MiniDrone-PilotingState-FlyingModeChanged">FlyingMode changed. Only supported by WingX</a><br/>
> FlyingMode changed. Only supported by WingX:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLYINGMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLYINGMODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_PILOTINGSTATE_FLYINGMODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLYINGMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLYINGMODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_PILOTINGSTATE_FLYINGMODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLYINGMODECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MINIDRONE_PILOTINGSTATE_FLYINGMODECHANGED_MODE_ENUM mode = ARCOMMANDS_MINIDRONE_PILOTINGSTATE_FLYINGMODECHANGED_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_FLYINGMODECHANGED_MODE));
        }
    }
}
```

FlyingMode changed. Only supported by WingX<br/>


* mode (enum): Drone Flying Mode<br/>
   * quadricopter: Fly as a quadrictopter<br/>
   * plane_forward: Fly as a plane in forward mode<br/>
   * plane_backward: Fly as a plane in backward mode<br/>
<br/>

<!-- MiniDrone-PilotingState-PlaneGearBoxChanged-->
### <a name="MiniDrone-PilotingState-PlaneGearBoxChanged">Plane Gear Box changed. Only supported by WingX</a><br/>
> Plane Gear Box changed. Only supported by WingX:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_PLANEGEARBOXCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_PLANEGEARBOXCHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_PILOTINGSTATE_PLANEGEARBOXCHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_PLANEGEARBOXCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_PLANEGEARBOXCHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_PILOTINGSTATE_PLANEGEARBOXCHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_PLANEGEARBOXCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MINIDRONE_PILOTINGSTATE_PLANEGEARBOXCHANGED_STATE_ENUM state = ARCOMMANDS_MINIDRONE_PILOTINGSTATE_PLANEGEARBOXCHANGED_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_PLANEGEARBOXCHANGED_STATE));
        }
    }
}
```

Plane Gear Box changed. Only supported by WingX<br/>


* state (enum): Plane Gear Box<br/>
   * gear_1: Gear 1. Low speed<br/>
   * gear_2: Gear 2. Middle speed<br/>
   * gear_3: Gear 3. High speed<br/>
<br/>

<!-- MiniDrone-PilotingState-PilotingModeChanged-->
### <a name="MiniDrone-PilotingState-PilotingModeChanged">Event informing about the piloting mode.</a><br/>
> Event informing about the piloting mode.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_PILOTINGMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_PILOTINGMODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_PILOTINGSTATE_PILOTINGMODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_PILOTINGMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_PILOTINGMODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_PILOTINGSTATE_PILOTINGMODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_PILOTINGMODECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MINIDRONE_PILOTINGSTATE_PILOTINGMODECHANGED_MODE_ENUM mode = ARCOMMANDS_MINIDRONE_PILOTINGSTATE_PILOTINGMODECHANGED_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSTATE_PILOTINGMODECHANGED_MODE));
        }
    }
}
```

Event informing about the piloting mode.<br/>


* mode (enum): <br/>
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

<!-- MiniDrone-MediaRecordState-PictureStateChanged-->
### <a name="MiniDrone-MediaRecordState-PictureStateChanged">@deprecated</a><br/>
> @deprecated:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                uint8_t state = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGED_MASS_STORAGE_ID, arg);
            if (arg != NULL)
            {
                uint8_t mass_storage_id = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                uint8_t state = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGED_MASS_STORAGE_ID, arg);
            if (arg != NULL)
            {
                uint8_t mass_storage_id = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte state = (byte)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGED_STATE)).intValue();
            byte mass_storage_id = (byte)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGED_MASS_STORAGE_ID)).intValue();
        }
    }
}
```

@deprecated<br/>
State of picture recording<br/>


* state (u8): 1 if picture has been taken, 0 otherwise<br/>
* mass_storage_id (u8): Mass storage id to record<br/>
<br/>

<!-- MiniDrone-MediaRecordState-PictureStateChangedV2-->
### <a name="MiniDrone-MediaRecordState-PictureStateChangedV2">State of device picture recording changed</a><br/>
> State of device picture recording changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE_ENUM state = ARCOMMANDS_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE));
            ARCOMMANDS_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR_ENUM error = ARCOMMANDS_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR));
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

<!-- MiniDrone-MediaRecordEvent-PictureEventChanged-->
### <a name="MiniDrone-MediaRecordEvent-PictureEventChanged">Event of picture recording</a><br/>
> Event of picture recording:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT event = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT event = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT_ENUM event = ARCOMMANDS_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT));
            ARCOMMANDS_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR_ENUM error = ARCOMMANDS_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR));
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

<!-- MiniDrone-PilotingSettingsState-MaxAltitudeChanged-->
### <a name="MiniDrone-PilotingSettingsState-MaxAltitudeChanged">Max Altitude sent by product</a><br/>
> Max Altitude sent by product:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_MAX, arg);
            if (arg != NULL)
            {
                float max = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_MAX, arg);
            if (arg != NULL)
            {
                float max = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float current = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_CURRENT)).doubleValue();
            float min = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_MIN)).doubleValue();
            float max = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_MAX)).doubleValue();
        }
    }
}
```

Max Altitude sent by product<br/>


* current (float): Current altitude max<br/>
* min (float): Range min of altitude<br/>
* max (float): Range max of altitude<br/>
<br/>

<!-- MiniDrone-PilotingSettingsState-MaxTiltChanged-->
### <a name="MiniDrone-PilotingSettingsState-MaxTiltChanged">Max tilt sent by product</a><br/>
> Max tilt sent by product:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTILTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_MAX, arg);
            if (arg != NULL)
            {
                float max = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTILTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_MAX, arg);
            if (arg != NULL)
            {
                float max = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTILTCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float current = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_CURRENT)).doubleValue();
            float min = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_MIN)).doubleValue();
            float max = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_MAX)).doubleValue();
        }
    }
}
```

Max tilt sent by product<br/>


* current (float): Current max tilt<br/>
* min (float): Range min of tilt<br/>
* max (float): Range max of tilt<br/>
<br/>

<!-- MiniDrone-PilotingSettingsState-BankedTurnChanged-->
### <a name="MiniDrone-PilotingSettingsState-BankedTurnChanged">Banked Turn mode</a><br/>
> Banked Turn mode:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_BANKEDTURNCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_BANKEDTURNCHANGED_STATE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_BANKEDTURNCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_BANKEDTURNCHANGED_STATE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_BANKEDTURNCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte state = (byte)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_BANKEDTURNCHANGED_STATE)).intValue();
        }
    }
}
```

Banked Turn mode.<br/>
If banked turn mode is enabled, the drone will use yaw values from the piloting command to infer with roll and pitch on the drone when its horizontal speed is not null.<br/>


* state (u8): 1 if enabled, 0 if disabled<br/>


Triggered by [SetBankedTurnMode](#MiniDrone-PilotingSettings-BankedTurn).<br/>



*Supported by <br/>*

- *Mambo since 3.0.6*<br/>


<br/>

<!-- MiniDrone-PilotingSettingsState-MaxThrottleChanged-->
### <a name="MiniDrone-PilotingSettingsState-MaxThrottleChanged">Event informing about the max throttle.</a><br/>
> Event informing about the max throttle.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTHROTTLECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTHROTTLECHANGED_MAX, arg);
            if (arg != NULL)
            {
                float max = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTHROTTLECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTHROTTLECHANGED_MAX, arg);
            if (arg != NULL)
            {
                float max = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTHROTTLECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float max = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_MAXTHROTTLECHANGED_MAX)).doubleValue();
        }
    }
}
```

Event informing about the max throttle.<br/>


* max (float): Max throttle, between 0 and 1.<br/>
<br/>

<!-- MiniDrone-PilotingSettingsState-PreferredPilotingModeChanged-->
### <a name="MiniDrone-PilotingSettingsState-PreferredPilotingModeChanged">Event informing about the preferred piloting mode.</a><br/>
> Event informing about the preferred piloting mode.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_PREFERREDPILOTINGMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_PREFERREDPILOTINGMODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_PILOTINGSETTINGSSTATE_PREFERREDPILOTINGMODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_PREFERREDPILOTINGMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_PREFERREDPILOTINGMODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_PILOTINGSETTINGSSTATE_PREFERREDPILOTINGMODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_PREFERREDPILOTINGMODECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MINIDRONE_PILOTINGSETTINGSSTATE_PREFERREDPILOTINGMODECHANGED_MODE_ENUM mode = ARCOMMANDS_MINIDRONE_PILOTINGSETTINGSSTATE_PREFERREDPILOTINGMODECHANGED_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_PILOTINGSETTINGSSTATE_PREFERREDPILOTINGMODECHANGED_MODE));
        }
    }
}
```

Event informing about the preferred piloting mode.<br/>


* mode (enum): <br/>
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

<!-- MiniDrone-SpeedSettingsState-MaxVerticalSpeedChanged-->
### <a name="MiniDrone-SpeedSettingsState-MaxVerticalSpeedChanged">Max vertical speed sent by product</a><br/>
> Max vertical speed sent by product:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_MAX, arg);
            if (arg != NULL)
            {
                float max = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_MAX, arg);
            if (arg != NULL)
            {
                float max = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float current = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_CURRENT)).doubleValue();
            float min = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_MIN)).doubleValue();
            float max = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_MAX)).doubleValue();
        }
    }
}
```

Max vertical speed sent by product<br/>


* current (float): Current max vertical speed in m/s<br/>
* min (float): Range min of vertical speed<br/>
* max (float): Range max of vertical speed<br/>
<br/>

<!-- MiniDrone-SpeedSettingsState-MaxRotationSpeedChanged-->
### <a name="MiniDrone-SpeedSettingsState-MaxRotationSpeedChanged">Max rotation speed sent by product</a><br/>
> Max rotation speed sent by product:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_MAX, arg);
            if (arg != NULL)
            {
                float max = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_MAX, arg);
            if (arg != NULL)
            {
                float max = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float current = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_CURRENT)).doubleValue();
            float min = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_MIN)).doubleValue();
            float max = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_MAX)).doubleValue();
        }
    }
}
```

Max rotation speed sent by product<br/>


* current (float): Current max rotation speed in degree/s<br/>
* min (float): Range min of rotation speed<br/>
* max (float): Range max of rotation speed<br/>
<br/>

<!-- MiniDrone-SpeedSettingsState-WheelsChanged-->
### <a name="MiniDrone-SpeedSettingsState-WheelsChanged">Presence of wheels sent by product</a><br/>
> Presence of wheels sent by product:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_WHEELSCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_WHEELSCHANGED_PRESENT, arg);
            if (arg != NULL)
            {
                uint8_t present = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_WHEELSCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_WHEELSCHANGED_PRESENT, arg);
            if (arg != NULL)
            {
                uint8_t present = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_WHEELSCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte present = (byte)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_WHEELSCHANGED_PRESENT)).intValue();
        }
    }
}
```

Presence of wheels sent by product<br/>


* present (u8): 1 if present, 0 if not present<br/>
<br/>

<!-- MiniDrone-SpeedSettingsState-MaxHorizontalSpeedChanged-->
### <a name="MiniDrone-SpeedSettingsState-MaxHorizontalSpeedChanged">Max horizontal speed sent by product (only used in case where PilotingSettings_MaxTilt is not used like in hydrofoil mode)</a><br/>
> Max horizontal speed sent by product (only used in case where PilotingSettings_MaxTilt is not used like in hydrofoil mode):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXHORIZONTALSPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXHORIZONTALSPEEDCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXHORIZONTALSPEEDCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXHORIZONTALSPEEDCHANGED_MAX, arg);
            if (arg != NULL)
            {
                float max = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXHORIZONTALSPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXHORIZONTALSPEEDCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXHORIZONTALSPEEDCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXHORIZONTALSPEEDCHANGED_MAX, arg);
            if (arg != NULL)
            {
                float max = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXHORIZONTALSPEEDCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float current = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXHORIZONTALSPEEDCHANGED_CURRENT)).doubleValue();
            float min = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXHORIZONTALSPEEDCHANGED_MIN)).doubleValue();
            float max = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXHORIZONTALSPEEDCHANGED_MAX)).doubleValue();
        }
    }
}
```

Max horizontal speed sent by product (only used in case where PilotingSettings_MaxTilt is not used like in hydrofoil mode)<br/>


* current (float): Current max horizontal speed in m/s<br/>
* min (float): Range min of horizontal speed<br/>
* max (float): Range max of horizontal speed<br/>
<br/>

<!-- MiniDrone-SpeedSettingsState-MaxPlaneModeRotationSpeedChanged-->
### <a name="MiniDrone-SpeedSettingsState-MaxPlaneModeRotationSpeedChanged">Max plane rotation speed sent by product (only available for wing x)</a><br/>
> Max plane rotation speed sent by product (only available for wing x):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXPLANEMODEROTATIONSPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXPLANEMODEROTATIONSPEEDCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXPLANEMODEROTATIONSPEEDCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXPLANEMODEROTATIONSPEEDCHANGED_MAX, arg);
            if (arg != NULL)
            {
                float max = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXPLANEMODEROTATIONSPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXPLANEMODEROTATIONSPEEDCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXPLANEMODEROTATIONSPEEDCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXPLANEMODEROTATIONSPEEDCHANGED_MAX, arg);
            if (arg != NULL)
            {
                float max = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXPLANEMODEROTATIONSPEEDCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float current = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXPLANEMODEROTATIONSPEEDCHANGED_CURRENT)).doubleValue();
            float min = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXPLANEMODEROTATIONSPEEDCHANGED_MIN)).doubleValue();
            float max = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SPEEDSETTINGSSTATE_MAXPLANEMODEROTATIONSPEEDCHANGED_MAX)).doubleValue();
        }
    }
}
```

Max plane rotation speed sent by product (only available for wing x)<br/>


* current (float): Current max plane mode rotation speed in degree/s<br/>
* min (float): Range min of plane mode rotation speed<br/>
* max (float): Range max of plane mode rotation speed<br/>
<br/>

<!-- MiniDrone-SettingsState-ProductMotorsVersionChanged-->
### <a name="MiniDrone-SettingsState-ProductMotorsVersionChanged">@deprecated</a><br/>
> @deprecated:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED_MOTOR, arg);
            if (arg != NULL)
            {
                uint8_t motor = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                char * type = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED_SOFTWARE, arg);
            if (arg != NULL)
            {
                char * software = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED_HARDWARE, arg);
            if (arg != NULL)
            {
                char * hardware = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED_MOTOR, arg);
            if (arg != NULL)
            {
                uint8_t motor = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                char * type = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED_SOFTWARE, arg);
            if (arg != NULL)
            {
                char * software = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED_HARDWARE, arg);
            if (arg != NULL)
            {
                char * hardware = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte motor = (byte)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED_MOTOR)).intValue();
            String type = (String)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED_TYPE);
            String software = (String)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED_SOFTWARE);
            String hardware = (String)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTMOTORSVERSIONCHANGED_HARDWARE);
        }
    }
}
```

@deprecated<br/>
Product Motors versions<br/>


* motor (u8): Product Motor number [1 - 4]<br/>
* type (string): Product Motor type<br/>
* software (string): Product Motors software version<br/>
* hardware (string): Product Motors hardware version<br/>
<br/>

<!-- MiniDrone-SettingsState-ProductInertialVersionChanged-->
### <a name="MiniDrone-SettingsState-ProductInertialVersionChanged">@deprecated</a><br/>
> @deprecated:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTINERTIALVERSIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTINERTIALVERSIONCHANGED_SOFTWARE, arg);
            if (arg != NULL)
            {
                char * software = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTINERTIALVERSIONCHANGED_HARDWARE, arg);
            if (arg != NULL)
            {
                char * hardware = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTINERTIALVERSIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTINERTIALVERSIONCHANGED_SOFTWARE, arg);
            if (arg != NULL)
            {
                char * software = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTINERTIALVERSIONCHANGED_HARDWARE, arg);
            if (arg != NULL)
            {
                char * hardware = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTINERTIALVERSIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            String software = (String)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTINERTIALVERSIONCHANGED_SOFTWARE);
            String hardware = (String)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_PRODUCTINERTIALVERSIONCHANGED_HARDWARE);
        }
    }
}
```

@deprecated<br/>
Product Inertial versions<br/>


* software (string): Product Inertial software version<br/>
* hardware (string): Product Inertial hardware version<br/>
<br/>

<!-- MiniDrone-SettingsState-CutOutModeChanged-->
### <a name="MiniDrone-SettingsState-CutOutModeChanged">MiniDrone cut out mode</a><br/>
> MiniDrone cut out mode:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_CUTOUTMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_CUTOUTMODECHANGED_ENABLE, arg);
            if (arg != NULL)
            {
                uint8_t enable = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_CUTOUTMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_CUTOUTMODECHANGED_ENABLE, arg);
            if (arg != NULL)
            {
                uint8_t enable = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_CUTOUTMODECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte enable = (byte)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_SETTINGSSTATE_CUTOUTMODECHANGED_ENABLE)).intValue();
        }
    }
}
```

MiniDrone cut out mode<br/>


* enable (u8): State of cut out mode (1 if is activate, 0 otherwise)<br/>
<br/>

<!-- MiniDrone-FloodControlState-FloodControlChanged-->
### <a name="MiniDrone-FloodControlState-FloodControlChanged">@deprecated</a><br/>
> @deprecated:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_FLOODCONTROLSTATE_FLOODCONTROLCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_FLOODCONTROLSTATE_FLOODCONTROLCHANGED_DELAY, arg);
            if (arg != NULL)
            {
                uint16_t delay = arg->value.U16;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_FLOODCONTROLSTATE_FLOODCONTROLCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_FLOODCONTROLSTATE_FLOODCONTROLCHANGED_DELAY, arg);
            if (arg != NULL)
            {
                uint16_t delay = arg->value.U16;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_FLOODCONTROLSTATE_FLOODCONTROLCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            short delay = (short)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_FLOODCONTROLSTATE_FLOODCONTROLCHANGED_DELAY)).intValue();
        }
    }
}
```

@deprecated<br/>
Flood control regulation<br/>


* delay (u16): Delay (in ms) between two PCMD<br/>
<br/>

<!-- MiniDrone-UsbAccessoryState-LightState-->
### <a name="MiniDrone-UsbAccessoryState-LightState">USB Light accessory state cmd.</a><br/>
> USB Light accessory state cmd.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE_ID, arg);
                if (arg != NULL)
                {
                    uint8_t id = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE_STATE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE_STATE state = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE_INTENSITY, arg);
                if (arg != NULL)
                {
                    uint8_t intensity = arg->value.U8;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE_ID, arg);
                if (arg != NULL)
                {
                    uint8_t id = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE_STATE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE_STATE state = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE_INTENSITY, arg);
                if (arg != NULL)
                {
                    uint8_t intensity = arg->value.U8;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    byte id = (byte)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE_ID)).intValue();
                    ARCOMMANDS_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE_STATE_ENUM state = ARCOMMANDS_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE_STATE));
                    byte intensity = (byte)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_LIGHTSTATE_INTENSITY)).intValue();
                }
            }
        } else {
            // list is empty
        }
    }
}
```

USB Light accessory state cmd.<br/>


* id (u8): Usb accessory id<br/>
* state (enum): Usb Light state.<br/>
   * FIXED: Fixed state at given intensity.<br/>
   * BLINKED: Blinked state.<br/>
   * OSCILLATED: Oscillated state.<br/>
* intensity (u8): Light intensity from 0 (OFF) to 100 (Max intensity).<br/>
Only used in FIXED state.<br/>
<br/>

<!-- MiniDrone-UsbAccessoryState-ClawState-->
### <a name="MiniDrone-UsbAccessoryState-ClawState">USB Claw accessory state cmd.</a><br/>
> USB Claw accessory state cmd.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_CLAWSTATE)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_CLAWSTATE_ID, arg);
                if (arg != NULL)
                {
                    uint8_t id = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_CLAWSTATE_STATE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MINIDRONE_USBACCESSORYSTATE_CLAWSTATE_STATE state = arg->value.I32;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_CLAWSTATE)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_CLAWSTATE_ID, arg);
                if (arg != NULL)
                {
                    uint8_t id = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_CLAWSTATE_STATE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MINIDRONE_USBACCESSORYSTATE_CLAWSTATE_STATE state = arg->value.I32;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_CLAWSTATE){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    byte id = (byte)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_CLAWSTATE_ID)).intValue();
                    ARCOMMANDS_MINIDRONE_USBACCESSORYSTATE_CLAWSTATE_STATE_ENUM state = ARCOMMANDS_MINIDRONE_USBACCESSORYSTATE_CLAWSTATE_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_CLAWSTATE_STATE));
                }
            }
        } else {
            // list is empty
        }
    }
}
```

USB Claw accessory state cmd.<br/>


* id (u8): Usb accessory id<br/>
* state (enum): Usb Claw state.<br/>
   * OPENED: Claw is fully opened.<br/>
   * OPENING: Claw open in progress.<br/>
   * CLOSED: Claw is fully closed.<br/>
   * CLOSING: Claw close in progress.<br/>
<br/>

<!-- MiniDrone-UsbAccessoryState-GunState-->
### <a name="MiniDrone-UsbAccessoryState-GunState">USB Gun accessory state cmd.</a><br/>
> USB Gun accessory state cmd.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_GUNSTATE)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_GUNSTATE_ID, arg);
                if (arg != NULL)
                {
                    uint8_t id = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_GUNSTATE_STATE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MINIDRONE_USBACCESSORYSTATE_GUNSTATE_STATE state = arg->value.I32;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_GUNSTATE)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_GUNSTATE_ID, arg);
                if (arg != NULL)
                {
                    uint8_t id = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_GUNSTATE_STATE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_MINIDRONE_USBACCESSORYSTATE_GUNSTATE_STATE state = arg->value.I32;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_GUNSTATE){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    byte id = (byte)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_GUNSTATE_ID)).intValue();
                    ARCOMMANDS_MINIDRONE_USBACCESSORYSTATE_GUNSTATE_STATE_ENUM state = ARCOMMANDS_MINIDRONE_USBACCESSORYSTATE_GUNSTATE_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_USBACCESSORYSTATE_GUNSTATE_STATE));
                }
            }
        } else {
            // list is empty
        }
    }
}
```

USB Gun accessory state cmd.<br/>


* id (u8): Usb accessory id.<br/>
* state (enum): USB Claw state.<br/>
   * READY: Gun is ready to fire.<br/>
   * BUSY: Gun is busy (ie not ready to fire).<br/>
<br/>

<!-- MiniDrone-NavigationDataState-DronePosition-->
### <a name="MiniDrone-NavigationDataState-DronePosition">Get the drone position from takeoff point (0, 0, 0, 0).</a><br/>
> Get the drone position from takeoff point (0, 0, 0, 0).:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_POSX, arg);
            if (arg != NULL)
            {
                float posx = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_POSY, arg);
            if (arg != NULL)
            {
                float posy = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_POSZ, arg);
            if (arg != NULL)
            {
                int16_t posz = arg->value.I16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_PSI, arg);
            if (arg != NULL)
            {
                int16_t psi = arg->value.I16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_TS, arg);
            if (arg != NULL)
            {
                int16_t ts = arg->value.I16;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_POSX, arg);
            if (arg != NULL)
            {
                float posx = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_POSY, arg);
            if (arg != NULL)
            {
                float posy = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_POSZ, arg);
            if (arg != NULL)
            {
                int16_t posz = arg->value.I16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_PSI, arg);
            if (arg != NULL)
            {
                int16_t psi = arg->value.I16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_TS, arg);
            if (arg != NULL)
            {
                int16_t ts = arg->value.I16;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float posx = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_POSX)).doubleValue();
            float posy = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_POSY)).doubleValue();
            short posz = (short)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_POSZ)).intValue();
            short psi = (short)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_PSI)).intValue();
            short ts = (short)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEPOSITION_TS)).intValue();
        }
    }
}
```

Get the drone position from takeoff point (0, 0, 0, 0).<br/>
The orthonormal basis is fixed at this point. The axis are<br/>
oriented the following way :<br/>
* X : From the rear of the drone to its front.<br/>
* Y : From the right of the drone to its left.<br/>
* Z : Orthogonal to X and Y and oriented upward.<br/>
* Psi : From 180 to -180 in the clockwise direction,<br/>


* posx (float): Position on X axis, relative to take off position (cm).<br/>
* posy (float): Position on Y axis, relative to take off position (cm).<br/>
* posz (i16): Position on Z axis, relative to take off position (cm).<br/>
* psi (i16): Psi angle [-180; 180], relative to take off orientation.<br/>
* ts (i16): Time elapsed since last data send (ms).<br/>
<br/>

<!-- MiniDrone-NavigationDataState-DroneSpeed-->
### <a name="MiniDrone-NavigationDataState-DroneSpeed">Event informing about the estimated drone speed in horizontal frame.</a><br/>
> Event informing about the estimated drone speed in horizontal frame.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED_SPEED_X, arg);
            if (arg != NULL)
            {
                float speed_x = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED_SPEED_Y, arg);
            if (arg != NULL)
            {
                float speed_y = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED_SPEED_Z, arg);
            if (arg != NULL)
            {
                float speed_z = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED_TS, arg);
            if (arg != NULL)
            {
                uint16_t ts = arg->value.U16;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED_SPEED_X, arg);
            if (arg != NULL)
            {
                float speed_x = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED_SPEED_Y, arg);
            if (arg != NULL)
            {
                float speed_y = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED_SPEED_Z, arg);
            if (arg != NULL)
            {
                float speed_z = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED_TS, arg);
            if (arg != NULL)
            {
                uint16_t ts = arg->value.U16;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float speed_x = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED_SPEED_X)).doubleValue();
            float speed_y = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED_SPEED_Y)).doubleValue();
            float speed_z = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED_SPEED_Z)).doubleValue();
            short ts = (short)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONESPEED_TS)).intValue();
        }
    }
}
```

Event informing about the estimated drone speed in horizontal frame.<br/>
It is similar to NED frame but with drone heading.<br/>
Down speed is positive when the drone is going down.<br/>
Speed is in m/s.<br/>


* speed_x (float): Speed on the x axis (when drone moves forward, speed is > 0).<br/>
* speed_y (float): Speed on the y axis (when drone moves right, speed is > 0).<br/>
* speed_z (float): Speed on the z axis (when drone moves down, speed is > 0).<br/>
* ts (u16): Acquisition timestamp (ms).<br/>
<br/>

<!-- MiniDrone-NavigationDataState-DroneAltitude-->
### <a name="MiniDrone-NavigationDataState-DroneAltitude">Event informing about the estimated altitude above takeoff level.</a><br/>
> Event informing about the estimated altitude above takeoff level.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEALTITUDE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEALTITUDE_ALTITUDE, arg);
            if (arg != NULL)
            {
                float altitude = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEALTITUDE_TS, arg);
            if (arg != NULL)
            {
                uint16_t ts = arg->value.U16;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEALTITUDE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEALTITUDE_ALTITUDE, arg);
            if (arg != NULL)
            {
                float altitude = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEALTITUDE_TS, arg);
            if (arg != NULL)
            {
                uint16_t ts = arg->value.U16;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEALTITUDE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float altitude = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEALTITUDE_ALTITUDE)).doubleValue();
            short ts = (short)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEALTITUDE_TS)).intValue();
        }
    }
}
```

Event informing about the estimated altitude above takeoff level.<br/>


* altitude (float): Altitude in meters.<br/>
* ts (u16): Acquisition timestamp (ms).<br/>
<br/>

<!-- MiniDrone-NavigationDataState-DroneQuaternion-->
### <a name="MiniDrone-NavigationDataState-DroneQuaternion">Event informing about the estimated quaternion.</a><br/>
> Event informing about the estimated quaternion.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_Q_W, arg);
            if (arg != NULL)
            {
                float q_w = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_Q_X, arg);
            if (arg != NULL)
            {
                float q_x = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_Q_Y, arg);
            if (arg != NULL)
            {
                float q_y = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_Q_Z, arg);
            if (arg != NULL)
            {
                float q_z = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_TS, arg);
            if (arg != NULL)
            {
                uint16_t ts = arg->value.U16;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_Q_W, arg);
            if (arg != NULL)
            {
                float q_w = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_Q_X, arg);
            if (arg != NULL)
            {
                float q_x = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_Q_Y, arg);
            if (arg != NULL)
            {
                float q_y = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_Q_Z, arg);
            if (arg != NULL)
            {
                float q_z = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_TS, arg);
            if (arg != NULL)
            {
                uint16_t ts = arg->value.U16;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float q_w = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_Q_W)).doubleValue();
            float q_x = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_Q_X)).doubleValue();
            float q_y = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_Q_Y)).doubleValue();
            float q_z = (float)((Double)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_Q_Z)).doubleValue();
            short ts = (short)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_NAVIGATIONDATASTATE_DRONEQUATERNION_TS)).intValue();
        }
    }
}
```

Event informing about the estimated quaternion.<br/>
They represent the rotation from the NED frame (determined at drone startup) to the estimated drone body frame.<br/>
Its elements are between -1 and 1.<br/>


* q_w (float): Element w.<br/>
* q_x (float): Element x.<br/>
* q_y (float): Element y.<br/>
* q_z (float): Element z.<br/>
* ts (u16): Acquisition timestamp (ms).<br/>
<br/>

<!-- MiniDrone-MinicamState-PowerModeChanged-->
### <a name="MiniDrone-MinicamState-PowerModeChanged">Event informing about the minicam power mode.</a><br/>
> Event informing about the minicam power mode.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_POWERMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_POWERMODECHANGED_POWER_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MINICAMSTATE_POWERMODECHANGED_POWER_MODE power_mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_POWERMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_POWERMODECHANGED_POWER_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MINICAMSTATE_POWERMODECHANGED_POWER_MODE power_mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_POWERMODECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MINIDRONE_MINICAMSTATE_POWERMODECHANGED_POWER_MODE_ENUM power_mode = ARCOMMANDS_MINIDRONE_MINICAMSTATE_POWERMODECHANGED_POWER_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_POWERMODECHANGED_POWER_MODE));
        }
    }
}
```

Event informing about the minicam power mode.<br/>


* power_mode (enum): Power mode of the camera.<br/>
   * low: Low power: most hardware is powered off, wake up via USB resume.<br/>
<br/>
Used when charging.<br/>
   * medium: Medium power: video hardware is powered off.<br/>
<br/>
Used when drone is not flying during more than 3 minutes.<br/>
Note that it can still stream the SD content.<br/>
   * normal: Normal power: all features are available.<br/>
<br/>
Used when flying.<br/>
<br/>

<!-- MiniDrone-MinicamState-ProductSerialChanged-->
### <a name="MiniDrone-MinicamState-ProductSerialChanged">Event informing about the minicam product serial number.</a><br/>
> Event informing about the minicam product serial number.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PRODUCTSERIALCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PRODUCTSERIALCHANGED_SERIAL_NUMBER, arg);
            if (arg != NULL)
            {
                char * serial_number = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PRODUCTSERIALCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PRODUCTSERIALCHANGED_SERIAL_NUMBER, arg);
            if (arg != NULL)
            {
                char * serial_number = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PRODUCTSERIALCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            String serial_number = (String)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PRODUCTSERIALCHANGED_SERIAL_NUMBER);
        }
    }
}
```

Event informing about the minicam product serial number.<br/>


* serial_number (string): Serial number.<br/>
<br/>

<!-- MiniDrone-MinicamState-StateChanged-->
### <a name="MiniDrone-MinicamState-StateChanged">Event informing about the state of the camera.</a><br/>
> Event informing about the state of the camera.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_STATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_STATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MINICAMSTATE_STATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_STATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_STATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MINICAMSTATE_STATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_STATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MINIDRONE_MINICAMSTATE_STATECHANGED_STATE_ENUM state = ARCOMMANDS_MINIDRONE_MINICAMSTATE_STATECHANGED_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_STATECHANGED_STATE));
        }
    }
}
```

Event informing about the state of the camera.<br/>


* state (enum): State of the camera.<br/>
   * unplugged: Minicam is unplugged.<br/>
   * plugged: Minicam is plugged, but not ready.<br/>
   * ready: Minicam is ready.<br/>
<br/>

<!-- MiniDrone-MinicamState-VersionChanged-->
### <a name="MiniDrone-MinicamState-VersionChanged">Get the accessory Version.</a><br/>
> Get the accessory Version.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VERSIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VERSIONCHANGED_SOFTWARE, arg);
            if (arg != NULL)
            {
                char * software = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VERSIONCHANGED_HARDWARE, arg);
            if (arg != NULL)
            {
                char * hardware = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VERSIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VERSIONCHANGED_SOFTWARE, arg);
            if (arg != NULL)
            {
                char * software = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VERSIONCHANGED_HARDWARE, arg);
            if (arg != NULL)
            {
                char * hardware = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VERSIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            String software = (String)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VERSIONCHANGED_SOFTWARE);
            String hardware = (String)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VERSIONCHANGED_HARDWARE);
        }
    }
}
```

Get the accessory Version.<br/>


* software (string): Accessory software version.<br/>
* hardware (string): Accessory hardware version.<br/>
<br/>

<!-- MiniDrone-MinicamState-PictureChanged-->
### <a name="MiniDrone-MinicamState-PictureChanged">Event informing that the picture has been taken.</a><br/>
> Event informing that the picture has been taken.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PICTURECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PICTURECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MINICAMSTATE_PICTURECHANGED_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PICTURECHANGED_RESULT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MINICAMSTATE_PICTURECHANGED_RESULT result = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PICTURECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PICTURECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MINICAMSTATE_PICTURECHANGED_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PICTURECHANGED_RESULT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MINICAMSTATE_PICTURECHANGED_RESULT result = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PICTURECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MINIDRONE_MINICAMSTATE_PICTURECHANGED_STATE_ENUM state = ARCOMMANDS_MINIDRONE_MINICAMSTATE_PICTURECHANGED_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PICTURECHANGED_STATE));
            ARCOMMANDS_MINIDRONE_MINICAMSTATE_PICTURECHANGED_RESULT_ENUM result = ARCOMMANDS_MINIDRONE_MINICAMSTATE_PICTURECHANGED_RESULT_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_PICTURECHANGED_RESULT));
        }
    }
}
```

Event informing that the picture has been taken.<br/>


* state (enum): State of device picture recording.<br/>
   * ready: Picture recording is ready.<br/>
   * busy: Picture recording is busy.<br/>
   * not_available: Picture recording is not available.<br/>
* result (enum): Result of device picture recording.<br/>
   * success: Success.<br/>
   * full_device: Device is full.<br/>
   * continuous_shooting: Continuous shooting is already running.<br/>
   * full_queue: Over snapshot max queue size.<br/>
   * error: Couldn't take picture.<br/>
   * no_sd: SD card doesn't exist.<br/>
   * sd_bad_format: SD card format error.<br/>
   * sd_formatting: SD card is formatting.<br/>
<br/>

<!-- MiniDrone-MinicamState-VideoStateChanged-->
### <a name="MiniDrone-MinicamState-VideoStateChanged">Event informing about the video recording state.</a><br/>
> Event informing about the video recording state.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED_STATE_ENUM state = ARCOMMANDS_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED_STATE));
            ARCOMMANDS_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED_ERROR_ENUM error = ARCOMMANDS_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED_ERROR_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_VIDEOSTATECHANGED_ERROR));
        }
    }
}
```

Event informing about the video recording state.<br/>


* state (enum): State of device video recording.<br/>
   * stopped: Video is stopped.<br/>
   * started: Video is started.<br/>
   * notAvailable: The video recording is not available.<br/>
* error (enum): Error to explain the state.<br/>
   * ok: No Error.<br/>
   * unknown: Unknown generic error.<br/>
   * camera_ko: Video camera is out of order.<br/>
   * memoryFull: Memory full ; cannot save one additional video.<br/>
   * lowBattery: Battery is too low to start/keep recording.<br/>
   * no_sd: SD card doesn't exist.<br/>
<br/>

<!-- MiniDrone-MinicamState-MassStorageFormatChanged-->
### <a name="MiniDrone-MinicamState-MassStorageFormatChanged">Event informing that the mass storage has been formatted.</a><br/>
> Event informing that the mass storage has been formatted.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_MASSSTORAGEFORMATCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_MASSSTORAGEFORMATCHANGED_STATE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_MASSSTORAGEFORMATCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_MASSSTORAGEFORMATCHANGED_STATE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_MASSSTORAGEFORMATCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte state = (byte)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_MINICAMSTATE_MASSSTORAGEFORMATCHANGED_STATE)).intValue();
        }
    }
}
```

Event informing that the mass storage has been formatted.<br/>


* state (u8): 1 if Mass Storage has been formatted, 0 otherwise.<br/>
<br/>

<!-- MiniDrone-VideoSettingsState-AutorecordChanged-->
### <a name="MiniDrone-VideoSettingsState-AutorecordChanged">Event informing about the video automatic recording status.</a><br/>
> Event informing about the video automatic recording status.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_AUTORECORDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_AUTORECORDCHANGED_ENABLED, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_AUTORECORDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_AUTORECORDCHANGED_ENABLED, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_AUTORECORDCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte enabled = (byte)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_AUTORECORDCHANGED_ENABLED)).intValue();
        }
    }
}
```

Event informing about the video automatic recording status.<br/>


* enabled (u8): 0: disabled<br/>
1: enabled<br/>
<br/>

<!-- MiniDrone-VideoSettingsState-ElectricFrequencyChanged-->
### <a name="MiniDrone-VideoSettingsState-ElectricFrequencyChanged">Event informing about the electric frequency (Anti-flickering).</a><br/>
> Event informing about the electric frequency (Anti-flickering).:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_ELECTRICFREQUENCYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_ELECTRICFREQUENCYCHANGED_FREQUENCY, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_VIDEOSETTINGSSTATE_ELECTRICFREQUENCYCHANGED_FREQUENCY frequency = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_ELECTRICFREQUENCYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_ELECTRICFREQUENCYCHANGED_FREQUENCY, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_VIDEOSETTINGSSTATE_ELECTRICFREQUENCYCHANGED_FREQUENCY frequency = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_ELECTRICFREQUENCYCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MINIDRONE_VIDEOSETTINGSSTATE_ELECTRICFREQUENCYCHANGED_FREQUENCY_ENUM frequency = ARCOMMANDS_MINIDRONE_VIDEOSETTINGSSTATE_ELECTRICFREQUENCYCHANGED_FREQUENCY_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_ELECTRICFREQUENCYCHANGED_FREQUENCY));
        }
    }
}
```

Event informing about the electric frequency (Anti-flickering).<br/>


* frequency (enum): Type of the electric frequency.<br/>
   * fifty_hertz: Electric frequency of the country is 50hz.<br/>
   * sixty_hertz: Electric frequency of the country is 60hz.<br/>
<br/>

<!-- MiniDrone-VideoSettingsState-VideoResolutionChanged-->
### <a name="MiniDrone-VideoSettingsState-VideoResolutionChanged">Event informing about the streaming resolution.</a><br/>
> Event informing about the streaming resolution.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_VIDEORESOLUTIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_VIDEORESOLUTIONCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_VIDEOSETTINGSSTATE_VIDEORESOLUTIONCHANGED_TYPE type = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_VIDEORESOLUTIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_VIDEORESOLUTIONCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_MINIDRONE_VIDEOSETTINGSSTATE_VIDEORESOLUTIONCHANGED_TYPE type = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_VIDEORESOLUTIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_MINIDRONE_VIDEOSETTINGSSTATE_VIDEORESOLUTIONCHANGED_TYPE_ENUM type = ARCOMMANDS_MINIDRONE_VIDEOSETTINGSSTATE_VIDEORESOLUTIONCHANGED_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_VIDEOSETTINGSSTATE_VIDEORESOLUTIONCHANGED_TYPE));
        }
    }
}
```

Event informing about the streaming resolution.<br/>


* type (enum): Video resolution type.<br/>
   * vga: 16/9 VGA streaming (640 x 360).<br/>
   * hd: HD streaming (1280 x 720).<br/>
<br/>

<!-- MiniDrone-RemoteControllerState-ConnectionChanged-->
### <a name="MiniDrone-RemoteControllerState-ConnectionChanged">State of the connection to the remote controller changed.</a><br/>
> State of the connection to the remote controller changed.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_REMOTECONTROLLERSTATE_CONNECTIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_REMOTECONTROLLERSTATE_CONNECTIONCHANGED_STATE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_REMOTECONTROLLERSTATE_CONNECTIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_REMOTECONTROLLERSTATE_CONNECTIONCHANGED_STATE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_REMOTECONTROLLERSTATE_CONNECTIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte state = (byte)((Integer)args.get(ARFeatureMiniDrone.ARCONTROLLER_DICTIONARY_KEY_MINIDRONE_REMOTECONTROLLERSTATE_CONNECTIONCHANGED_STATE)).intValue();
        }
    }
}
```

State of the connection to the remote controller changed.<br/>


* state (u8): New connection state.<br/>
0=disconnected<br/>
1=connected<br/>
<br/>

