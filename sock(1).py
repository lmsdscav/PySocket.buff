import base64
import socket
class b64:
    def encode(s):
        encoded_bytes = base64.b64encode(s.encode("utf-8"))
        encoded_str = encoded_bytes.decode("utf-8")
        return encoded_str
    def decode(s):
        decoded_bytes = base64.b64decode(s)
        decoded_str = decoded_bytes.decode("utf-8")
        return decoded_str
class cutl:
    def do(string,zil):
        segments = []
        num_segments = len(string) // zil
        if len(string) % zil != 0:
            num_segments += 1
        for i in range(num_segments):
            start = i * zil
            end = (i + 1) * zil
            segment = string[start:end]
            segments.append(segment)
        return segments
glh=1024
class server_connected:
    def __init__(self,socket_io,address):
        self.address=address
        self.socket_io=socket_io
    def send(self,String):
        String=b64.encode(String)
        for x in cutl.do(String,glh):
            self.socket_io.send(x.encode("utf-8"))
        self.socket_io.send("\0".encode("utf-8"))
        self.socket_io.recv(19)
    def receive(self):
        data = ""
        while True:
            chunk = self.socket_io.recv(glh)
            if not chunk:
                break
            data += chunk.decode("utf-8")
            if data.endswith("\0"):
                data=data[:-1]
                break
        self.socket_io.send("\0".encode('utf-8'))
        data=b64.decode(data)
        return data
    def close(self):
        self.socket_io.close()
class server:
    def __init__(self,address,port):
        self.address=address
        self.port=port
        self.socket=socket.socket()
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.socket.bind((address,port))
    def listen(self,nv=5):
        return self.socket.listen(nv)
    def close(self):
        return self.socket.close()
    def getAccept(self):
        return server_connected(*self.socket.accept())
class client_connected:
    def __init__(self, socket_io):
        self.socket_io = socket_io
    def send(self, string):
        string=b64.encode(string)
        for x in cutl.do(string, glh):
            self.socket_io.send(x.encode("utf-8"))
        self.socket_io.send("\0".encode("utf-8"))
        self.socket_io.recv(19)
    def receive(self):
        data = ""
        while True:
            chunk = self.socket_io.recv(glh)
            if not chunk:
                break
            data += chunk.decode("utf-8")
            if data.endswith("\0"):
                data=data[:-1]
                break
        self.socket_io.send("\0".encode('utf-8'))
        data=b64.decode(data)
        return data
class client:
    def __init__(self):
        self.socket = socket.socket()
    def connect(self, address, port):
        self.socket.connect((address, port))
    def close(self):
        self.socket.close()
    def getConnected(self):
        return client_connected(self.socket)