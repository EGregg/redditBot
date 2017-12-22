import os

credentialsFile = 'config.py'

#creates credentials file if not present
def configPresent():
	try:
	        open(credentialsFile,'r')
	except:
		open(credentialsFile,'w')
	
	if os.stat(credentialsFile).st_size == 0:
		configWriter()

#asks for username and password to be written to credentials file
def configWriter():
	username = input('create username: ')
	password = input('create password: ')
	fd = open(credentialsFile,"w")
	fd.write("username = '%s'\n" % (username))
	fd.write("password = '%s'" % (password))

