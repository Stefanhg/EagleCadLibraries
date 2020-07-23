import os
defaultDeviceSet = []

for lines in open("deviceset_0402.txt", "r"): 
	defaultDeviceSet.append(lines)

def replaceInList(myList, OldValue, NewValue):
	newList = []
	# For every line, if line include OldValue, replace with NewValue
	for lines in myList:
		if(int(lines.find(OldValue)) + 1):
			lines = lines.replace(OldValue, NewValue)
		newList.append(lines)
	
	return(newList)

try:
	os.remove("_newLibParts.txt") # Removes the file
except:
	pass # File already removed

for lines in open("devicesets_resistors.txt", "r"): 
	currentValue = lines.rstrip()
	currentModifValue = currentValue
	# Converts 1.5k into 1k5 or 1.5R into 1R5
	if ( (currentValue.find("R") + 1 or currentValue.find("K")+ 1 or currentValue.find("M")+ 1 ) and currentValue.find(".") + 1):
		if ( currentValue.find("R") + 1):
			currentModifValue = currentValue.replace("R", "")
			currentModifValue = currentModifValue.replace(".", "R")
		if ( currentValue.find("K") + 1):
			currentModifValue = currentValue.replace("K", "")
			currentModifValue = currentModifValue.replace(".", "K")
		if ( currentValue.find("M") + 1 ):
			currentModifValue = currentValue.replace("M", "")
			currentModifValue = currentModifValue.replace(".", "M")

	print(currentModifValue)
	# Replaces the two value variabels
	newDeviceSet = replaceInList(defaultDeviceSet, "$VALUE$", currentModifValue)
	newDeviceSet = replaceInList(newDeviceSet, "$TrueVALUE$", currentValue)
	f = open("_newLibParts.txt", "a+")
	for lines in newDeviceSet:
		
		f.write(lines)
	f.close()
	


	