# Errors

<aside class="notice">This error section is stored in a separate file in `includes/_errors.md`. Slate allows you to optionally separate out your docs into many files...just save them to the `includes` folder and add them to the top of your `index.md`'s frontmatter. Files are included in the order listed.</aside>

## Configuration errors

Error Code | Name | Error message
---------- | ------- | --------
9000  | UNKNOWN_LOCATION                                    | The requested garden location does not exist
9001  | SENSOR_SERIAL_ALREADY_EXISTS                        | Request to create a sensor with duplicate serial number
9002  | SENSOR_SERIAL_DOES_NOT_EXIST                        | Supplied sensor serial number does not exist or is not owned by me
9003  | NOT_MY_SENSOR                                       | Sensor assigned to a different account - cannot update
9004  | NOT_MY_LOCATION                                     | Location assigned to a different account
9005  | NO_PLANT_AT_LOCATION                                | This feature requires a plant to be assigned to the location
9008  | SENSOR_FIND_ERROR                                   | The sensor does not exist or is not assigned to this location
9009  | EVENT_ID_INVALID                                    | One, or more, of the event ids were invalid
9010  | LOCATION_FIND_ERROR                                 | The location does not exist or is not assigned to this user
9011  | UNKNOWN_DETECTOR_TYPE                               | The supplied detector type is invalid
9012  | UNSUPPORTED_HISTORY_FORMAT                          | Invalid or unsupported history format
9014  | UNSUPPORTED_RESOLUTION                              | Supplied sample resolution is not supported
9019  | STALE_DATA_UPDATE_ERROR                             | Cannot update from supplied data as server data is newer
9020  | INVALID_USER_DATA_VERSION                           | Cannot update as the supplied user data version EXCEEDS the server version
9021  | LOCATION_ALREADY_EXISTS                             | Cannot create a location with the same location identifier
9022  | UNKNOWN_ACTION                                      | Sync could not work out what to do for an item
9023  | EVENT_CREATE_ERROR                                  | Attempt to create an event failed
9030  | UNKNOWN_IMAGE_ACTION                                | Action not recognised, expected c,u or d
9031  | MISSING_LOCATION_IDENTIFIER                         | Location identifier parameter missing
9032  | GPS_DATA_MISSING                                    | GPS data missing - cannot suggest plants
9035  | RESET_ID_INVALID                                    | Supplied id is invalid or not found
9036  | RESET_ID_EXPIRED                                    | Supplied id has expired
9037  | RESET_ID_ALREADY_USED                               | Supplied id has been used
9038  | GARDEN_LOCATION_NOT_ACTIVE                          | Requested suggestions for a location that does not have sensor associated
9039  | NO_LOCATION_STATUS_PRESENT                          | Location for supplied location does not exist
9040  | MISSING_PLANT_ASSIGNED_DATE                         | If setting a plant id you MUST supply an assigned date (or removed)
9041  | INVALID_OR_MISSING_FROM_DATE                        | Expected a from date and was invalid or absent
9042  | INVALID_OR_MISSING_TO_DATE                          | Expected a to date and was invalid or absent
9043  | DEVICE_TIME_MISSING                                 | Expected a mandatory datetime and was absent
9044  | DEVICE_TIME_OUT_OF_RANGE                            | Device time out of acceptable synch with server time
9045  | USER_SHARING_INVALID_SET_OPTION                     | The parameter can only be to_be_reminded, never_remind or shared
9046  | USER_SHARING_INVALID_SET_OPTION_FOR_CURRENT_STATE   | User sharing cannot be set to new state when in current state
9047  | INVALID_UNKNOWN_OR_PRIVATE_LOCATION                 | Either the identifier does not exist or is private
9048  | REQUEST_DATE_SPAN_TOO_LARGE                         | The requested date span is too large
9049  | INVALID_DATE_FORMAT                                 | Could not parse the supplied date format use YYYY-MM-DD
9050  | UNKNOWN_PLANT_SCIENCE_DATABASE                      | The supplied library database identifier was not valid
9051  | INVALID_GPS_DATA                                    | The supplied gps data was invalid or out of range
9052  | SEASONALITY_DATA_NOT_FOUND                          | The seasonality data does not exist
9053  | DATETIME_VALUE_IS_IN_THE_FUTURE                     | One of the supplied dates was in the future and was rejected
9054  | DATETIME_REVERSAL_FOR_LOCATION                      | When un/assigning sensor sample block had reversed dates - all rejected
9057  | ACKNOWLEDGE_DONE_MISSING_DATE                       | All done acknowledgements must include a date when it occured
9058  | SESSION_HISTORY_MISSING_PARAMETERS                  | One or more parameters missing from session data
9059  | SENSOR_LOCATION_ASSIGNMENT_IN_THE_FUTURE            | When assigning a sensor to a location the assignment date was in the future
9060  | INVALID_DATETIME_FORMAT                             | Could not parse the supplied date format
9061  | SESSION_HISTORY_DATETIME_IN_FUTURE                  | The supplied session start time is in the future - not allowed
9062  | SENSOR_CREATE_MISSING_PARAMETERS                    | One or more parameters missing from sensor data
9063  | SENSOR_H20_CAPACITY_MISSING                         | If sensor type is h20 then capactiy is required
9064  | UNKNOWN_SENSOR_TYPE                                 | The supplied sensor type is unknown - expected pot, h20 or flower-power
9065  | VALUE_IS_NIL_WHEN_VALUE_EXPECTED                    | The parameter cannot be nil
9066  | MISSED_PARAMETER                                    | Missed parameter
9067  | FIRMWARE_DOESNT_EXIST                               | No such sensor firmware
9068  | INVALID_STATUS_CREATION_DATETIME_UTC                | Invalid status_creation_datetime_utc value
9069  | INVALID_TIME_RANGE                                  | Reversed or empty time Range
9070  | GARDEN_LOCATION_NOT_MINE                            | Garden location not mine
9071  | APIPIE_ERROR                                        | 
9072  | SENSOR_TYPE_CHANGED                                 | Sensor type change is not allowed

