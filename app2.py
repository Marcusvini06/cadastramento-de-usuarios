from flask import Flask, redirect, render_template, request
import requests
import mysql.connector 
import json

conexao = mysql.connector.connect(
host='localhost',
user='root',
password='vini12345',
database='cadastro'
) 

cursor = conexao.cursor(buffered=True)

app = Flask(__name__)
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/verprodutos')
def verprodutos():
    comando = "select * from cad_usuarios"
    cursor.execute(comando)
    resultado = []
    print(resultado)
    resultado = cursor.fetchall()
    #return json.dumps(resultado) 
    return render_template('index.html', resultado=resultado)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    email = request.form.get('email')
    sexo = request.form.get('sexo')
    pais = request.form.get('pais')
    comando = "insert into cad_usuarios (nome,email,sexo,nacionalidade) values('" + usuario + "', '" + email + "', '" + sexo + "', '" + pais + "')"
    cursor.execute(comando) 
    conexao.commit()
    print("usuario: {} , email: {} , M or F: {}  , pais: {} ".format(usuario,email,sexo,pais))
    return "usuario: {} , email: {} , M or F: {} , pais: {} ".format(usuario,email,sexo,pais)

if __name__ == '__main__':
    app.run(debug=True) 
    