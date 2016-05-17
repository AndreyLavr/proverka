import socket, asyncore
host = ''
port = 2222
class EchoHand(asyncore.dispatcher_with_send):
	def hand_read(self):
		data = self.recv(1024)
		if data:
			if data == 'close': self.close()
			else:
				print("DATA ECHAND", data)
				self.send(data)
class EchoServ(asyncore.dispatcher):
	def __init__(self, host, port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)                           
		self.set_reuse_addr()
		self.bind((host, port))
		self.listen(10)
	def handle_accept(self):
		pair = self.accept()
		if pair is not None:
			sock, addr = pair
			print('Connect from %s' % repr(addr)
			handler = EchoHand(sock)
server = EchoServ(host, port)
asyncore.loop()
