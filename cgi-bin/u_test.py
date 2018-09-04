#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html\r\n\r\n")

print("<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css'>")

print("<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>")

print("<script src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.j'></script>")

print("<script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js'></script>")

print('<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">')

print("<script type= 'text/javascript'> \
		function newLocation() { \
			window.location = '/look/main.html'; \
		} \
	</script>");
	
import os
import sys
import argparse
import socket 
import datetime
from urlparse import urlparse

sys.path.append(os.path.dirname( os.path.abspath( __file__ )) + "/module")

from M_ccsinjection import *
from M_heartbleed import *
from M_poodle import *
from M_freak import *
from M_logjam import *
from M_drown import *
from M_crime import *
from M_anonymous import *
from C_display import *

#==============================================
displayMode=0
targetMode=0
output_ck=0
output_path="./a2sv_output.txt"

targetfileList = []
# Version 
myPath=os.path.dirname( os.path.abspath( __file__ ))
vfp = open(myPath+"/version","r")  #Version File Pointer
a2sv_version = vfp.read()
a2sv_version = a2sv_version.rstrip()
#==============================================

global targetIP
global port
global ccs_result
global heartbleed_result
global poodle_result
global freak_result
global logjam_result
global drown_result
global crime_result
global anonymous_result

ccs_result = "-1"
heartbleed_result = "-1"
poodle_result = "-1"
freak_result = "-1"
logjam_result = "-1"
drown_result = "-1"
crime_result = "-1"
anonymous_result = "-1"
#===========================
f = '18'
RED = '<b> <font color= "red" style= "font-size: ' + f + 'px; font-family: \'Merienda\', cursive;">'
GREEN = '<b> <font color= "green" style= "font-size: ' + f + 'px; font-family: \'Merienda\', cursive;">'
YELLOW = '<b> <font color= "yellow" style= "font-size: ' + f + 'px; font-family: \'Merienda\', cursive;">'
BLUE = '<b> <font color= "blue" style= "font-size: ' + f + 'px; font-family: \'Merienda\', cursive;">'
PURPLE = '<b> <font color= "purple" style= "font-size: ' + f + 'px; font-family: \'Merienda\', cursive;">'
VIOLET = '<b> <font color= "vioet" style= "font-size: ' + f + 'px; font-family: \'Merienda\', cursive;">'
END = '</font> </b>'

initmain()

## Report Table
class TablePrinter(object):
    "Print a list of dicts as a table"
    def __init__(self, fmt, sep=' ', ul=None):
        """        
        @param fmt: list of tuple(heading, key, width)
            heading: str, column label
            key: dictionary key to value to print
            width: int, column width in chars
        @param sep: string, separation between columns
        @param ul: string, character to underline column label, or None for no underlining
        """
        super(TablePrinter,self).__init__()
        self.fmt   = str(sep).join('{lb}{0}:{1}{rb}'.format(key, width, lb='{', rb='}') for heading,key,width in fmt)
        self.head  = {key:heading for heading,key,width in fmt}
        self.ul    = {key:str(ul)*width for heading,key,width in fmt} if ul else None
        self.width = {key:width for heading,key,width in fmt}

    def row(self, data):
        return self.fmt.format(**{ k:str(data.get(k,''))[:w] for k,w in self.width.iteritems() })

    def __call__(self, dataList):
        _r = self.row
        res = [_r(data) for data in dataList]
        res.insert(0, _r(self.head))
        if self.ul:
            res.insert(1, _r(self.ul))
        return '\n'.join(res)
########################

