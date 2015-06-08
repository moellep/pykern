# -*- coding: utf-8 -*-
u"""Wrapper for :mod:`yaml`

:copyright: Copyright (c) 2015 Bivio Software, Inc.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
from __future__ import absolute_import, division, print_function, unicode_literals
from io import open

import yaml

from pykern import pkcompat
from pykern import pkio


def load_file(filename):
    """Read a file, making sure all keys and values are locale

    Args:
        filename (str): file to read

    Returns:
        obj: dict or array
    """
    return _locale_str(yaml.load(pkio.read_text(filename)))


def _locale_str(obj):
    """Convert all objects to locale strings"""
    if isinstance(obj, dict):
        res = {}
        for k in obj:
            res[pkcompat.locale_str(k)] = _locale_str(obj[k])
        return res
    if isinstance(obj, list):
        res = []
        for v in obj:
            res.append(_locale_str(v))
        return res
    if type(obj) == bytes or type(obj) == str and hasattr(obj, 'decode'):
        return pkcompat.locale_str(obj)
    return obj