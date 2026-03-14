from flask import Flask, request, render_template
from openai import OpenAI

app = Flask(__name__)

from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

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

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
