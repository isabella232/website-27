<!-- animation-availability-->
### <a name="animation-availability">Availability of the animations</a><br/>
> Availability of the animations:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_AVAILABILITY) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_AVAILABILITY_VALUES, arg);
            if (arg != NULL)
            {
                uint32_t values = arg->value.U32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_AVAILABILITY) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_AVAILABILITY_VALUES, arg);
            if (arg != NULL)
            {
                uint32_t values = arg->value.U32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_AVAILABILITY) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            int values = (int)((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_AVAILABILITY_VALUES)).intValue();
        }
    }
}
```

<br/>


* values (bitfield as u32): Animation type.<br/>
   * none: No animation<br/>
   * flip: The drone makes a flip<br/>
   * horizontal_panorama: The drone horizontaly rotates on itself<br/>
   * dronie: The drone flies away on a given distance with a computed angle<br/>
   * horizontal_reveal: The drone starts looking down, then moves forward while slowly looking at the horizon<br/>
   * vertical_reveal: The drone starts looking down, then moves up while slowly looking at the horizon.<br/>
When it reaches its target altitude, it rotates on itself to do a panorama.<br/>
   * spiral: The drone circles around its target.<br/>
   * parabola: The drone makes a parabola on top of its target and ends on the other side of it.<br/>
   * candle: The drone flies horizontally in direction of the target then flies up.<br/>
   * dolly_slide: The drone slides horizontally.<br/>


Triggered when the list of available animations changes.<br/>



*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-state-->
### <a name="animation-state">State of the animation</a><br/>
> State of the animation:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_STATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_STATE_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_STATE_PERCENT, arg);
            if (arg != NULL)
            {
                uint8_t percent = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_STATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_STATE_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_STATE_PERCENT, arg);
            if (arg != NULL)
            {
                uint8_t percent = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_STATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ANIMATION_TYPE_ENUM type = ARCOMMANDS_ANIMATION_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_STATE_TYPE));
            byte percent = (byte)((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_STATE_PERCENT)).intValue();
        }
    }
}
```

<br/>


* type (enum): Animation type.<br/>
   * none: No animation<br/>
   * flip: The drone makes a flip<br/>
   * horizontal_panorama: The drone horizontaly rotates on itself<br/>
   * dronie: The drone flies away on a given distance with a computed angle<br/>
   * horizontal_reveal: The drone starts looking down, then moves forward while slowly looking at the horizon<br/>
   * vertical_reveal: The drone starts looking down, then moves up while slowly looking at the horizon.<br/>
When it reaches its target altitude, it rotates on itself to do a panorama.<br/>
   * spiral: The drone circles around its target.<br/>
   * parabola: The drone makes a parabola on top of its target and ends on the other side of it.<br/>
   * candle: The drone flies horizontally in direction of the target then flies up.<br/>
   * dolly_slide: The drone slides horizontally.<br/>
* percent (u8): Percentage of the animation (only accurate if type is not none) (from 0 to 100).<br/>


Triggered when the state of the animation changes.<br/>



*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-flip_state-->
### <a name="animation-flip_state">Flip state</a><br/>
> Flip state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_FLIPSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_FLIPSTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_FLIPSTATE_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_FLIP_TYPE type = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_FLIPSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_FLIPSTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_FLIPSTATE_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_FLIP_TYPE type = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_FLIPSTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ANIMATION_STATE_ENUM state = ARCOMMANDS_ANIMATION_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_FLIPSTATE_STATE));
            ARCOMMANDS_ANIMATION_FLIP_TYPE_ENUM type = ARCOMMANDS_ANIMATION_FLIP_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_FLIPSTATE_TYPE));
        }
    }
}
```

<br/>


* state (enum): Animation state.<br/>
   * idle: The animation is not running.<br/>
   * running: The animation is running.<br/>
   * canceling: The current animation is canceling.<br/>
* type (enum): Animation flip type.<br/>
   * front: The drone makes a front flip<br/>
   * back: The drone makes a back flip<br/>
   * left: The drone makes a left flip (its left side goes up)<br/>
   * right: The drone makes a right flip (its right side goes up)<br/>


Triggered by [StartFlip](#animation-start_flip) and when the state changes.<br/>



*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-horizontal_panorama_state-->
### <a name="animation-horizontal_panorama_state">Horizontal panorama state</a><br/>
> Horizontal panorama state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALPANORAMASTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALPANORAMASTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALPANORAMASTATE_ROTATION_ANGLE, arg);
            if (arg != NULL)
            {
                float rotation_angle = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALPANORAMASTATE_ROTATION_SPEED, arg);
            if (arg != NULL)
            {
                float rotation_speed = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALPANORAMASTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALPANORAMASTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALPANORAMASTATE_ROTATION_ANGLE, arg);
            if (arg != NULL)
            {
                float rotation_angle = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALPANORAMASTATE_ROTATION_SPEED, arg);
            if (arg != NULL)
            {
                float rotation_speed = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALPANORAMASTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ANIMATION_STATE_ENUM state = ARCOMMANDS_ANIMATION_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALPANORAMASTATE_STATE));
            float rotation_angle = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALPANORAMASTATE_ROTATION_ANGLE)).doubleValue();
            float rotation_speed = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALPANORAMASTATE_ROTATION_SPEED)).doubleValue();
        }
    }
}
```

