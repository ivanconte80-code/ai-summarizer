from flask import Flask, request, render_template
from openai import OpenAI

app = Flask(__name__)

import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=["GET","POST"])
def home():

    risultato = ""

    if request.method == "POST":

        testo = request.form["testo"]

        risposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": f"Riassumi questo testo: {testo}"}
            ]
        )

        risultato = risposta.choices[0].message.content

    return render_template("index.html", risultato=risultato)

app.run(debug=True)
