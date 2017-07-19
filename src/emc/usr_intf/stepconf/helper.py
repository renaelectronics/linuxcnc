#!/usr/bin/python
import string
from subprocess import Popen, PIPE


# helper function
def run_cmd(cmd):
	"""
	Execute the external command and get its exitcode, stdout and stderr.
	eg. out = run_cmd(cmd)
	"""
	proc = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	out, err = proc.communicate()
	exitcode = proc.returncode
	# return the output
	return out

# write motor setting
def write_motor_setting(motor, setting):
	
	return None

# read motor setting
def get_motor_setting(motor):
	# motor eeprom setting offset
	EEPROM_ABS_POS = 0
	EEPROM_EL_POS = (EEPROM_ABS_POS + 3*2) 
	EEPROM_MARK = (EEPROM_EL_POS + 2*2)
	EEPROM_TVAL = (EEPROM_MARK + 3*2)
	EEPROM_T_FAST = (EEPROM_TVAL + 1*2)
	EEPROM_TON_MIN = (EEPROM_T_FAST + 1*2)
	EEPROM_TOFF_MIN = (EEPROM_TON_MIN + 1*2)
	EEPROM_ADC_OUT = (EEPROM_TOFF_MIN + 1*2)
	EEPROM_OCD_TH = (EEPROM_ADC_OUT + 1*2)
	EEPROM_STEP_MODE = (EEPROM_OCD_TH + 1*2)
	EEPROM_ALARM_EN = (EEPROM_STEP_MODE + 1*2)
	EEPROM_CONFIG = (EEPROM_ALARM_EN + 1*2)
	EEPROM_STATUS = (EEPROM_CONFIG + 2*2)
	EEPROM_CHECK_SUM = (EEPROM_STATUS + 2*2)
	EEPROM_MAX_BYTE = (EEPROM_CHECK_SUM + 1*2)
	print EEPROM_MAX_BYTE
	
	# read motor setting
	cmd_string = "wch6474 -r -m " + motor
	cmd_out = run_cmd(cmd_string)
	if cmd_out:
		# remove all whitespace
		cmd_out = cmd_out.translate(None, string.whitespace)
		# checkout the lenght
		if len(cmd_out) != EEPROM_MAX_BYTE:
			return None

		# process the data into dictionary
		dict = {}
		dict['EEPROM_ABS_POS'] = cmd_out[EEPROM_ABS_POS:EEPROM_EL_POS]
		dict['EEPROM_EL_POS'] = cmd_out[EEPROM_EL_POS:EEPROM_MARK]
		dict['EEPROM_MARK'] = cmd_out[EEPROM_MARK:EEPROM_TVAL]
		dict['EEPROM_TVAL'] = cmd_out[EEPROM_TVAL:EEPROM_T_FAST]
		dict['EEPROM_T_FAST'] = cmd_out[EEPROM_T_FAST:EEPROM_TON_MIN]
		dict['EEPROM_TON_MIN'] = cmd_out[EEPROM_TON_MIN:EEPROM_TOFF_MIN]
		dict['EEPROM_TOFF_MIN'] = cmd_out[EEPROM_TOFF_MIN:EEPROM_ADC_OUT]
		dict['EEPROM_ADC_OUT'] = cmd_out[EEPROM_ADC_OUT:EEPROM_OCD_TH]
		dict['EEPROM_OCD_TH'] = cmd_out[EEPROM_OCD_TH:EEPROM_STEP_MODE]
		dict['EEPROM_STEP_MODE'] = cmd_out[EEPROM_STEP_MODE:EEPROM_ALARM_EN]
		dict['EEPROM_ALARM_EN'] = cmd_out[EEPROM_ALARM_EN:EEPROM_CONFIG]
		dict['EEPROM_CONFIG'] = cmd_out[EEPROM_CONFIG:EEPROM_STATUS]
		dict['EEPROM_STATUS'] = cmd_out[EEPROM_STATUS:EEPROM_CHECK_SUM]
		return dict

	return None

# main
dict = get_motor_setting('0')
if dict != None:
	print dict['EEPROM_STEP_MODE']
