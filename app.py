import mysql.connector 
from flask import Flask , render_template

app = Flask(__name__)

conexao = mysql.connector.connect(
host='localhost',
user='root',
password='vini12345',
database='cadastro'
)

cursor = conexao.cursor(buffered=True)

comando='SELECT * FROM usuarios'
cursor.execute(comando)
conexao.commit()
resultado = cursor.fetchall()
print(resultado)

cursor.close()
conexao.close()

@app.route('/index.html')
def index():
    return render_template('index.html')
@app.route('/send' , methods=['POST'])
def send():
    comando = '''
    insert into cad_usuarios (nome,email,sexo,nacionalidade)
    values('usuario', 'email', 'M , F', 'pais'')'''
    cursor.execute(comando)
    cursor.commit()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True) 