def mainScreen():
    os.system('cls' if os.name=='nt' else 'clear')
    '''
    showDisplay(displayMode,"                               A_A")
    showDisplay(displayMode,"                                   (-.-)")
    showDisplay(displayMode,"                              /   h ")
    showDisplay(displayMode,"                             |     |   __ ")
    showDisplay(displayMode,"                             |  || |  |  t__  ")
    showDisplay(displayMode,"                              t_|| /_/ ")
    showDisplay(displayMode,"                              &#9608;&#9608;&#9608;&#9608;&#9608;&#9559; &#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9559; &#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9559;&#9608;&#9608;&#9559;   &#9608;&#9608;&#9559; ")
    showDisplay(displayMode,"                             &#9608;&#9608;&#9556;&#9552;&#9552;&#9608;&#9608;&#9559;&#9562;&#9552;&#9552;&#9552;&#9552;&#9608;&#9608;&#9559;&#9608;&#9608;&#9556;&#9552;&#9552;&#9552;&#9552;&#9565;&#9608;&#9608;&#9553;   &#9608;&#9608;&#9553; ")
    showDisplay(displayMode,"                             &#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9553; &#9608;&#9608;&#9608;&#9608;&#9608;&#9556;&#9565;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9559;&#9608;&#9608;&#9553;   &#9608;&#9608;&#9553; ")
    showDisplay(displayMode,"                             &#9608;&#9608;&#9556;&#9552;&#9552;&#9608;&#9608;&#9553;&#9608;&#9608;&#9556;&#9552;&#9552;&#9552;&#9565; &#9562;&#9552;&#9552;&#9552;&#9552;&#9608;&#9608;&#9553;&#9562;&#9608;&#9608;&#9559; &#9608;&#9608;&#9556;&#9565;")
    showDisplay(displayMode,"                             &#9608;&#9608;&#9553;  &#9608;&#9608;&#9553;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9559;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9553; &#9562;&#9608;&#9608;&#9608;&#9608;&#9556;&#9565; ")
    showDisplay(displayMode,"                             &#9562;&#9552;&#9565;  &#9562;&#9552;&#9565;&#9562;&#9552;&#9552;&#9552;&#9552;&#9552;&#9552;&#9565;&#9562;&#9552;&#9552;&#9552;&#9552;&#9552;&#9552;&#9565;  &#9562;&#9552;&#9552;&#9552;&#9565;  ")
    showDisplay(displayMode,BLUE+" [Auto Scanning to SSL Vulnerability "+a2sv_version+"]"+END)
    showDisplay(displayMode,VIOLET+" by HaHwul (www.hahwul.com)"+END)
    '''
    showDisplay(displayMode,"<br />")

def runScan(s_type):
    global ccs_result
    global heartbleed_result
    global poodle_result
    global freak_result
    global logjam_result
    global drown_result
    global crime_result
    global anonymous_result
    
    print " "
    # SSL Check Logic --------------------------- 
    showDisplay(displayMode,GREEN+" Check the SSL.."+END)
    result = subprocess.Popen(['timeout','4','openssl','s_client','-connect',targetIP+":"+str(port)], stderr=subprocess.STDOUT, stdout=subprocess.PIPE).communicate()[0]
    if "Connection refused" in result:
        showDisplay(displayMode,RED+" This target does not support SSL.."+END)
    # ------------------------------------------------------
    else:
        showDisplay(displayMode,GREEN+" This target supports SSL.."+END)
        if s_type == "anonymous":
            showDisplay(displayMode,GREEN+" <h2>Scan Anonymous Cipher..</h2>"+END)
            anonymous_result = m_anonymous_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" Anonymous Cipher :: "+anonymous_result+END)
        elif s_type == "crime":
            showDisplay(displayMode,GREEN+" Scan CRIME(SPDY).."+END)
            crime_result = m_crime_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" CRIME(SPDY) :: "+crime_result+END)
        elif s_type == "heart":
            showDisplay(displayMode,GREEN+" Scan HeartBleed.."+END)
            heartbleed_result = m_heartbleed_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" HeartBleed :: "+heartbleed_result+END)
        elif s_type == "ccs":
            showDisplay(displayMode,GREEN+" Scan CCS Injection.."+END)
            ccs_result = m_ccsinjection_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" CCS Injection :: "+ccs_result+END)
        elif s_type == "poodle":
            showDisplay(displayMode,GREEN+" Scan SSLv3 POODLE.."+END)
            poodle_result = m_poodle_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" SSLv3 POODLE :: "+poodle_result+END)
        elif s_type == "freak":
            showDisplay(displayMode,GREEN+" Scan OpenSSL FREAK.."+END)
            freak_result = m_freak_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" OpenSSL FREAK :: "+freak_result+END)
        elif s_type == "logjam":
            showDisplay(displayMode,GREEN+" Scan OpenSSL LOGJAM.."+END)
            logjam_result = m_logjam_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" OpenSSL LOGJAM :: "+logjam_result+END)
        elif s_type == "drown":
            showDisplay(displayMode,GREEN+" Scan SSLv2 DROWN.."+END)
            logjam_result = m_drown_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" SSLv2 DROWN :: "+drown_result+END)
        else:
            showDisplay(displayMode,GREEN+" Scan Anonymous Cipher.."+END)
            anonymous_result = m_anonymous_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" Scan CRIME(SPDY).."+END)
            crime_result = m_crime_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" Scan CCS Injection.."+END)
            ccs_result = m_ccsinjection_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" Scan HeartBleed.."+END)
            heartbleed_result = m_heartbleed_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" Scan SSLv3 POODLE.."+END)
            poodle_result = m_poodle_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" Scan OpenSSL FREAK.."+END)
            freak_result = m_freak_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" Scan OpenSSL LOGJAM.."+END)
            logjam_result = m_logjam_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" Scan SSLv2 DROWN.."+END)
            drown_result = m_drown_run(targetIP,port,displayMode)
            showDisplay(displayMode,GREEN+" Finish scan all vulnerability.."+END)

