import sys
import nams
def le32(a, b):
	return a[b] | a[b+1] << 8 | a[b+2] << 16 | a[b+3] << 24
def be32(a, b):
	return a[b+3] | a[b+2] << 8 | a[b+1] << 16 | a[b] << 24
with open(sys.argv[1], "rb") as infile:
	indata = infile.read()
for i in range(0, len(indata), 4):
	d = le32(indata, i)
	
	print(hex(i), nams.getinst(d), hex(d))
