largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == 'done':break
    
    numInt = None
    
    try:numInt = int(num)
    except:
		print 'invalid input'
		numInt = None
		continue
	
    
    if largest is None: largest = numInt
    elif numInt > largest: largest = numInt
    
    if smallest is None: smallest = numInt
    elif numInt < smallest: smallest = numInt   

print "Maximum is", largest
print "Minimum is", smallest



    #numInt = None
    #try:
		#numInt = int(num)
	#except:
		#numInt = None
	
	#if largest is None:
		#largest = numInt
	#elif numInt > largest:
		#largest = numInt
	
	#if smallest is None:
		#smallest = numInt
	#elif numInt < smallest:
		#smallest = numInt
		
