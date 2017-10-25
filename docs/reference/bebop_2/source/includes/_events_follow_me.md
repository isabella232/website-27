<!-- follow_me-state-->
### <a name="follow_me-state">State of the FollowMe</a><br/>
> State of the FollowMe:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_FOLLOW_ME_MODE mode = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE_BEHAVIOR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_FOLLOW_ME_BEHAVIOR behavior = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE_ANIMATION, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_FOLLOW_ME_ANIMATION animation = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE_ANIMATION_AVAILABLE, arg);
            if (arg != NULL)
            {
                uint16_t animation_available = arg->value.U16;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_FOLLOW_ME_MODE mode = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE_BEHAVIOR, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_FOLLOW_ME_BEHAVIOR behavior = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE_ANIMATION, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_FOLLOW_ME_ANIMATION animation = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE_ANIMATION_AVAILABLE, arg);
            if (arg != NULL)
            {
                uint16_t animation_available = arg->value.U16;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_FOLLOW_ME_MODE_ENUM mode = ARCOMMANDS_FOLLOW_ME_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE_MODE));
            ARCOMMANDS_FOLLOW_ME_BEHAVIOR_ENUM behavior = ARCOMMANDS_FOLLOW_ME_BEHAVIOR_ENUM.getFromValue((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE_BEHAVIOR));
            ARCOMMANDS_FOLLOW_ME_ANIMATION_ENUM animation = ARCOMMANDS_FOLLOW_ME_ANIMATION_ENUM.getFromValue((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE_ANIMATION));
            short animation_available = (short)((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_STATE_ANIMATION_AVAILABLE)).intValue();
        }
    }
}
```

<br/>


* mode (enum): FollowMe mode<br/>
   * none: No follow me<br/>
   * look_at: Look at the target without moving automatically<br/>
   * geographic: Follow the target keeping the same vector<br/>
   * relative: Follow the target keeping the same orientation to its direction<br/>
* behavior (enum): FollowMe behavior<br/>
   * idle: Drone is not moving according to the target<br/>
This means that at least one required input is missing<br/>
   * follow: Follow the target<br/>
   * look_at: Look at the target without moving<br/>
* animation (enum): FollowMe animation type<br/>
   * none: No animation<br/>
   * helicoid: Turn around the target<br/>
   * swing: Pass by the zenith and change of side<br/>
   * boomerang: Fly far from the target and fly back<br/>
   * candle: Move to the target and go high when it is near<br/>
   * dolly_slide: Fly in line<br/>
* animation_available (bitfield as u16): FollowMe animation type<br/>
   * none: No animation<br/>
   * helicoid: Turn around the target<br/>
   * swing: Pass by the zenith and change of side<br/>
   * boomerang: Fly far from the target and fly back<br/>
   * candle: Move to the target and go high when it is near<br/>
   * dolly_slide: Fly in line<br/>


Triggered by any changes on the followme, like [start](#follow_me-start),<br/>

[stop](#follow_me-stop), [start helicoid anim](#follow_me-relative_config)...<br/>



*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-mode_info-->
### <a name="follow_me-mode_info">FollowMe mode info</a><br/>
> FollowMe mode info:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_MODEINFO)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_MODEINFO_MODE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_FOLLOW_ME_MODE mode = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_MODEINFO_MISSING_REQUIREMENTS, arg);
                if (arg != NULL)
                {
                    uint16_t missing_requirements = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_MODEINFO_IMPROVEMENTS, arg);
                if (arg != NULL)
                {
                    uint16_t improvements = arg->value.U16;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_MODEINFO)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_MODEINFO_MODE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_FOLLOW_ME_MODE mode = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_MODEINFO_MISSING_REQUIREMENTS, arg);
                if (arg != NULL)
                {
                    uint16_t missing_requirements = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_MODEINFO_IMPROVEMENTS, arg);
                if (arg != NULL)
                {
                    uint16_t improvements = arg->value.U16;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_MODEINFO){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    ARCOMMANDS_FOLLOW_ME_MODE_ENUM mode = ARCOMMANDS_FOLLOW_ME_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_MODEINFO_MODE));
                    short missing_requirements = (short)((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_MODEINFO_MISSING_REQUIREMENTS)).intValue();
                    short improvements = (short)((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_MODEINFO_IMPROVEMENTS)).intValue();
                }
            }
        } else {
            // list is empty
        }
    }
}
```

