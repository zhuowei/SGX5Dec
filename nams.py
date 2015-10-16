ba_type1_subtypes = ["BA", "BR", "LAPC", "SETL", "SAVL", "NOP"]

def dump_rcp(instr):
	subtype = (instr >> 9) & 0x3;
	return ["RCP", "RSQ", "LOG", "EXP"][subtype]

def dump_min(instr):
	subtype = (instr >> 9) & 0x1;
	return ["MIN", "MAX"][subtype]

def dump_ba(instr):
	type1 = (instr >> 20) & 0x3;
	type1_subtype = (instr >> 6) & 0x7;
	twentyfour = (instr >> 24) & 0x7
	if type1 == 0:
		return ba_type1_subtypes[type1_subtype]
	elif type1 == 2: # register/mem operations
		return ["IDF", "WDF", "SETM", "EMIT", "LIMM", "LockOrRelease", "LdrOrStr", "WOP"][twentyfour]
	return "UnknownBA{},{}".format(type1, twentyfour)

def dump_dot3(instr):
	subtype = (instr >> 24) & 0x1;
	return ["DOT3", "DOT4"][subtype]

insts = [
	"MAD", ("RCP", dump_rcp), "DP", ("MIN", dump_min), "DSX", "MOVC", "FMAD16", "EFO", 
	"PCKUNPCK", "TEST", "AND", "XOR", "SHL", "SHR", "RLP", "TESTMASK",
	"SOP2", "SOP3", "SOPWM", "IMA8", "IMA16", "IMAE", "ADLF", "FIRH",
	("DOT3", dump_dot3), "FPMA", "Inst1A", "Inst1B", "SMP", "LD", "ST", ("BA", dump_ba)]
def getinst(d):
	o = (d >> 27) & 0x1f
	inst = insts[o]
	if isinstance(inst, str):
		return inst
	return inst[1](d)