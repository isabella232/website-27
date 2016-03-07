<!-- SkyController-WifiState-WifiList-->
### <a name="SkyController-WifiState-WifiList">Visible wifi networks</a><br/>
> Visible wifi networks:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_BSSID, arg);
            if (arg != NULL)
            {
                char * bssid = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_SSID, arg);
            if (arg != NULL)
            {
                char * ssid = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_SECURED, arg);
            if (arg != NULL)
            {
                uint8_t secured = arg->value.U8;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_SAVED, arg);
            if (arg != NULL)
            {
                uint8_t saved = arg->value.U8;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_RSSI, arg);
            if (arg != NULL)
            {
                int32_t rssi = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_FREQUENCY, arg);
            if (arg != NULL)
            {
                int32_t frequency = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_BSSID, arg);
            if (arg != NULL)
            {
                char * bssid = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_SSID, arg);
            if (arg != NULL)
            {
                char * ssid = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_SECURED, arg);
            if (arg != NULL)
            {
                uint8_t secured = arg->value.U8;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_SAVED, arg);
            if (arg != NULL)
            {
                uint8_t saved = arg->value.U8;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_RSSI, arg);
            if (arg != NULL)
            {
                int32_t rssi = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_FREQUENCY, arg);
            if (arg != NULL)
            {
                int32_t frequency = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST) && (elementDictionary != null)){
        Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
        while (itr.hasNext()) {
            ARControllerArgumentDictionary<Object> args = itr.next();
            if (args != null) {
                String bssid = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_BSSID);
                String ssid = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_SSID);
                byte secured = (byte)((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_SECURED)).intValue();
                byte saved = (byte)((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_SAVED)).intValue();
                int rssi = (int)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_RSSI);
                int frequency = (int)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFILIST_FREQUENCY);
            }
        }
    }
}
```

Return the available wifi list<br/>

* bssid (string): Wifi bssid<br/>
* ssid (string): Wifi ssid<br/>
* secured (u8): Is wifi secured by passphrase<br/>
* saved (u8): Is wifi saved in terminal<br/>
* rssi (i32): Wifi rssi<br/>
* frequency (i32): Wifi frequency<br/>

Triggered for each visible wifi network after a [RequestWifiList](#SkyController-Wifi-RequestWifiList) command.<br/>

<br/>

<!-- SkyController-WifiState-ConnexionChanged-->
### <a name="SkyController-WifiState-ConnexionChanged">Wifi connexion status</a><br/>
> Wifi connexion status:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_CONNEXIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_CONNEXIONCHANGED_SSID, arg);
            if (arg != NULL)
            {
                char * ssid = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_CONNEXIONCHANGED_STATUS, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_WIFISTATE_CONNEXIONCHANGED_STATUS status = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_CONNEXIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_CONNEXIONCHANGED_SSID, arg);
            if (arg != NULL)
            {
                char * ssid = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_CONNEXIONCHANGED_STATUS, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_WIFISTATE_CONNEXIONCHANGED_STATUS status = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_CONNEXIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            String ssid = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_CONNEXIONCHANGED_SSID);
            ARCOMMANDS_SKYCONTROLLER_WIFISTATE_CONNEXIONCHANGED_STATUS_ENUM status = ARCOMMANDS_SKYCONTROLLER_WIFISTATE_CONNEXIONCHANGED_STATUS_ENUM.getFromValue((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_CONNEXIONCHANGED_STATUS));
        }
    }
}
```

Return connexion status<br/>

* ssid (string): Wifi ssid<br/>
* status (enum): Wifi status<br/>
   * connected: Connected<br/>
   * error: Error<br/>
   * disconnected: Disconnected<br/>

Triggered by each connection status change, or the [RequestCurrentWifi](#SkyController-Wifi-RequestCurrentWifi) command.<br/>

If status is `disconnected`, then the ssid argument is meaningless (and can be anything).

<br/>

<!-- SkyController-WifiState-WifiAuthChannelListChanged-->
### <a name="SkyController-WifiState-WifiAuthChannelListChanged">List authorized wifi channels</a><br/>
> List authorized wifi channels:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED_BAND, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED_BAND band = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED_CHANNEL, arg);
            if (arg != NULL)
            {
                uint8_t channel = arg->value.U8;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED_IN_OR_OUT, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED_BAND, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED_BAND band = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED_CHANNEL, arg);
            if (arg != NULL)
            {
                uint8_t channel = arg->value.U8;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED_IN_OR_OUT, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED) && (elementDictionary != null)){
        Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
        while (itr.hasNext()) {
            ARControllerArgumentDictionary<Object> args = itr.next();
            if (args != null) {
                ARCOMMANDS_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED_BAND_ENUM band = ARCOMMANDS_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED_BAND_ENUM.getFromValue((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED_BAND));
                byte channel = (byte)((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED_CHANNEL)).intValue();
                byte in_or_out = (byte)((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFIAUTHCHANNELLISTCHANGED_IN_OR_OUT)).intValue();
            }
        }
    }
}
```

Notify of an Authorized Channel<br/>

* band (enum): The band of this channel : 2.4 GHz or 5 GHz<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
* channel (u8): The authorized channel<br/>
* in_or_out (u8): Bitfield:
   * Bit 0 is 1 if channel is authorized outside (0 otherwise)
   * Bit 1 is 1 if channel is authorized inside (0 otherwise)<br/>
<br/>

Triggered by the [WifiAuthChannel](#SkyController-Wifi-WifiAuthChannel) command. The list of events is followed by an [AllWifiAuthChannelChanged](#SkyController-WifiState-AllWifiAuthChannelChanged) event.

<!-- SkyController-WifiState-AllWifiAuthChannelChanged-->
### <a name="SkyController-WifiState-AllWifiAuthChannelChanged">End of authorized wifi channel list</a><br/>
> End of authorized wifi channel list:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_ALLWIFIAUTHCHANNELCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_ALLWIFIAUTHCHANNELCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_ALLWIFIAUTHCHANNELCHANGED) && (elementDictionary != null)){

    }
}
```

