from socketserver import BaseRequestHandler,TCPServer


class receptorSolicitudes(BaseRequestHandler):
    
    def handle(self):
        print("Se ha recibido un pedido de conexion desde {}".format(self.client_address))
        
        while True:
            #print(self.request.recv(8192))
            mensaje = self.request.recv(8192)
            if not mensaje:
                break

            self.request.send(mensaje)
        
if __name__ == "__main__":
    servidor = TCPServer(("", 20064), receptorSolicitudes)
    print("El servidor TCP se ha iniciado")
    servidor.serve_forever()
