

maxmultiplier = 10000000
multiplier = 10


stringbuffer = ""
valuebuffer = ""
f = open("_newLibParts.txt", "a+")
for value in open("devicesets_resistors.txt", "r"): 
	value = float(value.rstrip())
	while value <= maxmultiplier:
		
		
		if(value < 100.0): 
			#stringbuffer = str(value) + "R"
			stringbuffer = str(value)
			stringbuffer = stringbuffer.replace(".","R")
			
		if(value >= 1e2 and value < 1e3): 
			stringbuffer = str(int(value)) + "R"
		if(value >= 1e3 and value < 1e5): 
			stringbuffer = str(float(value / 1000.0)) 
			stringbuffer = stringbuffer.replace(".","K")

		if(value >= 1e5 and value < 1e6): 
			stringbuffer = str(int(value / 1000.0)) + "K"
			
		if(value >= 1e6 and value < 1e8): 
			stringbuffer = str(value / 1000000.0)
			stringbuffer = stringbuffer.replace(".","M")
			
		

		
		stringbuffer = stringbuffer.replace(".0","")
		stringbuffer = stringbuffer.replace("R0","R")
		stringbuffer = stringbuffer.replace("K0","K")
		stringbuffer = stringbuffer.replace("M0","M")
		
		print(str(value) + "		" + stringbuffer)
		value = round(value * 10, 5)
		f.write(stringbuffer + "\n")

	
f.close()