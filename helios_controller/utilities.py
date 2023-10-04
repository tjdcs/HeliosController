from typing import Any


def path_to_dict(path: str) -> dict:
    """Convert between a dot delimited path to a full python dict. The dict
    can be used to set / access / update python JSON objects

    Parameters
    ----------
    path : str
        The API path in dot delimited format

    Returns
    -------
    dict
        A python dict with nested attributes based on the dot-delimited path
    """
    if len(path) == 0:
        return {}

    d = {}
    t = d
    for k in path.split("."):
        t[k] = {}
        t = t[k]
    return d


def update_dict_with_path(d: dict, path: str, value: Any) -> None:
    """Update a particular dict, d, with a new value based on the dot
    delimited path variable

    Parameters
    ----------
    d : dict
        Python dict with nested values mimicing Helios API structure.
    path : str
        A dot delimited path determining the specific property to update
    value : Any
        A new value

    Returns
    -------
    None
    """
    if len(path) == 0:
        return

    keys = path.split(".")
    t = d
    for k in keys[:-1]:
        t = t[k]
    t[keys[-1]] = value


def path_value_to_dict(path: str, value: Any) -> dict:
    """Construct a new dict to mimic the path structure used in python
    Helios API.

    Parameters
    ----------
    path : str
        A dot delimited path determining the specific property to update
    value : Any
        default / new value

    Returns
    -------
    dict
        Python dict with nested values mimicing Helios API structure.
    """
    d = path_to_dict(path)
    update_dict_with_path(d, path, value)
    return d
