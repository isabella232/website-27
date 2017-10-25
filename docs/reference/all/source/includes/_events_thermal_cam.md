<!-- thermal_cam-camera_state-->
### <a name="thermal_cam-camera_state">Camera state</a><br/>
> Camera state:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CAMERASTATE)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CAMERASTATE_CAM_ID, arg);
                if (arg != NULL)
                {
                    uint8_t cam_id = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CAMERASTATE_STATE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_THERMAL_CAM_STATE state = arg->value.I32;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CAMERASTATE)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CAMERASTATE_CAM_ID, arg);
                if (arg != NULL)
                {
                    uint8_t cam_id = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CAMERASTATE_STATE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_THERMAL_CAM_STATE state = arg->value.I32;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CAMERASTATE){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    byte cam_id = (byte)((Integer)args.get(ARFeatureThermalCam.ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CAMERASTATE_CAM_ID)).intValue();
                    ARCOMMANDS_THERMAL_CAM_STATE_ENUM state = ARCOMMANDS_THERMAL_CAM_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureThermalCam.ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CAMERASTATE_STATE));
                }
            }
        } else {
            // list is empty
        }
    }
}
```

Camera state.<br/>


* cam_id (u8): Thermal camera id, as given in the [connected accessories](#1-33-0) event.<br/>
* state (enum): Camera state<br/>
   * activated: Camera is activated<br/>
   * deactivated: Camera is deactivated<br/>
   * pending: Activation is pending<br/>


Triggered by [Activate](#thermal_cam-activate) or [Deactivate](#thermal_cam-deactivate).<br/>



*Supported by <br/>*

- *no product*<br/>


<br/>

<!-- thermal_cam-sensitivity-->
### <a name="thermal_cam-sensitivity">Thermal cam sensitivity</a><br/>
> Thermal cam sensitivity:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_SENSITIVITY)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_SENSITIVITY_CAM_ID, arg);
                if (arg != NULL)
                {
                    uint8_t cam_id = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_SENSITIVITY_CURRENT_RANGE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_THERMAL_CAM_RANGE current_range = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_SENSITIVITY_AVAILABLE_RANGES, arg);
                if (arg != NULL)
                {
                    uint8_t available_ranges = arg->value.U8;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_SENSITIVITY)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_SENSITIVITY_CAM_ID, arg);
                if (arg != NULL)
                {
                    uint8_t cam_id = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_SENSITIVITY_CURRENT_RANGE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_THERMAL_CAM_RANGE current_range = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_SENSITIVITY_AVAILABLE_RANGES, arg);
                if (arg != NULL)
                {
                    uint8_t available_ranges = arg->value.U8;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_SENSITIVITY){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    byte cam_id = (byte)((Integer)args.get(ARFeatureThermalCam.ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_SENSITIVITY_CAM_ID)).intValue();
                    ARCOMMANDS_THERMAL_CAM_RANGE_ENUM current_range = ARCOMMANDS_THERMAL_CAM_RANGE_ENUM.getFromValue((Integer)args.get(ARFeatureThermalCam.ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_SENSITIVITY_CURRENT_RANGE));
                    byte available_ranges = (byte)((Integer)args.get(ARFeatureThermalCam.ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_SENSITIVITY_AVAILABLE_RANGES)).intValue();
                }
            }
        } else {
            // list is empty
        }
    }
}
```

Thermal cam sensitivity range.<br/>


* cam_id (u8): Thermal camera id, as given in the [connected accessories](#1-33-0) event.<br/>
* current_range (enum): Thermal range<br/>
   * high: High range (from 0 to 400°C)<br/>
   * low: Low range (from 0 to 120°C)<br/>
* available_ranges (bitfield as u8): Thermal range<br/>
   * high: High range (from 0 to 400°C)<br/>
   * low: Low range (from 0 to 120°C)<br/>


Triggered by [SetSensitivity](#thermal_cam-set_sensitivity)<br/>



*Supported by <br/>*

- *no product*<br/>


<br/>

<!-- thermal_cam-calibration_infos-->
### <a name="thermal_cam-calibration_infos">Thermal cam calibration informations</a><br/>
> Thermal cam calibration informations:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS_CAM_ID, arg);
                if (arg != NULL)
                {
                    uint8_t cam_id = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS_ROLL, arg);
                if (arg != NULL)
                {
                    float roll = arg->value.Float;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS_PITCH, arg);
                if (arg != NULL)
                {
                    float pitch = arg->value.Float;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS_YAW, arg);
                if (arg != NULL)
                {
                    float yaw = arg->value.Float;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS_CAM_ID, arg);
                if (arg != NULL)
                {
                    uint8_t cam_id = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS_ROLL, arg);
                if (arg != NULL)
                {
                    float roll = arg->value.Float;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS_PITCH, arg);
                if (arg != NULL)
                {
                    float pitch = arg->value.Float;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS_YAW, arg);
                if (arg != NULL)
                {
                    float yaw = arg->value.Float;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    byte cam_id = (byte)((Integer)args.get(ARFeatureThermalCam.ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS_CAM_ID)).intValue();
                    float roll = (float)((Double)args.get(ARFeatureThermalCam.ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS_ROLL)).doubleValue();
                    float pitch = (float)((Double)args.get(ARFeatureThermalCam.ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS_PITCH)).doubleValue();
                    float yaw = (float)((Double)args.get(ARFeatureThermalCam.ARCONTROLLER_DICTIONARY_KEY_THERMAL_CAM_CALIBRATIONINFOS_YAW)).doubleValue();
                }
            }
        } else {
            // list is empty
        }
    }
}
```

Visible camera position relative to the drone. The thermal camera is considered at an ideal position.<br/>


* cam_id (u8): Thermal camera id, as given in the [connected accessories](#1-33-0) event.<br/>
* roll (float): Euler angle roll in degree difference between visible cam and thermal cam.<br/>
* pitch (float): Euler angle pitch in degree difference between visible cam and thermal cam.<br/>
* yaw (float): Euler angle yaw in degree difference between visible cam and thermal cam.<br/>


Triggered at connection or when the thermal cam is connected.<br/>



*Supported by <br/>*

- *no product*<br/>


<br/>

