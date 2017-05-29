<!-- drone_manager-drone_list_item-->
### <a name="drone_manager-drone_list_item">Drone list item</a><br/>
> Drone list item:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_SERIAL, arg);
                if (arg != NULL)
                {
                    char * serial = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_MODEL, arg);
                if (arg != NULL)
                {
                    uint16_t model = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_NAME, arg);
                if (arg != NULL)
                {
                    char * name = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_CONNECTION_ORDER, arg);
                if (arg != NULL)
                {
                    uint8_t connection_order = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_ACTIVE, arg);
                if (arg != NULL)
                {
                    uint8_t active = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_VISIBLE, arg);
                if (arg != NULL)
                {
                    uint8_t visible = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_SECURITY, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_DRONE_MANAGER_SECURITY security = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_HAS_SAVED_KEY, arg);
                if (arg != NULL)
                {
                    uint8_t has_saved_key = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_RSSI, arg);
                if (arg != NULL)
                {
                    int8_t rssi = arg->value.I8;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_SERIAL, arg);
                if (arg != NULL)
                {
                    char * serial = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_MODEL, arg);
                if (arg != NULL)
                {
                    uint16_t model = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_NAME, arg);
                if (arg != NULL)
                {
                    char * name = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_CONNECTION_ORDER, arg);
                if (arg != NULL)
                {
                    uint8_t connection_order = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_ACTIVE, arg);
                if (arg != NULL)
                {
                    uint8_t active = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_VISIBLE, arg);
                if (arg != NULL)
                {
                    uint8_t visible = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_SECURITY, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_DRONE_MANAGER_SECURITY security = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_HAS_SAVED_KEY, arg);
                if (arg != NULL)
                {
                    uint8_t has_saved_key = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_RSSI, arg);
                if (arg != NULL)
                {
                    int8_t rssi = arg->value.I8;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    String serial = (String)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_SERIAL);
                    short model = (short)((Integer)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_MODEL)).intValue();
                    String name = (String)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_NAME);
                    byte connection_order = (byte)((Integer)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_CONNECTION_ORDER)).intValue();
                    byte active = (byte)((Integer)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_ACTIVE)).intValue();
                    byte visible = (byte)((Integer)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_VISIBLE)).intValue();
                    ARCOMMANDS_DRONE_MANAGER_SECURITY_ENUM security = ARCOMMANDS_DRONE_MANAGER_SECURITY_ENUM.getFromValue((Integer)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_SECURITY));
                    byte has_saved_key = (byte)((Integer)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_HAS_SAVED_KEY)).intValue();
                    byte rssi = (byte)((Integer)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_DRONELISTITEM_RSSI)).intValue();
                }
            }
        } else {
            // list is empty
        }
    }
}
```

Item describing a drone.<br/>


* serial (string): Serial number of the drone.<br/>
* model (u16): Model id of the drone.<br/>
* name (string): Name (SSID) of the drone.<br/>
* connection_order (u8): 0 if the drone is unknwon (never connected).<br/>
Else, order of last connection (1 = most recent)<br/>
* active (u8): 1 if the drone is active (the drone manager tries to connect or is connected to it)<br/>
0 if the drone is not the active one.<br/>
* visible (u8): 1 if the drone is currently visible, 0 otherwise.<br/>
* security (enum): The security of the drone network.<br/>
   * none: The drone is not protected.<br/>
   * wpa2: The drone is protected with Wpa2 (passphrase).<br/>
* has_saved_key (u8): 1 if the drone manager has a saved security key for the drone, 0 otherwise.<br/>
If security method is not 'none', and this value is 0, then the controller should prompt the user for a passphrase before sending a connect.<br/>
* rssi (i8): The drone rssi (wifi signal strength estimation).<br/>
The value is meaningless if the drone is not visible.<br/>


Triggered when requested [discover_drones](#drone_manager-discover_drones).<br/>



*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- drone_manager-connection_state-->
### <a name="drone_manager-connection_state">State of the connection</a><br/>
> State of the connection:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_DRONE_MANAGER_CONNECTION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE_SERIAL, arg);
            if (arg != NULL)
            {
                char * serial = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE_MODEL, arg);
            if (arg != NULL)
            {
                uint16_t model = arg->value.U16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE_NAME, arg);
            if (arg != NULL)
            {
                char * name = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE_STATE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_DRONE_MANAGER_CONNECTION_STATE state = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE_SERIAL, arg);
            if (arg != NULL)
            {
                char * serial = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE_MODEL, arg);
            if (arg != NULL)
            {
                uint16_t model = arg->value.U16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE_NAME, arg);
            if (arg != NULL)
            {
                char * name = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_DRONE_MANAGER_CONNECTION_STATE_ENUM state = ARCOMMANDS_DRONE_MANAGER_CONNECTION_STATE_ENUM.getFromValue((Integer)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE_STATE));
            String serial = (String)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE_SERIAL);
            short model = (short)((Integer)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE_MODEL)).intValue();
            String name = (String)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONSTATE_NAME);
        }
    }
}
```

State of the connection.<br/>


* state (enum): The state of the connection to a drone.<br/>
   * idle: The drone manager do nothing (wait for command).<br/>
   * searching: The drone manager is searching for a known drone.<br/>
   * connecting: The drone manager is connecting to a drone.<br/>
   * connected: The drone manager is connected to a drone.<br/>
   * disconnecting: The drone manager is finishing the connection with the drone before taking further action.<br/>
* serial (string): Serial number of the drone.<br/>
* model (u16): Model id of the drone.<br/>
* name (string): Name (SSID) of the drone.<br/>


Triggered when the state changes.<br/>

If the state is 'searching', all informations about the drone will refer to the last connected drone.<br/>

