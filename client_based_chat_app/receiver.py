import socket 


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address =" 192.168.252.62"
    ## ip khud ki device ka
port_number = 1355
complete_add = (ip_address,port_number)
s.bind(complete_add)
while True:
    message = s.recv(1024)
    print(message)
    data = message[0]
    data = "\n"
    print(data.encode("ascii"))