<br/>


* mode (enum): FollowMe mode<br/>
   * none: No follow me<br/>
   * look_at: Look at the target without moving automatically<br/>
   * geographic: Follow the target keeping the same vector<br/>
   * relative: Follow the target keeping the same orientation to its direction<br/>
* missing_requirements (bitfield as u16): Input values used by the FollowMe<br/>
   * drone_calibrated: Drone is calibrated<br/>
   * drone_gps_good_accuracy: Drone gps has fixed and has a good accuracy<br/>
   * target_gps_good_accuracy: Target gps data is known and has a good accuracy<br/>
   * target_barometer_ok: Target barometer data is available<br/>
   * drone_far_enough: Drone is far enough from the target<br/>
   * drone_high_enough: Drone is high enough from the ground<br/>
   * image_detection: Target detection is done by image detection among other things<br/>
* improvements (bitfield as u16): Input values used by the FollowMe<br/>
   * drone_calibrated: Drone is calibrated<br/>
   * drone_gps_good_accuracy: Drone gps has fixed and has a good accuracy<br/>
   * target_gps_good_accuracy: Target gps data is known and has a good accuracy<br/>
   * target_barometer_ok: Target barometer data is available<br/>
   * drone_far_enough: Drone is far enough from the target<br/>
   * drone_high_enough: Drone is high enough from the ground<br/>
   * image_detection: Target detection is done by image detection among other things<br/>


Triggered When the list of missing requirements or improvments changes<br/>



*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-geographic_config-->
### <a name="follow_me-geographic_config">Geographic configuration changed</a><br/>
> Geographic configuration changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG_USE_DEFAULT, arg);
            if (arg != NULL)
            {
                uint8_t use_default = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG_DISTANCE, arg);
            if (arg != NULL)
            {
                float distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG_ELEVATION, arg);
            if (arg != NULL)
            {
                float elevation = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG_AZIMUTH, arg);
            if (arg != NULL)
            {
                float azimuth = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG_USE_DEFAULT, arg);
            if (arg != NULL)
            {
                uint8_t use_default = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG_DISTANCE, arg);
            if (arg != NULL)
            {
                float distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG_ELEVATION, arg);
            if (arg != NULL)
            {
                float elevation = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG_AZIMUTH, arg);
            if (arg != NULL)
            {
                float azimuth = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte use_default = (byte)((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG_USE_DEFAULT)).intValue();
            float distance = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG_DISTANCE)).doubleValue();
            float elevation = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG_ELEVATION)).doubleValue();
            float azimuth = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_GEOGRAPHICCONFIG_AZIMUTH)).doubleValue();
        }
    }
}
```

Geographic configuration changed.<br/>
This event is only valid when arg behavior in [state](#follow_me-state) is equal to Follow.<br/>


* use_default (bitfield as u8): Geographic and Relative follow me configuration parameters<br/>
   * distance: Distance configuration<br/>
   * elevation: Elevation configuration<br/>
   * azimuth: Azimuth configuration<br/>
* distance (float): The distance leader-follower in meter<br/>
If distance is default, this value is the current drone distance<br/>
* elevation (float): The elevation leader-follower in rad<br/>
If elevation is default, this value is the current leader to drone elevation<br/>
* azimuth (float): The azimuth north-leader-follower in rad<br/>
If azimuth is default, this value is the current leader to drone azimuth<br/>


Triggered By [start geographic](#follow_me-start) or [configure geographic](#follow_me-mode_info).<br/>



*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-relative_config-->
### <a name="follow_me-relative_config">Relative configuration changed</a><br/>
> Relative configuration changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG_USE_DEFAULT, arg);
            if (arg != NULL)
            {
                uint8_t use_default = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG_DISTANCE, arg);
            if (arg != NULL)
            {
                float distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG_ELEVATION, arg);
            if (arg != NULL)
            {
                float elevation = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG_AZIMUTH, arg);
            if (arg != NULL)
            {
                float azimuth = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG_USE_DEFAULT, arg);
            if (arg != NULL)
            {
                uint8_t use_default = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG_DISTANCE, arg);
            if (arg != NULL)
            {
                float distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG_ELEVATION, arg);
            if (arg != NULL)
            {
                float elevation = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG_AZIMUTH, arg);
            if (arg != NULL)
            {
                float azimuth = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte use_default = (byte)((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG_USE_DEFAULT)).intValue();
            float distance = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG_DISTANCE)).doubleValue();
            float elevation = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG_ELEVATION)).doubleValue();
            float azimuth = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_RELATIVECONFIG_AZIMUTH)).doubleValue();
        }
    }
}
```

