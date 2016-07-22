<!-- ARDrone3-MediaRecordState-PictureStateChanged-->
### <a name="ARDrone3-MediaRecordState-PictureStateChanged">Picture record state V1</a><br/>
> Picture state V1 (deprecated):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                uint8_t state = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGED_MASS_STORAGE_ID, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                uint8_t state = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGED_MASS_STORAGE_ID, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte state = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGED_STATE)).intValue();
            byte mass_storage_id = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGED_MASS_STORAGE_ID)).intValue();
        }
    }
}
```

This event is deprecated.

<br/>

<!-- ARDrone3-MediaRecordState-VideoStateChanged-->
### <a name="ARDrone3-MediaRecordState-VideoStateChanged">Video record state v1</a><br/>
> Video record state v1 (deprecated):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGED_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGED_MASS_STORAGE_ID, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGED_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGED_MASS_STORAGE_ID, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGED_STATE_ENUM state = ARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGED_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGED_STATE));
            byte mass_storage_id = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGED_MASS_STORAGE_ID)).intValue();
        }
    }
}
```

This event is deprecated.
<br/>

<!-- ARDrone3-MediaRecordState-PictureStateChangedV2-->
### <a name="ARDrone3-MediaRecordState-PictureStateChangedV2">Picture record state</a><br/>
> Picture record state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE_ENUM state = ARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_STATE));
            ARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR_ENUM error = ARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_PICTURESTATECHANGEDV2_ERROR));
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

Triggered by [TakePicture](#ARDrone3-MediaRecord-PictureV2) or by a change in the picture state.

*Supported by <br/>*   

- *Bebop since 2.0.1<br/>*
- *Bebop 2<br/>* 

<br/>

<!-- ARDrone3-MediaRecordState-VideoStateChangedV2-->
### <a name="ARDrone3-MediaRecordState-VideoStateChangedV2">Video record state</a><br/>
> Video record state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_STATE_ENUM state = ARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_STATE));
            ARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_ERROR_ENUM error = ARCOMMANDS_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_ERROR_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDSTATE_VIDEOSTATECHANGEDV2_ERROR));
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

Triggered by [VideoRecord](#ARDrone3-MediaRecord-VideoV2) or by a change in the video state.

*Supported by <br/>*   

- *Bebop since 2.0.1<br/>*
- *Bebop 2<br/>* 

<br/>

<!-- ARDrone3-MediaRecordEvent-PictureEventChanged-->
### <a name="ARDrone3-MediaRecordEvent-PictureEventChanged">Event of picture recording</a><br/>
> Event of picture recording:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT event = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT event = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT_ENUM event = ARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED_EVENT));
            ARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR_ENUM error = ARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_PICTUREEVENTCHANGED_ERROR));
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

Triggered by [TakePicture](#ARDrone3-MediaRecord-PictureV2).

**This event is a notification, you can't retrieve it in the cache of the device controller.**

*Supported by <br/>*   

- *Bebop since 2.0.1<br/>*
- *Bebop 2<br/>* 

<br/>

<!-- ARDrone3-MediaRecordEvent-VideoEventChanged-->
### <a name="ARDrone3-MediaRecordEvent-VideoEventChanged">Event of video recording</a><br/>
> Event of video recording:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED_EVENT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED_EVENT event = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED_EVENT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED_EVENT event = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED_EVENT_ENUM event = ARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED_EVENT_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED_EVENT));
            ARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED_ERROR_ENUM error = ARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED_ERROR_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIARECORDEVENT_VIDEOEVENTCHANGED_ERROR));
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

Triggered by [VideoRecord](#ARDrone3-MediaRecord-VideoV2) or by a change in the video state.

**This event is a notification, you can't retrieve it in the cache of the device controller.**

*Supported by <br/>*   

- *Bebop since 2.0.1<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingState-FlatTrimChanged-->
### <a name="ARDrone3-PilotingState-FlatTrimChanged">Drone acknowledges that flat trim was correctly processed</a><br/>
> Drone acknowledges that flat trim was correctly processed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLATTRIMCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLATTRIMCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLATTRIMCHANGED) && (elementDictionary != null)){

    }
}
```

Drone acknowledges that flat trim was correctly processed<br/>

Triggered by [FlatTrim](#ARDrone3-Piloting-FlatTrim).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingState-FlyingStateChanged-->
### <a name="ARDrone3-PilotingState-FlyingStateChanged">Drone flying state changed</a><br/>
> Drone flying state changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM state = ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE));
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
   
Triggered when the flying state changes.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*
<br/>

<!-- ARDrone3-PilotingState-AlertStateChanged-->
### <a name="ARDrone3-PilotingState-AlertStateChanged">Drone alert state changed</a><br/>
> Drone alert state changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ALERTSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ALERTSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PILOTINGSTATE_ALERTSTATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ALERTSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ALERTSTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PILOTINGSTATE_ALERTSTATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ALERTSTATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_PILOTINGSTATE_ALERTSTATECHANGED_STATE_ENUM state = ARCOMMANDS_ARDRONE3_PILOTINGSTATE_ALERTSTATECHANGED_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ALERTSTATECHANGED_STATE));
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
   * too_much_angle: The angle of the drone is too high<br/>

Triggered when an alert happens on the drone.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingState-NavigateHomeStateChanged-->
### <a name="ARDrone3-PilotingState-NavigateHomeStateChanged">Navigating home state</a><br/>
> Navigating home state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED_REASON, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED_REASON reason = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED_REASON, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED_REASON reason = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED_STATE_ENUM state = ARCOMMANDS_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED_STATE));
            ARCOMMANDS_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED_REASON_ENUM reason = ARCOMMANDS_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED_REASON_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_NAVIGATEHOMESTATECHANGED_REASON));
        }
    }
}
```

Navigating home state<br/>

* state (enum): State of navigate home<br/>
   * available: Navigate home is available<br/>
   * inProgress: Navigate home is in progress<br/>
   * unavailable: Navigate home is not available<br/>
   * pending: Navigate home has been received, but its process is pending<br/>
* reason (enum): Reason of the state<br/>
   * userRequest: User requested a navigate home (available->inProgress)<br/>
   * connectionLost: Connection between controller and product lost (available->inProgress)<br/>
   * lowBattery: Low battery occurred (available->inProgress)<br/>
   * finished: Navigate home is finished (inProgress->available)<br/>
   * stopped: Navigate home has been stopped (inProgress->available)<br/>
   * disabled: Navigate home disabled by product (inProgress->unavailable or available->unavailable)<br/>
   * enabled: Navigate home enabled by product (unavailable->available)<br/>

To be available, the gps should be fixed, magnetometer should be calibrated.

Triggered by [NavigateHome](#ARDrone3-Piloting-NavigateHome) or when the state of the return home changes.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingState-PositionChanged-->
### <a name="ARDrone3-PilotingState-PositionChanged">Drone position changed</a><br/>
> Drone position changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_POSITIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_POSITIONCHANGED_LATITUDE, arg);
            if (arg != NULL)
            {
                double latitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_POSITIONCHANGED_LONGITUDE, arg);
            if (arg != NULL)
            {
                double longitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_POSITIONCHANGED_ALTITUDE, arg);
            if (arg != NULL)
            {
                double altitude = arg->value.Double;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_POSITIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_POSITIONCHANGED_LATITUDE, arg);
            if (arg != NULL)
            {
                double latitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_POSITIONCHANGED_LONGITUDE, arg);
            if (arg != NULL)
            {
                double longitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_POSITIONCHANGED_ALTITUDE, arg);
            if (arg != NULL)
            {
                double altitude = arg->value.Double;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_POSITIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            double latitude = (double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_POSITIONCHANGED_LATITUDE);
            double longitude = (double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_POSITIONCHANGED_LONGITUDE);
            double altitude = (double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_POSITIONCHANGED_ALTITUDE);
        }
    }
}
```

Drone position changed<br/>

* latitude (double): Latitude position in decimal degrees (500.0 if not available)<br/>
* longitude (double): Longitude position in decimal degrees (500.0 if not available)<br/>
* altitude (double): Altitude in meters (from GPS)<br/>

Triggered regularly when the drone flies (if its gps has fixed).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingState-SpeedChanged-->
### <a name="ARDrone3-PilotingState-SpeedChanged">Drone speed changed</a><br/>
> Drone speed changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_SPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_SPEEDCHANGED_SPEEDX, arg);
            if (arg != NULL)
            {
                float speedX = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_SPEEDCHANGED_SPEEDY, arg);
            if (arg != NULL)
            {
                float speedY = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_SPEEDCHANGED_SPEEDZ, arg);
            if (arg != NULL)
            {
                float speedZ = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_SPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_SPEEDCHANGED_SPEEDX, arg);
            if (arg != NULL)
            {
                float speedX = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_SPEEDCHANGED_SPEEDY, arg);
            if (arg != NULL)
            {
                float speedY = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_SPEEDCHANGED_SPEEDZ, arg);
            if (arg != NULL)
            {
                float speedZ = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_SPEEDCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float speedX = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_SPEEDCHANGED_SPEEDX)).doubleValue();
            float speedY = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_SPEEDCHANGED_SPEEDY)).doubleValue();
            float speedZ = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_SPEEDCHANGED_SPEEDZ)).doubleValue();
        }
    }
}
```

Drone speed changed in the North East Down coordinates.<br/>

* speedX (float): Speed on the x axis (when drone moves forward, speed is > 0) (in m/s)<br/>
* speedY (float): Speed on the y axis (when drone moves to right, speed is > 0) (in m/s)<br/>
* speedZ (float): Speed on the z axis (when drone moves down, speed is > 0) (in m/s)<br/>

