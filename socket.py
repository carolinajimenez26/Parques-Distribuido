# telnet program example
import socket, select, string, sys
import pygame
import sys

class mySock():
	def __init__(self):
		self.host = "localhost"
    	self.port = 5000
    	self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	self.socket_list = [sys.stdin, self.s]

	def connect(self):
		# connect to remote host
	    try :
	        self.s.connect((self.host, self.port))
	    except :
	        print ('Unable to connect')
	        sys.exit()
	    print ('Connected to remote host. Start sending messages')

	def createUser(self, username):
		self.s.send(username)
		data = self.s.recv(4096)
        #print data
        if (data=="Parques lleno, intentalo mas tarde"):
        	self.s.close()
        	return False
        if (data == "Bienvenido al chat"):
        	return True       

def main():
	sock = mySock()
	sock.connect()
	correcto = False
	while not correcto:
		user = raw_input("Ingrese usuario")
		correcto = sock.createUser(user)
	sock.s.close()

main()