<br/>


* state (enum): Animation state.<br/>
   * idle: The animation is not running.<br/>
   * running: The animation is running.<br/>
   * canceling: The current animation is canceling.<br/>
* rotation_angle (float): Rotation angle in rad. Positive value makes a clockwise panorama, negative is anti-clockwise.<br/>
(only accurate if state is not idle)<br/>
* rotation_speed (float): The rotation speed of the anim in rad/s<br/>
(only accurate if state is not idle)<br/>


Triggered by [StartHorizontalPanorama](#animation-start_horizontal_panorama) and when the state changes.<br/>



*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-dronie_state-->
### <a name="animation-dronie_state">Dronie state</a><br/>
> Dronie state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE_DISTANCE, arg);
            if (arg != NULL)
            {
                float distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE_PLAY_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_PLAY_MODE play_mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE_DISTANCE, arg);
            if (arg != NULL)
            {
                float distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE_PLAY_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_PLAY_MODE play_mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ANIMATION_STATE_ENUM state = ARCOMMANDS_ANIMATION_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE_STATE));
            float speed = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE_SPEED)).doubleValue();
            float distance = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE_DISTANCE)).doubleValue();
            ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM play_mode = ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DRONIESTATE_PLAY_MODE));
        }
    }
}
```

<br/>


* state (enum): Animation state.<br/>
   * idle: The animation is not running.<br/>
   * running: The animation is running.<br/>
   * canceling: The current animation is canceling.<br/>
* speed (float): Speed in m/s.<br/>
(only accurate if state is not idle)<br/>
* distance (float): Dronie distance in m.<br/>
(only accurate if state is not idle)<br/>
* play_mode (enum): Animation play mode.<br/>
   * normal: Animation is played once, normally.<br/>
   * once_then_mirrored: Animation is played once and then the animation is played mirrored.<br/>


Triggered by [StartDronie](#animation-start_dronie) and when the state changes.<br/>



*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-horizontal_reveal_state-->
### <a name="animation-horizontal_reveal_state">Horizontal reveal state</a><br/>
> Horizontal reveal state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE_DISTANCE, arg);
            if (arg != NULL)
            {
                float distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE_PLAY_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_PLAY_MODE play_mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE_DISTANCE, arg);
            if (arg != NULL)
            {
                float distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE_PLAY_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_PLAY_MODE play_mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ANIMATION_STATE_ENUM state = ARCOMMANDS_ANIMATION_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE_STATE));
            float speed = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE_SPEED)).doubleValue();
            float distance = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE_DISTANCE)).doubleValue();
            ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM play_mode = ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_HORIZONTALREVEALSTATE_PLAY_MODE));
        }
    }
}
```

<br/>


* state (enum): Animation state.<br/>
   * idle: The animation is not running.<br/>
   * running: The animation is running.<br/>
   * canceling: The current animation is canceling.<br/>
* speed (float): Speed in m/s.<br/>
(only accurate if state is not idle)<br/>
* distance (float): Distance in m.<br/>
(only accurate if state is not idle)<br/>
* play_mode (enum): Animation play mode.<br/>
   * normal: Animation is played once, normally.<br/>
   * once_then_mirrored: Animation is played once and then the animation is played mirrored.<br/>


