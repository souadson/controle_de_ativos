from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def carregar_blocos():
    df = pd.read_excel("dados.xlsx", header=1)

    df = df.dropna(how="all")
    df = df.fillna("")

    # BLOCO 1 → primeiras 4 colunas
    bloco1 = df.iloc[:, 0:4]

    # BLOCO 2 → colunas 5 a 8
    bloco2 = df.iloc[:, 5:9]

    return bloco1, bloco2


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/bloco/<int:numero>")
def mostrar_bloco(numero):
    bloco1, bloco2 = carregar_blocos()

    if numero == 1:
        df = bloco1
        titulo = "BLOCO 1"
    else:
        df = bloco2
        titulo = "BLOCO 2"

    return render_template("tabela.html",
                           colunas=df.columns,
                           dados=df.values,
                           titulo=titulo)


if __name__ == "__main__":
    app.run(debug=True)