## Search errors

Error Code | Name | Error message
---------- | ------- | --------
7002  | MORE_DATA_REQUIRED                                  | More data required for suggestions:
7000  | UNKNOWN_PLANT_IDENTIFIER                            | The requested plant does not exist
7001  | UNKNOWN_PLANT_IN_LANGUAGE                           | The requested plant does not exist in this language
7002  | LANGUAGE_DICTIONARY_NOY_FOUND                       | Dictionary is missing
7003  | INVALID_SUNLIGHT_ESTIMATION                         | The sunlight estimation value is invalid
7004  | INVALID_OR_MISSING_GPS                              | Missing or invalid GPS value
7005  | SUGGESTION_NOT_READY                                | Suggestion not ready - not enough data samples
7006  | INDOOR_OUTDOOR_VALUE_MISSING                        | Suggestion mode requires indoor/outdoor value to be set
7007  | INVALID_DLI_VALUE                                   | DLI value is nil - cannot be used
7008  | INVALID_HARDINESS_ZONE                              | Hardiness value is nil - cannot be used
7009  | INVALID_HEAT_ZONE                                   | Heat value is nil - cannot be used
7010  | NO_PLANT_ASSIGNED_TO_LOCATION                       | This call requires a plant to have been assigned to the location
7011  | SUPPLIED_PLANT_LIBRARY_IDENTIFIER_NOT_RECOGNISED    | The supplied plant library identifier is not recognised

## Common errors

Error Code | Name | Error message
---------- | ------- | --------
5000  | UNSUPPORTED_API                 | The requested version of this message is not supported
5001  | NOT_YET_IMPLEMENTED             | This feature has not yet been implemented
5003  | NOT_ENOUGH_PARAMETERS           | Invalid number of parameters
5004  | DEPRECATED_IS_ERROR             | This function is deprecated and cannot be called
5005  | JSON_PARSE_ERROR                | Malformed JSON error
5006  | S3_ID_MISSING                   | S3_ID_MISSING
5007  | S3_SECRET_MISSING               | S3_SECRET_MISSING
5008  | UNSUPPORTED_LANGUAGE            | Unsupported language
5009  | MISSED_SENSOR_TYPE              | Missed sensor_type
5010  | WRONG_SENSOR_TYPE               | Bad sensor_type value
5011  | MISSED_H20_CAPACITY             | Missed h20_capacity for H20 sensor
5012  | WRONG_H20_CAPACITY              | Wrong value of h20_capacity for H20 sensor
5013  | MISSING_USE_LITER               | Missed use_liter parameter
5014  | MISSING_UTC_TIMEZONE            | Missed utc_timezone parameter
5015  | MISSING_USER_UUID               | Missed user_uuid parameter
5016  | MISSED_EXPERT_MODE_CFG          | Missed expert mode config
5017  | REQUIRED_PARAMETER_MISSING      | One or more parameters are missing
5017  | UNKNOWN_STATUS_UPDATE_TYPE      | The status to update was not recognised
5018  | INCORRECT_DATA_TYPE             | Supplied data type is incorrect
5019  | INCORRECT_DATA_VALUE_OF_ENUM    | Supplied value was not in enum set
5020  | SENSOR_NOT_CONFIGURED           | The sensor has not been correctly configured
5021  | INVALID_CALIBRATION_DATA        | Supplied calibration data is invalid 
5200  | INTERNAL_ERROR                  | Unexpected

## User errors

Error Code | Name | Error message
---------- | ------- | --------
8000  | USER_ALREADY_EXISTS             | The user email already exists
8001  | INVALID_EMAIL_FORMAT            | The supplied email is invalid
8002  | INVALID_PASSWORD_FORMAT         | The supplied password is invalid
8004  | UNKNOWN_USER_EMAIL              | The supplied email is not recognised
8008  | UNKNOWN_OR_INVALID_USER         | User is missing
8009  | CLIENT_APP_IDENTIFIER_MISSING   | The client app identifier MUST be present
8010  | INVALID_USER                    | Incorrect email and/or password
8011  | UNSUPPORTED_APP_IDENTIFIER      | Unknown app identifier
8012  | INVALID_UPDATE_DATA             | The supplied update data is invalid or missing
8013  | ALREADY_LINKED_ACCOUNT          | Already linked that account
8014  | MISSED_USE_LITER                | Use liter parameter is missing
8015  | MISSED_UTC_TIMEZONE             | UTC Timezone paramter is missing
8016  | MISSED_USER_UUID                | User uuid parameter is missing
8018  | MISSING_EMAIL                   | Email is missing
8019  | MISSING_PASSWORD                | Password is missing
8020  | EMAIL_EXISTS                    | Email is already in system
8021  | USE_LITER_BOOL                  | use_liter'is a boolean, not a string
8022  | NO_SUCH_USER_ON_HAWAII1         | No such user on Hawaii_1 WS