Notify the end of the list of Authorized wifi Channel<br/>

Closes the list of [WifiAuthChannelListChanged](#SkyController-WifiState-WifiAuthChannelListChanged) events.

<br/>

<!-- SkyController-WifiState-WifiSignalChanged-->
### <a name="SkyController-WifiState-WifiSignalChanged">Wifi signal strength</a><br/>
> Wifi signal strength:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFISIGNALCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFISIGNALCHANGED_LEVEL, arg);
            if (arg != NULL)
            {
                uint8_t level = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFISIGNALCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFISIGNALCHANGED_LEVEL, arg);
            if (arg != NULL)
            {
                uint8_t level = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFISIGNALCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte level = (byte)((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_WIFISTATE_WIFISIGNALCHANGED_LEVEL)).intValue();
        }
    }
}
```

State of the wifi signal<br/>

* level (u8): Level of the signal. Levels are from 0 to 5. 0 is an unknown value. 1 is a weak wifi signal, 5 is the best.<br/>

Sent each time the wifi level is updated.<br/>

The wifi level correspond to the number of activated LEDs on the SkyController left arm:

* 0: Not connected (one red led)
* 1: Weakest (blinking red)
* 2 to 5: Standard levels (1 to 4 white led)


<br/>

<!-- SkyController-DeviceState-DeviceList-->
### <a name="SkyController-DeviceState-DeviceList">Available devices list</a><br/>
> Available devices list (deprecated):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_DEVICELIST) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_DEVICELIST_NAME, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_DEVICELIST) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_DEVICELIST_NAME, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_DEVICELIST) && (elementDictionary != null)){
        Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
        while (itr.hasNext()) {
            ARControllerArgumentDictionary<Object> args = itr.next();
            if (args != null) {
                String name = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_DEVICELIST_NAME);
            }
        }
    }
}
```

Return the available Device list<br/>

* name (string): Device name<br/>

Deprecated event, do not use.

<br/>

<!-- SkyController-DeviceState-ConnexionChanged-->
### <a name="SkyController-DeviceState-ConnexionChanged">Device connexion status</a><br/>
> Device connexion status:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED_STATUS, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED_STATUS status = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED_DEVICENAME, arg);
            if (arg != NULL)
            {
                char * deviceName = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED_DEVICEPRODUCTID, arg);
            if (arg != NULL)
            {
                uint16_t deviceProductID = arg->value.U16;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED_STATUS, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED_STATUS status = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED_DEVICENAME, arg);
            if (arg != NULL)
            {
                char * deviceName = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED_DEVICEPRODUCTID, arg);
            if (arg != NULL)
            {
                uint16_t deviceProductID = arg->value.U16;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED_STATUS_ENUM status = ARCOMMANDS_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED_STATUS_ENUM.getFromValue((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED_STATUS));
            String deviceName = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED_DEVICENAME);
            short deviceProductID = (short)((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_DEVICESTATE_CONNEXIONCHANGED_DEVICEPRODUCTID)).intValue();
        }
    }
}
```

Return device connexion status<br/>

* status (enum): Wifi status to Device<br/>
   * notConnected: Not Connected<br/>
   * connecting: Connecting to Device<br/>
   * connected: Connected to Device<br/>
   * disconnecting: Disconnecting from Device<br/>
* deviceName (string): Device name<br/>
* deviceProductID (u16): Device name<br/>

Triggered when the connection status to a drone changes.<br/>

**This event triggers the [extensionStateChangedCallback](#create_device_controller) of the DeviceController, and should be handled by this callback only if you use the libARController API**<br/>

<br/>

<!-- SkyController-SettingsState-AllSettingsChanged-->
### <a name="SkyController-SettingsState-AllSettingsChanged">All settings has been sent</a><br/>
> All settings has been sent:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_ALLSETTINGSCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_ALLSETTINGSCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_ALLSETTINGSCHANGED) && (elementDictionary != null)){

    }
}
```

State sent when all settings has been sent<br/>

All settings have been sent.<br/>

**Please note that you should not care about this event if you are using the libARController API as this library is handling the connection process for you.**<br/>

<br/>

<!-- SkyController-SettingsState-ResetChanged-->
### <a name="SkyController-SettingsState-ResetChanged">All settings has been reset</a><br/>
> All settings has been reset (deprecated):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_RESETCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_RESETCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_RESETCHANGED) && (elementDictionary != null)){

    }
}
```

All settings has been reset<br/>

Deprecated event, do not use.

<br/>

<!-- SkyController-SettingsState-ProductSerialChanged-->
### <a name="SkyController-SettingsState-ProductSerialChanged">Product serial number</a><br/>
> Product serial number:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_PRODUCTSERIALCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_PRODUCTSERIALCHANGED_SERIALNUMBER, arg);
            if (arg != NULL)
            {
                char * serialNumber = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_PRODUCTSERIALCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_PRODUCTSERIALCHANGED_SERIALNUMBER, arg);
            if (arg != NULL)
            {
                char * serialNumber = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_PRODUCTSERIALCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            String serialNumber = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_PRODUCTSERIALCHANGED_SERIALNUMBER);
        }
    }
}
```

