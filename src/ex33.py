i = 0;
numbers = []
while i < 6:
	print "At the top i is %d" % i 
	numbers.append (i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	

print "The numbers: "
for num in numbers:
	print num
	

# Study drills

def create_list(iterations):
	iterator = 0;
	number_list = []
	while iterator < iterations:
		print "At the top iterator is %d" % iterator
		number_list.append(iterator)
		
		iterator = iterator + 1
		print "number_list now: ", number_list
		print "At the bottom iterator is %d" % iterator
		
create_list(3)