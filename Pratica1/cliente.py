import socket            
 
s = socket.socket()        

port = 6456               
 
s.connect(('127.0.0.1', port))
 
while True:
    entrada = input('Digite a entrada: ')
    sentence = str(entrada)
    if(sentence == "close"): break
    print(sentence)
    s.send(sentence.encode())
    retSentence = s.recv(1024)
    print('Server; ', retSentence.decode())


s.close() 