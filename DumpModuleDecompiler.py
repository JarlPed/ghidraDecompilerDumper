#TODO write a description for this script
# @category: DecompilerDumper
#@author: Jarl Heer 
#@category Analysis
#@keybinding 
#@menupath 
#@toolbar 


import datetime



Dump = ""
decompInterface = ghidra.app.decompiler.DecompInterface()
decompInterface.openProgram(currentProgram)
for func in currentProgram.functionManager.getFunctions(True):
	decompileResults = decompInterface.decompileFunction(func, 300, monitor)
	while(decompileResults.decompileCompleted() != True):
		c=1
	if (decompileResults.decompileCompleted()):
		decompiledFunction = decompileResults.getDecompiledFunction()
		Dump += str(decompiledFunction.getC()).replace("\n", "")
		#print(decompiledFunction.getC())


f = open("Dump_"+str(datetime.datetime.now()).replace(":", "_") + ".cpp", "w")
f.write(Dump)
f.close()