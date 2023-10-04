from enum import Enum
from typing import Any
import requests
import json

from .utilities import path_value_to_dict


class PatternTypes(str, Enum):
    """Common processor based test patterns

    This enum can be used to use python symbolic values to set specific
    control strings on the test pattern property of the Helios API
    """

    CUSTOM = "customColor"
    WHITE = "white"
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class CommonPaths(str, Enum):
    """A `str` Enum for some common property paths. Makes it easier to access
    common properties with the `get` and `patch` functions.
    """

    BRIGHTNESS = "dev.display.brightness"
    BLACKOUT = "dev.display.blackout"
    FREEZE = "dev.display.freeze"
    CCT = "dev.display.cct"
    TILES_INFO_STRING = "dev.display.tilesInfo"
    TEST_PATTERN_BASE_PATH = "dev.ingest.testPattern"
    TEST_PATTERN_TYPE = TEST_PATTERN_BASE_PATH + ".type"
    TEST_PATTERN_CUSTOM_COLOR_VALUE = TEST_PATTERN_BASE_PATH + ".color"


class HeliosController:
    """Helios LED Wall Processor Python Controller

    This object can easily get / patch dot delimited API targets on the Helios
    LED Processor. The full list of API targets can be determined by calling the
    `get` function with no arguments. Sub-properties can be accessed by using a
    dot delimited object path.
    """

    def __init__(self, ip: str) -> None:
        """Construct a new HeliosController python interface.

        Parameters
        ----------
        ip : str
            The target IP address of the HeliosController. Should only be set by
            the constructor.
        """
        self._ip = ip
        self._refresh_backend()

    def _refresh_backend(self):
        """Set local cached device json to match actual device state."""
        self._json = self.get()

    def get(self, path=""):
        """Use HTTP GET to retrieve the value of a specific path on the Helios
        json API. Default path retrieves full system state.

        Parameters
        ----------
        path : str, optional
            The target API path, by default ""

        Returns
        -------
        _type_
            _description_
        """
        response = requests.get(f"{self.api_root}?{path}")
        if response.status_code != 200:
            print("Helios API GET Error")

        data = response.json()
        if len(path) == 0:
            return data

        for k in path.split("."):
            data = data[k]

        return data

    def patch(self, path: str | CommonPaths, value: Any):
        """Use HTTP PATCH to set / change a settable value on the Helios JSON
        API.

        Parameters
        ----------
        path : str | Paths
            The target API path to update
        value : str
            The new attribute value
        """
        data = path_value_to_dict(path, value)

        headers = {"Content-type": "application/json"}
        response = requests.patch(
            f"{self.api_root}?{path}", data=json.dumps(data), headers=headers
        )

        if response.status_code != 200:
            print("Helios API PATCH Error")

        self._refresh_backend()

    @property
    def brightness(self):
        return self.get("dev.display.brightness")

    @property
    def json(self) -> dict:
        return self._json

    @property
    def api_root(self) -> str:
        return f"http://{self.ip}/api/v1/public"

    @property
    def ip(self) -> str:
        return self._ip
