import zmq

context = zmq.Context()

#  Socket para conversar com o servidor
print("Conectando com o servidor ZeroMQ…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:6464")

#  Fazendo 10 requisições, esperando cada tempo de resposta
for request in range(10):
    print("Mandando requisição %s …" % request)
    socket.send(b"Hello")

    #  Get the reply.
    message = socket.recv()
    print("Retorno recebido %s [ %s ]" % (request, message))

socket.send(b"Close")