Triggered by [StartHorizontalReveal](#animation-start_horizontal_reveal) and when the state changes.<br/>



*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-vertical_reveal_state-->
### <a name="animation-vertical_reveal_state">Vertical reveal state</a><br/>
> Vertical reveal state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_VERTICAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float vertical_distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_ROTATION_ANGLE, arg);
            if (arg != NULL)
            {
                float rotation_angle = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_ROTATION_SPEED, arg);
            if (arg != NULL)
            {
                float rotation_speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_PLAY_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_PLAY_MODE play_mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_VERTICAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float vertical_distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_ROTATION_ANGLE, arg);
            if (arg != NULL)
            {
                float rotation_angle = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_ROTATION_SPEED, arg);
            if (arg != NULL)
            {
                float rotation_speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_PLAY_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_PLAY_MODE play_mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ANIMATION_STATE_ENUM state = ARCOMMANDS_ANIMATION_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_STATE));
            float speed = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_SPEED)).doubleValue();
            float vertical_distance = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_VERTICAL_DISTANCE)).doubleValue();
            float rotation_angle = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_ROTATION_ANGLE)).doubleValue();
            float rotation_speed = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_ROTATION_SPEED)).doubleValue();
            ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM play_mode = ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_VERTICALREVEALSTATE_PLAY_MODE));
        }
    }
}
```

<br/>


* state (enum): Animation state.<br/>
   * idle: The animation is not running.<br/>
   * running: The animation is running.<br/>
   * canceling: The current animation is canceling.<br/>
* speed (float): Speed in m/s.<br/>
(only accurate if state is not idle)<br/>
* vertical_distance (float): Vertical distance in m.<br/>
(only accurate if state is not idle)<br/>
* rotation_angle (float): Rotation angle in rad. Positive value makes a clockwise panorama, negative is anti-clockwise.<br/>
(only accurate if state is not idle)<br/>
* rotation_speed (float): The rotation speed of the anim in rad/s<br/>
(only accurate if state is not idle)<br/>
* play_mode (enum): Animation play mode.<br/>
   * normal: Animation is played once, normally.<br/>
   * once_then_mirrored: Animation is played once and then the animation is played mirrored.<br/>


Triggered by [StartVerticalReveal](#animation-start_vertical_reveal) and when the state changes.<br/>



*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-spiral_state-->
### <a name="animation-spiral_state">Spiral state</a><br/>
> Spiral state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_RADIUS_VARIATION, arg);
            if (arg != NULL)
            {
                float radius_variation = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_VERTICAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float vertical_distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_REVOLUTION_NB, arg);
            if (arg != NULL)
            {
                float revolution_nb = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_PLAY_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_PLAY_MODE play_mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_RADIUS_VARIATION, arg);
            if (arg != NULL)
            {
                float radius_variation = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_VERTICAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float vertical_distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_REVOLUTION_NB, arg);
            if (arg != NULL)
            {
                float revolution_nb = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_PLAY_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_PLAY_MODE play_mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ANIMATION_STATE_ENUM state = ARCOMMANDS_ANIMATION_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_STATE));
            float speed = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_SPEED)).doubleValue();
            float radius_variation = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_RADIUS_VARIATION)).doubleValue();
            float vertical_distance = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_VERTICAL_DISTANCE)).doubleValue();
            float revolution_nb = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_REVOLUTION_NB)).doubleValue();
            ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM play_mode = ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_SPIRALSTATE_PLAY_MODE));
        }
    }
}
```

<br/>


* state (enum): Animation state.<br/>
   * idle: The animation is not running.<br/>
   * running: The animation is running.<br/>
   * canceling: The current animation is canceling.<br/>
* speed (float): Speed in m/s.<br/>
(only accurate if state is not idle)<br/>
* radius_variation (float): Relative radius variation in m.<br/>
(only accurate if state is not idle)<br/>
* vertical_distance (float): Vertical distance in m. Negative value means the animation is directed toward the ground.<br/>
(only accurate if state is not idle)<br/>
* revolution_nb (float): The number of revolution (in turn).<br/>
(only accurate if state is not idle)<br/>
* play_mode (enum): Animation play mode.<br/>
   * normal: Animation is played once, normally.<br/>
   * once_then_mirrored: Animation is played once and then the animation is played mirrored.<br/>


