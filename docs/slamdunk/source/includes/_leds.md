# How to use the LEDs

The Parrot S.L.A.M.dunk has 4 RGB LEDs.

The LEDs can be controlled from the
the [sysfs](https://www.kernel.org/doc/Documentation/filesystems/sysfs.txt),
more specifically they are compatible with
[gpio-leds](https://www.kernel.org/doc/Documentation/devicetree/bindings/leds/leds-gpio.txt).

Each color can be set independently,
the available sysfs entries are:

- `/sys/class/leds/front:left:blue`
- `/sys/class/leds/front:left:green`
- `/sys/class/leds/front:left:red`
- `/sys/class/leds/front:right:blue`
- `/sys/class/leds/front:right:green`
- `/sys/class/leds/front:right:red`
- `/sys/class/leds/rear:left:blue`
- `/sys/class/leds/rear:left:green`
- `/sys/class/leds/rear:left:red`
- `/sys/class/leds/rear:right:blue`
- `/sys/class/leds/rear:right:green`
- `/sys/class/leds/rear:right:red`

To enable a color, write the value `1` to the `brightness` file, e.g:

    echo 1 > /sys/class/leds/rear:right:red/brightness

To reset the color, write `0`:

    echo 0 > /sys/class/leds/rear:right:red/brightness

Multiple colors can be combined:

    # red
    echo 1 > /sys/class/leds/front:left:red/brightness
    # yellow
    echo 1 > /sys/class/leds/front:left:green/brightness
    # white
    echo 1 > /sys/class/leds/front:left:blue/brightness

To blink, write `timer` to the `trigger` file, e.g:

    echo 1 > /sys/class/leds/rear:left:red/brightness
    echo timer > /sys/class/leds/rear:left:red/trigger

To reset blinking, write `none` to the `trigger` file:

    echo none > /sys/class/leds/rear:left:red/trigger
