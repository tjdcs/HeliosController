# Helios Controller

This project implements a basic python controller for Helios LED processors made
by [Megapixel](https://megapixelvr.com/helios/)

Improvements / documentation / extensions are welcome!! Especially to the
CommonPaths enum and supporting Enums for common options.

## Install

This project is available on pypi

```zsh
pip install helios_controller
```

## Examples

```python
from helios_controller import HeliosController, CommonPaths, PatternTypes

hc = HeliosController("192.168.1.105")
hc.patch("dev.display.brightness", 50)
hc.patch("dev.display.blackout", False)

hc.patch(CommonPaths.TEST_PATTERN_TYPE, PatternTypes.RED)

#Print all available paths / options
print(hc.get())
```

## API Documentation

Helios API documentation for is available [from
Megapixel](https://megapixelvr.com/product-support/helios/).
