
class bandwidth:
	def __init__(self):
		INFO_NO_PARAM="no admite parametro, se envia consulta"
	def ndb(*n):
		if len(n) == 0:
			inst.query("CALCulate:BANDwidth:NDB?")
		else:
			inst.write("CALCulate:BANDwidth:NDB " +str(param))
	def result(*n):
		if len(n) == 0:
			inst.query("CALCulate:BANDwidth:RESult?")
		else:
			inst.query("CALCulate:BANDwidth:RESult " +str(param))

class lline:
	def __init__(self):
		INFO_NO_PARAM="no admite parametro, se envia consulta"
	def all_delete(*n):
		if len(n) == 0:
			inst.write("CALCulate:LLINe:ALL:DELete?")
		else:
			inst.write("CALCulate:LLINe:ALL:DELete " +str(param))
	def control_domain(*n):
		if len(n) == 0:
			inst.query("CALCulate:LLINe:CONTrol:DOMain?")
		else:
			inst.write("CALCulate:LLINe:CONTrol:DOMain " +str(param))
	def fail(*n):
		if len(n) == 0:
			inst.query("CALCulate:LLINe:FAIL?")
		else:
			inst.query("CALCulate:LLINe:FAIL " +str(param))
	def fail_ratio(*n):
		if len(n) == 0:
			inst.query("CALCulate:LLINe:FAIL:RATIo?")
		else:
			inst.query("CALCulate:LLINe:FAIL:RATIo " +str(param))
	def fail_stop_state(*n):
		if len(n) == 0:
			inst.query("CALCulate:LLINe:FAIL:STOP:STATe?")
		else:
			inst.write("CALCulate:LLINe:FAIL:STOP:STATe " +str(param))
	def control_interpolate_type(*n):
		if len(n) == 0:
			inst.query("CALCulate:LLINe"+str(op)+":CONTrol:INTerpolate:TYPE?")
		else:
			inst.write("CALCulate:LLINe"+str(op)+":CONTrol:INTerpolate:TYPE " +str(param))
	def data(*n):
		if len(n) == 0:
			inst.query("CALCulate:LLINe"+str(op)+":DATA?")
		else:
			inst.write("CALCulate:LLINe"+str(op)+":DATA " +str(param))
	def data_merge(*n):
		if len(n) == 0:
			inst.write("CALCulate:LLINe"+str(op)+":DATA:MERGe?")
		else:
			inst.write("CALCulate:LLINe"+str(op)+":DATA:MERGe " +str(param))
	def delete(*n):
		if len(n) == 0:
			inst.write("CALCulate:LLINe"+str(op)+":DELete?")
		else:
			inst.write("CALCulate:LLINe"+str(op)+":DELete " +str(param))
	def relampt_state(*n):
		if len(n) == 0:
			inst.query("CALCulate:LLINe"+str(op)+":RELAmpt[:STATe]?")
		else:
			inst.write("CALCulate:LLINe"+str(op)+":RELAmpt[:STATe] " +str(param))
	def relfreq_state(*n):
		if len(n) == 0:
			inst.query("CALCulate:LLINe"+str(op)+":RELFreq[:STATe]?")
		else:
			inst.write("CALCulate:LLINe"+str(op)+":RELFreq[:STATe] " +str(param))
	def state(*n):
		if len(n) == 0:
			inst.query("CALCulate:LLINe"+str(op)+":STATe?")
		else:
			inst.write("CALCulate:LLINe"+str(op)+":STATe " +str(param))

