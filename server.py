from flask import Flask, redirect, url_for, render_template
from datetime import date

app = Flask(__name__)
data_atual = date.today()

@app.route('/')
@app.route('/home')
def init():
    return render_template('index.html', data={'idade': data_atual.year - 1997 })


@app.route('/estudos')
def estudos():
    return render_template('estudos.html')


@app.route('/jobs')
def jobs():
    return render_template('profissional.html')


@app.route('/redes_sociais')
def social():
    return render_template('social.html')


@app.route('/chat')
def chat():
    return render_template('contato.html')


if __name__ == "__main__":
    app.run(debug=True)