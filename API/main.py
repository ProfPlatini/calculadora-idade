from fastapi import FastAPI

app = FastAPI()

usuarios = [
    {"id": 1, "nome":"Luiz Platini"},
    {"id": 2, "nome":"Victor Ganciar"},
    {"id": 3, "nome": "Manuela Ganciar"},
    {"id": 4, "nome": "Tati Ganciar"}
]

@app.get("/")
def home():
    return {"mensagem": "Minha primeira API em Python"}

@app.get("/usuarios")
def listar_usuarios():
    return usuarios 

@app.get("/usuarios/{id}")
def consulta_usuario(id: int):
    for user in usuarios:
        if user["id"] == id:
            return user
        else:
            return "Usuário não encontrado!"

@app.post("/usuarios")
def criar_usuario(usuario: dict):

    usuarios.append(usuario)
    return usuario