#!/usr/bin/env python
# -*- coding: utf-8 -*-





import warnings, sys
from watchdog.utils import platform
from watchdog.utils import UnsupportedLibc

if platform.is_linux():
    try:
        from .inotify import InotifyObserver as Observer
    except UnsupportedLibc:
        from .polling import PollingObserver as Observer
else:
	sys.exit(1)