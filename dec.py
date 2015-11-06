import sys
import nams
def le32(a, b):
	return a[b] | a[b+1] << 8 | a[b+2] << 16 | a[b+3] << 24
def be32(a, b):
	return a[b+3] | a[b+2] << 8 | a[b+1] << 16 | a[b] << 24
def regnam(a, b):
	t = "i" if b & 1 else "c"
	return t + str(a)
def getinputs(d):
	b = d & 0x3f;
	types = (d >> 27)
	a = (d >> 7) & 0x3f
	atype = (types >> 4) & 0x3
	btype = (types >> 2) & 0x3
	detype = types & 0x3
	de = (d >> 21) & 0x3f
	return regnam(de, ~detype) + ", " + regnam(a, atype) + ", " + regnam(b, btype)
with open(sys.argv[1], "rb") as infile:
	indata = infile.read()
for i in range(0, len(indata), 8):
	d = le32(indata, i + 4)
	inputs = le32(indata, i)
	
	print(hex(i), hex(d), hex(inputs), nams.getinst(d), getinputs(inputs))
