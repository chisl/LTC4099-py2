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

from LTC4099_constants import *

# name:        LTC4099
# description: I2C Controlled USB Power Manager/Charger with Overvoltage Protection
# manuf:       Linear Technology
# version:     0.1
# url:         http://cds.linear.com/docs/en/datasheet/4099fd.pdf
# date:        2017-12-20


# Derive from this class and implement read and write
class LTC4099_Base:
	"""I2C Controlled USB Power Manager/Charger with Overvoltage Protection"""
	# Register COMMAND_0
	
	
	def setCOMMAND_0(self, val):
		"""Set register COMMAND_0"""
		self.write(REG.COMMAND_0, val, 8)
	
	def getCOMMAND_0(self):
		"""Get register COMMAND_0"""
		return self.read(REG.COMMAND_0, 8)
	
	# Bits ILim
	# the maximum current that will be drawn from the VBUS pin in the event that the load at
	#           VOUT (battery charger plus systemload) exceeds the power
	#           available. Any additional power will be drawn from the battery.
	#           The default state for the input current limit setting is
	#           000, representing the low power 100mA USB setting. 
	
	# Bits ICharge
	# The battery charger current settings are adjusted
	#           by selecting one of the eight servo voltages for the PROG
	#           pin. Recall that the programmed charge current is given
	#           by the expression:
	#           ICHG = VPROG / RPROG * 1030
	#           The default state forthe battery charger current settings is
	#           000, giving the lowest available servo voltage of 500mV 
	
	# Bits COVERX
	# The C/x setting controls the PROG pin level that the
	#           LTC4099’s C/x comparator uses to report full capacity
	#           charge. For example, if the 100mV setting is chosen, then
	#           the LTC4099 reports that its PROG pin voltage has fallen
	#           below 100mV. For the 50mV setting, LTC4099 reports
	#           that its PROG pin voltage has fallen below 50mV. The C/x
	#           settings are adjusted by comparing the PROG pin voltage
	#           with the values shows in Table 4. The default value for the
	#           C/x setting is 00, giving 100mV detection. 
	
	# Register COMMAND_1
	
	
	def setCOMMAND_1(self, val):
		"""Set register COMMAND_1"""
		self.write(REG.COMMAND_1, val, 8)
	
	def getCOMMAND_1(self):
		"""Get register COMMAND_1"""
		return self.read(REG.COMMAND_1, 8)
	
	# Bits TIMER
	# The TIMER2–TIMER0 bits control the duration of the battery
	#           charger safety timer. The safety timer starts once the
	#           LTC4099 reaches the 4.100V or the 4.200V float voltage.
	#           As long as input power is available, charging will continue
	#           in float voltage mode until the safety timer expires. 
	
	# Bits DISABLE_CHARGER
	# The DISABLE_CHARGER bit can be used to prevent battery
	#           charging if needed. This bit should be used with caution
	#           as it can prevent the battery charger from bringing up
	#           the battery voltage. Without the ability to address the I2C
	#           port, only a low voltage on DVCC will clear the I
	#           2C port to its default state and re-enable charging. 
	
	# Bits ENABLE_BATTERY_CONDITIONER
	# The ENABLE_BATTERY_CONDITIONER bit enables the
	#           automatic battery load circuit in the event of simultaneously
	#           high battery voltage and temperature. See the Overtemperature
	#           Battery Conditioner section. 
	
	# Bits VFLOAT
	# The VFLOAT = 4.2V bit controls the final float voltage of the
	#           LTC4099’s battery charger. A 1 in this bit position changes
	#           the charger from the default float voltage value of 4.100V
	#           to the higher 4.200V level. 
	
	# Bits TREG
	# The TREG = 85°C control bit changes the LTC4099’s battery
	#           charger junction thermal regulation temperature from its
	#           default value of 105°C to a lower setting of 85°C. This may
	#           be used to reduce heat in highly thermally compromised
	#           systems. In general, the high efficiency charging system
	#           of the LTC4099 will keep the junction temperature low
	#           enough to avoid junction thermal regulation. 
	
	# Bits unused_0
	# Register IRQ_MASK
	# A 1 written to a given position in the mask
	#       register allows status change in that category to generate
	#       an interrupt. A zero in a given position in the mask register
	#       prohibits the generation of an interrupt. The start-up state
	#       of the LTC4099 is all zeros for this register indicating that
	#       no interrupts will be generated without explicit request via
	#       the I2C port. See the Interrupt Generation section. 
	
	
	def setIRQ_MASK(self, val):
		"""Set register IRQ_MASK"""
		self.write(REG.IRQ_MASK, val, 8)
	
	def getIRQ_MASK(self):
		"""Get register IRQ_MASK"""
		return self.read(REG.IRQ_MASK, 8)
	
	# Bits USBGOOD
	# Bits WALLGOOD
	# Bits BADCELL
	# Bits THERMAL_REG
	# Bits THERMISTOR_STATUS
	# Bits CHARGER_STATUS
	# Bits unused_0
	# Register OUTPUT
	# One status byte may be read from the LTC4099.
	#       A 1 read back in any of the bit positions indicates that the condition is true. 
	
	
	def setOUTPUT(self, val):
		"""Set register OUTPUT"""
		self.write(REG.OUTPUT, val, 8)
	
	def getOUTPUT(self):
		"""Get register OUTPUT"""
		return self.read(REG.OUTPUT, 8)
	
	# Bits USBGOOD
	# indicates the presence of power at VBUS. Criteria for determining this status bit
	#           is derived from the undervoltage lockout circuit on VBUS and is given by the
	#           electrical parameters VUVLO and VDUVLO. 
	
	# Bits WALLGOOD
	# indicates the presence of voltage available at the WALL pin and is derived from
	#           the WALL undervoltage lockout circuit. Like the VBUS pin, this pin has both an
	#           absolute voltage detection level given by the electrical parameter VWALL, as well
	#           as a level relative to BAT given by ΔVWALL. Both of the conditions must be met for
	#           bit 6 to indicate the presence of power at WALL. 
	
	# Bits BADCELL
	# indicates that the battery has been below the pre- charge threshold level of approximately
	#           2.85V for more than one-half hour while the charger was attempting to charge. When this occurs,
	#           it is usually the result of a defective cell. However, in some cases a bad cell indication
	#           may be caused by system load prioritization over battery charging. System software can test
	#           for this by forcing a reduction of system load and restarting the battery charger via I2C
	#           (a disable followed by an enable). If the bad cell indication returns, then the cell is
	#           definitively bad.
	
	# Bits THERMAL_REG
	# indicates that the battery charger is in thermal regulation due to excessive LTC4099
	#           junction temperature. Recall that there are two I2C programmable junction temperature
	#           settings available at which to regulate, 85°C and 105°C. Bit 4 indicates thermal regulation
	#           at whichever setting is chosen. 
	
	# Bits NTC
	# indicate the status of the thermistor measurement circuit 
	# Bits CHRGR
	# status of the battery charger 