Triggered regularly when the drone flies.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingState-AttitudeChanged-->
### <a name="ARDrone3-PilotingState-AttitudeChanged">Drone attitude changed</a><br/>
> Drone attitude changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ATTITUDECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ATTITUDECHANGED_ROLL, arg);
            if (arg != NULL)
            {
                float roll = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ATTITUDECHANGED_PITCH, arg);
            if (arg != NULL)
            {
                float pitch = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ATTITUDECHANGED_YAW, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ATTITUDECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ATTITUDECHANGED_ROLL, arg);
            if (arg != NULL)
            {
                float roll = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ATTITUDECHANGED_PITCH, arg);
            if (arg != NULL)
            {
                float pitch = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ATTITUDECHANGED_YAW, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ATTITUDECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float roll = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ATTITUDECHANGED_ROLL)).doubleValue();
            float pitch = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ATTITUDECHANGED_PITCH)).doubleValue();
            float yaw = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ATTITUDECHANGED_YAW)).doubleValue();
        }
    }
}
```

Drone attitude changed<br/>

* roll (float): roll value (in radian)<br/>
* pitch (float): Pitch value (in radian)<br/>
* yaw (float): Yaw value (in radian)<br/>

Triggered regularly when the drone flies.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingState-AutoTakeOffModeChanged-->
### <a name="ARDrone3-PilotingState-AutoTakeOffModeChanged">Status automatic take off mode</a><br/>
> Status of the drone3 automatic take off mode (deprecated):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_AUTOTAKEOFFMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_AUTOTAKEOFFMODECHANGED_STATE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_AUTOTAKEOFFMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_AUTOTAKEOFFMODECHANGED_STATE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_AUTOTAKEOFFMODECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte state = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_AUTOTAKEOFFMODECHANGED_STATE)).intValue();
        }
    }
}
```

This event is deprecated.
<br/>

<!-- ARDrone3-PilotingState-AltitudeChanged-->
### <a name="ARDrone3-PilotingState-AltitudeChanged">Drone altitude changed</a><br/>
> Drone altitude changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ALTITUDECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ALTITUDECHANGED_ALTITUDE, arg);
            if (arg != NULL)
            {
                double altitude = arg->value.Double;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ALTITUDECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ALTITUDECHANGED_ALTITUDE, arg);
            if (arg != NULL)
            {
                double altitude = arg->value.Double;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ALTITUDECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            double altitude = (double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSTATE_ALTITUDECHANGED_ALTITUDE);
        }
    }
}
```

Drone altitude changed<br/>

* altitude (double): Altitude in meters<br/>

Triggered regularly when the drone flies.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingEvent-moveByEnd-->
### <a name="ARDrone3-PilotingEvent-moveByEnd">End of relative displacement of the drone</a><br/>
> End of relative displacement of the drone (not implemented):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_DX, arg);
            if (arg != NULL)
            {
                float dX = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_DY, arg);
            if (arg != NULL)
            {
                float dY = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_DZ, arg);
            if (arg != NULL)
            {
                float dZ = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_DPSI, arg);
            if (arg != NULL)
            {
                float dPsi = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PILOTINGEVENT_MOVEBYEND_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_DX, arg);
            if (arg != NULL)
            {
                float dX = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_DY, arg);
            if (arg != NULL)
            {
                float dY = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_DZ, arg);
            if (arg != NULL)
            {
                float dZ = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_DPSI, arg);
            if (arg != NULL)
            {
                float dPsi = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_ERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PILOTINGEVENT_MOVEBYEND_ERROR error = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float dX = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_DX)).doubleValue();
            float dY = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_DY)).doubleValue();
            float dZ = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_DZ)).doubleValue();
            float dPsi = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_DPSI)).doubleValue();
            ARCOMMANDS_ARDRONE3_PILOTINGEVENT_MOVEBYEND_ERROR_ENUM error = ARCOMMANDS_ARDRONE3_PILOTINGEVENT_MOVEBYEND_ERROR_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGEVENT_MOVEBYEND_ERROR));
        }
    }
}
```

End of relative displacement of the drone<br/>

**Draft: this event is not implemented yet by the firmware**<br/>

The frame is horizontal and relative to the current drone orientation:<br/>

- X is front<br/>

- Y is right<br/>

- Z is down<br/>

* dX (float): Distance traveled along the front axis [m]<br/>
* dY (float): Distance traveled along the right axis [m]<br/>
* dZ (float): Distance traveled along the down axis [m]<br/>
* dPsi (float): Applied angle on heading  [rad]<br/>
* error (enum): Error to explain the event<br/>
   * ok: No Error ; The relative displacement<br/>
   * unknown: Unknown generic error<br/>
   * busy: The Device is busy ; command moveBy ignored<br/>
   * notAvailable: Command moveBy is not available ; command moveBy ignored<br/>
   * interrupted: Command moveBy interrupted<br/>

Triggered by the end of a [MoveBy](#ARDrone3-Piloting-moveBy) (error should be *ok*) or by a new command [MoveBy](#ARDrone3-Piloting-moveBy) (error should be *interrupted*). 

**This event is a notification, you can't retrieve it in the cache of the device controller.**

*Supported by no products<br/>*    

<br/>

<!-- ARDrone3-NetworkState-WifiScanListChanged-->
### <a name="ARDrone3-NetworkState-WifiScanListChanged">Wifi scan results</a><br/>
> Wifi scan results:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_SSID, arg);
            if (arg != NULL)
            {
                char * ssid = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_RSSI, arg);
            if (arg != NULL)
            {
                int16_t rssi = arg->value.I16;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_BAND, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_BAND band = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_CHANNEL, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_SSID, arg);
            if (arg != NULL)
            {
                char * ssid = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_RSSI, arg);
            if (arg != NULL)
            {
                int16_t rssi = arg->value.I16;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_BAND, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_BAND band = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_CHANNEL, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED) && (elementDictionary != null)){
        Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
        while (itr.hasNext()) {
            ARControllerArgumentDictionary<Object> args = itr.next();
            if (args != null) {
                String ssid = (String)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_SSID);
                short rssi = (short)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_RSSI)).intValue();
                ARCOMMANDS_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_BAND_ENUM band = ARCOMMANDS_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_BAND_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_BAND));
                byte channel = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFISCANLISTCHANGED_CHANNEL)).intValue();
            }
        }
    }
}
```

Wifi scan results.<br/>

* ssid (string): SSID of the AP<br/>
* rssi (i16): RSSI of the AP in dbm (negative value)<br/>
* band (enum): The band : 2.4 GHz or 5 GHz<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
* channel (u8): Channel of the AP<br/>

Triggered for each wifi scanned after a [WifiScan](#ARDrone3-Network-WifiScan).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-NetworkState-AllWifiScanChanged-->
### <a name="ARDrone3-NetworkState-AllWifiScanChanged">State sent when all scanning result sent</a><br/>
> State sent when all scanning result sent:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_ALLWIFISCANCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_ALLWIFISCANCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_ALLWIFISCANCHANGED) && (elementDictionary != null)){

    }
}
```

State sent when all scanning result sent<br/>

Triggered after the last [WifiScanResult](#ARDrone3-NetworkState-WifiScanListChanged) has been sent.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-NetworkState-WifiAuthChannelListChanged-->
### <a name="ARDrone3-NetworkState-WifiAuthChannelListChanged">Authorized channel results</a><br/>
> Authorized channel results:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_BAND, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_BAND band = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_CHANNEL, arg);
            if (arg != NULL)
            {
                uint8_t channel = arg->value.U8;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_IN_OR_OUT, arg);
            if (arg != NULL)
            {
                uint8_t in_or_out = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_BAND, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_BAND band = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_CHANNEL, arg);
            if (arg != NULL)
            {
                uint8_t channel = arg->value.U8;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_IN_OR_OUT, arg);
            if (arg != NULL)
            {
                uint8_t in_or_out = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED) && (elementDictionary != null)){
        Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
        while (itr.hasNext()) {
            ARControllerArgumentDictionary<Object> args = itr.next();
            if (args != null) {
                ARCOMMANDS_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_BAND_ENUM band = ARCOMMANDS_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_BAND_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_BAND));
                byte channel = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_CHANNEL)).intValue();
                byte in_or_out = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_WIFIAUTHCHANNELLISTCHANGED_IN_OR_OUT)).intValue();
            }
        }
    }
}
```

Authorized channel results.<br/>

* band (enum): The band of this channel : 2.4 GHz or 5 GHz<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
* channel (u8): The authorized channel.<br/>
* in_or_out (u8): Bit 0 is 1 if channel is authorized outside (0 otherwise) ; Bit 1 is 1 if channel is authorized inside (0 otherwise)<br/>

Triggered for each channels found after a [GetAvailableChannels](#ARDrone3-Network-WifiAuthChannel).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-NetworkState-AllWifiAuthChannelChanged-->
### <a name="ARDrone3-NetworkState-AllWifiAuthChannelChanged">Notify the end of the list of Authorized wifi Channel.</a><br/>
> Notify the end of the list of Authorized wifi Channel.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_ALLWIFIAUTHCHANNELCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_ALLWIFIAUTHCHANNELCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSTATE_ALLWIFIAUTHCHANNELCHANGED) && (elementDictionary != null)){

    }
}
```

Notify the end of the list of Authorized wifi Channel.<br/>

