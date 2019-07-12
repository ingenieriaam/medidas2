import visa
rm = visa.ResourceManager()
a = rm.list_resources()
inst = rm.open_resource(a[0])
class common:
	def identify(*n):
		if len(n) == 1:
			return inst.query("*IDN?")
		else:
			print("no admite parametro, se envia consulta")
			return inst.query("*IDN?")
	def close(self):
		inst.close()
class bandwidth:

	def ndb(*n):
		if len(n) == 1:
			inst.query("CALCulate:BANDwidth:NDB?")
		else:
			inst.write("CALCulate:BANDwidth:NDB " +str(n[1]))
	def result(*n):
		if len(n) == 1:
			inst.query("CALCulate:BANDwidth:RESult?")
		else:
			inst.query("CALCulate:BANDwidth:RESult " +str(n[1]))

class lline:

	def all_delete(*n):
		if len(n) == 1:
			inst.write("CALCulate:LLINe:ALL:DELete")
		else:
			inst.write("CALCulate:LLINe:ALL:DELete")
	def control_domain(*n):
		if len(n) == 1:
			inst.query("CALCulate:LLINe:CONTrol:DOMain?")
		else:
			inst.write("CALCulate:LLINe:CONTrol:DOMain " +str(n[1]))
	def fail(*n):
		if len(n) == 1:
			inst.query("CALCulate:LLINe:FAIL?")
		else:
			inst.query("CALCulate:LLINe:FAIL " +str(n[1]))
	def fail_ratio(*n):
		if len(n) == 1:
			inst.query("CALCulate:LLINe:FAIL:RATIo?")
		else:
			inst.query("CALCulate:LLINe:FAIL:RATIo " +str(n[1]))
	def fail_stop_state(*n):
		if len(n) == 1:
			inst.query("CALCulate:LLINe:FAIL:STOP:STATe?")
		else:
			inst.write("CALCulate:LLINe:FAIL:STOP:STATe " +str(n[1]))
	def control_interpolate_type(*n):
		if len(n) == 1:
			inst.query("CALCulate:LLINe"+str(op)+":CONTrol:INTerpolate:TYPE?")
		else:
			inst.write("CALCulate:LLINe"+str(op)+":CONTrol:INTerpolate:TYPE " +str(n[1]))
	def data(*n):
		if len(n) == 1:
			inst.query("CALCulate:LLINe"+str(op)+":DATA?")
		else:
			inst.write("CALCulate:LLINe"+str(op)+":DATA " +str(n[1]))
	def data_merge(*n):
		if len(n) == 1:
			inst.write("CALCulate:LLINe"+str(op)+":DATA:MERGe?")
		else:
			inst.write("CALCulate:LLINe"+str(op)+":DATA:MERGe " +str(n[1]))
	def delete(*n):
		if len(n) == 1:
			inst.write("CALCulate:LLINe"+str(op)+":DELete?")
		else:
			inst.write("CALCulate:LLINe"+str(op)+":DELete " +str(n[1]))
	def relampt_state(*n):
		if len(n) == 1:
			inst.query("CALCulate:LLINe"+str(op)+":RELAmpt[:STATe]?")
		else:
			inst.write("CALCulate:LLINe"+str(op)+":RELAmpt[:STATe] " +str(n[1]))
	def relfreq_state(*n):
		if len(n) == 1:
			inst.query("CALCulate:LLINe"+str(op)+":RELFreq[:STATe]?")
		else:
			inst.write("CALCulate:LLINe"+str(op)+":RELFreq[:STATe] " +str(n[1]))
	def state(*n):
		if len(n) == 1:
			inst.query("CALCulate:LLINe"+str(op)+":STATe?")
		else:
			inst.write("CALCulate:LLINe"+str(op)+":STATe " +str(n[1]))