Triggered by [StartSpiral](#animation-start_spiral) and when the state changes.<br/>



*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-parabola_state-->
### <a name="animation-parabola_state">Parabola state</a><br/>
> Parabola state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE_VERTICAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float vertical_distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE_PLAY_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_PLAY_MODE play_mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE_VERTICAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float vertical_distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE_PLAY_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_PLAY_MODE play_mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ANIMATION_STATE_ENUM state = ARCOMMANDS_ANIMATION_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE_STATE));
            float speed = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE_SPEED)).doubleValue();
            float vertical_distance = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE_VERTICAL_DISTANCE)).doubleValue();
            ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM play_mode = ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_PARABOLASTATE_PLAY_MODE));
        }
    }
}
```

<br/>


* state (enum): Animation state.<br/>
   * idle: The animation is not running.<br/>
   * running: The animation is running.<br/>
   * canceling: The current animation is canceling.<br/>
* speed (float): Speed in m/s.<br/>
(only accurate if state is not idle)<br/>
* vertical_distance (float): Vertical distance in m.<br/>
(only accurate if state is not idle)<br/>
* play_mode (enum): Animation play mode.<br/>
   * normal: Animation is played once, normally.<br/>
   * once_then_mirrored: Animation is played once and then the animation is played mirrored.<br/>


Triggered by [StartParabola](#animation-start_parabola) and when the state changes.<br/>



*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-candle_state-->
### <a name="animation-candle_state">Candle state</a><br/>
> Candle state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE_VERTICAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float vertical_distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE_PLAY_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_PLAY_MODE play_mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE_VERTICAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float vertical_distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE_PLAY_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_PLAY_MODE play_mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ANIMATION_STATE_ENUM state = ARCOMMANDS_ANIMATION_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE_STATE));
            float speed = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE_SPEED)).doubleValue();
            float vertical_distance = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE_VERTICAL_DISTANCE)).doubleValue();
            ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM play_mode = ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_CANDLESTATE_PLAY_MODE));
        }
    }
}
```

<br/>


* state (enum): Animation state.<br/>
   * idle: The animation is not running.<br/>
   * running: The animation is running.<br/>
   * canceling: The current animation is canceling.<br/>
* speed (float): Speed in m/s.<br/>
(only accurate if state is not idle)<br/>
* vertical_distance (float): Vertical distance in m.<br/>
(only accurate if state is not idle)<br/>
* play_mode (enum): Animation play mode.<br/>
   * normal: Animation is played once, normally.<br/>
   * once_then_mirrored: Animation is played once and then the animation is played mirrored.<br/>


Triggered by [StartCandle](#animation-start_candle) and when the state changes.<br/>



*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

<!-- animation-dolly_slide_state-->
### <a name="animation-dolly_slide_state">Dolly slide state</a><br/>
> Dolly slide state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_ANGLE, arg);
            if (arg != NULL)
            {
                float angle = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_HORIZONTAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float horizontal_distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_PLAY_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_PLAY_MODE play_mode = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_SPEED, arg);
            if (arg != NULL)
            {
                float speed = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_ANGLE, arg);
            if (arg != NULL)
            {
                float angle = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_HORIZONTAL_DISTANCE, arg);
            if (arg != NULL)
            {
                float horizontal_distance = arg->value.Float;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_PLAY_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_ANIMATION_PLAY_MODE play_mode = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_ANIMATION_STATE_ENUM state = ARCOMMANDS_ANIMATION_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_STATE));
            float speed = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_SPEED)).doubleValue();
            float angle = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_ANGLE)).doubleValue();
            float horizontal_distance = (float)((Double)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_HORIZONTAL_DISTANCE)).doubleValue();
            ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM play_mode = ARCOMMANDS_ANIMATION_PLAY_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureAnimation.ARCONTROLLER_DICTIONARY_KEY_ANIMATION_DOLLYSLIDESTATE_PLAY_MODE));
        }
    }
}
```

<br/>


* state (enum): Animation state.<br/>
   * idle: The animation is not running.<br/>
   * running: The animation is running.<br/>
   * canceling: The current animation is canceling.<br/>
* speed (float): Speed in m/s.<br/>
(only accurate if state is not idle)<br/>
* angle (float): Drone-target-destination angle in rad.<br/>
(only accurate if state is not idle)<br/>
* horizontal_distance (float): Horizontal distance in m.<br/>
(only accurate if state is not idle)<br/>
* play_mode (enum): Animation play mode.<br/>
   * normal: Animation is played once, normally.<br/>
   * once_then_mirrored: Animation is played once and then the animation is played mirrored.<br/>


Triggered by [StartDollySlide](#animation-start_dolly_slide) and when the state changes.<br/>



*Supported by <br/>*

- *Bebop 2 since 4.3.0*<br/>


<br/>