Relative configuration changed.<br/>
This event is only valid when arg behavior in [state](#follow_me-state) is equal to Follow.<br/>


* use_default (bitfield as u8): Geographic and Relative follow me configuration parameters<br/>
   * distance: Distance configuration<br/>
   * elevation: Elevation configuration<br/>
   * azimuth: Azimuth configuration<br/>
* distance (float): The distance leader-follower in meter<br/>
If distance is default, this value is the current drone distance<br/>
* elevation (float): The elevation leader-follower in rad<br/>
If elevation is default, this value is the current leader to drone elevation<br/>
* azimuth (float): The azimuth course-leader-follower in rad<br/>
If azimuth is default, this value is the current leader to drone azimuth<br/>


Triggered By [start relative](#follow_me-start) or [configure relative](#follow_me-mode_info).<br/>



*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-target_trajectory-->
### <a name="follow_me-target_trajectory">Target estimated trajectory</a><br/>
> Target estimated trajectory:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_LATITUDE, arg);
            if (arg != NULL)
            {
                double latitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_LONGITUDE, arg);
            if (arg != NULL)
            {
                double longitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_ALTITUDE, arg);
            if (arg != NULL)
            {
                float altitude = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_NORTH_SPEED, arg);
            if (arg != NULL)
            {
                float north_speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_EAST_SPEED, arg);
            if (arg != NULL)
            {
                float east_speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_DOWN_SPEED, arg);
            if (arg != NULL)
            {
                float down_speed = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_LATITUDE, arg);
            if (arg != NULL)
            {
                double latitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_LONGITUDE, arg);
            if (arg != NULL)
            {
                double longitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_ALTITUDE, arg);
            if (arg != NULL)
            {
                float altitude = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_NORTH_SPEED, arg);
            if (arg != NULL)
            {
                float north_speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_EAST_SPEED, arg);
            if (arg != NULL)
            {
                float east_speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_DOWN_SPEED, arg);
            if (arg != NULL)
            {
                float down_speed = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            double latitude = (double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_LATITUDE);
            double longitude = (double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_LONGITUDE);
            float altitude = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_ALTITUDE)).doubleValue();
            float north_speed = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_NORTH_SPEED)).doubleValue();
            float east_speed = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_EAST_SPEED)).doubleValue();
            float down_speed = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETTRAJECTORY_DOWN_SPEED)).doubleValue();
        }
    }
}
```

<br/>


* latitude (double): Target latitude (in degrees)<br/>
* longitude (double): Target longitude (in degrees)<br/>
* altitude (float): Target altitude (in meters, relative to sea level)<br/>
* north_speed (float): Target north speed (in m/s)<br/>
* east_speed (float): Target east speed (in m/s)<br/>
* down_speed (float): Target down speed (in m/s)<br/>


Triggered Regularly when a FollowMe is started.<br/>



*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-helicoid_anim_config-->
### <a name="follow_me-helicoid_anim_config">Helicoid animation configuration</a><br/>
> Helicoid animation configuration:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG_USE_DEFAULT, arg);
            if (arg != NULL)
            {
                uint8_t use_default = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG_REVOLUTION_NB, arg);
            if (arg != NULL)
            {
                float revolution_nb = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG_VERTICAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float vertical_distance = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG_USE_DEFAULT, arg);
            if (arg != NULL)
            {
                uint8_t use_default = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG_REVOLUTION_NB, arg);
            if (arg != NULL)
            {
                float revolution_nb = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG_VERTICAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float vertical_distance = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte use_default = (byte)((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG_USE_DEFAULT)).intValue();
            float speed = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG_SPEED)).doubleValue();
            float revolution_nb = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG_REVOLUTION_NB)).doubleValue();
            float vertical_distance = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_HELICOIDANIMCONFIG_VERTICAL_DISTANCE)).doubleValue();
        }
    }
}
```