Triggered after the last [AuthorizedChannelResult](#ARDrone3-NetworkState-WifiAuthChannelListChanged) has been sent.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingSettingsState-MaxAltitudeChanged-->
### <a name="ARDrone3-PilotingSettingsState-MaxAltitudeChanged">Max Altitude changed</a><br/>
> Max Altitude changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float current = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_CURRENT)).doubleValue();
            float min = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_MIN)).doubleValue();
            float max = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXALTITUDECHANGED_MAX)).doubleValue();
        }
    }
}
```

Max Altitude changed.<br/>

* current (float): Current altitude max<br/>
* min (float): Range min of altitude<br/>
* max (float): Range max of altitude<br/>

Triggered by [SetMaxAltitude](#ARDrone3-PilotingSettings-MaxAltitude).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingSettingsState-MaxTiltChanged-->
### <a name="ARDrone3-PilotingSettingsState-MaxTiltChanged">Max tilt changed</a><br/>
> Max tilt changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXTILTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXTILTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXTILTCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float current = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_CURRENT)).doubleValue();
            float min = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_MIN)).doubleValue();
            float max = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXTILTCHANGED_MAX)).doubleValue();
        }
    }
}
```

Max tilt changed.<br/>

* current (float): Current max tilt<br/>
* min (float): Range min of tilt<br/>
* max (float): Range max of tilt<br/>

Triggered by [SetMaxTilt](#ARDrone3-PilotingSettings-MaxTilt).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingSettingsState-AbsolutControlChanged-->
### <a name="ARDrone3-PilotingSettingsState-AbsolutControlChanged">Absolut control changed</a><br/>
> Absolut control changed (deprecated):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_ABSOLUTCONTROLCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_ABSOLUTCONTROLCHANGED_ON, arg);
            if (arg != NULL)
            {
                uint8_t on = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_ABSOLUTCONTROLCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_ABSOLUTCONTROLCHANGED_ON, arg);
            if (arg != NULL)
            {
                uint8_t on = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_ABSOLUTCONTROLCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte on = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_ABSOLUTCONTROLCHANGED_ON)).intValue();
        }
    }
}
```

This event is deprecated.
<br/>

<!-- ARDrone3-PilotingSettingsState-MaxDistanceChanged-->
### <a name="ARDrone3-PilotingSettingsState-MaxDistanceChanged">Max distance changed</a><br/>
> Max distance changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXDISTANCECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXDISTANCECHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXDISTANCECHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXDISTANCECHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXDISTANCECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXDISTANCECHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXDISTANCECHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXDISTANCECHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXDISTANCECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float current = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXDISTANCECHANGED_CURRENT)).doubleValue();
            float min = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXDISTANCECHANGED_MIN)).doubleValue();
            float max = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_MAXDISTANCECHANGED_MAX)).doubleValue();
        }
    }
}
```

Max distance sent by the drone<br/>

* current (float): Current max distance in meter<br/>
* min (float): Minimal possible max distance<br/>
* max (float): Maximal possible max distance<br/>

Triggered by [SetMaxDistance](#ARDrone3-PilotingSettings-MaxDistance).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PilotingSettingsState-NoFlyOverMaxDistanceChanged-->
### <a name="ARDrone3-PilotingSettingsState-NoFlyOverMaxDistanceChanged">Max distance limitation behaviour</a><br/>
> Indication about how the product handle flying over the max distance limitation (not implemented):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_NOFLYOVERMAXDISTANCECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_NOFLYOVERMAXDISTANCECHANGED_SHOULDNOTFLYOVER, arg);
            if (arg != NULL)
            {
                uint8_t shouldNotFlyOver = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_NOFLYOVERMAXDISTANCECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_NOFLYOVERMAXDISTANCECHANGED_SHOULDNOTFLYOVER, arg);
            if (arg != NULL)
            {
                uint8_t shouldNotFlyOver = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_NOFLYOVERMAXDISTANCECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte shouldNotFlyOver = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_NOFLYOVERMAXDISTANCECHANGED_SHOULDNOTFLYOVER)).intValue();
        }
    }
}
```

Indication about how the product handle flying over the max distance limitation<br/>

* shouldNotFlyOver (u8): 1 if the drone won't fly further than max distance, 0 if no limitation on the drone will be done<br/>

**Draft: this event is not implemented yet by the firmware**<br/>

Triggered by [MaxDistanceLimitationBehaviour](#ARDrone3-PilotingSettings-NoFlyOverMaxDistance).

*Supported by no products<br/>*

<br/>

<!-- ARDrone3-PilotingSettingsState-AutonomousFlightMaxHorizontalSpeed-->
### <a name="ARDrone3-PilotingSettingsState-AutonomousFlightMaxHorizontalSpeed">Maximum horizontal speed used by the autonomous flight changed</a><br/>
> Maximum horizontal speed used by the autonomous flight changed (not implemented):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXHORIZONTALSPEED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXHORIZONTALSPEED_VALUE, arg);
            if (arg != NULL)
            {
                float value = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXHORIZONTALSPEED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXHORIZONTALSPEED_VALUE, arg);
            if (arg != NULL)
            {
                float value = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXHORIZONTALSPEED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float value = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXHORIZONTALSPEED_VALUE)).doubleValue();
        }
    }
}
```

Maximum horizontal speed used by the autonomous flight<br/>

* value (float): maximum horizontal speed [m/s]<br/>

**Draft: this event is not implemented yet by the firmware**<br/>

Triggered by [SetAutonomousFlightMaxHorizontalSpeed](#ARDrone3-PilotingSettings-setAutonomousFlightMaxHorizontalSpeed).

*Supported by no products<br/>*

<br/>

<!-- ARDrone3-PilotingSettingsState-AutonomousFlightMaxVerticalSpeed-->
### <a name="ARDrone3-PilotingSettingsState-AutonomousFlightMaxVerticalSpeed">Maximum vertical speed used by the autonomous flight changed</a><br/>
> Maximum vertical speed used by the autonomous flight changed (not implemented):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXVERTICALSPEED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXVERTICALSPEED_VALUE, arg);
            if (arg != NULL)
            {
                float value = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXVERTICALSPEED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXVERTICALSPEED_VALUE, arg);
            if (arg != NULL)
            {
                float value = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXVERTICALSPEED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float value = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXVERTICALSPEED_VALUE)).doubleValue();
        }
    }
}
```

Maximum vertical speed used by the autonomous flight<br/>

* value (float): maximum vertical speed [m/s]<br/>

**Draft: this event is not implemented yet by the firmware**<br/>

Triggered by [SetAutonomousFlightMaxVerticalSpeed](#ARDrone3-PilotingSettings-setAutonomousFlightMaxVerticalSpeed).

*Supported by no products<br/>*

<br/>

<!-- ARDrone3-PilotingSettingsState-AutonomousFlightMaxHorizontalAcceleration-->
### <a name="ARDrone3-PilotingSettingsState-AutonomousFlightMaxHorizontalAcceleration">Maximum horizontal acceleration used by the autonomous flight changed</a><br/>
> Maximum horizontal acceleration used by the autonomous flight changed (not implemented):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXHORIZONTALACCELERATION) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXHORIZONTALACCELERATION_VALUE, arg);
            if (arg != NULL)
            {
                float value = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXHORIZONTALACCELERATION) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXHORIZONTALACCELERATION_VALUE, arg);
            if (arg != NULL)
            {
                float value = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXHORIZONTALACCELERATION) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float value = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXHORIZONTALACCELERATION_VALUE)).doubleValue();
        }
    }
}
```

Maximum horizontal acceleration used by the autonomous flight<br/>

* value (float): maximum horizontal acceleration [m/s2]<br/>

**Draft: this event is not implemented yet by the firmware**<br/>

Triggered by [SetAutonomousFlightMaxHorizontalAcceleration](#ARDrone3-PilotingSettings-setAutonomousFlightMaxHorizontalAcceleration).

*Supported by no products<br/>*

<br/>

<!-- ARDrone3-PilotingSettingsState-AutonomousFlightMaxVerticalAcceleration-->
### <a name="ARDrone3-PilotingSettingsState-AutonomousFlightMaxVerticalAcceleration">Maximum vertical acceleration used by the autonomous flight changed</a><br/>
> Maximum vertical acceleration used by the autonomous flight changed (not implemented):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXVERTICALACCELERATION) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXVERTICALACCELERATION_VALUE, arg);
            if (arg != NULL)
            {
                float value = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXVERTICALACCELERATION) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXVERTICALACCELERATION_VALUE, arg);
            if (arg != NULL)
            {
                float value = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXVERTICALACCELERATION) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float value = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXVERTICALACCELERATION_VALUE)).doubleValue();
        }
    }
}
```

Maximum vertical acceleration used by the autonomous flight<br/>

* value (float): maximum vertical acceleration [m/s2]<br/>

**Draft: this event is not implemented yet by the firmware**<br/>

Triggered by [SetAutonomousFlightMaxVerticalAcceleration](#ARDrone3-PilotingSettings-setAutonomousFlightMaxVerticalAcceleration).

*Supported by no products<br/>*

<br/>

<!-- ARDrone3-PilotingSettingsState-AutonomousFlightMaxRotationSpeed-->
### <a name="ARDrone3-PilotingSettingsState-AutonomousFlightMaxRotationSpeed">Maximum yaw rotation speed used by the autonomous flight changed</a><br/>
> Maximum yaw rotation speed used by the autonomous flight changed (not implemented):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXROTATIONSPEED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXROTATIONSPEED_VALUE, arg);
            if (arg != NULL)
            {
                float value = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXROTATIONSPEED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXROTATIONSPEED_VALUE, arg);
            if (arg != NULL)
            {
                float value = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXROTATIONSPEED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float value = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_AUTONOMOUSFLIGHTMAXROTATIONSPEED_VALUE)).doubleValue();
        }
    }
}
```

Maximum yaw rotation speed used by the autonomous flight<br/>

