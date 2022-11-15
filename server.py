import socket
 
# Here we use localhost ip address
# and port number
LOCALHOST = "127.0.0.1"
PORT = 8081
# calling server socket method
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Server started")
print("Waiting for client request..")
# Here server socket is ready for
# get input from the user
clientConnection, clientAddress = server.accept()
print("Connected client :", clientAddress)
msg = ''
# Running infinite loop
while True:
    
    inp,sub,choice=[str(i) for i in clientConnection.recv(1024).decode('utf-8').split('\n')]
    print(inp)
    print(sub)
    print(choice)
    list1=[]
    
    print("IP adress is recievied")
    
    ip_octets = inp.split('.')
        

    if(len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
        print("\n valid")

    else:
        print("\nThe IP address in INVALID! Please retry!\n")
                       
    
    masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
    
    mask_octets = sub.split('.')
            
    if(len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
        print("valid subnet")

    else:
        print("\nThe subnet mask is INVALID! Please retry!\n")


    def Int2Bin(integer):
        binary = '.'.join([bin(int(x)+256)[3:] for x in integer.split('.')])
        return binary

    def complement(number):
        if number == '0':
            number = '1'
        elif number == '.':
            pass
        else:
            number = '0'
        return number

    
    if choice == "1":
        result=Int2Bin(inp)
        t=str(result)
        output=str(t)
        clientConnection.send(output.encode())
        
    
clientConnection.close()
            
            
            

 

    
    
