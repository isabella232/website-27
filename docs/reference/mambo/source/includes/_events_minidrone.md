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

