import socket, select

#Function to broadcast chat messages to all connected clients
def broadcast_data (sock, message):
    #Do not send the message to master socket and the client who has send us the message
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                CONNECTION_LIST.remove(socket)

def getUsername(sock, dic):
    for u,s in dic.items():
        if s == sock:
            return u
    print "usuario no encontrado"
    return None


def verifyUser(new_client, dic, CONNECTION_LIST, sock):
    while True:
        #new_client.send("Ingresa un nombre de usuario: ")
        user = new_client.recv(1024)
        print "User: %s" %user

        if (user in dic):
            new_client.send("Nombre de usuario ya ha sido utilizado\n")
        else:
            CONNECTION_LIST.append(new_client)
            dic[user] = new_client
            new_client.send("Bienvenido")
            break
    return user

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


if __name__ == "__main__":

    # List to keep track of socket descriptors
    CONNECTION_LIST = [] # jugadores
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 5000
    turno = 1 # turnos de los jugadores

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)

    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket) # no se tiene en cuenta esta primera posicion en los jugadores

    print ("Chat server started on port " + str(PORT))

    users_list = {}

    while True:
        turno %= 5 # que no se pase de 4
        if (turno == 0):
            turno += 1 # no se puede tomar el socket del servidor

        print "Turno : " + str(turno)

        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

        for sock in read_sockets: # sockets entrantes
            # Nueva conexion
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                # se admiten hasta 4 jugadores maximo
                if(len(CONNECTION_LIST)>4):
                    sockfd.send("Parques lleno, intentalo mas tarde")
                    break

                username = verifyUser(sockfd, users_list, CONNECTION_LIST, sock)

                broadcast_data(sockfd, username + " entered room\n")

            #Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        print "Datos enviados al servidor : " + data
                        user = getUsername(sock, users_list)
                        print "Usuario que lo envio : " + user
                        idx = getIndex(user,users_list,CONNECTION_LIST)
                        print "Indice : " + str(idx)
                        print "Turno aca : " + str(turno)
                        if (idx == turno): # si el usuario que envio el dato es el que debe jugar:
                            broadcast_data(sock, "\r" + '<' + str(user) + '> ' + data)
                            print "Se envio el mensaje"
                            turno += 1

                        # si no, se ignora

                except:
                    broadcast_data(sock, "Client %s is out\n" %username)
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue

    server_socket.close()
