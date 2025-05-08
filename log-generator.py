import time
import random

usuarios = ['usuario1', ' usuario2', ' usuario3', ' usuario4']
eventos = ['login_sucesso', 'falha_login']

while True
    usuario = random.choice(usuarios)
    evento = random.choice(eventos, weights=[0.7, 0.3])[0]
    with open("log.acessos.txt", "a") as f:
        f.write(f"{evento} {usuario}\n"
    time.sleep(2)
