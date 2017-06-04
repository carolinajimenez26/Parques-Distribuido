import socket, select
import string


#Function to broadcast chat messages to all connected clients
def broadcast_data (sock, message, CONNECTION_LIST):
	#Do not send the message to master socket and the client who has send us the message
	for socket in CONNECTION_LIST:
		if socket != server_socket and socket != sock :
			try :
				socket.send(message)
			except :
				# broken socket connection may be, chat client pressed ctrl+c for example
				socket.close()
				CONNECTION_LIST.remove(socket)


def sendData(sock, CONNECTION_LIST):
	print ("sendData")
	f = open("users.txt",'r')
	data = f.read()
	print("data: ", data)
	f.close()
	if (len(data) == 0):
		return
	for socket in CONNECTION_LIST:
		if socket != server_socket:
			try :
				socket.send(data)
			except :
				socket.close()
				CONNECTION_LIST.remove(socket)
	print ("fin sendData")

def getUsername(sock, dic):
	for u,s in dic.items():
		if s == sock:
			return u
	print "usuario no encontrado"
	return None


def verifyUser(new_client, dic, CONNECTION_LIST, sock,COLOR_LIST, users_colors):
	while True:
		#new_client.send("Ingresa un nombre de usuario: ")
		user = new_client.recv(1024).split(":")
		print "User: %s" %user
		if (len(user) == 0): # error
			continue
		if (user[1] not in COLOR_LIST):
			new_client.send("Color ya ha sido utilizado\n")
		elif (user[0] in dic):
			new_client.send("Nombre de usuario ya ha sido utilizado\n")

		else:
			COLOR_LIST.remove(user[1])
			CONNECTION_LIST.append(new_client)
			dic[user[0]] = new_client
			users_colors[user[0]] = user[1]
			new_client.send("Bienvenido")
			break
	return string.join(user,"")

# Encuentra el socket segun un nombre de usuario
def getSocket(username, dic):
	for u,s in dic.items():
		if u == username:
			return s
	print "Socket no encontrado"
	return None

# Retorna el indice de un nombre de usuario
def getIndex(username, dic, CONNECTION_LIST):
	s = getSocket(username, dic)
	return CONNECTION_LIST.index(s)


def save_user(data):
	f = open("users.txt",'a')
	for user,color in data.iteritems():
		f.write(user + ":" + color + "\n")

	f.close()

if __name__ == "__main__":

	# List to keep track of socket descriptors
	CONNECTION_LIST = [] # jugadores
	COLOR_LIST = ["green","red","yellow","blue"]
	RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
	PORT = 5000

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(("0.0.0.0", PORT))
	server_socket.listen(10)

	# Add server socket to the list of readable connections
	CONNECTION_LIST.append(server_socket) # no se tiene en cuenta esta primera posicion en los jugadores

	print ("Chat server started on port " + str(PORT))

	users_list = {}
	users_colors = {}

	f = open("users.txt",'w')
	f.close()

	while True:

		# Get the list sockets which are ready to be read through select
		read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

		for sock in read_sockets: # sockets entrantes
			# Nueva conexion
			if sock == server_socket:
				print ("Nueva conexion")
				# Handle the case in which there is a new connection recieved through server_socket
				sockfd, addr = server_socket.accept()
				# se admiten hasta 4 jugadores maximo
				if(len(CONNECTION_LIST) > 4):
					sockfd.send("Parques lleno, intentalo mas tarde")
					break

				# nuevo usuario
				username = verifyUser(sockfd, users_list, CONNECTION_LIST, sock, COLOR_LIST, users_colors)
				save_user(users_colors)

				#broadcast_data(sockfd, username, CONNECTION_LIST)
				sendData(sockfd,CONNECTION_LIST)

			#Some incoming message from a client
			else:
				# Data recieved from client, process it
				try:
					#In Windows, sometimes when a TCP program closes abruptly,
					# a "Connection reset by peer" exception will be thrown
					data = sock.recv(RECV_BUFFER)

					print ("Datos enviados al servidor : " + data)
					user = getUsername(sock, users_list)
					print ("Usuario que lo envio : " + user)

					if (data == "Necesito el orden de los turnos"):
						sock.send("green,red,yellow,blue")

					elif (data == ""):
						continue

					else :
						broadcast_data(sock, data, CONNECTION_LIST)

				except:
					broadcast_data(sock, "Client %s is out\n" %username, CONNECTION_LIST)
					print "Client (%s, %s) is offline" % addr
					CONNECTION_LIST.remove(sock)
					sock.close()
					continue

	server_socket.close()