class marker:

	def aoff(*n):
		if len(n) == 1:
			inst.write("CALCulate:MARKer:AOFF")
		else:
			inst.write("CALCulate:MARKer:AOFF")
	def fcount_resolution(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer:FCOunt:RESolution?")
		else:
			inst.write("CALCulate:MARKer:FCOunt:RESolution " +str(n[1]))
	def fcount_resolution_auto(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer:FCOunt:RESolution:AUTO?")
		else:
			inst.write("CALCulate:MARKer:FCOunt:RESolution:AUTO " +str(n[1]))
	def fcount_x(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer:FCOunt:X?")
		else:
			inst.query("CALCulate:MARKer:FCOunt:X " +str(n[1]))
	def fcount_state(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer:FCOunt[:STATe]?")
		else:
			inst.write("CALCulate:MARKer:FCOunt[:STATe] " +str(n[1]))
	def cpeak_state(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":CPEak[:STATe]?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":CPEak[:STATe] " +str(n[1]))
            
            
            
	def delta_set_center(*n):
		if len(n) == 1:
			inst.read("CALCulate:MARKer"+str(op)+":DELTa[:SET]:CENTer?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":DELTa[:SET]:CENTer " +str(n[1]))
	def delta_set_span(*n):
		if len(n) == 1:
			inst.read("CALCulate:MARKer"+str(op)+":DELTa[:SET]:SPAN?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":DELTa[:SET]:SPAN " +str(n[1]))
            
            
	def function(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":FUNCtion?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":FUNCtion " +str(n[1]))
	def maximum_left(*n):
		if len(n) == 1:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:LEFT?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:LEFT " +str(n[1]))
	def maximum_max(*n):
		if len(n) == 1:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:MAX?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:MAX " +str(n[1]))
	def maximum_next(*n):
		if len(n) == 1:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:NEXT?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:NEXT " +str(n[1]))
	def maximum_right(*n):
		if len(n) == 1:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:RIGHt?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":MAXimum:RIGHt " +str(n[1]))
	def minimum(*n):
		if len(n) == 1:
			inst.read("CALCulate:MARKer"+str(op)+":MINimum?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":MINimum " +str(n[1]))
	def mode(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":MODE?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":MODE " +str(n[1]))
	def peak_excursion(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":PEAK:EXCursion?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":PEAK:EXCursion " +str(n[1]))
	def peak_search_mode(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":PEAK:SEARch:MODE?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":PEAK:SEARch:MODE " +str(n[1]))
	def peak_set_cf(*n):
		if len(n) == 1:
			inst.read("CALCulate:MARKer"+str(op)+":PEAK[:SET]:CF?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":PEAK[:SET]:CF " +str(n[1]))
	def peak_threshold(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":PEAK:THReshold?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":PEAK:THReshold " +str(n[1]))
	def ptpeak(*n):
		if len(n) == 1:
			inst.read("CALCulate:MARKer"+str(op)+":PTPeak?")
		else:
			inst.read("CALCulate:MARKer"+str(op)+":PTPeak " +str(n[1]))
	def set_center(*n):
		if len(n) == 1:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:CENTer?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:CENTer " +str(n[1]))
	def set_rlevel(*n):
		if len(n) == 1:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:RLEVel?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:RLEVel " +str(n[1]))
	def set_start(*n):
		if len(n) == 1:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:STARt?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:STARt " +str(n[1]))
	def set_step(*n):
		if len(n) == 1:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:STEP?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:STEP " +str(n[1]))
	def set_stop(*n):
		if len(n) == 1:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:STOP?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+"[:SET]:STOP " +str(n[1]))
	def state(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":STATe?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":STATe " +str(n[1]))
	def trace(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":TRACe?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":TRACe " +str(n[1]))
	def trace_auto(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":TRACe:AUTO?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":TRACe:AUTO " +str(n[1]))
	def x(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":X?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X " +str(n[1]))
	def x_center(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":X:CENTer?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:CENTer " +str(n[1]))
	def x_position(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":X:POSition?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:POSition " +str(n[1]))
	def x_position_center(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":X:POSition:CENTer?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:POSition:CENTer " +str(n[1]))
	def x_position_span(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":X:POSition:SPAN?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:POSition:SPAN " +str(n[1]))
	def x_position_start(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":X:POSition:STARt?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:POSition:STARt " +str(n[1]))
	def x_position_stop(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":X:POSition:STOP?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:POSition:STOP " +str(n[1]))
	def x_readout(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":X:READout?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:READout " +str(n[1]))
	def x_span(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":X:SPAN?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:SPAN " +str(n[1]))
	def x_start(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":X:STARt?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:STARt " +str(n[1]))
	def x_stop(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":X:STOP?")
		else:
			inst.write("CALCulate:MARKer"+str(op)+":X:STOP " +str(n[1]))
	def y(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer"+str(op)+":Y?")
		else:
			inst.query("CALCulate:MARKer"+str(op)+":Y " +str(n[1]))
	def table_state(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer:TABLe:STATe?")
		else:
			inst.write("CALCulate:MARKer:TABLe:STATe " +str(n[1]))
	def tracking_state(*n):
		if len(n) == 1:
			inst.query("CALCulate:MARKer:TRACking:STATe?")
		else:
			inst.write("CALCulate:MARKer:TRACking:STATe " +str(n[1]))
            
class sense:

	def freq_center(*n):
		if len(n) == 1:
			return inst.query(":SENSe:FREQuency:CENTer?")
		else:
			inst.write(":SENSe:FREQuency:CENTer " +str(n[1]))
	def freq_span(*n):
		if len(n) == 1:
			return inst.query(":SENSe:FQuency:SPAN?")
		else:
			inst.write(":SENSe:FREQuency:SPAN "+str(n[1]))       
class ntdata:

	def state(*n):
		if len(n) == 1:
			inst.query("CALCulate:NTData[:STATe]?")
		else:
			inst.write("CALCulate:NTData[:STATe] " +str(n[1]))
class calculate:
	def __init__(self):
		self.bandwidth=bandwidth()
		self.lline=lline()
		self.marker=marker()
		self.ntdata=ntdata()
		self.sense=sense()
		self.common=common()
class auto:

	def auto(*n):
		if len(n) == 1:
			inst.query("CALibration:AUTO?")
		else:
			inst.write("CALibration:AUTO " +str(n[1]))
class calibration:
	def __init__(self):
		self.auto=auto()
class rigol:
	def __init__(self):
		self.calculate=calculate()
		self.calibration=calibration()