def outVersion():
    print "A2SV v"+a2sv_version

def updateVersion():
    print GREEN+" Update A2SV"+END
    print GREEN+" This A2SV version is .. v"+a2sv_version+END
    os.chdir(os.path.dirname( os.path.abspath( __file__ )))
    os.system("git reset --hard HEAD")
    os.system("git pull -v")
    vfp = open(myPath+"/version","r")  #Version File Pointer
    print RED+" Updated A2SV"+END

def outReport(o_ck,o_path,tmode):
    global ccs_result
    global heartbleed_result
    global poodle_result
    global freak_result
    global logjam_result
    global drown_result
    global crime_result
    global anonymous_result
    if anonymous_result == "0x01":
        anonymous_result = "Vulnerable!"
    elif anonymous_result == "0x00":
        anonymous_result = "Not Vulnerable."
    elif anonymous_result == "0x02":
        anonymous_result = "Exception."        
    else:
        anonymous_result = "Not Scan."
    if crime_result == "0x01":
        crime_result = "Vulnerable!"
    elif crime_result == "0x00":
        crime_result = "Not Vulnerable."
    elif crime_result == "0x02":
        crime_result = "Exception."        
    else:
        crime_result = "Not Scan."
    if ccs_result == "0x01":
        ccs_result = "Vulnerable!"
    elif ccs_result == "0x00":
        ccs_result = "Not Vulnerable."
    elif ccs_result == "0x02":
        ccs_result = "Exception."        
    else:
        ccs_result = "Not Scan."
    if heartbleed_result == "0x01":
        heartbleed_result = "Vulnerable!"
    elif heartbleed_result == "0x00":
        heartbleed_result = "Not Vulnerable."
    elif heartbleed_result == "0x02":
        heartbleed_result = "Exception"
    else:
        heartbleed_result = "Not Scan."
    if poodle_result == "0x01":
        poodle_result = "Vulnerable!"
    elif poodle_result == "0x00":
        poodle_result = "Not Vulnerable."
    elif poodle_result == "0x02":
        poodle_result = "Exception"
    else:
        poodle_result = "Not Scan."
    if freak_result == "0x01":
        freak_result = "Vulnerable!"
    elif freak_result == "0x00":
        freak_result = "Not Vulnerable."
    elif freak_result == "0x02":
        freak_result = "Exception"
    else:
        freak_result = "Not Scan."
    if logjam_result == "0x01":
        logjam_result = "Vulnerable!"
    elif logjam_result == "0x00":
        logjam_result = "Not Vulnerable."
    elif logjam_result == "0x02":
        logjam_result = "Exception"
    else:
        logjam_result = "Not Scan."
    if drown_result == "0x01":
        drown_result = "Vulnerable!"
    elif drown_result == "0x00":
        drown_result = "Not Vulnerable."
    elif drown_result == "0x02":
        drown_result = "Exception"
    else:
        drown_result = "Not Scan."

	#----------- Template -----------
	#    if logjam_result == "0x01":
	#        logjam_result = "Vulnerable!"
	#    elif logjam_result == "0x00":
	#        logjam_result = "Not Vulnerable."
	#    else:
	#        logjam_result = "Not Scan."
	#----------- -------- -----------

    data = [
    {'v_vuln':'Anonymous Cipher', 'v_cve':'CVE-2007-1858', 'cvss':'AV:N/AC:H/Au:N/C:P/I:N/A:N', 'v_state':anonymous_result},
    {'v_vuln':'CRIME(SPDY)', 'v_cve':'CVE-2012-4929', 'cvss':'AV:N/AC:H/Au:N/C:P/I:N/A:N', 'v_state':crime_result},
    {'v_vuln':'HeartBleed', 'v_cve':'CVE-2014-0160', 'cvss':'AV:N/AC:L/Au:N/C:P/I:N/A:N', 'v_state':heartbleed_result},
    {'v_vuln':'CCS Injection', 'v_cve':'CVE-2014-0224', 'cvss':'AV:N/AC:M/Au:N/C:P/I:P/A:P', 'v_state':ccs_result},
    {'v_vuln':'SSLv3 POODLE', 'v_cve':'CVE-2014-3566', 'cvss':'AV:N/AC:M/Au:N/C:P/I:N/A:N', 'v_state':poodle_result},    
    {'v_vuln':'OpenSSL FREAK', 'v_cve':'CVE-2015-0204', 'cvss':'AV:N/AC:M/Au:N/C:N/I:P/A:N', 'v_state':freak_result},
    {'v_vuln':'OpenSSL LOGJAM', 'v_cve':'CVE-2015-4000', 'cvss':'AV:N/AC:M/Au:N/C:N/I:P/A:N', 'v_state':logjam_result},
    {'v_vuln':'SSLv2 DROWN', 'v_cve':'CVE-2016-0800', 'cvss':'AV:N/AC:M/Au:N/C:P/I:N/A:N', 'v_state':drown_result}
    ]

    fmt = [
    ("Vulnerability", 'v_vuln', 16),
    ("CVE", 'v_cve', 13),
    ("CVSS v2 Base Score", 'cvss', 26),
    ("State", 'v_state', 15)
    ]

    if o_ck == 1:
    	print("The result is in \""+str(o_path)+"\".")
    	if t_mode == 1:
    		of = open(str(o_path),'a')
    		of.write(" [TARGET]: "+targetIP+"<br />")
    		of.write(" [PORT]: "+str(port)+"\r\n<br />")
    		of.write(" [SCAN TIME]: "+str(datetime.datetime.now())+"\r\n<br />")
    		of.write(" [VULNERABILITY]"+"\r\n<br />")
    		of.write(TablePrinter(fmt, ul='=')(data))
    		of.write("\r\n<br />")
    	else:
    		of = open(str(o_path),'w')
    		of.write(" [TARGET]: "+targetIP+"\r\n<br />")
    		of.write(" [PORT]: "+str(port)+"\r\n<br />")
    		of.write(" [SCAN TIME]: "+str(datetime.datetime.now())+"\r\n<br />")
    		of.write(" [VULNERABILITY]"+"\r\n<br />")
    		of.write(TablePrinter(fmt, ul='=')(data))
    		of.write("\r\n<br />")
    else:
    	open(str('/opt/lampp/htdocs/look/result.html'), 'w').close()
    	of = open(str('/opt/lampp/htdocs/look/result.html'), 'w')

    	of.write("<!DOCTYPE html> \n <html> \n <head>" + "\n")
    	of.write('<link href="https://fonts.googleapis.com/css?family=Merienda" rel="stylesheet"> ')
    	of.write("<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css'>" + "\n")
    	of.write("<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>" + "\n")
    	of.write("<script src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js'></script>" + "\n")
    	of.write("<script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js'></script>" + "\n")
    	of.write('<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">' + '\n')
    	of.write("<body> <h5 style= 'font-size:60px; text-align:center; font-family:Verdana;'> REPORT </h1> <br />" + "\n")

    	of.write("<font color= 'blue'>" + " [TARGET]: " + targetIP + END + "<br />" + "\n")
    	of.write("<font color= 'blue'>" + " [PORT]: " + str(port) + END + "<br />" + "\n")
    	of.write("<font color= 'blue'>" + " [SCAN TIME]: " + str(datetime.datetime.now())+END + "<br /> <br />" + "\n")
    	of.write("<center> <font color= 'red'>" + " [VULNERABILITY]" + END + "<br /> </center>" + "\n")

    	of.write("<table border class='w3-table-all'>" + "\n")
    	of.write("<tr class='w3-red'>" + "\n")
    	for f in fmt:
    		of.write("<th style='text-align:center;'> " + f[0] + "\n")

    	for d in data:
    		if d['v_state'] == "Vulnerable!":
    			of.write("<tr> " + "\n")
	    		for ind in d.keys():
	    			of.write("<td> " + d[ind] + "\n")

    	of.write("</table> \n </body> \n </html>")
        of.close()
    	#print( TablePrinter(fmt, ul='=')(data) )