Helicoid animation configuration.<br/>
This should only be taken in account if arg animation in [state](#follow_me-state) is equal to helicoid.<br/>
This message has been deprecated. Please use the animation feature.<br/>


* use_default (bitfield as u8): Helicoid animation configuration parameters.<br/>
   * speed: Speed parameter<br/>
   * revolution_nb: Number of turn<br/>
   * vertical_distance: Vertical distance<br/>
* speed (float): The speed of the anim in m/s<br/>
* revolution_nb (float): The number of revolution (in turn)<br/>
Negative value is infinite<br/>
* vertical_distance (float): Distance that will be made by the product to reach the top of the helicoid in m<br/>


Triggered by a [start helicoid animation](#follow_me-relative_config).<br/>



*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-swing_anim_config-->
### <a name="follow_me-swing_anim_config">Swing animation configuration changed</a><br/>
> Swing animation configuration changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_SWINGANIMCONFIG) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_SWINGANIMCONFIG_USE_DEFAULT, arg);
            if (arg != NULL)
            {
                uint8_t use_default = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_SWINGANIMCONFIG_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_SWINGANIMCONFIG_VERTICAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float vertical_distance = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_SWINGANIMCONFIG) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_SWINGANIMCONFIG_USE_DEFAULT, arg);
            if (arg != NULL)
            {
                uint8_t use_default = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_SWINGANIMCONFIG_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_SWINGANIMCONFIG_VERTICAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float vertical_distance = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_SWINGANIMCONFIG) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte use_default = (byte)((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_SWINGANIMCONFIG_USE_DEFAULT)).intValue();
            float speed = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_SWINGANIMCONFIG_SPEED)).doubleValue();
            float vertical_distance = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_SWINGANIMCONFIG_VERTICAL_DISTANCE)).doubleValue();
        }
    }
}
```

Swing animation configuration changed.<br/>
This should only be taken in account if arg animation in [state](#follow_me-state) is equal to swing.<br/>
This message has been deprecated. Please use the animation feature.<br/>


* use_default (bitfield as u8): Swing configure parameters.<br/>
   * speed: Speed parameter<br/>
   * vertical_distance: Vertical distance<br/>
* speed (float): The speed of the anim in m/s<br/>
* vertical_distance (float): Distance that will be made by the product to reach the top of the swing in m<br/>


Triggered by a [start swing animation](#follow_me-stop_animation).<br/>



*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-boomerang_anim_config-->
### <a name="follow_me-boomerang_anim_config">Boomerang animation configuration changed</a><br/>
> Boomerang animation configuration changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_BOOMERANGANIMCONFIG) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_BOOMERANGANIMCONFIG_USE_DEFAULT, arg);
            if (arg != NULL)
            {
                uint8_t use_default = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_BOOMERANGANIMCONFIG_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_BOOMERANGANIMCONFIG_DISTANCE, arg);
            if (arg != NULL)
            {
                float distance = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_BOOMERANGANIMCONFIG) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_BOOMERANGANIMCONFIG_USE_DEFAULT, arg);
            if (arg != NULL)
            {
                uint8_t use_default = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_BOOMERANGANIMCONFIG_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_BOOMERANGANIMCONFIG_DISTANCE, arg);
            if (arg != NULL)
            {
                float distance = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_BOOMERANGANIMCONFIG) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte use_default = (byte)((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_BOOMERANGANIMCONFIG_USE_DEFAULT)).intValue();
            float speed = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_BOOMERANGANIMCONFIG_SPEED)).doubleValue();
            float distance = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_BOOMERANGANIMCONFIG_DISTANCE)).doubleValue();
        }
    }
}
```

