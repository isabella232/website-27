<!-- wifi-scanned_item-->
### <a name="wifi-scanned_item">Wifi scan results</a><br/>
> Wifi scan results:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_SSID, arg);
                if (arg != NULL)
                {
                    char * ssid = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_RSSI, arg);
                if (arg != NULL)
                {
                    int16_t rssi = arg->value.I16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_BAND, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_WIFI_BAND band = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_CHANNEL, arg);
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_SSID, arg);
                if (arg != NULL)
                {
                    char * ssid = arg->value.String;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_RSSI, arg);
                if (arg != NULL)
                {
                    int16_t rssi = arg->value.I16;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_BAND, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_WIFI_BAND band = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_CHANNEL, arg);
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    String ssid = (String)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_SSID);
                    short rssi = (short)((Integer)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_RSSI)).intValue();
                    ARCOMMANDS_WIFI_BAND_ENUM band = ARCOMMANDS_WIFI_BAND_ENUM.getFromValue((Integer)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_BAND));
                    byte channel = (byte)((Integer)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_SCANNEDITEM_CHANNEL)).intValue();
                }
            }
        } else {
            // list is empty
        }
    }
}
```

Wifi scan results.<br/>


* ssid (string): SSID of the AP<br/>
* rssi (i16): RSSI of the AP.<br/>
* band (enum): The band : 2.4 Ghz or 5 Ghz<br/>
   * 2_4_ghz: 2.4 GHz band<br/>
   * 5_ghz: 5 GHz band<br/>
* channel (u8): Channel of the AP<br/>


Triggered Triggered for each wifi scanned after a [ScanWifi](#wifi-scan).<br/>



*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2*<br/>


<br/>

<!-- wifi-authorized_channel-->
### <a name="wifi-authorized_channel">Available channel results</a><br/>
> Available channel results:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_BAND, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_WIFI_BAND band = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_CHANNEL, arg);
                if (arg != NULL)
                {
                    uint8_t channel = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_ENVIRONMENT, arg);
                if (arg != NULL)
                {
                    uint8_t environment = arg->value.U8;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL)
    {
        if (elementDictionary != NULL)
        {
            ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictElement = NULL;
            ARCONTROLLER_DICTIONARY_ELEMENT_t *dictTmp = NULL;
            HASH_ITER(hh, elementDictionary, dictElement, dictTmp)
            {
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_BAND, arg);
                if (arg != NULL)
                {
                    eARCOMMANDS_WIFI_BAND band = arg->value.I32;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_CHANNEL, arg);
                if (arg != NULL)
                {
                    uint8_t channel = arg->value.U8;
                }
                HASH_FIND_STR (dictElement->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_ENVIRONMENT, arg);
                if (arg != NULL)
                {
                    uint8_t environment = arg->value.U8;
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
    if (commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL){
        if ((elementDictionary != null) && (elementDictionary.size() > 0)) {
            Iterator<ARControllerArgumentDictionary<Object>> itr = elementDictionary.values().iterator();
            while (itr.hasNext()) {
                ARControllerArgumentDictionary<Object> args = itr.next();
                if (args != null) {
                    ARCOMMANDS_WIFI_BAND_ENUM band = ARCOMMANDS_WIFI_BAND_ENUM.getFromValue((Integer)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_BAND));
                    byte channel = (byte)((Integer)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_CHANNEL)).intValue();
                    byte environment = (byte)((Integer)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_AUTHORIZEDCHANNEL_ENVIRONMENT)).intValue();
                }
            }
        } else {
            // list is empty
        }
    }
}
```

Available channel results.<br/>


* band (enum): The band : 2.4 Ghz or 5 Ghz<br/>
   * 2_4_ghz: 2.4 GHz band<br/>
   * 5_ghz: 5 GHz band<br/>
* channel (u8): The channel number<br/>
* environment (bitfield as u8): Type of environment<br/>
   * indoor: indoor environment<br/>
   * outdoor: outdoor environment<br/>


