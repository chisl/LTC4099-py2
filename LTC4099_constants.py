#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""LTC4099: I2C Controlled USB Power Manager/Charger with Overvoltage Protection"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Linear Technology"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

class REG:
	COMMAND_0 = 0
	COMMAND_1 = 1
	IRQ_MASK = 2
	OUTPUT = 3