Product serial number<br/>

* serialNumber (string): Serial number (hexadecimal value)<br/>

Triggered by the [AllStates](#SkyController-Common-AllStates) command.<br/>

<br/>

<!-- SkyController-SettingsState-ProductVariantChanged-->
### <a name="SkyController-SettingsState-ProductVariantChanged">Variant of SkyController</a><br/>
> Variant of SkyController:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_PRODUCTVARIANTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_PRODUCTVARIANTCHANGED_VARIANT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_SETTINGSSTATE_PRODUCTVARIANTCHANGED_VARIANT variant = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_PRODUCTVARIANTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_PRODUCTVARIANTCHANGED_VARIANT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_SETTINGSSTATE_PRODUCTVARIANTCHANGED_VARIANT variant = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_PRODUCTVARIANTCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_SKYCONTROLLER_SETTINGSSTATE_PRODUCTVARIANTCHANGED_VARIANT_ENUM variant = ARCOMMANDS_SKYCONTROLLER_SETTINGSSTATE_PRODUCTVARIANTCHANGED_VARIANT_ENUM.getFromValue((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SETTINGSSTATE_PRODUCTVARIANTCHANGED_VARIANT));
        }
    }
}
```

Product variant of SkyController<br/>

* variant (enum): Variant of the product<br/>
   * bebop: SkyController of the bebop generation. (Bebop battery, and original key layout)<br/>
   * bebop2: SkyController of the bebop2 generation. (Bebop2 battery, and updated key layout)<br/>

Triggered by the [AllStates](#SkyController-Common-AllStates) command.<br/>
*Only supported on 1.6 or newer firmwares. Older versions are always of the* `bebop` *variant.*<br/>

<br/>

<!-- SkyController-CommonState-AllStatesChanged-->
### <a name="SkyController-CommonState-AllStatesChanged">All states has been sent</a><br/>
> All states has been sent:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_COMMONSTATE_ALLSTATESCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_COMMONSTATE_ALLSTATESCHANGED) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_COMMONSTATE_ALLSTATESCHANGED) && (elementDictionary != null)){

    }
}
```

State sent when all product states has been sent<br/>

All product states have been sent.<br/>

**Please note that you should not care about this event if you are using the libARController API as this library is handling the connection process for you.**<br/>

<br/>

<!-- SkyController-SkyControllerState-BatteryChanged-->
### <a name="SkyController-SkyControllerState-BatteryChanged">Battery changed</a><br/>
> Battery changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_BATTERYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_BATTERYCHANGED_PERCENT, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_BATTERYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_BATTERYCHANGED_PERCENT, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_BATTERYCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte percent = (byte)((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_BATTERYCHANGED_PERCENT)).intValue();
        }
    }
}
```

State sent when SkyController battery has changed<br/>

* percent (u8): SkyController battery<br/>

Triggered when the battery level changes.

<br/>

<!-- SkyController-SkyControllerState-GpsFixChanged-->
### <a name="SkyController-SkyControllerState-GpsFixChanged">Gps fix changed</a><br/>
> Gps fix changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSFIXCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSFIXCHANGED_FIXED, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSFIXCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSFIXCHANGED_FIXED, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSFIXCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte fixed = (byte)((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSFIXCHANGED_FIXED)).intValue();
        }
    }
}
```

State sent when SkyController gps fix has changed<br/>

* fixed (u8): SkyController fixed<br/>

Triggered when the gps status changes (fix/unfix).

<br/>

<!-- SkyController-SkyControllerState-GpsPositionChanged-->
### <a name="SkyController-SkyControllerState-GpsPositionChanged">Position changed</a><br/>
> Position changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED_LATITUDE, arg);
            if (arg != NULL)
            {
                double latitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED_LONGITUDE, arg);
            if (arg != NULL)
            {
                double longitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED_ALTITUDE, arg);
            if (arg != NULL)
            {
                double altitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED_HEADING, arg);
            if (arg != NULL)
            {
                float heading = arg->value.Float;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED_LATITUDE, arg);
            if (arg != NULL)
            {
                double latitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED_LONGITUDE, arg);
            if (arg != NULL)
            {
                double longitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED_ALTITUDE, arg);
            if (arg != NULL)
            {
                double altitude = arg->value.Double;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED_HEADING, arg);
            if (arg != NULL)
            {
                float heading = arg->value.Float;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            double latitude = (double)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED_LATITUDE);
            double longitude = (double)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED_LONGITUDE);
            double altitude = (double)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED_ALTITUDE);
            float heading = (float)((Double)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_SKYCONTROLLERSTATE_GPSPOSITIONCHANGED_HEADING)).doubleValue();
        }
    }
}
```

State sent when the SkyController gps position has changed<br/>

* latitude (double): SkyController latitude (500. if not available)<br/>
* longitude (double): SkyController longiture (500. if not available)<br/>
* altitude (double): Altitude (in meters) above sea level<br/>
Only meaningful if latitude and longiture are available<br/>
* heading (float): SkyController heading relative to magnetic north (500.f if not available)<br/>

Triggered when the SkyController position changes.<br/>
Values of 500.f means that the given coordinate is not available:

* latitude & longitude need a gps fix
* altitude is only valid if latitude & longitude are
* heading is available only if the SkyController's magnetometer is calibrated.

<br/>

<!-- SkyController-AccessPointSettingsState-AccessPointSSIDChanged-->
### <a name="SkyController-AccessPointSettingsState-AccessPointSSIDChanged">AccessPoint SSID changed</a><br/>
> AccessPoint SSID changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_ACCESSPOINTSSIDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_ACCESSPOINTSSIDCHANGED_SSID, arg);
            if (arg != NULL)
            {
                char * ssid = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_ACCESSPOINTSSIDCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_ACCESSPOINTSSIDCHANGED_SSID, arg);
            if (arg != NULL)
            {
                char * ssid = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_ACCESSPOINTSSIDCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            String ssid = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_ACCESSPOINTSSIDCHANGED_SSID);
        }
    }
}
```