###MAIN##
parser = argparse.ArgumentParser("a2sv",formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-t","--target", help="Target URL and IP Address\n > e.g -t 127.0.0.1")
parser.add_argument("-tf","--targetfile", help="Target file(list) URL and IP Address\n > e.g -tf ./target.list")
parser.add_argument("-p","--port", help="Custom Port / Default: 443\n > e.g -p 8080")
parser.add_argument("-m","--module", help="Check SSL Vuln with one module\n[anonymous]: Anonymous Cipher\n[crime]: Crime(SPDY)\n[heart]: HeartBleed\n: CCS Injection\n[poodle]: SSLv3 POODLE\n[freak]: OpenSSL FREAK\n[logjam]: OpenSSL LOGJAM\n[drown]: SSLv2 DROWN")
parser.add_argument("-d","--display", help="Display output\n Show output\n Hide output")
parser.add_argument("-o","--out", help="Result write to file\n > e.g -o /home/yourdir/result.txt")
parser.add_argument("-u","--update", help="Update A2SV (GIT)",action='store_true')
parser.add_argument("-v","--version", help="Show Version",action='store_true')
args = parser.parse_args()

input_data = cgi.FieldStorage()

args.target = str(input_data["ip"].value)

if args.version:
    outVersion()
    exit()
if args.update:
    updateVersion()
    exit()
if args.display:
    disoption = args.display
    if((disoption == "n") or (disoption == "N")):
		print "Running a2sv sillent mode"
		displayMode = 1
    else:
		displayMode = 0
if args.target:
    target = args.target
    showDisplay(displayMode,BLUE+" Target => "+args.target+END)
    targetIP = socket.gethostbyname(target)
    showDisplay(displayMode,BLUE+" IP Address => "+targetIP+END)
elif args.targetfile:
    f = open(args.targetfile,"r")
    showDisplay(displayMode,BLUE+" Target => "+args.targetfile+END)
    showDisplay(displayMode,BLUE+" IP Address list"+END)
    line = f.readline()
    while line:
        targetfileList.append(socket.gethostbyname(line.rstrip('\n')))
        showDisplay(displayMode,BLUE+"       => "+str(targetfileList)+END)
        line = f.readline()        
    targetMode = 1
    displayMode = 1
    print "Running a2sv sillent mode[file list default]"
    f.close()
else:
    mainScreen()
    showDisplay(displayMode,"Please Input Target Argument / -h --help")
    exit()
if args.port:
    port = int(args.port)
    showDisplay(displayMode,BLUE+" Target port => "+args.port+END)
else:
    port = 443
    showDisplay(displayMode,BLUE+" Target port => 443"+END)
if args.module:
    checkVun = args.module
    ModuleName = args.module
    if ModuleName == "ccs":
        ModuleName = "CCS Injection"
    elif ModuleName == "heart":
        ModuleName = "HeartBleed"
    elif ModuleName == "poodle":
        ModuleName = "SSLv3 POODLE Attack"
    elif ModuleName == "freak":
        ModuleName = "OpenSSL FREAK Attack"
    elif ModuleName == "logjam":
        ModuleName = "OpenSSL LOGJAM Attack"
    elif ModuleName == "drown":
        ModuleName = "SSLv2 DROWN Attack"
    elif ModuleName == "crime":
        ModuleName = "CRIME(SPDY)"
    elif ModuleName == "anonymous":
        ModuleName = "Anonymous Cipher Suite"
    showDisplay(displayMode,BLUE+" include => "+ModuleName+" Module"+END)
else:
    checkVun = "all"
    #showDisplay(displayMode,BLUE+" include => All Module"+END)

if args.out:
	output_path = args.out
	output_ck = 1
else:
	output_ck = 0

if displayMode == 0:
	mainScreen()
if targetMode == 1:
    i=0
    imax = len(targetfileList)
    #print "_________________________________________________________________________ <br />"
    print("<hr />")
    print("<h1 style='font-size:30px;text-align:center;'> REPORT </h1> <br />")
    while(i<imax):
        targetIP = targetfileList.pop()
        runScan(checkVun)
        outReport(output_ck,output_path,targetMode)
        i+=1
    #print "_________________________________________________________________________<br />"
    print("<hr />")
else:
    runScan(checkVun)
    #print("<hr />")
    #print "                             [A2SV REPORT]                                      <br />"
    #print("<hr />")

    outReport(output_ck,output_path,targetMode)
    #print "_________________________________________________________________________<br />"
    #print("<hr />")

showDisplay(displayMode,RED+" Scan Finish!"+END)
print("<script type= 'text/javascript'> newLocation(); </script>")