* value (float): maximum yaw rotation speed [rad/s]<br/>

**Draft: this event is not implemented yet by the firmware**<br/>

Triggered by [SetAutonomousFlightMaxRotationSpeed](#ARDrone3-PilotingSettings-setAutonomousFlightMaxRotationSpeed).

*Supported by no products<br/>*

<br/>

<!-- ARDrone3-PilotingSettingsState-BankedTurnChanged-->
### <a name="ARDrone3-PilotingSettingsState-BankedTurnChanged">Banked Turn state.</a><br/>
> Banked Turn state.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_BANKEDTURNCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_BANKEDTURNCHANGED_STATE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_BANKEDTURNCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATE_BANKEDTURNCHANGED_STATE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATEBANKEDTURNCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte state = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PILOTINGSETTINGSSTATEBANKEDTURNCHANGED_STATE)).intValue();
        }
    }
}
```

Banked Turn state.<br/>

* state (u8): 1 if enabled, 0 if disabled<br/>
<br/>

Triggered by [SetBankedTurnMode](#ARDrone3-PilotingSettings-BankedTurn).

*Supported by <br/>*

- *Bebop since 3.2.0<br/>*
- *Bebop 2 since 3.2.0<br/>*

<br/>

<!-- ARDrone3-SpeedSettingsState-MaxVerticalSpeedChanged-->
### <a name="ARDrone3-SpeedSettingsState-MaxVerticalSpeedChanged">Max vertical speed changed</a><br/>
> Max vertical speed changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float current = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_CURRENT)).doubleValue();
            float min = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_MIN)).doubleValue();
            float max = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXVERTICALSPEEDCHANGED_MAX)).doubleValue();
        }
    }
}
```

Max vertical speed changed.<br/>

* current (float): Current max vertical speed in m/s<br/>
* min (float): Range min of vertical speed<br/>
* max (float): Range max of vertical speed<br/>

Triggered by [SetMaxVerticalSpeed](#ARDrone3-SpeedSettings-MaxVerticalSpeed).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-SpeedSettingsState-MaxRotationSpeedChanged-->
### <a name="ARDrone3-SpeedSettingsState-MaxRotationSpeedChanged">Max rotation speed changed</a><br/>
> Max rotation speed changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float current = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_CURRENT)).doubleValue();
            float min = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_MIN)).doubleValue();
            float max = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXROTATIONSPEEDCHANGED_MAX)).doubleValue();
        }
    }
}
```

Max rotation speed changed.<br/>

* current (float): Current max rotation speed in degree/s<br/>
* min (float): Range min of rotation speed<br/>
* max (float): Range max of rotation speed<br/>

Triggered by [SetMaxRotationSpeed](#ARDrone3-SpeedSettings-MaxRotationSpeed).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-SpeedSettingsState-HullProtectionChanged-->
### <a name="ARDrone3-SpeedSettingsState-HullProtectionChanged">Presence of hull protection changed</a><br/>
> Presence of hull protection changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_HULLPROTECTIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_HULLPROTECTIONCHANGED_PRESENT, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_HULLPROTECTIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_HULLPROTECTIONCHANGED_PRESENT, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_HULLPROTECTIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte present = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_HULLPROTECTIONCHANGED_PRESENT)).intValue();
        }
    }
}
```

Presence of hull protection changed.<br/>

* present (u8): 1 if present, 0 if not present<br/>

Triggered by [SetHullProtection](#ARDrone3-SpeedSettings-HullProtection).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*


<br/>

<!-- ARDrone3-SpeedSettingsState-OutdoorChanged-->
### <a name="ARDrone3-SpeedSettingsState-OutdoorChanged">Outdoor property changed</a><br/>
> Outdoor property changed (deprecated):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_OUTDOORCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_OUTDOORCHANGED_OUTDOOR, arg);
            if (arg != NULL)
            {
                uint8_t outdoor = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_OUTDOORCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_OUTDOORCHANGED_OUTDOOR, arg);
            if (arg != NULL)
            {
                uint8_t outdoor = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_OUTDOORCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte outdoor = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_OUTDOORCHANGED_OUTDOOR)).intValue();
        }
    }
}
```

This event is deprecated.
<br/>

<!-- ARDrone3-SpeedSettingsState-MaxPitchRollRotationSpeedChanged-->
### <a name="ARDrone3-SpeedSettingsState-MaxPitchRollRotationSpeedChanged">Max pitch/roll rotation speed sent by product</a><br/>
> Max pitch/roll rotation speed sent by product:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXPITCHROLLROTATIONSPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXPITCHROLLROTATIONSPEEDCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXPITCHROLLROTATIONSPEEDCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXPITCHROLLROTATIONSPEEDCHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXPITCHROLLROTATIONSPEEDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXPITCHROLLROTATIONSPEEDCHANGED_CURRENT, arg);
            if (arg != NULL)
            {
                float current = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXPITCHROLLROTATIONSPEEDCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATE_MAXPITCHROLLROTATIONSPEEDCHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATEMAXPITCHROLLROTATIONSPEEDCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float current = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATEMAXPITCHROLLROTATIONSPEEDCHANGED_CURRENT)).doubleValue();
            float min = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATEMAXPITCHROLLROTATIONSPEEDCHANGED_MIN)).doubleValue();
            float max = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SPEEDSETTINGSSTATEMAXPITCHROLLROTATIONSPEEDCHANGED_MAX)).doubleValue();
        }
    }
}
```

Max pitch/roll rotation speed sent by product<br/>

* current (float): Current max pitch/roll rotation speed in degree/s<br/>
* min (float): Range min of pitch/roll rotation speed<br/>
* max (float): Range max of pitch/roll rotation speed<br/>
<br/>

Triggered by [SetMaxPitchRollRotationSpeed](#ARDrone3-SpeedSettings-MaxPitchRollRotationSpeed).

*Supported by no products<br/>*

<br/>


<!-- ARDrone3-NetworkSettingsState-WifiSelectionChanged-->
### <a name="ARDrone3-NetworkSettingsState-WifiSelectionChanged">Wifi selection changed</a><br/>
> Wifi selection changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_BAND, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_BAND band = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_CHANNEL, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_BAND, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_BAND band = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_CHANNEL, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE_ENUM type = ARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE));
            ARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_BAND_ENUM band = ARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_BAND_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_BAND));
            byte channel = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISELECTIONCHANGED_CHANNEL)).intValue();
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
* band (enum): The actual  wifi band state<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
   * all: Both 2.4 and 5 GHz bands<br/>
* channel (u8): The channel (depends of the band)<br/>

Triggered by [WifiSelection](#ARDrone3-NetworkSettings-WifiSelection).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-NetworkSettingsState-wifiSecurityChanged-->
### <a name="ARDrone3-NetworkSettingsState-wifiSecurityChanged">Wifi security changed (deprecated)</a><br/>
> Wifi security changed (deprecated):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITYCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITYCHANGED_TYPE type = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITYCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITYCHANGED_TYPE type = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITYCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITYCHANGED_TYPE_ENUM type = ARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITYCHANGED_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITYCHANGED_TYPE));
        }
    }
}
```

*This event is deprecated.<br/>*

<br/>

<!-- ARDrone3-NetworkSettingsState-WifiSecurity-->
### <a name="ARDrone3-NetworkSettingsState-WifiSecurity">Wifi security changed</a><br/>
> Wifi security changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY_KEY, arg);
            if (arg != NULL)
            {
                char * key = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY_KEYTYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY_KEYTYPE keyType = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY_KEY, arg);
            if (arg != NULL)
            {
                char * key = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY_KEYTYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY_KEYTYPE keyType = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATEWIFISECURITY) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY_TYPE_ENUM type = ARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATEWIFISECURITY_TYPE));
            String key = (String)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATEWIFISECURITY_KEY);
            ARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY_KEYTYPE_ENUM keyType = ARCOMMANDS_ARDRONE3_NETWORKSETTINGSSTATE_WIFISECURITY_KEYTYPE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_NETWORKSETTINGSSTATEWIFISECURITY_KEYTYPE));
        }
    }
}
```

Sent by the drone when its wifi security changes.<br/>

* type (enum): The type of wifi security (open, wpa2)<br/>
   * open: Wifi is not protected by any security (default)<br/>
   * wpa2: Wifi is protected by wpa2<br/>
* key (string): The key used to secure the network (empty if type is open)<br/>
* keyType (enum): Type of the key<br/>
   * plain: Key is plain text, not encrypted<br/>
<br/>