Boomerang animation configuration changed.<br/>
This should only be taken in account if arg animation in [state](#follow_me-state) is equal to boomerang.<br/>
This message has been deprecated. Please use the animation feature.<br/>


* use_default (bitfield as u8): Boomerang animation configure parameters.<br/>
   * speed: Speed parameter<br/>
   * distance: Distance<br/>
* speed (float): The speed of the anim in m/s<br/>
* distance (float): Distance that will be made by the product to reach its return point in m<br/>


Triggered by a [start boomerang animation](#follow_me-helicoid_anim_config).<br/>



*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-candle_anim_config-->
### <a name="follow_me-candle_anim_config">Candle animation configuration changed</a><br/>
> Candle animation configuration changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_CANDLEANIMCONFIG) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_CANDLEANIMCONFIG_USE_DEFAULT, arg);
            if (arg != NULL)
            {
                uint8_t use_default = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_CANDLEANIMCONFIG_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_CANDLEANIMCONFIG_VERTICAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float vertical_distance = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_CANDLEANIMCONFIG) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_CANDLEANIMCONFIG_USE_DEFAULT, arg);
            if (arg != NULL)
            {
                uint8_t use_default = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_CANDLEANIMCONFIG_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_CANDLEANIMCONFIG_VERTICAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float vertical_distance = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_CANDLEANIMCONFIG) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte use_default = (byte)((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_CANDLEANIMCONFIG_USE_DEFAULT)).intValue();
            float speed = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_CANDLEANIMCONFIG_SPEED)).doubleValue();
            float vertical_distance = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_CANDLEANIMCONFIG_VERTICAL_DISTANCE)).doubleValue();
        }
    }
}
```

Candle animation configuration changed.<br/>
This should only be taken in account if arg animation in [state](#follow_me-state) is equal to candle.<br/>
This message has been deprecated. Please use the animation feature.<br/>


* use_default (bitfield as u8): Candle animation configure parameters.<br/>
   * speed: Speed parameter<br/>
   * vertical_distance: Follow the target keeping the same vector<br/>
* speed (float): The speed of the anim in m/s<br/>
* vertical_distance (float): Distance that will be made by the product to reach the top of the vertical zoom-out in m<br/>


Triggered by a [start candle animation](#follow_me-swing_anim_config).<br/>



*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-dolly_slide_anim_config-->
### <a name="follow_me-dolly_slide_anim_config">DollySlide animation configuration changed</a><br/>
> DollySlide animation configuration changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG_USE_DEFAULT, arg);
            if (arg != NULL)
            {
                uint8_t use_default = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG_ANGLE, arg);
            if (arg != NULL)
            {
                float angle = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG_HORIZONTAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float horizontal_distance = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG_USE_DEFAULT, arg);
            if (arg != NULL)
            {
                uint8_t use_default = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG_ANGLE, arg);
            if (arg != NULL)
            {
                float angle = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG_HORIZONTAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float horizontal_distance = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte use_default = (byte)((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG_USE_DEFAULT)).intValue();
            float speed = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG_SPEED)).doubleValue();
            float angle = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG_ANGLE)).doubleValue();
            float horizontal_distance = (float)((Double)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_DOLLYSLIDEANIMCONFIG_HORIZONTAL_DISTANCE)).doubleValue();
        }
    }
}
```

