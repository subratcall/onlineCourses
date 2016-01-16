hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)
pay = 0.0
if hrs > 40.0:
	pay = 40.0 * r + (h-40.0)*1.5*r
else:
	pay = h * r

print pay