Triggered by [WifiSecurity](#ARDrone3-NetworkSettings-wifiSecurity).

*Supported by <br/>*   

- *Bebop since 3.2.0<br/>*
- *Bebop 2 since 3.2.0<br/>*


<!-- ARDrone3-SettingsState-ProductMotorVersionListChanged-->
### <a name="ARDrone3-SettingsState-ProductMotorVersionListChanged">Product Motor version</a><br/>
> Product Motor version (deprecated):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED_MOTOR_NUMBER, arg);
            if (arg != NULL)
            {
                uint8_t motor_number = arg->value.U8;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                char * type = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED_SOFTWARE, arg);
            if (arg != NULL)
            {
                char * software = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED_HARDWARE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED_MOTOR_NUMBER, arg);
            if (arg != NULL)
            {
                uint8_t motor_number = arg->value.U8;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                char * type = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED_SOFTWARE, arg);
            if (arg != NULL)
            {
                char * software = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED_HARDWARE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED) && (elementDictionary != null)){
        Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
        while (itr.hasNext()) {
            ARControllerArgumentDictionary<Object> args = itr.next();
            if (args != null) {
                byte motor_number = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED_MOTOR_NUMBER)).intValue();
                String type = (String)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED_TYPE);
                String software = (String)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED_SOFTWARE);
                String hardware = (String)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTMOTORVERSIONLISTCHANGED_HARDWARE);
            }
        }
    }
}
```

This event is deprecated.
<br/>

<!-- ARDrone3-SettingsState-ProductGPSVersionChanged-->
### <a name="ARDrone3-SettingsState-ProductGPSVersionChanged">Product GPS versions</a><br/>
> Product GPS versions:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTGPSVERSIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTGPSVERSIONCHANGED_SOFTWARE, arg);
            if (arg != NULL)
            {
                char * software = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTGPSVERSIONCHANGED_HARDWARE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTGPSVERSIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTGPSVERSIONCHANGED_SOFTWARE, arg);
            if (arg != NULL)
            {
                char * software = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTGPSVERSIONCHANGED_HARDWARE, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTGPSVERSIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            String software = (String)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTGPSVERSIONCHANGED_SOFTWARE);
            String hardware = (String)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_PRODUCTGPSVERSIONCHANGED_HARDWARE);
        }
    }
}
```

Product GPS versions<br/>

* software (string): Product GPS software version<br/>
* hardware (string): Product GPS hardware version<br/>

Triggered at the connection.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*


<br/>

<!-- ARDrone3-SettingsState-MotorErrorStateChanged-->
### <a name="ARDrone3-SettingsState-MotorErrorStateChanged">Motor status changed</a><br/>
> Motor status changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORSTATECHANGED_MOTORIDS, arg);
            if (arg != NULL)
            {
                uint8_t motorIds = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORSTATECHANGED_MOTORERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_SETTINGSSTATE_MOTORERRORSTATECHANGED_MOTORERROR motorError = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORSTATECHANGED_MOTORIDS, arg);
            if (arg != NULL)
            {
                uint8_t motorIds = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORSTATECHANGED_MOTORERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_SETTINGSSTATE_MOTORERRORSTATECHANGED_MOTORERROR motorError = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORSTATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte motorIds = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORSTATECHANGED_MOTORIDS)).intValue();
            ARCOMMANDS_ARDRONE3_SETTINGSSTATE_MOTORERRORSTATECHANGED_MOTORERROR_ENUM motorError = ARCOMMANDS_ARDRONE3_SETTINGSSTATE_MOTORERRORSTATECHANGED_MOTORERROR_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORSTATECHANGED_MOTORERROR));
        }
    }
}
```

Motor status changed<br/>

* motorIds (u8): Bit field for concerned motor. If bit 0 = 1, motor 1 is affected by this error. Same with bit 1, 2 and 3.<br/>
* motorError (enum): Enumeration of the motor error<br/>
   * noError: No error detected<br/>
   * errorEEPRom: EEPROM access failure<br/>
   * errorMotorStalled: Motor stalled<br/>
   * errorPropellerSecurity: Propeller cutout security triggered<br/>
   * errorCommLost: Communication with motor failed by timeout<br/>
   * errorRCEmergencyStop: RC emergency stop<br/>
   * errorRealTime: Motor controler scheduler real-time out of bounds<br/>
   * errorMotorSetting: One or several incorrect values in motor settings<br/>
   * errorTemperature: Too hot or too cold Cypress temperature<br/>
   * errorBatteryVoltage: Battery voltage out of bounds<br/>
   * errorLipoCells: Incorrect number of LIPO cells<br/>
   * errorMOSFET: Defectuous MOSFET or broken motor phases<br/>
   * errorBootloader: Not use for BLDC but useful for HAL<br/>
   * errorAssert: Error Made by BLDC_ASSERT()<br/>

Triggered when an error on motors happens.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*
   
<br/>

<!-- ARDrone3-SettingsState-MotorSoftwareVersionChanged-->
### <a name="ARDrone3-SettingsState-MotorSoftwareVersionChanged">Motor software version status</a><br/>
> Motor software version status (deprecated):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORSOFTWAREVERSIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORSOFTWAREVERSIONCHANGED_VERSION, arg);
            if (arg != NULL)
            {
                char * version = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORSOFTWAREVERSIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORSOFTWAREVERSIONCHANGED_VERSION, arg);
            if (arg != NULL)
            {
                char * version = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORSOFTWAREVERSIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            String version = (String)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORSOFTWAREVERSIONCHANGED_VERSION);
        }
    }
}
```

This event is deprecated.
<br/>

<!-- ARDrone3-SettingsState-MotorFlightsStatusChanged-->
### <a name="ARDrone3-SettingsState-MotorFlightsStatusChanged">Motor flights status</a><br/>
> Motor flights status:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORFLIGHTSSTATUSCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORFLIGHTSSTATUSCHANGED_NBFLIGHTS, arg);
            if (arg != NULL)
            {
                uint16_t nbFlights = arg->value.U16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORFLIGHTSSTATUSCHANGED_LASTFLIGHTDURATION, arg);
            if (arg != NULL)
            {
                uint16_t lastFlightDuration = arg->value.U16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORFLIGHTSSTATUSCHANGED_TOTALFLIGHTDURATION, arg);
            if (arg != NULL)
            {
                uint32_t totalFlightDuration = arg->value.U32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORFLIGHTSSTATUSCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORFLIGHTSSTATUSCHANGED_NBFLIGHTS, arg);
            if (arg != NULL)
            {
                uint16_t nbFlights = arg->value.U16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORFLIGHTSSTATUSCHANGED_LASTFLIGHTDURATION, arg);
            if (arg != NULL)
            {
                uint16_t lastFlightDuration = arg->value.U16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORFLIGHTSSTATUSCHANGED_TOTALFLIGHTDURATION, arg);
            if (arg != NULL)
            {
                uint32_t totalFlightDuration = arg->value.U32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORFLIGHTSSTATUSCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            short nbFlights = (short)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORFLIGHTSSTATUSCHANGED_NBFLIGHTS)).intValue();
            short lastFlightDuration = (short)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORFLIGHTSSTATUSCHANGED_LASTFLIGHTDURATION)).intValue();
            int totalFlightDuration = (int)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORFLIGHTSSTATUSCHANGED_TOTALFLIGHTDURATION);
        }
    }
}
```

Motor flights status<br/>

* nbFlights (u16): total number of flights<br/>
* lastFlightDuration (u16): Duration of the last flight (in seconds)<br/>
* totalFlightDuration (u32): Duration of all flights (in seconds)<br/>
<br/>

<!-- ARDrone3-SettingsState-MotorErrorLastErrorChanged-->
### <a name="ARDrone3-SettingsState-MotorErrorLastErrorChanged">Motor status about last error</a><br/>
> Motor status about last error:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORLASTERRORCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORLASTERRORCHANGED_MOTORERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_SETTINGSSTATE_MOTORERRORLASTERRORCHANGED_MOTORERROR motorError = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORLASTERRORCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORLASTERRORCHANGED_MOTORERROR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_SETTINGSSTATE_MOTORERRORLASTERRORCHANGED_MOTORERROR motorError = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORLASTERRORCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_SETTINGSSTATE_MOTORERRORLASTERRORCHANGED_MOTORERROR_ENUM motorError = ARCOMMANDS_ARDRONE3_SETTINGSSTATE_MOTORERRORLASTERRORCHANGED_MOTORERROR_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_MOTORERRORLASTERRORCHANGED_MOTORERROR));
        }
    }
}
```

Motor status about last error<br/>

* motorError (enum): Enumeration of the motor error<br/>
   * noError: No error detected<br/>
   * errorEEPRom: EEPROM access failure<br/>
   * errorMotorStalled: Motor stalled<br/>
   * errorPropellerSecurity: Propeller cutout security triggered<br/>
   * errorCommLost: Communication with motor failed by timeout<br/>
   * errorRCEmergencyStop: RC emergency stop<br/>
   * errorRealTime: Motor controler scheduler real-time out of bounds<br/>
   * errorMotorSetting: One or several incorrect values in motor settings<br/>
   * errorBatteryVoltage: Battery voltage out of bounds<br/>
   * errorLipoCells: Incorrect number of LIPO cells<br/>
   * errorMOSFET: Defectuous MOSFET or broken motor phases<br/>
   * errorTemperature: Too hot or too cold Cypress temperature<br/>
   * errorBootloader: Not use for BLDC but useful for HAL<br/>
   * errorAssert: Error Made by BLDC_ASSERT()<br/>

Triggered after an error occured.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*
<br/>

<!-- ARDrone3-SettingsState-P7ID-->
### <a name="ARDrone3-SettingsState-P7ID">Product P7ID</a><br/>
> Product P7ID (deprecated):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_P7ID) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_P7ID_SERIALID, arg);
            if (arg != NULL)
            {
                char * serialID = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_P7ID) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_P7ID_SERIALID, arg);
            if (arg != NULL)
            {
                char * serialID = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_P7ID) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            String serialID = (String)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_SETTINGSSTATE_P7ID_SERIALID);
        }
    }
}
```

This event is deprecated.
<br/>

<!-- ARDrone3-PictureSettingsState-PictureFormatChanged-->
### <a name="ARDrone3-PictureSettingsState-PictureFormatChanged">Picture format changed</a><br/>
> Picture format changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_PICTUREFORMATCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_PICTUREFORMATCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_PICTUREFORMATCHANGED_TYPE type = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_PICTUREFORMATCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_PICTUREFORMATCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_PICTUREFORMATCHANGED_TYPE type = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_PICTUREFORMATCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_PICTUREFORMATCHANGED_TYPE_ENUM type = ARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_PICTUREFORMATCHANGED_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_PICTUREFORMATCHANGED_TYPE));
        }
    }
}
```

