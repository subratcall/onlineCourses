#temperatur converter

tempC = raw_input('temperature in Celcius = ')

tempC_F = 0;
try:
	tempC_F = float(tempC)
except:
	tempC_F = -999999
	

if (tempC_F != -999999):
	tempF = tempC_F * 9.0/5.0 + 32.0
	print 'temp in fahrenheit = ', tempF
else:
	print 'wrong input'