Triggered Triggered for each channels found after a [UpdateAvailableChannels](#wifi-update_authorized_channels).<br/>



*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2*<br/>


<br/>

<!-- wifi-ap_channel_changed-->
### <a name="wifi-ap_channel_changed">Wifi selection changed</a><br/>
> Wifi selection changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_WIFI_SELECTION_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_BAND, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_WIFI_BAND band = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_CHANNEL, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_WIFI_SELECTION_TYPE type = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_BAND, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_WIFI_BAND band = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_CHANNEL, arg);
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
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_WIFI_SELECTION_TYPE_ENUM type = ARCOMMANDS_WIFI_SELECTION_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_TYPE));
            ARCOMMANDS_WIFI_BAND_ENUM band = ARCOMMANDS_WIFI_BAND_ENUM.getFromValue((Integer)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_BAND));
            byte channel = (byte)((Integer)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_APCHANNELCHANGED_CHANNEL)).intValue();
        }
    }
}
```

Wifi selection changed.<br/>


* type (enum): The wifi selection type available<br/>
   * auto_all: Auto selection on all channels<br/>
   * auto_2_4_ghz: Auto selection 2.4ghz<br/>
   * auto_5_ghz: Auto selection 5 ghz<br/>
   * manual: manual selection<br/>
* band (enum): The band : 2.4 Ghz or 5 Ghz<br/>
   * 2_4_ghz: 2.4 GHz band<br/>
   * 5_ghz: 5 GHz band<br/>
* channel (u8): The channel of the drone's access point<br/>


Triggered Triggered by [WifiSelection](#wifi-set_ap_channel).<br/>



*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2*<br/>


<br/>

<!-- wifi-security_changed-->
### <a name="wifi-security_changed">Wifi security changed</a><br/>
> Wifi security changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_WIFI_SECURITYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_SECURITYCHANGED_KEY, arg);
            if (arg != NULL)
            {
                char * key = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_SECURITYCHANGED_KEY_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_WIFI_SECURITY_TYPE key_type = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_WIFI_SECURITYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_SECURITYCHANGED_KEY, arg);
            if (arg != NULL)
            {
                char * key = arg->value.String;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_SECURITYCHANGED_KEY_TYPE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_WIFI_SECURITY_TYPE key_type = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_WIFI_SECURITYCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            String key = (String)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_SECURITYCHANGED_KEY);
            ARCOMMANDS_WIFI_SECURITY_TYPE_ENUM key_type = ARCOMMANDS_WIFI_SECURITY_TYPE_ENUM.getFromValue((Integer)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_SECURITYCHANGED_KEY_TYPE));
        }
    }
}
```

<br/>


* key (string): The key to secure the network. Not used if type is open<br/>
* key_type (enum): The type of wifi security (open, wpa2)<br/>
   * open: Wifi is not protected by any security (default)<br/>
   * wpa2: Wifi is protected by wpa2<br/>


Triggered Triggered by [SetWifiSecurity](#wifi-set_security).<br/>



*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2 since 3.1.0*<br/>


<br/>

<!-- wifi-country_changed-->
### <a name="wifi-country_changed">Wifi country changed</a><br/>
> Wifi country changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_WIFI_COUNTRYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_COUNTRYCHANGED_SELECTION_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_WIFI_COUNTRY_SELECTION selection_mode = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_COUNTRYCHANGED_CODE, arg);
            if (arg != NULL)
            {
                char * code = arg->value.String;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_WIFI_COUNTRYCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_COUNTRYCHANGED_SELECTION_MODE, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_WIFI_COUNTRY_SELECTION selection_mode = arg->value.I32;
            }
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_COUNTRYCHANGED_CODE, arg);
            if (arg != NULL)
            {
                char * code = arg->value.String;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_WIFI_COUNTRYCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_WIFI_COUNTRY_SELECTION_ENUM selection_mode = ARCOMMANDS_WIFI_COUNTRY_SELECTION_ENUM.getFromValue((Integer)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_COUNTRYCHANGED_SELECTION_MODE));
            String code = (String)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_COUNTRYCHANGED_CODE);
        }
    }
}
```

Wifi country changed.<br/>


* selection_mode (enum): Type of country selection<br/>
   * manual: Manual selection.<br/>
   * auto: Automatic selection.<br/>
* code (string): Country code with ISO 3166 format, empty string means unknown country.<br/>


Triggered Triggered by [SetCountry](#wifi-set_country).<br/>



*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2*<br/>


<br/>

<!-- wifi-environment_changed-->
### <a name="wifi-environment_changed">Outdoor setting changed</a><br/>
> Outdoor setting changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_WIFI_ENVIRONMENTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_ENVIRONMENTCHANGED_ENVIRONMENT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_WIFI_ENVIRONMENT environment = arg->value.I32;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_WIFI_ENVIRONMENTCHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_ENVIRONMENTCHANGED_ENVIRONMENT, arg);
            if (arg != NULL)
            {
                eARCOMMANDS_WIFI_ENVIRONMENT environment = arg->value.I32;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_WIFI_ENVIRONMENTCHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            ARCOMMANDS_WIFI_ENVIRONMENT_ENUM environment = ARCOMMANDS_WIFI_ENVIRONMENT_ENUM.getFromValue((Integer)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_ENVIRONMENTCHANGED_ENVIRONMENT));
        }
    }
}
```

