"""Miscellaneous utility functions."""

import rtc


def timestamp():
    """Return timestamp of ISO 8601 format using onboard RTC."""
    r = rtc.RTC()
    t = r.datetime

    ts = f"{t.tm_year:04d}-{t.tm_mon:02d}-{t.tm_mday:02d}T{t.tm_hour:02d}:{t.tm_min:02d}:{t.tm_sec:02d}"

    return ts


def eval_payload_meta(obj):
    """Recursively iterate through payload metadata and return dictionary with the same structure with callables replaced by their return values."""
    if isinstance(obj, dict):
        return {key: eval_payload_meta(val) for key, val in obj.items()}

    if callable(obj):
        return obj()

    return obj
