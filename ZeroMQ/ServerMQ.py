import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6464")




while True:
    message = socket.recv()
    print("Requisição receida: %s" %message)
    if message == b"Close":
        break
    else:
        time.sleep(1)
        socket.send(b"Mensagem recebida")

