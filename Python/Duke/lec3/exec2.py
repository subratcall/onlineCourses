inp = raw_input('input score: ')
inpF = 0.0

try:
	inpF = float(inp)
except:
	inpF = -1.0

print inpF
if (inpF >= 0.0 and inpF <= 1.0):
	if inpF >= 0.9:
		print 'A'
	elif inpF >= 0.8:
		print 'B'
	elif inpF >= 0.7:
		print 'C'
	elif inpF >= 0.6:
		print 'D'
	else:
		print 'F'
else:
	print 'score is invalid'
	

		