Status of the wifi config : either indoor or outdoor.<br/>


* environment (enum): Type of environment<br/>
   * indoor: indoor environment<br/>
   * outdoor: outdoor environment<br/>


Triggered Triggered by [SetOutdoor](#wifi-set_environment).<br/>



*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2*<br/>


<br/>

<!-- wifi-rssi_changed-->
### <a name="wifi-rssi_changed">Rssi changed</a><br/>
> Rssi changed:

```c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_WIFI_RSSICHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_RSSICHANGED_RSSI, arg);
            if (arg != NULL)
            {
                int16_t rssi = arg->value.I16;
            }
        }
    }
}
```

```objective_c
void onCommandReceived (eARCONTROLLER_DICTIONARY_KEY commandKey, ARCONTROLLER_DICTIONARY_ELEMENT_t *elementDictionary, void *customData)
{
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_WIFI_RSSICHANGED) && (elementDictionary != NULL))
    {
        ARCONTROLLER_DICTIONARY_ARG_t *arg = NULL;
        ARCONTROLLER_DICTIONARY_ELEMENT_t *element = NULL;
        HASH_FIND_STR (elementDictionary, ARCONTROLLER_DICTIONARY_SINGLE_KEY, element);
        if (element != NULL)
        {
            HASH_FIND_STR (element->arguments, ARCONTROLLER_DICTIONARY_KEY_WIFI_RSSICHANGED_RSSI, arg);
            if (arg != NULL)
            {
                int16_t rssi = arg->value.I16;
            }
        }
    }
}
```

```java
@Override
public void onCommandReceived (ARDeviceController deviceController, ARCONTROLLER_DICTIONARY_KEY_ENUM commandKey, ARControllerDictionary elementDictionary) {
    if ((commandKey == ARCONTROLLER_DICTIONARY_KEY_ENUM.ARCONTROLLER_DICTIONARY_KEY_WIFI_RSSICHANGED) && (elementDictionary != null)){
        ARControllerArgumentDictionary<Object> args = elementDictionary.get(ARControllerDictionary.ARCONTROLLER_DICTIONARY_SINGLE_KEY);
        if (args != null) {
            short rssi = (short)((Integer)args.get(ARFeatureWifi.ARCONTROLLER_DICTIONARY_KEY_WIFI_RSSICHANGED_RSSI)).intValue();
        }
    }
}
```

Rssi Changed. This is an information about the Wifi link quality.<br/>


* rssi (i16): Rssi on the connected wifi network. Rssi values are generally between -30 and -120dBm. The nearest of 0 is the better.<br/>


Triggered Triggered regularly when the link quality changes.<br/>



*Supported by <br/>*

- *Bebop*<br/>
- *Jumping Sumo*<br/>
- *Jumping Night*<br/>
- *Jumping Race*<br/>
- *Bebop 2*<br/>


<br/>