State sent when AccessPoint ssid has been sent<br/>

* ssid (string): AccessPoint SSID<br/>

Triggered by the [AccessPointSSID](#SkyController-AccessPointSettings-AccessPointSSID) command. The value will only be applied at next reboot.<br/>

*Also triggered by the [AllSettings](#SkyController-Settings-AllSettings) command sent during startup by the libARController API. In this case, it will return the currently applied SSID)*<br/>

<br/>

<!-- SkyController-AccessPointSettingsState-AccessPointChannelChanged-->
### <a name="SkyController-AccessPointSettingsState-AccessPointChannelChanged">AccessPoint channel changed</a><br/>
> AccessPoint channel changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_ACCESSPOINTCHANNELCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_ACCESSPOINTCHANNELCHANGED_CHANNEL, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_ACCESSPOINTCHANNELCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_ACCESSPOINTCHANNELCHANGED_CHANNEL, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_ACCESSPOINTCHANNELCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte channel = (byte)((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_ACCESSPOINTCHANNELCHANGED_CHANNEL)).intValue();
        }
    }
}
```

State sent when AccessPoint channel has been sent<br/>

* channel (u8): AccessPoint Channel<br/>

Sent when the access point channel is changed by the [AccessPointChannel](#SkyController-AccessPointSettings-AccessPointChannel) command.<br/>

**You should not listen to this event, and use the [WifiSelectionChanged](#SkyController-AccessPointSettingsState-WifiSelectionChanged) event instead.**<br/>

<br/>

<!-- SkyController-AccessPointSettingsState-WifiSelectionChanged-->
### <a name="SkyController-AccessPointSettingsState-WifiSelectionChanged">AccessPoint settings changed (band and channel)</a><br/>
> AccessPoint settings changed (band and channel):

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_BAND, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_BAND band = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_CHANNEL, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_BAND, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_BAND band = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_CHANNEL, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE_ENUM type = ARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_TYPE));
            ARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_BAND_ENUM band = ARCOMMANDS_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_BAND_ENUM.getFromValue((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_BAND));
            byte channel = (byte)((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_ACCESSPOINTSETTINGSSTATE_WIFISELECTIONCHANGED_CHANNEL)).intValue();
        }
    }
}
```

Wifi selection from product<br/>

* type (enum): The type of wifi selection (only manual at the moment)<br/>
   * manual: Manual selection<br/>
* band (enum): The allowed band : 2.4 Ghz or 5 Ghz<br/>
   * 2_4ghz: 2.4 GHz band<br/>
   * 5ghz: 5 GHz band<br/>
* channel (u8): The channel<br/>

Triggered by the [WifiSelection](#SkyController-AccessPointSettings-WifiSelection) command.<br/>
Contains all the information about the current access point settings, except for the SSID.<br/>

<br/>

<!-- SkyController-GamepadInfosState-gamepadControl-->
### <a name="SkyController-GamepadInfosState-gamepadControl">List buttons and axis</a><br/>
> List buttons and axis:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL_ID, arg);
            if (arg != NULL)
            {
                int32_t id = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL_NAME, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL_ID, arg);
            if (arg != NULL)
            {
                int32_t id = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL_NAME, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL) && (elementDictionary != null)){
        Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
        while (itr.hasNext()) {
            ARControllerArgumentDictionary<Object> args = itr.next();
            if (args != null) {
                ARCOMMANDS_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL_TYPE_ENUM type = ARCOMMANDS_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL_TYPE));
                int id = (int)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL_ID);
                String name = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_GAMEPADCONTROL_NAME);
            }
        }
    }
}
```

Describe an existing button or axis of the gamepad<br/>

* type (enum): The type (axis/button) of the control<br/>
   * axis: An analog axis (one of the 4 joysticks)<br/>
   * button: A button (including small joystick clicks)<br/>
* id (i32): The button or axis id<br/>
   * note: A button and an axis can have the same ID, but their type is different<br/>
* name (string): Display name for the control<br/>

Triggered by the [getGamepadControls](#SkyController-GamepadInfos-getGamepadControls) commands.<br/>
The list is followed by an [allGamepadControlsSent](#SkyController-GamepadInfosState-allGamepadControlsSent) event.<br/>

<br/>

<!-- SkyController-GamepadInfosState-allGamepadControlsSent-->
### <a name="SkyController-GamepadInfosState-allGamepadControlsSent">End of button/axis list</a><br/>
> End of button/axis list:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_ALLGAMEPADCONTROLSSENT) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_ALLGAMEPADCONTROLSSENT) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_GAMEPADINFOSSTATE_ALLGAMEPADCONTROLSSENT) && (elementDictionary != null)){

    }
}
```