Picture format changed.<br/>

* type (enum): The type of photo format<br/>
   * raw: Take raw image<br/>
   * jpeg: Take a 4:3 jpeg photo<br/>
   * snapshot: Take a 16:9 snapshot from camera<br/>

Triggered by [SetPictureFormat](#ARDrone3-PictureSettings-PictureFormatSelection).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PictureSettingsState-AutoWhiteBalanceChanged-->
### <a name="ARDrone3-PictureSettingsState-AutoWhiteBalanceChanged">White balance mode changed</a><br/>
> White balance mode changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_AUTOWHITEBALANCECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_AUTOWHITEBALANCECHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_AUTOWHITEBALANCECHANGED_TYPE type = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_AUTOWHITEBALANCECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_AUTOWHITEBALANCECHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_AUTOWHITEBALANCECHANGED_TYPE type = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_AUTOWHITEBALANCECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_AUTOWHITEBALANCECHANGED_TYPE_ENUM type = ARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_AUTOWHITEBALANCECHANGED_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_AUTOWHITEBALANCECHANGED_TYPE));
        }
    }
}
```

White balance mode<br/>

* type (enum): The type auto white balance<br/>
   * auto: Auto guess of best white balance params<br/>
   * tungsten: Tungsten white balance<br/>
   * daylight: Daylight white balance<br/>
   * cloudy: Cloudy white balance<br/>
   * cool_white: White balance for a flash<br/>

Triggered by [SetWhiteBalanceMode](#ARDrone3-PictureSettings-AutoWhiteBalanceSelection).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PictureSettingsState-ExpositionChanged-->
### <a name="ARDrone3-PictureSettingsState-ExpositionChanged">Image exposure changed</a><br/>
> Image exposure changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_EXPOSITIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_EXPOSITIONCHANGED_VALUE, arg);
            if (arg != NULL)
            {
                float value = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_EXPOSITIONCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_EXPOSITIONCHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_EXPOSITIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_EXPOSITIONCHANGED_VALUE, arg);
            if (arg != NULL)
            {
                float value = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_EXPOSITIONCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_EXPOSITIONCHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_EXPOSITIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float value = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_EXPOSITIONCHANGED_VALUE)).doubleValue();
            float min = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_EXPOSITIONCHANGED_MIN)).doubleValue();
            float max = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_EXPOSITIONCHANGED_MAX)).doubleValue();
        }
    }
}
```

Image exposure changed.<br/>

* value (float): Exposure value<br/>
* min (float): Min exposure value<br/>
* max (float): Max exposure value<br/>

Triggered by [SetImageExposure](#ARDrone3-PictureSettings-ExpositionSelection).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PictureSettingsState-SaturationChanged-->
### <a name="ARDrone3-PictureSettingsState-SaturationChanged">Image saturation changed</a><br/>
> Image saturation changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_SATURATIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_SATURATIONCHANGED_VALUE, arg);
            if (arg != NULL)
            {
                float value = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_SATURATIONCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_SATURATIONCHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_SATURATIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_SATURATIONCHANGED_VALUE, arg);
            if (arg != NULL)
            {
                float value = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_SATURATIONCHANGED_MIN, arg);
            if (arg != NULL)
            {
                float min = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_SATURATIONCHANGED_MAX, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_SATURATIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            float value = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_SATURATIONCHANGED_VALUE)).doubleValue();
            float min = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_SATURATIONCHANGED_MIN)).doubleValue();
            float max = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_SATURATIONCHANGED_MAX)).doubleValue();
        }
    }
}
```

Image saturation changed.<br/>

* value (float): Saturation value<br/>
* min (float): Min saturation value<br/>
* max (float): Max saturation value<br/>

Triggered by [SetImageSaturation](#ARDrone3-PictureSettings-SaturationSelection).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PictureSettingsState-TimelapseChanged-->
### <a name="ARDrone3-PictureSettingsState-TimelapseChanged">Timelapse mode configuration changed</a><br/>
> Timelapse mode configuration changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED_ENABLED, arg);
            if (arg != NULL)
            {
                uint8_t enabled = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED_INTERVAL, arg);
            if (arg != NULL)
            {
                float interval = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED_MININTERVAL, arg);
            if (arg != NULL)
            {
                float minInterval = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED_MAXINTERVAL, arg);
            if (arg != NULL)
            {
                float maxInterval = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED_ENABLED, arg);
            if (arg != NULL)
            {
                uint8_t enabled = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED_INTERVAL, arg);
            if (arg != NULL)
            {
                float interval = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED_MININTERVAL, arg);
            if (arg != NULL)
            {
                float minInterval = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED_MAXINTERVAL, arg);
            if (arg != NULL)
            {
                float maxInterval = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte enabled = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED_ENABLED)).intValue();
            float interval = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED_INTERVAL)).doubleValue();
            float minInterval = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED_MININTERVAL)).doubleValue();
            float maxInterval = (float)((Double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_TIMELAPSECHANGED_MAXINTERVAL)).doubleValue();
        }
    }
}
```

Timelapse mode configuration changed.<br/>

* enabled (u8): 1 if timelapse is enabled, 0 otherwise<br/>
* interval (float): interval in seconds for taking pictures<br/>
* minInterval (float): Minimal interval for taking pictures<br/>
* maxInterval (float): Maximal interval for taking pictures<br/>

Triggered by [TimelapseModeConfiguration](#ARDrone3-PictureSettings-TimelapseSelection).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PictureSettingsState-VideoAutorecordChanged-->
### <a name="ARDrone3-PictureSettingsState-VideoAutorecordChanged">Video autorecord changed</a><br/>
> Video autorecord changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOAUTORECORDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOAUTORECORDCHANGED_ENABLED, arg);
            if (arg != NULL)
            {
                uint8_t enabled = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOAUTORECORDCHANGED_MASS_STORAGE_ID, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOAUTORECORDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOAUTORECORDCHANGED_ENABLED, arg);
            if (arg != NULL)
            {
                uint8_t enabled = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOAUTORECORDCHANGED_MASS_STORAGE_ID, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOAUTORECORDCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte enabled = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOAUTORECORDCHANGED_ENABLED)).intValue();
            byte mass_storage_id = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOAUTORECORDCHANGED_MASS_STORAGE_ID)).intValue();
        }
    }
}
```

Video autorecord changed.<br/>

* enabled (u8): 1 if video autorecord is enabled, 0 otherwise<br/>
* mass_storage_id (u8): Mass storage id for the taken video<br/>

Triggered by [SetVideoAutorecord](#ARDrone3-PictureSettings-VideoAutorecordSelection).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PictureSettingsState-VideoStabilizationModeChanged-->
### <a name="ARDrone3-PictureSettingsState-VideoStabilizationModeChanged">Video stabilization mode</a><br/>
> Video stabilization mode:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOSTABILIZATIONMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOSTABILIZATIONMODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_VIDEOSTABILIZATIONMODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOSTABILIZATIONMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOSTABILIZATIONMODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_VIDEOSTABILIZATIONMODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATEVIDEOSTABILIZATIONMODECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_VIDEOSTABILIZATIONMODECHANGED_MODE_ENUM mode = ARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_VIDEOSTABILIZATIONMODECHANGED_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATEVIDEOSTABILIZATIONMODECHANGED_MODE));
        }
    }
}
```

Video stabilization mode.<br/>

* mode (enum): Video stabilization mode<br/>
   * roll_pitch: Video flat on roll and pitch<br/>
   * pitch: Video flat on pitch only<br/>
   * roll: Video flat on roll only<br/>
   * none: Video follows drone angles<br/>
<br/>

Triggered by [SetVideoStabilizationMode](#ARDrone3-PictureSettings-VideoStabilizationMode).

*Supported by no products.<br/>*

<!-- ARDrone3-PictureSettingsState-VideoRecordingModeChanged-->
### <a name="ARDrone3-PictureSettingsState-VideoRecordingModeChanged">Video recording mode</a><br/>
> Video recording mode:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEORECORDINGMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEORECORDINGMODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_VIDEORECORDINGMODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEORECORDINGMODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEORECORDINGMODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_VIDEORECORDINGMODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATEVIDEORECORDINGMODECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_VIDEORECORDINGMODECHANGED_MODE_ENUM mode = ARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_VIDEORECORDINGMODECHANGED_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATEVIDEORECORDINGMODECHANGED_MODE));
        }
    }
}
```

Video recording mode<br/>

* mode (enum): <br/>
   * quality: Maximize recording quality.<br/>
   * time: Maximize recording time.<br/>

Triggered by [SetVideoRecordMode](#ARDrone3-PictureSettings-VideoRecordingMode).

*Supported by <br/>*   

- *Bebop since 3.3.0<br/>*
- *Bebop 2 since 3.3.0<br/>*
<br/>

<!-- ARDrone3-PictureSettingsState-VideoFramerateChanged-->
### <a name="ARDrone3-PictureSettingsState-VideoFramerateChanged">Video framerate</a><br/>
> Video framerate:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOFRAMERATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOFRAMERATECHANGED_FRAMERATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_VIDEOFRAMERATECHANGED_FRAMERATE framerate = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOFRAMERATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATE_VIDEOFRAMERATECHANGED_FRAMERATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_VIDEOFRAMERATECHANGED_FRAMERATE framerate = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATEVIDEOFRAMERATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_VIDEOFRAMERATECHANGED_FRAMERATE_ENUM framerate = ARCOMMANDS_ARDRONE3_PICTURESETTINGSSTATE_VIDEOFRAMERATECHANGED_FRAMERATE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PICTURESETTINGSSTATEVIDEOFRAMERATECHANGED_FRAMERATE));
        }
    }
}
```

