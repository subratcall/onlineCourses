def greet(friend, money):
	if (friend and money >= 20):
		print "Hi!"
		money -= 20
	elif friend:
		print "Hi!"
	else:
		print "put uncle ben on my pocket dude"
		money += 100
	return money	

dolla = 15

dolla = greet(True, dolla)
print dolla

dolla = greet(False, dolla)
print dolla

dolla = greet(True, dolla)
print dolla