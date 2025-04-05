import socket 

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   ## d_gram == for sending data from one to another system
    ip_address = " 192.168.70.109" #dusri device ka ip
    port_number = 1355      
    # 0-65536

    target_add = (ip_address,port_number)
    message  = input("Enter message here--")
    encripted_message = message.encode("ascii")
    s.sendto(encripted_message,target_add)

except Exception as e:
    print("msg not sent")