Sent by the SkyController after sending its last 'gamepadControl' command<br/>

Always sent after the last [gamepadControl](#SkyController-GamepadInfosState-gamepadControl) event.

<br/>

<!-- SkyController-ButtonMappingsState-currentButtonMappings-->
### <a name="SkyController-ButtonMappingsState-currentButtonMappings">Current button mappings</a><br/>
> Current button mappings:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_CURRENTBUTTONMAPPINGS) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_CURRENTBUTTONMAPPINGS_KEY_ID, arg);
            if (arg != NULL)
            {
                int32_t key_id = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_CURRENTBUTTONMAPPINGS_MAPPING_UID, arg);
            if (arg != NULL)
            {
                char * mapping_uid = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_CURRENTBUTTONMAPPINGS) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_CURRENTBUTTONMAPPINGS_KEY_ID, arg);
            if (arg != NULL)
            {
                int32_t key_id = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_CURRENTBUTTONMAPPINGS_MAPPING_UID, arg);
            if (arg != NULL)
            {
                char * mapping_uid = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_CURRENTBUTTONMAPPINGS) && (elementDictionary != null)){
        Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
        while (itr.hasNext()) {
            ARControllerArgumentDictionary<Object> args = itr.next();
            if (args != null) {
                int key_id = (int)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_CURRENTBUTTONMAPPINGS_KEY_ID);
                String mapping_uid = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_CURRENTBUTTONMAPPINGS_MAPPING_UID);
            }
        }
    }
}
```

Sent by the SkyController each time a mapping changes<br/>

* key_id (i32): The keycode mapped<br/>
* mapping_uid (string): The mapping associated<br/>

Triggered by the [getCurrentButtonMappings](#SkyController-ButtonMappings-getCurrentButtonMappings), [setButtonMapping](#SkyController-ButtonMappings-setButtonMapping) and [defaultButtonMapping](#SkyController-ButtonMappings-defaultButtonMapping) commands.<br/>
The list is followed by an [allCurrentButtonMappingsSent](#SkyController-ButtonMappingsState-allCurrentButtonMappingsSent) event.

<br/>

<!-- SkyController-ButtonMappingsState-allCurrentButtonMappingsSent-->
### <a name="SkyController-ButtonMappingsState-allCurrentButtonMappingsSent">End of current button mappings list</a><br/>
> End of current button mappings list:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_ALLCURRENTBUTTONMAPPINGSSENT) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_ALLCURRENTBUTTONMAPPINGSSENT) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_ALLCURRENTBUTTONMAPPINGSSENT) && (elementDictionary != null)){

    }
}
```

Sent by the SkyController after sending its last 'currentButtonMappings' command<br/>

Always sent after the last [currentButtonMappings](#SkyController-ButtonMappingsState-currentButtonMappings) event.

<br/>

<!-- SkyController-ButtonMappingsState-availableButtonMappings-->
### <a name="SkyController-ButtonMappingsState-availableButtonMappings">Available button mappings</a><br/>
> Available button mappings:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_AVAILABLEBUTTONMAPPINGS) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_AVAILABLEBUTTONMAPPINGS_MAPPING_UID, arg);
            if (arg != NULL)
            {
                char * mapping_uid = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_AVAILABLEBUTTONMAPPINGS_NAME, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_AVAILABLEBUTTONMAPPINGS) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_AVAILABLEBUTTONMAPPINGS_MAPPING_UID, arg);
            if (arg != NULL)
            {
                char * mapping_uid = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_AVAILABLEBUTTONMAPPINGS_NAME, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_AVAILABLEBUTTONMAPPINGS) && (elementDictionary != null)){
        Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
        while (itr.hasNext()) {
            ARControllerArgumentDictionary<Object> args = itr.next();
            if (args != null) {
                String mapping_uid = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_AVAILABLEBUTTONMAPPINGS_MAPPING_UID);
                String name = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_AVAILABLEBUTTONMAPPINGS_NAME);
            }
        }
    }
}
```

Sent after a 'getAvailableButtonMappings' request<br/>

* mapping_uid (string): The mapping UID (used in communication with the SkyController)<br/>
* name (string): Display name for the user<br/>

Triggered by the [getAvailableButtonMappings](#SkyController-ButtonMappings-getAvailableButtonMappings) command.<br/>
The list is followed by an [allAvailableButtonsMappingsSent](#SkyController-ButtonMappingsState-allAvailableButtonsMappingsSent) event.

<br/>

<!-- SkyController-ButtonMappingsState-allAvailableButtonsMappingsSent-->
### <a name="SkyController-ButtonMappingsState-allAvailableButtonsMappingsSent">End of available button mapping list</a><br/>
> End of available button mapping list:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_ALLAVAILABLEBUTTONSMAPPINGSSENT) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_ALLAVAILABLEBUTTONSMAPPINGSSENT) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONMAPPINGSSTATE_ALLAVAILABLEBUTTONSMAPPINGSSENT) && (elementDictionary != null)){

    }
}
```

Sent by the SkyController after sending its last 'availableButtonMappings' command<br/>