Video framerate<br/>

* framerate (enum): <br/>
   * 24_FPS: 23.976 frames per second.<br/>
   * 25_FPS: 25 frames per second.<br/>
   * 30_FPS: 29.97 frames per second.<br/>

Triggered by [SetVideoFramerate](#ARDrone3-PictureSettings-VideoFramerate).

*Supported by <br/>*   

- *Bebop since 3.3.0<br/>*
- *Bebop 2 since 3.3.0<br/>*
<br/>

<!-- ARDrone3-MediaStreamingState-VideoEnableChanged-->
### <a name="ARDrone3-MediaStreamingState-VideoEnableChanged">Video streaming status changed</a><br/>
> Video streaming status changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED_ENABLED, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED_ENABLED enabled = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED_ENABLED, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED_ENABLED enabled = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED_ENABLED_ENUM enabled = ARCOMMANDS_ARDRONE3_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED_ENABLED_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_MEDIASTREAMINGSTATE_VIDEOENABLECHANGED_ENABLED));
        }
    }
}
```

Video streaming status changed.<br/>

* enabled (enum): Current video streaming status.<br/>
   * enabled: Video streaming is enabled.<br/>
   * disabled: Video streaming is disabled.<br/>
   * error: Video streaming failed to start.<br/>

Triggered by [EnableVideoStream](#ARDrone3-MediaStreaming-VideoEnable).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*
<br/>

<!-- ARDrone3-GPSSettingsState-HomeChanged-->
### <a name="ARDrone3-GPSSettingsState-HomeChanged">Home location changed</a><br/>
> Home location changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMECHANGED_LATITUDE, arg);
            if (arg != NULL)
            {
                double latitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMECHANGED_LONGITUDE, arg);
            if (arg != NULL)
            {
                double longitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMECHANGED_ALTITUDE, arg);
            if (arg != NULL)
            {
                double altitude = arg->value.Double;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMECHANGED_LATITUDE, arg);
            if (arg != NULL)
            {
                double latitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMECHANGED_LONGITUDE, arg);
            if (arg != NULL)
            {
                double longitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMECHANGED_ALTITUDE, arg);
            if (arg != NULL)
            {
                double altitude = arg->value.Double;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            double latitude = (double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMECHANGED_LATITUDE);
            double longitude = (double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMECHANGED_LONGITUDE);
            double altitude = (double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMECHANGED_ALTITUDE);
        }
    }
}
```

Home location changed.<br/>

* latitude (double): Home latitude in decimal degrees<br/>
* longitude (double): Home longitude in decimal degrees<br/>
* altitude (double): Home altitude in meters<br/>

Triggered by [SetHomeLocation](#ARDrone3-GPSSettings-SetHome).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-GPSSettingsState-ResetHomeChanged-->
### <a name="ARDrone3-GPSSettingsState-ResetHomeChanged">Home location has been reset</a><br/>
> Home location has been reset:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RESETHOMECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RESETHOMECHANGED_LATITUDE, arg);
            if (arg != NULL)
            {
                double latitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RESETHOMECHANGED_LONGITUDE, arg);
            if (arg != NULL)
            {
                double longitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RESETHOMECHANGED_ALTITUDE, arg);
            if (arg != NULL)
            {
                double altitude = arg->value.Double;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RESETHOMECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RESETHOMECHANGED_LATITUDE, arg);
            if (arg != NULL)
            {
                double latitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RESETHOMECHANGED_LONGITUDE, arg);
            if (arg != NULL)
            {
                double longitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RESETHOMECHANGED_ALTITUDE, arg);
            if (arg != NULL)
            {
                double altitude = arg->value.Double;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RESETHOMECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            double latitude = (double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RESETHOMECHANGED_LATITUDE);
            double longitude = (double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RESETHOMECHANGED_LONGITUDE);
            double altitude = (double)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RESETHOMECHANGED_ALTITUDE);
        }
    }
}
```

Home location has been reset.<br/>

* latitude (double): Home latitude in decimal degrees<br/>
* longitude (double): Home longitude in decimal degrees<br/>
* altitude (double): Home altitude in meters<br/>

Triggered by [ResetHomeLocation](#ARDrone3-GPSSettings-ResetHome).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-GPSSettingsState-GPSFixStateChanged-->
### <a name="ARDrone3-GPSSettingsState-GPSFixStateChanged">GPS fix changed</a><br/>
> GPS fix changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_GPSFIXSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_GPSFIXSTATECHANGED_FIXED, arg);
            if (arg != NULL)
            {
                uint8_t fixed = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_GPSFIXSTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_GPSFIXSTATECHANGED_FIXED, arg);
            if (arg != NULL)
            {
                uint8_t fixed = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_GPSFIXSTATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte fixed = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_GPSFIXSTATECHANGED_FIXED)).intValue();
        }
    }
}
```

GPS fix changed.<br/>

* fixed (u8): 1 if gps on drone is fixed, 0 otherwise<br/>

Triggered when the GPS fix state changed.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-GPSSettingsState-GPSUpdateStateChanged-->
### <a name="ARDrone3-GPSSettingsState-GPSUpdateStateChanged">GPS update state</a><br/>
> GPS update state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_GPSUPDATESTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_GPSUPDATESTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_GPSSETTINGSSTATE_GPSUPDATESTATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_GPSUPDATESTATECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_GPSUPDATESTATECHANGED_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_GPSSETTINGSSTATE_GPSUPDATESTATECHANGED_STATE state = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_GPSUPDATESTATECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_GPSSETTINGSSTATE_GPSUPDATESTATECHANGED_STATE_ENUM state = ARCOMMANDS_ARDRONE3_GPSSETTINGSSTATE_GPSUPDATESTATECHANGED_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_GPSUPDATESTATECHANGED_STATE));
        }
    }
}
```

GPS update state<br/>

* state (enum): The state of the gps update<br/>
   * updated: Drone GPS update succeed<br/>
   * inProgress: Drone GPS update In progress<br/>
   * failed: Drone GPS update failed<br/>

Triggered when the GPS update state changed.

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-GPSSettingsState-HomeTypeChanged-->
### <a name="ARDrone3-GPSSettingsState-HomeTypeChanged">Prefered home type changed</a><br/>
> Prefered home type changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMETYPECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMETYPECHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_GPSSETTINGSSTATE_HOMETYPECHANGED_TYPE type = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMETYPECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMETYPECHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_GPSSETTINGSSTATE_HOMETYPECHANGED_TYPE type = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMETYPECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_GPSSETTINGSSTATE_HOMETYPECHANGED_TYPE_ENUM type = ARCOMMANDS_ARDRONE3_GPSSETTINGSSTATE_HOMETYPECHANGED_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_HOMETYPECHANGED_TYPE));
        }
    }
}
```

User preference home type changed. <br/>
See [HomeTypeChosenChanged](#ARDrone3-GPSState-HomeTypeChosenChanged) to get the drone actual home type.

* type (enum): The type of the home position<br/>
   * TAKEOFF: The drone will try to return to the take off position<br/>
   * PILOT: The drone will try to return to the pilot position<br/>

Triggered by [SetPreferedHomeType](#ARDrone3-GPSSettings-HomeType).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-GPSSettingsState-ReturnHomeDelayChanged-->
### <a name="ARDrone3-GPSSettingsState-ReturnHomeDelayChanged">Delay of the return home changed</a><br/>
> Delay of the return home changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RETURNHOMEDELAYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RETURNHOMEDELAYCHANGED_DELAY, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RETURNHOMEDELAYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RETURNHOMEDELAYCHANGED_DELAY, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RETURNHOMEDELAYCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            short delay = (short)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSETTINGSSTATE_RETURNHOMEDELAYCHANGED_DELAY)).intValue();
        }
    }
}
```

Delay of the return home changed. This delay represents the time after which th return home is automatically triggered after a disconnection.<br/>

* delay (u16): Delay in second<br/>

Triggered by [SetReturnHomeDelay](#ARDrone3-GPSSettings-ReturnHomeDelay).

*Supported by <br/>*   

- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-CameraState-Orientation-->
### <a name="ARDrone3-CameraState-Orientation">Camera orientation changed</a><br/>
> Camera orientation:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_ORIENTATION) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_ORIENTATION_TILT, arg);
            if (arg != NULL)
            {
                int8_t tilt = arg->value.I8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_ORIENTATION_PAN, arg);
            if (arg != NULL)
            {
                int8_t pan = arg->value.I8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_ORIENTATION) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_ORIENTATION_TILT, arg);
            if (arg != NULL)
            {
                int8_t tilt = arg->value.I8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_ORIENTATION_PAN, arg);
            if (arg != NULL)
            {
                int8_t pan = arg->value.I8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_ORIENTATION) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte tilt = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_ORIENTATION_TILT)).intValue();
            byte pan = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_ORIENTATION_PAN)).intValue();
        }
    }
}
```

Camera orientation<br/>

* tilt (i8): Tilt camera consign for the drone [-100;100]<br/>
* pan (i8): Pan camera consign for the drone [-100;100]<br/>

