#!/usr/bin/env python3

"""
An object-oriented framework for command-line apps.
"""

__version__ = '0.23.0'

# Define the public API
from .app import App, AppMeta
from .model import (
        init, load, reload, insert_config, insert_configs, append_config,
        append_configs, prepend_config, prepend_configs, share_configs,
)
from .params.param import param
from .params.toggle import toggle_param, pick_toggled, Toggle as toggle
from .params.inherited import inherited_param
from .configs.configs import *
from .configs.layers import Layer, DictLayer, dict_like
from .configs.attrs import config_attr
from .configs.on_load import on_load
from .getters import Key, Method, Func, Value
from .errors import *
from .utils import lookup
