"""Miscellaneous utility functions."""

import rtc


def timestamp():
    """Return timestamp of ISO 8601 format using onboard RTC.

    Returns:
        str: ISO 8601 timestamp.
    """
    r = rtc.RTC()
    t = r.datetime

    ts = (
        f"{t.tm_year:04d}-{t.tm_mon:02d}-{t.tm_mday:02d}T"
        f"{t.tm_hour:02d}:{t.tm_min:02d}:{t.tm_sec:02d}"
    )

    return ts


def eval_payload_meta(obj):
    """Create a measurement payload based on payload metadata.

    Recursively iterates through payload metadata and return dictionary with
    the same structure with callables replaced by their return values.

    Args:
        obj (dict | Callable): Sub-dictionary or callable to be evaluated.

    Returns:
        dict | Any: Sub-dictionary with callables replaced with return values,
            or the return value of a callable.
    """
    if isinstance(obj, dict):
        return {key: eval_payload_meta(val) for key, val in obj.items()}

    if callable(obj):
        return obj()

    return obj