Otherwise, these informations will refer to the active drone.<br/>



*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- drone_manager-authentication_failed-->
### <a name="drone_manager-authentication_failed">Authentication failed</a><br/>
> Authentication failed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_AUTHENTICATIONFAILED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_AUTHENTICATIONFAILED_SERIAL, arg);
            if (arg != NULL)
            {
                char * serial = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_AUTHENTICATIONFAILED_MODEL, arg);
            if (arg != NULL)
            {
                uint16_t model = arg->value.U16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_AUTHENTICATIONFAILED_NAME, arg);
            if (arg != NULL)
            {
                char * name = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_AUTHENTICATIONFAILED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_AUTHENTICATIONFAILED_SERIAL, arg);
            if (arg != NULL)
            {
                char * serial = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_AUTHENTICATIONFAILED_MODEL, arg);
            if (arg != NULL)
            {
                uint16_t model = arg->value.U16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_AUTHENTICATIONFAILED_NAME, arg);
            if (arg != NULL)
            {
                char * name = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_AUTHENTICATIONFAILED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            String serial = (String)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_AUTHENTICATIONFAILED_SERIAL);
            short model = (short)((Integer)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_AUTHENTICATIONFAILED_MODEL)).intValue();
            String name = (String)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_AUTHENTICATIONFAILED_NAME);
        }
    }
}
```

Authentication failed because of a wrong key (passphrase).<br/>


* serial (string): Serial number of the drone.<br/>
* model (u16): Model id of the drone.<br/>
* name (string): Name (SSID) of the drone.<br/>


Triggered when trying to [connect](#drone_manager-connect) to a protected drone with a wrong key (passphrase)<br/>



*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- drone_manager-connection_refused-->
### <a name="drone_manager-connection_refused">Connection refused</a><br/>
> Connection refused:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONREFUSED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONREFUSED_SERIAL, arg);
            if (arg != NULL)
            {
                char * serial = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONREFUSED_MODEL, arg);
            if (arg != NULL)
            {
                uint16_t model = arg->value.U16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONREFUSED_NAME, arg);
            if (arg != NULL)
            {
                char * name = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONREFUSED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONREFUSED_SERIAL, arg);
            if (arg != NULL)
            {
                char * serial = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONREFUSED_MODEL, arg);
            if (arg != NULL)
            {
                uint16_t model = arg->value.U16;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONREFUSED_NAME, arg);
            if (arg != NULL)
            {
                char * name = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONREFUSED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            String serial = (String)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONREFUSED_SERIAL);
            short model = (short)((Integer)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONREFUSED_MODEL)).intValue();
            String name = (String)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_CONNECTIONREFUSED_NAME);
        }
    }
}
```

Connection refused by the drone because another peer is already connected to.<br/>


* serial (string): Serial number of the drone.<br/>
* model (u16): Model id of the drone.<br/>
* name (string): Name (SSID) of the drone.<br/>


Triggered Try to [connect](#drone_manager-connect) to a drone where another peer is already connected to.<br/>



*Supported by <br/>*

- *SkyController 2*<br/>


<br/>

<!-- drone_manager-known_drone_item-->
### <a name="drone_manager-known_drone_item">Known drone item</a><br/>
> Known drone item:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_SERIAL, arg);
                if (arg != NULL)
                {
                    char * serial = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_MODEL, arg);
                if (arg != NULL)
                {
                    uint16_t model = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_NAME, arg);
                if (arg != NULL)
                {
                    char * name = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_SECURITY, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_DRONE_MANAGER_SECURITY security = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_HAS_SAVED_KEY, arg);
                if (arg != NULL)
                {
                    uint8_t has_saved_key = arg->value.U8;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_SERIAL, arg);
                if (arg != NULL)
                {
                    char * serial = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_MODEL, arg);
                if (arg != NULL)
                {
                    uint16_t model = arg->value.U16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_NAME, arg);
                if (arg != NULL)
                {
                    char * name = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_SECURITY, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_DRONE_MANAGER_SECURITY security = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_HAS_SAVED_KEY, arg);
                if (arg != NULL)
                {
                    uint8_t has_saved_key = arg->value.U8;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    String serial = (String)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_SERIAL);
                    short model = (short)((Integer)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_MODEL)).intValue();
                    String name = (String)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_NAME);
                    ARCOMMANDS_DRONE_MANAGER_SECURITY_ENUM security = ARCOMMANDS_DRONE_MANAGER_SECURITY_ENUM.getFromValue((Integer)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_SECURITY));
                    byte has_saved_key = (byte)((Integer)args.get(ARFeatureDroneManager.ARCONTROLLER_DICTIONARY_KEY_DRONE_MANAGER_KNOWNDRONEITEM_HAS_SAVED_KEY)).intValue();
                }
            }
        } else {
            // list is empty
        }
    }
}
```

Item describing a known drone (already connected).<br/>


* serial (string): Serial number of the drone.<br/>
* model (u16): Model id of the drone.<br/>
* name (string): Last visible Name (SSID) of the drone.<br/>
* security (enum): The security of the drone network.<br/>
   * none: The drone is not protected.<br/>
   * wpa2: The drone is protected with Wpa2 (passphrase).<br/>
* has_saved_key (u8): 1 if the drone manager has a saved security key for the drone, 0 otherwise.<br/>
If security method is not 'none', and this value is 0, then the controller should prompt the user for a passphrase before sending a connect.<br/>


Triggered when [AllSettings](#SkyController-Settings-AllSettings) is requested or when a drone is forgotten or connected for the first time.<br/>



*Supported by <br/>*

- *SkyController 2 since 1.0.3*<br/>


<br/>