class marker:
	def __init__(self):
		INFO_NO_PARAM="no admite parametro, se envia consulta"
	def aoff(*n):
		if len(n) == 0:
			inst.write("CALCulate:MARKer:AOFF?")
		else:
			inst.write("CALCulate:MARKer:AOFF " +str(param))
	def fcount_resolution(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer:FCOunt:RESolution?")
		else:
			inst.write("CALCulate:MARKer:FCOunt:RESolution " +str(param))
	def fcount_resolution_auto(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer:FCOunt:RESolution:AUTO?")
		else:
			inst.write("CALCulate:MARKer:FCOunt:RESolution:AUTO " +str(param))
	def fcount_x(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer:FCOunt:X?")
		else:
			inst.query("CALCulate:MARKer:FCOunt:X " +str(param))
	def fcount_state(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer:FCOunt[:STATe]?")
		else:
			inst.write("CALCulate:MARKer:FCOunt[:STATe] " +str(param))
	def cpeak_state(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":CPEak[:STATe]?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":CPEak[:STATe] " +str(param))
	def delta_set_center(*n):
		if len(n) == 0:
			inst.read("CALCulate:MARKer"+str(op)+":DELTa[:SET]:CENTer?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":DELTa[:SET]:CENTer " +str(param))
	def delta_set_span(*n):
		if len(n) == 0:
			inst.read("CALCulate:MARKer"+str(op)+":DELTa[:SET]:SPAN?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":DELTa[:SET]:SPAN " +str(param))
	def function(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":FUNCtion?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":FUNCtion " +str(param))
	def maximum_left(*n):
		if len(n) == 0:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:LEFT?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:LEFT " +str(param))
	def maximum_max(*n):
		if len(n) == 0:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:MAX?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:MAX " +str(param))
	def maximum_next(*n):
		if len(n) == 0:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:NEXT?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:NEXT " +str(param))
	def maximum_right(*n):
		if len(n) == 0:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:RIGHt?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:RIGHt " +str(param))
	def minimum(*n):
		if len(n) == 0:
			inst.read("CALCulate:MARKer"+str(op)+":MINimum?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":MINimum " +str(param))
	def mode(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":MODE?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":MODE " +str(param))
	def peak_excursion(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":PEAK:EXCursion?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":PEAK:EXCursion " +str(param))
	def peak_search_mode(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":PEAK:SEARch:MODE?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":PEAK:SEARch:MODE " +str(param))
	def peak_set_cf(*n):
		if len(n) == 0:
			inst.read("CALCulate:MARKer"+str(op)+":PEAK[:SET]:CF?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":PEAK[:SET]:CF " +str(param))
	def peak_threshold(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":PEAK:THReshold?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":PEAK:THReshold " +str(param))
	def ptpeak(*n):
		if len(n) == 0:
			inst.read("CALCulate:MARKer"+str(op)+":PTPeak?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":PTPeak " +str(param))
	def set_center(*n):
		if len(n) == 0:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:CENTer?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:CENTer " +str(param))
	def set_rlevel(*n):
		if len(n) == 0:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:RLEVel?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:RLEVel " +str(param))
	def set_start(*n):
		if len(n) == 0:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:STARt?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:STARt " +str(param))
	def set_step(*n):
		if len(n) == 0:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:STEP?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:STEP " +str(param))
	def set_stop(*n):
		if len(n) == 0:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:STOP?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:STOP " +str(param))
	def state(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":STATe?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":STATe " +str(param))
	def trace(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":TRACe?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":TRACe " +str(param))
	def trace_auto(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":TRACe:AUTO?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":TRACe:AUTO " +str(param))
	def x(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":X?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X " +str(param))
	def x_center(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":X:CENTer?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:CENTer " +str(param))
	def x_position(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":X:POSition?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:POSition " +str(param))
	def x_position_center(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":X:POSition:CENTer?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:POSition:CENTer " +str(param))
	def x_position_span(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":X:POSition:SPAN?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:POSition:SPAN " +str(param))
	def x_position_start(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":X:POSition:STARt?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:POSition:STARt " +str(param))
	def x_position_stop(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":X:POSition:STOP?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:POSition:STOP " +str(param))
	def x_readout(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":X:READout?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:READout " +str(param))
	def x_span(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":X:SPAN?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:SPAN " +str(param))
	def x_start(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":X:STARt?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:STARt " +str(param))
	def x_stop(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":X:STOP?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:STOP " +str(param))
	def y(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer"+str(op)+":Y?")
		else:
			inst.query("CALCulate:MARKer"+str(op)+":Y " +str(param))
	def table_state(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer:TABLe:STATe?")
		else:
			inst.write("CALCulate:MARKer:TABLe:STATe " +str(param))
	def tracking_state(*n):
		if len(n) == 0:
			inst.query("CALCulate:MARKer:TRACking:STATe?")
		else:
			inst.write("CALCulate:MARKer:TRACking:STATe " +str(param))

class ntdata:
	def __init__(self):
		INFO_NO_PARAM="no admite parametro, se envia consulta"
	def state(*n):
		if len(n) == 0:
			inst.query("CALCulate:NTData[:STATe]?")
		else:
			inst.write("CALCulate:NTData[:STATe] " +str(param))
class calculate:
	def __init__(self):
		self.bandwidth=bandwidth()
		self.lline=lline()
		self.marker=marker()
		self.ntdata=ntdata()
