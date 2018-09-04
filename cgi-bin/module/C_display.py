#===========================
#              Display option                  #
def showDisplay(mode,string):
	if(mode == 0):
		of = open(str("/opt/lampp/htdocs/look/main.html"), 'a')
		of.write(string + "<br />" + "\n")
		of.close()
	else:
		pass
#===========================
def setDisplay(mode):
	displayMode = mode

def initmain():
	of = open(str("/opt/lampp/htdocs/look/main.html"), 'w')
	of.write("<!DOCTYPE html> \n <html> \n <head>" + "\n")
	of.write('<link href="https://fonts.googleapis.com/css?family=Merienda" rel="stylesheet"> ')
	of.write("</head> \n <body bgcolor= '#DCDCDC'>")
	of.close()

#global displayMode
#displayMode = 0
#global displayMode
#global displayMode
#===========================
