import socket            
 

s = socket.socket()        
print ("Socket criado com sucesso")
 
port = 6456               
 
s.bind(('127.0.0.1', port))        
print ("Socket vinculado a %s" %(port))
 

s.listen(5)    
print ("Socket está escutando")           
 
try:
  while True:
  
    c, addr = s.accept()    
    print ('Conectado de', addr)
  
    while True:
          sentence = c.recv(1024).decode()
          print(sentence)
          if sentence != 'close':
            capSentence = sentence.upper()
            c.send(capSentence.encode())
          else:
            break
    c.close()
    print('Desconectado de', addr)
    break
finally:
  s.close()

