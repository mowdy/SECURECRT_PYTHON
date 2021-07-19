# $language = "python"
# $interface = "1.0"

# Connect to an SSH server using the SSH2 protocol. Specify the
# username and password and hostname on the command line as well as
# some SSH2 protocol specific options.

host = "localhost"
user = "mowdy"
pwd = "mowdy"

COMMANDS = [
    "date",
    "cat /home/mowdy/test_20210716/SHOW_S_V_R_gdvolteas1_ROOT_20210601_2112.txt",
	]

#currentTab = crt.GetScriptTab()
currentTab = crt.GetActiveTab()

def main():
	# Prompt for a password instead of embedding it in a script...
	#
#	passwd = crt.Dialog.Prompt("Enter password for " + host, "Login", "", True)

	# Build a command-line string to pass to the Connect method.
#	cmd = "/SSH2 /L %s /PASSWORD %s %s" % (user, pwd, host)
#	cmd = "/SSH2 /PASSWORD mowdy mowdy@localhost"
	cmd = "/SSH2 /PASSWORD %s %s@%s" % (pwd, user,host)

	crt.Session.Connect(cmd)

def log():
#    tabCap = currentTab.Caption
#    crt.Dialog.MessageBox(tabCap)
    currentSession = currentTab.Session

#SET LOG FILE NAME; IF "Start log upon connect IS CHECKED ON GUI, THIS CONFIG WON'T TAKE EFFECT.
    currentSession.LogFileName = "C:\Users\mowdy\Documents\LOG_SECURECRT\%Y_%M_%D_%h_%m_TO_%H_FROM_%USERNAME%@%COMPUTERNAME%_AUTO.log"
#ENABLE LOGGING; IF DISABLED FROM DEFAULT ENABLED, LOG FILE NAME WILL BE SET AS ABOVE, BUT WON'T TAKE EFFECT.
    currentSession.Log(False)
#EANBLE LOGGING AGAIN, SO NEW LOG FILE NAME WILL TAKE EFFECT, BUT TWO FILES WILL BE GENERATED;
    currentSession.Log(True)
#    crt.Dialog.MessageBox("CURRENT LOG STATUS: " + str(currentSession.Logging) + "\n\nCURRENT LOG FILE NAME: " + currentSession.LogFileName + "\n\nCURRENT SCRIPT: " + crt.ScriptFullName)

def sendCMD():
    for (index, command) in enumerate(COMMANDS):
        command = command.strip()
        currentTab.Screen.Send(command + '\r')
        currentTab.Screen.WaitForString('\r', 1)
        currentTab.Screen.WaitForString('\n', 1)

def disconn():
    currentSession = currentTab.Session
    currentSession.Disconnect() 



main()
log()
sendCMD()
while True:
    if not currentTab.Screen.WaitForCursor(3):
        disconn()
        crt.Dialog.MessageBox("FINISHED, AND DISCONNECTED~!")
        break

