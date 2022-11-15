import socket
 
# In this Line we define our local host
# address with port number
SERVER = "127.0.0.1"
PORT = 8081
# Making a socket instance
client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
# connect to the server
client.connect((SERVER, PORT))
# Running a infinite loop
while True:
    print("Example : 192.234.56.43")
    # here we get the input from the user
    inp = input("Enter IP adress")
    sub = input("enter subnet mask")
    choice=input("Enter choice")
    # If user wants to terminate
    # the server connection he can type Over
    if inp == "over":
        break
    # Here we send the user input
    # to server socket by send Method
    client.sendall(str.encode("\n".join([str(inp),str(sub),str(choice)])))
 
    # Here we received output from the server socket
    answer = client.recv(1024)
    print("Answer is "+answer.decode())
    print("Type 'Over' to terminate")
 
client.close()
