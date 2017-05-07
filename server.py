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
    print "No encontrado"
    return None


def verifyUser(new_client, dic, CONNECTION_LIST, sock):
    while True:
        new_client.send("Ingresa un nombre de usuario: ")
        user = new_client.recv(1024)
        print "User: %s" %user

        if (user in dic):
            new_client.send("Nombre de usuario ya ha sido utilizado\n")
        else:
            CONNECTION_LIST.append(new_client)
            dic[user] = new_client
            new_client.send("Bienvenido al chat")
            break
    return user


 
if __name__ == "__main__":
     
    # List to keep track of socket descriptors
    CONNECTION_LIST = []
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 5000
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)
 
    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)
 
    print "Chat server started on port " + str(PORT)

    users_list = {}
 
    while True:
        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
 
        for sock in read_sockets:
            #New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()

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
                        user = getUsername(sock, users_list)
                        broadcast_data(sock, "\r" + '<' + str(user) + '> ' + data)                
                 
                except:
                    broadcast_data(sock, "Client %s is out\n" %username)
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
     
    server_socket.close()