DollySlide animation configuration changed.<br/>
This should only be taken in account if arg animation in [state](#follow_me-state) is equal to dolly_slide.<br/>
This message has been deprecated. Please use the animation feature.<br/>


* use_default (bitfield as u8): Dolly slide animation configure parameters.<br/>
   * speed: Speed parameter<br/>
   * angle: Angle<br/>
   * horizontal_distance: Horizontal distance<br/>
* speed (float): The speed of the anim in m/s<br/>
* angle (float): Angle Product-User-Target in rad<br/>
* horizontal_distance (float): Distance that will be made by the product to reach its target in m<br/>


Triggered by a [start dolly slide animation](#follow_me-boomerang_anim_config).<br/>



*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-target_framing_position_changed-->
### <a name="follow_me-target_framing_position_changed">Desired target framing</a><br/>
> Desired target framing:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETFRAMINGPOSITIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETFRAMINGPOSITIONCHANGED_HORIZONTAL, arg);
            if (arg != NULL)
            {
                int8_t horizontal = arg->value.I8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETFRAMINGPOSITIONCHANGED_VERTICAL, arg);
            if (arg != NULL)
            {
                int8_t vertical = arg->value.I8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETFRAMINGPOSITIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETFRAMINGPOSITIONCHANGED_HORIZONTAL, arg);
            if (arg != NULL)
            {
                int8_t horizontal = arg->value.I8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETFRAMINGPOSITIONCHANGED_VERTICAL, arg);
            if (arg != NULL)
            {
                int8_t vertical = arg->value.I8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETFRAMINGPOSITIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte horizontal = (byte)((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETFRAMINGPOSITIONCHANGED_HORIZONTAL)).intValue();
            byte vertical = (byte)((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETFRAMINGPOSITIONCHANGED_VERTICAL)).intValue();
        }
    }
}
```

<br/>


* horizontal (i8): Horizontal position in the video (in %, from left to right)<br/>
* vertical (i8): Vertical position in the video (in %, from bottom to top)<br/>


Triggered by [set target framing](#follow_me-candle_anim_config).<br/>



*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

<!-- follow_me-target_image_detection_state-->
### <a name="follow_me-target_image_detection_state">State of the image detection</a><br/>
> State of the image detection:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETIMAGEDETECTIONSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETIMAGEDETECTIONSTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_FOLLOW_ME_IMAGE_DETECTION_STATUS state = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETIMAGEDETECTIONSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETIMAGEDETECTIONSTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_FOLLOW_ME_IMAGE_DETECTION_STATUS state = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETIMAGEDETECTIONSTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_FOLLOW_ME_IMAGE_DETECTION_STATUS_ENUM state = ARCOMMANDS_FOLLOW_ME_IMAGE_DETECTION_STATUS_ENUM.getFromValue((Integer)args.get(ARFeatureFollowMe.ARCONTROLLER_DICTIONARY_KEY_FOLLOW_ME_TARGETIMAGEDETECTIONSTATE_STATE));
        }
    }
}
```

<br/>


* state (enum): State of the image detection<br/>
   * none: No image detection<br/>
   * ok: Image detection is considered ok by the drone<br/>
   * lost: Image detection is considered lost or<br/>
in contradiction with gps value.<br/>
This state will remain until a new selection of the target is done<br/>


Triggered By a possible wrong [target image detection](#follow_me-target_image_detection).<br/>



*Supported by <br/>*

- *Bebop 2 since 4.0.0*<br/>


<br/>