Always sent after the last [availableButtonMappings](#SkyController-ButtonMappingsState-availableButtonMappings) event.

<br/>

<!-- SkyController-AxisMappingsState-currentAxisMappings-->
### <a name="SkyController-AxisMappingsState-currentAxisMappings">Current axis mappings</a><br/>
> Current axis mappings:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_CURRENTAXISMAPPINGS) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_CURRENTAXISMAPPINGS_AXIS_ID, arg);
            if (arg != NULL)
            {
                int32_t axis_id = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_CURRENTAXISMAPPINGS_MAPPING_UID, arg);
            if (arg != NULL)
            {
                char * mapping_uid = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_CURRENTAXISMAPPINGS) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_CURRENTAXISMAPPINGS_AXIS_ID, arg);
            if (arg != NULL)
            {
                int32_t axis_id = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_CURRENTAXISMAPPINGS_MAPPING_UID, arg);
            if (arg != NULL)
            {
                char * mapping_uid = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_CURRENTAXISMAPPINGS) && (elementDictionary != null)){
        Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
        while (itr.hasNext()) {
            ARControllerArgumentDictionary<Object> args = itr.next();
            if (args != null) {
                int axis_id = (int)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_CURRENTAXISMAPPINGS_AXIS_ID);
                String mapping_uid = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_CURRENTAXISMAPPINGS_MAPPING_UID);
            }
        }
    }
}
```

Sent by the SkyController each time a mapping changes<br/>

* axis_id (i32): The axiscode mapped<br/>
* mapping_uid (string): The mapping associated<br/>
<br/>

Triggered by the [getCurrentAxisMappings](#SkyController-AxisMappings-getCurrentAxisMappings), [setAxisMapping](#SkyController-AxisMappings-setAxisMapping) and [defaultAxisMapping](#SkyController-AxisMappings-defaultAxisMapping) commands.
The list is followed by an [allCurrentAxisMappingsSent](#SkyController-AxisMappingsState-allCurrentAxisMappingsSent) event.

<!-- SkyController-AxisMappingsState-allCurrentAxisMappingsSent-->
### <a name="SkyController-AxisMappingsState-allCurrentAxisMappingsSent">End of current axis mapping list</a><br/>
> End of current axis mapping list:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_ALLCURRENTAXISMAPPINGSSENT) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_ALLCURRENTAXISMAPPINGSSENT) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_ALLCURRENTAXISMAPPINGSSENT) && (elementDictionary != null)){

    }
}
```

Sent by the SkyController after sending its last 'currentAxisMappings' command<br/>

Always sent after the last [currentAxisMappings](#SkyController-AxisMappingsState-currentAxisMappings) event.

<br/>

<!-- SkyController-AxisMappingsState-availableAxisMappings-->
### <a name="SkyController-AxisMappingsState-availableAxisMappings">Available axis mappings</a><br/>
> Available axis mappings:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_AVAILABLEAXISMAPPINGS) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_AVAILABLEAXISMAPPINGS_MAPPING_UID, arg);
            if (arg != NULL)
            {
                char * mapping_uid = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_AVAILABLEAXISMAPPINGS_NAME, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_AVAILABLEAXISMAPPINGS) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_AVAILABLEAXISMAPPINGS_MAPPING_UID, arg);
            if (arg != NULL)
            {
                char * mapping_uid = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_AVAILABLEAXISMAPPINGS_NAME, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_AVAILABLEAXISMAPPINGS) && (elementDictionary != null)){
        Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
        while (itr.hasNext()) {
            ARControllerArgumentDictionary<Object> args = itr.next();
            if (args != null) {
                String mapping_uid = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_AVAILABLEAXISMAPPINGS_MAPPING_UID);
                String name = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_AVAILABLEAXISMAPPINGS_NAME);
            }
        }
    }
}
```

Sent after a 'getAvailableAxisMappings' request<br/>

* mapping_uid (string): The mapping UID (used in communication with the SkyController)<br/>
* name (string): Display name for the user<br/>

Triggered by the [getAvailableAxisMappings](#SkyController-AxisMappings-getAvailableAxisMappings) command.<br/>
The list is followed by an [allAvailableAxisMappingsSent](#SkyController-AxisMappingsState-allAvailableAxisMappingsSent) event.

<br/>

<!-- SkyController-AxisMappingsState-allAvailableAxisMappingsSent-->
### <a name="SkyController-AxisMappingsState-allAvailableAxisMappingsSent">End of available axis mapping list</a><br/>
> End of available axis mapping list:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_ALLAVAILABLEAXISMAPPINGSSENT) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_ALLAVAILABLEAXISMAPPINGSSENT) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISMAPPINGSSTATE_ALLAVAILABLEAXISMAPPINGSSENT) && (elementDictionary != null)){

    }
}
```

Sent by the SkyController after sending its last 'availableAxisMappings' command<br/>

