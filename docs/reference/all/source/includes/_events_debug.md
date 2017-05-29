<!-- debug-settings_info-->
### <a name="debug-settings_info">Sent by the drone as answer to get_settings_info</a><br/>
> Sent by the drone as answer to get_settings_info:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_ID, arg);
                if (arg != NULL)
                {
                    uint16_t id = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_LABEL, arg);
                if (arg != NULL)
                {
                    char * label = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_TYPE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_DEBUG_SETTING_TYPE type = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_MODE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_DEBUG_SETTING_MODE mode = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_RANGE_MIN, arg);
                if (arg != NULL)
                {
                    char * range_min = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_RANGE_MAX, arg);
                if (arg != NULL)
                {
                    char * range_max = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_RANGE_STEP, arg);
                if (arg != NULL)
                {
                    char * range_step = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_VALUE, arg);
                if (arg != NULL)
                {
                    char * value = arg->value.String;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_ID, arg);
                if (arg != NULL)
                {
                    uint16_t id = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_LABEL, arg);
                if (arg != NULL)
                {
                    char * label = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_TYPE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_DEBUG_SETTING_TYPE type = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_MODE, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_DEBUG_SETTING_MODE mode = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_RANGE_MIN, arg);
                if (arg != NULL)
                {
                    char * range_min = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_RANGE_MAX, arg);
                if (arg != NULL)
                {
                    char * range_max = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_RANGE_STEP, arg);
                if (arg != NULL)
                {
                    char * range_step = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_VALUE, arg);
                if (arg != NULL)
                {
                    char * value = arg->value.String;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    short id = (short)((Integer)args.get(ARFeatureDebug.ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_ID)).intValue();
                    String label = (String)args.get(ARFeatureDebug.ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_LABEL);
                    ARCOMMANDS_DEBUG_SETTING_TYPE_ENUM type = ARCOMMANDS_DEBUG_SETTING_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureDebug.ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_TYPE));
                    ARCOMMANDS_DEBUG_SETTING_MODE_ENUM mode = ARCOMMANDS_DEBUG_SETTING_MODE_ENUM.getFromValue((Integer)args.get(ARFeatureDebug.ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_MODE));
                    String range_min = (String)args.get(ARFeatureDebug.ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_RANGE_MIN);
                    String range_max = (String)args.get(ARFeatureDebug.ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_RANGE_MAX);
                    String range_step = (String)args.get(ARFeatureDebug.ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_RANGE_STEP);
                    String value = (String)args.get(ARFeatureDebug.ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSINFO_VALUE);
                }
            }
        } else {
            // list is empty
        }
    }
}
```

Sent by the drone as answer to get_settings_info<br/>
Describe a debug setting and give the current value.<br/>


* id (u16): Setting Id.<br/>
* label (string): Setting displayed label (single line).<br/>
* type (enum): Setting type.<br/>
   * BOOL: Boolean Setting. (ex: 0, 1)<br/>
   * DECIMAL: Decimal Setting. (ex: -3.5, 0, 2, 3.6, 6.5)<br/>
   * TEXT: Single line text Setting.<br/>
* mode (enum): Setting mode.<br/>
   * READ_ONLY: Controller can only read setting.<br/>
   * READ_WRITE: Controller can read and write setting.<br/>
* range_min (string): Setting range minimal value for decimal type.<br/>
* range_max (string): Setting range max value for decimal type.<br/>
* range_step (string): Setting step value for decimal type<br/>
* value (string): Current Setting value (string encoded).<br/>
<br/>

<!-- debug-settings_list-->
### <a name="debug-settings_list">Setting value changed.</a><br/>
> Setting value changed.:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSLIST) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSLIST_ID, arg);
            if (arg != NULL)
            {
                uint16_t id = arg->value.U16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSLIST_VALUE, arg);
            if (arg != NULL)
            {
                char * value = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSLIST) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSLIST_ID, arg);
            if (arg != NULL)
            {
                uint16_t id = arg->value.U16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSLIST_VALUE, arg);
            if (arg != NULL)
            {
                char * value = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSLIST) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            short id = (short)((Integer)args.get(ARFeatureDebug.ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSLIST_ID)).intValue();
            String value = (String)args.get(ARFeatureDebug.ARCONTROLLER_DICTIONARY_KEY_DEBUG_SETTINGSLIST_VALUE);
        }
    }
}
```

Setting value changed.<br/>
Cmd sent by drone when setting changed occurred.<br/>


* id (u16): Setting Id.<br/>
* value (string): New setting value (string encoded).<br/>
<br/>

