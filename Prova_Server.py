import socket
from messages import MasaMessage

#Creo socket UDP per mandare messaggio e inizializzo indirizzo e porta
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8891))

#Ciclo che aspetta messaggi
while True:
    data, addr = s.recvfrom(2048)
    #La funzione receive restituisce un MasaMessage
    message = MasaMessage.receive(data)
    print(message)
    print(message.objects[0])
    print(message.objects[1])
    print(message.lights[1])