Always sent after the last [availableAxisMappings](#SkyController-AxisMappingsState-availableAxisMappings) event.

<br/>

<!-- SkyController-AxisFiltersState-currentAxisFilters-->
### <a name="SkyController-AxisFiltersState-currentAxisFilters">Current axis filters</a><br/>
> Current axis filters:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_CURRENTAXISFILTERS) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_CURRENTAXISFILTERS_AXIS_ID, arg);
            if (arg != NULL)
            {
                int32_t axis_id = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_CURRENTAXISFILTERS_FILTER_UID_OR_BUILDER, arg);
            if (arg != NULL)
            {
                char * filter_uid_or_builder = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_CURRENTAXISFILTERS) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_CURRENTAXISFILTERS_AXIS_ID, arg);
            if (arg != NULL)
            {
                int32_t axis_id = arg->value.I32;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_CURRENTAXISFILTERS_FILTER_UID_OR_BUILDER, arg);
            if (arg != NULL)
            {
                char * filter_uid_or_builder = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_CURRENTAXISFILTERS) && (elementDictionary != null)){
        Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
        while (itr.hasNext()) {
            ARControllerArgumentDictionary<Object> args = itr.next();
            if (args != null) {
                int axis_id = (int)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_CURRENTAXISFILTERS_AXIS_ID);
                String filter_uid_or_builder = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_CURRENTAXISFILTERS_FILTER_UID_OR_BUILDER);
            }
        }
    }
}
```

Sent by the SkyController each time a filter changes<br/>

* axis_id (i32): The axiscode filtered<br/>
* filter_uid_or_builder (string): The filter associated<br/>

Triggered by the [getAvailableAxisMappings](#SkyController-AxisMappings-getAvailableAxisMappings), [setAxisMapping](#SkyController-AxisMappings-setAxisMapping) and [defaultAxisMapping](#SkyController-AxisMappings-defaultAxisMapping) commands.<br/>
The syntax of the builder string is explained in the [setAxisMapping](#SkyController-AxisMappings-setAxisMapping) command documentation.<br/>
The list is followed by an [allCurrentFiltersSent](#SkyController-AxisFiltersState-allCurrentFiltersSent) event.

<br/>

<!-- SkyController-AxisFiltersState-allCurrentFiltersSent-->
### <a name="SkyController-AxisFiltersState-allCurrentFiltersSent">End of current axis filter list</a><br/>
> End of current axis filter list:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_ALLCURRENTFILTERSSENT) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_ALLCURRENTFILTERSSENT) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_ALLCURRENTFILTERSSENT) && (elementDictionary != null)){

    }
}
```

Sent by the SkyController after sending its last 'currentAxisFilters' command<br/>

Always sent after the last [currentAxisFilters](#SkyController-AxisFiltersState-currentAxisFilters) event.

<br/>

<!-- SkyController-AxisFiltersState-presetAxisFilters-->
### <a name="SkyController-AxisFiltersState-presetAxisFilters">Preset axis filters</a><br/>
> Preset axis filters:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_PRESETAXISFILTERS) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_PRESETAXISFILTERS_FILTER_UID, arg);
            if (arg != NULL)
            {
                char * filter_uid = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_PRESETAXISFILTERS_NAME, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_PRESETAXISFILTERS) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
        HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
        {
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_PRESETAXISFILTERS_FILTER_UID, arg);
            if (arg != NULL)
            {
                char * filter_uid = arg->value.String;
            }
            HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_PRESETAXISFILTERS_NAME, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_PRESETAXISFILTERS) && (elementDictionary != null)){
        Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
        while (itr.hasNext()) {
            ARControllerArgumentDictionary<Object> args = itr.next();
            if (args != null) {
                String filter_uid = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_PRESETAXISFILTERS_FILTER_UID);
                String name = (String)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_PRESETAXISFILTERS_NAME);
            }
        }
    }
}
```

Sent after a 'getPresetAxisFilters' request<br/>

* filter_uid (string): The filter UID (used in communication with the SkyController)<br/>
* name (string): Display name for the user<br/>

Triggered by the [getPresetAxisFilters](#SkyController-AxisFilters-getPresetAxisFilters) command.<br/>
The list is followed by an [allPresetFiltersSent](#SkyController-AxisFiltersState-allPresetFiltersSent) event.<br/>

**This list is empty on 1.6.6 firmware, and will probably stay empty in further releases. All filters actually uses the builder syntax described in the [setAxisFilter](#SkyController-AxisFilters-setAxisFilter) command documentation.**<br/>

<br/>

<!-- SkyController-AxisFiltersState-allPresetFiltersSent-->
### <a name="SkyController-AxisFiltersState-allPresetFiltersSent">End of preset axis filter list</a><br/>
> End of preset axis filter list:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_ALLPRESETFILTERSSENT) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_ALLPRESETFILTERSSENT) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_AXISFILTERSSTATE_ALLPRESETFILTERSSENT) && (elementDictionary != null)){

    }
}
```

Sent by the SkyController after sending its last 'presetAxisFilters' command<br/>

