from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    alerts = []
    try:
        with open("log.acessos.txt", "r") as f:
            for linha in f:
                if "falha_login" in linha:
                    alerts.append(linha.strip())
    except FileNotFoundError:
        return "<h1>Log ainda não criado</h1>"
    return f"<h1>Monitor de Segurança</h1><p>{'<br>'.join(alerts)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

