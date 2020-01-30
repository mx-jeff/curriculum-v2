from flask import Flask, redirect, url_for, render_template, request
from flask_mail import Mail,Message
from datetime import date


app = Flask(__name__)

app.config['debug'] = True
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = 'addtestfield@gmail.com' 
app.config["MAIL_PASSWORD"]  = 'meuteste@01'
app.config["MAIL_DEFAULT_SENDER"] = None
app.config["MAIL_MAX_EMAILS"] = None
app.config["MAIL_ASCII_ATTACHMENTS"] = False 

mail = Mail(app)

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


@app.route('/chat', methods=["POST","GET"])
def chat():
    if request.method == "POST":
        email = request.form["email"]
        assunto = request.form["assunto"]
        conteudo = request.form["conteudo"]

        msg = Message(assunto, sender=email, recipients=["addtestfield@gmail.com"])
        msg.body = str(conteudo) 
        mail.send(msg)

    else:
        print("vazio")

    return render_template('contato.html')


if __name__ == "__main__":
    app.run(debug=True)