Always sent after the last [presetAxisFilters](#SkyController-AxisFiltersState-presetAxisFilters) event.

<br/>

<!-- SkyController-CoPilotingState-pilotingSource-->
### <a name="SkyController-CoPilotingState-pilotingSource">Source of the piloting commands</a><br/>
> Source of the piloting commands:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_COPILOTINGSTATE_PILOTINGSOURCE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_COPILOTINGSTATE_PILOTINGSOURCE_SOURCE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_COPILOTINGSTATE_PILOTINGSOURCE_SOURCE source = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_COPILOTINGSTATE_PILOTINGSOURCE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_COPILOTINGSTATE_PILOTINGSOURCE_SOURCE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_COPILOTINGSTATE_PILOTINGSOURCE_SOURCE source = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_COPILOTINGSTATE_PILOTINGSOURCE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_SKYCONTROLLER_COPILOTINGSTATE_PILOTINGSOURCE_SOURCE_ENUM source = ARCOMMANDS_SKYCONTROLLER_COPILOTINGSTATE_PILOTINGSOURCE_SOURCE_ENUM.getFromValue((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_COPILOTINGSTATE_PILOTINGSOURCE_SOURCE));
        }
    }
}
```

Source of the piloting commands<br/>

* source (enum): The source<br/>
   * SkyController: Use the SkyController joysticks<br/>
   * Controller: Use the Tablet (or smartphone, or whatever) controls. Disables the SkyController joysticks<br/>

Triggered by the [setPilotingSource](#SkyController-CoPiloting-setPilotingSource) command.<br/>

*The piloting source is automatically reset to* `SkyController` *when the controller is no longer connected, so it will always be* `SkyController` *when first queried by an application.*

<br/>

<!-- SkyController-CalibrationState-MagnetoCalibrationState-->
### <a name="SkyController-CalibrationState-MagnetoCalibrationState">State of the magnetometer calibration</a><br/>
> State of the magnetometer calibration:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_STATUS, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_STATUS status = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_X_QUALITY, arg);
            if (arg != NULL)
            {
                uint8_t X_Quality = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_Y_QUALITY, arg);
            if (arg != NULL)
            {
                uint8_t Y_Quality = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_Z_QUALITY, arg);
            if (arg != NULL)
            {
                uint8_t Z_Quality = arg->value.U8;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_STATUS, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_STATUS status = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_X_QUALITY, arg);
            if (arg != NULL)
            {
                uint8_t X_Quality = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_Y_QUALITY, arg);
            if (arg != NULL)
            {
                uint8_t Y_Quality = arg->value.U8;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_Z_QUALITY, arg);
            if (arg != NULL)
            {
                uint8_t Z_Quality = arg->value.U8;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_STATUS_ENUM status = ARCOMMANDS_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_STATUS_ENUM.getFromValue((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_STATUS));
            byte X_Quality = (byte)((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_X_QUALITY)).intValue();
            byte Y_Quality = (byte)((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_Y_QUALITY)).intValue();
            byte Z_Quality = (byte)((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONSTATE_Z_QUALITY)).intValue();
        }
    }
}
```

The current state of the magnetometer calibration<br/>

* status (enum): The global status of the calibration<br/>
   * Unreliable: A calibration is needed<br/>
   * Assessing: A calibration is applied, but still need to be checked<br/>
   * Calibrated: The sensor is properly calibrated<br/>
* X_Quality (u8): Calibration quality on X axis.<br/>
   * 0 is bad, 255 is perfect<br/>
* Y_Quality (u8): Calibration quality on Y axis.<br/>
   * 0 is bad, 255 is perfect<br/>
* Z_Quality (u8): Calibration quality on Z axis.<br/>
   * 0 is bad, 255 is perfect<br/>

Sent when the magnetometer calibration status changes.<br/>
If the quality updates are enabled (by the [enableMagnetoCalibrationQualityUpdates](#SkyController-Calibration-enableMagnetoCalibrationQualityUpdates) command), also sent every time a quality indicator changes.<br/>

Contrary to the Bebop Drone, the calibration is always active on the SkyController, so its status (and the quality) can change during the lifetime of the connection. Once the product is calibrated, the quality indicators will all be fixed to 255.<br/>

<br/>

<!-- SkyController-CalibrationState-MagnetoCalibrationQualityUpdatesState-->
### <a name="SkyController-CalibrationState-MagnetoCalibrationQualityUpdatesState">Fine calibration request status</a><br/>
> Fine calibration request status:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONQUALITYUPDATESSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONQUALITYUPDATESSTATE_ENABLED, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONQUALITYUPDATESSTATE) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONQUALITYUPDATESSTATE_ENABLED, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONQUALITYUPDATESSTATE) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            byte enabled = (byte)((Integer)args.get(ARFeatureSkyController.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_CALIBRATIONSTATE_MAGNETOCALIBRATIONQUALITYUPDATESSTATE_ENABLED)).intValue();
        }
    }
}
```

State of the "send calibration state on quality change" setting.<br/>

* enabled (u8): Flag (is the feature enabled).<br/>
   * 1 = The skycontroller sends a [MagnetoCalibrationState](#SkyController-CalibrationState-MagnetoCalibrationState) event for each quality update<br/>
   * 0 = The skycontroller sends a [MagnetoCalibrationState](#SkyController-CalibrationState-MagnetoCalibrationState) event only when the global state changes<br/>

Triggered by the [enableMagnetoCalibrationQualityUpdates](#SkyController-Calibration-enableMagnetoCalibrationQualityUpdates) command.<br/>

<br/>

<!-- SkyController-ButtonEvents-Settings-->
### <a name="SkyController-ButtonEvents-Settings">Settings button pressed</a><br/>
> Settings button pressed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONEVENTS_SETTINGS) && (elementDictionary != NULL))
    {

    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONEVENTS_SETTINGS) && (elementDictionary != NULL))
    {

    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_SKYCONTROLLER_BUTTONEVENTS_SETTINGS) && (elementDictionary != null)){

    }
}
```

Event sent when the settings button is pressed.<br/>

This event is sent only when the sky controller is connected to a drone.<br/>

This event is made so application can open their settings screen when the settings button is pressed on the SkyController. Handling this event is not mandatory.<br/>

<br/>
