#Importing MasaProtocol from directory
import socket, sys
sys.path.insert(1, '../python')
from MasaProtocol import *

#Creating socket UDP with given IP and PORT to listen to
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8888))

#Loop for incoming connections
while True:
    #Accepting the connection
    #TODO: If message is grater than 2048 bytes? UDP problems here...
    data, addr = s.recvfrom(2048)
    
    #Passing the "data" to the MasaMessage.receive() will return the complete object (MasaMessage python object)
    message = MasaMessage.receive(data)
    
    #Testing some message informations
    print(message)
    print(message.objects[0])
    print(message.objects[1])
    print(message.lights[1])