Tilt and pan values are clamped to given values. You can get these bounds with [CameraSettingsChanged](#common-CameraSettingsState-CameraSettingsChanged).

Triggered by [SetCameraOrientation](#ARDrone3-Camera-Orientation).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-CameraState-defaultCameraOrientation-->
### <a name="ARDrone3-CameraState-defaultCameraOrientation">Orientation of the camera center.</a><br/>
> Orientation of the camera center.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_DEFAULTCAMERAORIENTATION) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_DEFAULTCAMERAORIENTATION_TILT, arg);
            if (arg != NULL)
            {
                int8_t tilt = arg->value.I8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_DEFAULTCAMERAORIENTATION_PAN, arg);
            if (arg != NULL)
            {
                int8_t pan = arg->value.I8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_DEFAULTCAMERAORIENTATION) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_DEFAULTCAMERAORIENTATION_TILT, arg);
            if (arg != NULL)
            {
                int8_t tilt = arg->value.I8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_DEFAULTCAMERAORIENTATION_PAN, arg);
            if (arg != NULL)
            {
                int8_t pan = arg->value.I8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_DEFAULTCAMERAORIENTATION) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte tilt = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_DEFAULTCAMERAORIENTATION_TILT)).intValue();
            byte pan = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_CAMERASTATE_DEFAULTCAMERAORIENTATION_PAN)).intValue();
        }
    }
}
```

Orientation of the camera center.<br/>

This is the value to send when we want to center the camera.<br/>

* tilt (i8): Tilt value (in degree)<br/>
* pan (i8): Pan value (in degree)<br/>

Triggered at the connection.

*Supported by <br/>*   

- *Bebop 2.0.57<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-AntiflickeringState-electricFrequencyChanged-->
### <a name="ARDrone3-AntiflickeringState-electricFrequencyChanged">Electric frequency changed</a><br/>
> Electric frequency changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_ANTIFLICKERINGSTATE_ELECTRICFREQUENCYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_ANTIFLICKERINGSTATE_ELECTRICFREQUENCYCHANGED_FREQUENCY, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_ANTIFLICKERINGSTATE_ELECTRICFREQUENCYCHANGED_FREQUENCY frequency = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_ANTIFLICKERINGSTATE_ELECTRICFREQUENCYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_ANTIFLICKERINGSTATE_ELECTRICFREQUENCYCHANGED_FREQUENCY, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_ANTIFLICKERINGSTATE_ELECTRICFREQUENCYCHANGED_FREQUENCY frequency = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_ANTIFLICKERINGSTATE_ELECTRICFREQUENCYCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_ANTIFLICKERINGSTATE_ELECTRICFREQUENCYCHANGED_FREQUENCY_ENUM frequency = ARCOMMANDS_ARDRONE3_ANTIFLICKERINGSTATE_ELECTRICFREQUENCYCHANGED_FREQUENCY_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_ANTIFLICKERINGSTATE_ELECTRICFREQUENCYCHANGED_FREQUENCY));
        }
    }
}
```

Electric frequency changed.<br/>

* frequency (enum): Type of the electric frequency<br/>
   * fiftyHertz: Electric frequency of the country is 50hz<br/>
   * sixtyHertz: Electric frequency of the country is 60hz<br/>

Triggered by [SetElectricFrequency](#ARDrone3-Antiflickering-electricFrequency).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-AntiflickeringState-modeChanged-->
### <a name="ARDrone3-AntiflickeringState-modeChanged">Anti flickering mode changed</a><br/>
> Anti flickering mode changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_ANTIFLICKERINGSTATE_MODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_ANTIFLICKERINGSTATE_MODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_ANTIFLICKERINGSTATE_MODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_ANTIFLICKERINGSTATE_MODECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_ANTIFLICKERINGSTATE_MODECHANGED_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_ANTIFLICKERINGSTATE_MODECHANGED_MODE mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_ANTIFLICKERINGSTATE_MODECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_ANTIFLICKERINGSTATE_MODECHANGED_MODE_ENUM mode = ARCOMMANDS_ARDRONE3_ANTIFLICKERINGSTATE_MODECHANGED_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_ANTIFLICKERINGSTATE_MODECHANGED_MODE));
        }
    }
}
```

Anti flickering mode changed.<br/>

* mode (enum): Mode of the anti flickering functionnality<br/>
   * auto: Anti flickering based on the electric frequency previously sent<br/>
   * FixedFiftyHertz: Anti flickering based on a fixed frequency of 50Hz<br/>
   * FixedSixtyHertz: Anti flickering based on a fixed frequency of 60Hz<br/>

Triggered by [SetAntiflickeringMode](#ARDrone3-Antiflickering-setMode).

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-GPSState-NumberOfSatelliteChanged-->
### <a name="ARDrone3-GPSState-NumberOfSatelliteChanged">The number of gps sattelites seen changed</a><br/>
> The number of gps sattelites seen changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_NUMBEROFSATELLITECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_NUMBEROFSATELLITECHANGED_NUMBEROFSATELLITE, arg);
            if (arg != NULL)
            {
                uint8_t numberOfSatellite = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_NUMBEROFSATELLITECHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_NUMBEROFSATELLITECHANGED_NUMBEROFSATELLITE, arg);
            if (arg != NULL)
            {
                uint8_t numberOfSatellite = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_NUMBEROFSATELLITECHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte numberOfSatellite = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_NUMBEROFSATELLITECHANGED_NUMBEROFSATELLITE)).intValue();
        }
    }
}
```

The number of gps sattelites seen changed.<br/>

* numberOfSatellite (u8): The number of satellite<br/>

Triggered when the number of satellites seen changes.

*Supported by <br/>*   

- *Bebop 2<br/>*
<br/>

<!-- ARDrone3-GPSState-HomeTypeAvailabilityChanged-->
### <a name="ARDrone3-GPSState-HomeTypeAvailabilityChanged">Home types availability changed</a><br/>
> Home types availability changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPEAVAILABILITYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPEAVAILABILITYCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_GPSSTATE_HOMETYPEAVAILABILITYCHANGED_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPEAVAILABILITYCHANGED_AVAILABLE, arg);
            if (arg != NULL)
            {
                uint8_t available = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPEAVAILABILITYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPEAVAILABILITYCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_GPSSTATE_HOMETYPEAVAILABILITYCHANGED_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPEAVAILABILITYCHANGED_AVAILABLE, arg);
            if (arg != NULL)
            {
                uint8_t available = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPEAVAILABILITYCHANGED) && (elementDictionary != null)){
        Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
        while (itr.hasNext()) {
            ARControllerArgumentDictionary<Object> args = itr.next();
            if (args != null) {
                ARCOMMANDS_ARDRONE3_GPSSTATE_HOMETYPEAVAILABILITYCHANGED_TYPE_ENUM type = ARCOMMANDS_ARDRONE3_GPSSTATE_HOMETYPEAVAILABILITYCHANGED_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPEAVAILABILITYCHANGED_TYPE));
                byte available = (byte)((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPEAVAILABILITYCHANGED_AVAILABLE)).intValue();
            }
        }
    }
}
```

Return home types availability changed.<br/>
Results are given in a map: for each type availability is given.<br/>

* type (enum): The type of the return home<br/>
   * TAKEOFF: The drone will try to return to the take off position<br/>
   * PILOT: The drone will try to return to the pilot position<br/>
   * FIRST_FIX: The drone has not enough information, it will try to return to the first GPS fix<br/>
* available (u8): 1 if this type is available, 0 otherwise<br/>

Normally, *FIRST_FIX* should be always available.

Triggered when the availability of, at least, one type changes. This might be due to controller position availability, gps fix before take off or other reason.<br/>

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-GPSState-HomeTypeChosenChanged-->
### <a name="ARDrone3-GPSState-HomeTypeChosenChanged">The return home type chosen</a><br/>
> The return home type chosen:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPECHOSENCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPECHOSENCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_GPSSTATE_HOMETYPECHOSENCHANGED_TYPE type = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPECHOSENCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPECHOSENCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ARDRONE3_GPSSTATE_HOMETYPECHOSENCHANGED_TYPE type = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPECHOSENCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ARDRONE3_GPSSTATE_HOMETYPECHOSENCHANGED_TYPE_ENUM type = ARCOMMANDS_ARDRONE3_GPSSTATE_HOMETYPECHOSENCHANGED_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_GPSSTATE_HOMETYPECHOSENCHANGED_TYPE));
        }
    }
}
```

The return home type chosen.<br/>
This choice is made by the drone, according to the user preference and the availability of the home types. The drone will choose the type matching with the user preference only if this type is available.

* type (enum): The type of the return home chosen<br/>
   * TAKEOFF: The drone will try to return to the take off position<br/>
   * PILOT: The drone will try to return to the pilot position<br/>
   * FIRST_FIX: The drone has not enough information, it will try to return to the first GPS fix<br/>

Triggered when the return home type chosen by the drone changes. This might be produced by a user preference triggered by [SetPreferedHomeType](#ARDrone3-GPSSettings-HomeType) or by a change in the [HomeTypesAvailabilityChanged](#ARDrone3-GPSState-HomeTypeAvailabilityChanged).<br/>

*Supported by <br/>*   

- *Bebop<br/>*
- *Bebop 2<br/>*

<br/>

<!-- ARDrone3-PROState-Features-->
### <a name="ARDrone3-PROState-Features">Features enabled</a><br/>
> Features enabled (deprecated):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PROSTATE_FEATURES) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PROSTATE_FEATURES_FEATURES, arg);
            if (arg != NULL)
            {
                uint64_t features = arg->value.U64;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PROSTATE_FEATURES) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PROSTATE_FEATURES_FEATURES, arg);
            if (arg != NULL)
            {
                uint64_t features = arg->value.U64;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PROSTATE_FEATURES) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            long features = (long)args.get(ARFeatureARDrone3.ARCONTROLLER_DICTIONARY_KEY_ARDRONE3_PROSTATE_FEATURES_FEATURES);
        }
    }
}
```

This event is deprecated.

<br/>

