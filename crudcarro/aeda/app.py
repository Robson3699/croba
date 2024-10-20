import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

arquivo = 'usuarios.json'

def carregar_usuarios():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/usuarios':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            usuarios = carregar_usuarios()
            self.wfile.write(json.dumps(usuarios).encode())
        else:
            # Servir o HTML
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            with open('index.html', 'r') as f:
                self.wfile.write(f.read().encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()
        dados = json.loads(post_data)

        if self.path == '/adicionar':
            usuarios = carregar_usuarios()
            usuarios.append(dados)
            salvar_usuarios(usuarios)
            self.send_response(200)
            self.end_headers()
        elif self.path == '/excluir':
            nome = dados['nome']
            usuarios = carregar_usuarios()
            usuarios = [u for u in usuarios if u['nome'] != nome]
            salvar_usuarios(usuarios)
            self.send_response(200)
            self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), RequestHandler)
    print("Servidor rodando em http://localhost:8080")
    server.serve_forever()
