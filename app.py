from flask import Flask,flash,session,request,render_template,redirect, url_for
from classes import *

app = Flask(__name__)
app.secret_key = 'random'

@app.route('/login',methods=['GET', 'POST'])
def login():
	msg = ""
	if request.method == 'POST':
		try:
			u1 = (Usuario.select().where((Usuario.email == request.form['email']) & (Usuario.senha == request.form['password']) & (Usuario.ativo == 1)).get())
			session['username'] = u1.nome
			session['ativo'] = u1.ativo				
		except:
			msg = "Erro ao logar"
	return render_template('login.html',mensagem=msg)
	 
	  
    
@app.route('/users')
def users():
	  u1 = Usuario()
	  items = []
	  for usuario  in u1.select():
	  	if usuario.ativo == 1:
	  		status = "Ativo"
	  	else:
	  		status = "Bloqueado"
	  	an_item = dict(id=usuario.id, nome=usuario.nome,email=usuario.email,telefone=usuario.telefone,celular=usuario.celular,ativo=status)
	  	items.append(an_item)
	  return render_template('new_user.html',items=items)

@app.route('/pacientes')
def  pacientes():
     u1 = Paciente()
     items = []
     for paciente  in u1.select():
        an_item = dict(id=paciente.id, nome=paciente.nome,leito=paciente.leito, sensor=paciente.sensor)
        items.append(an_item)
     return render_template('new_paciente.html',items=items)

@app.route('/sensores')
def  sensores():
     u1 = Sensor()
     items = []
     for sensor  in u1.select():
        an_item = dict(id=sensor.id, chave=sensor.chave)
        items.append(an_item)
     return render_template('new_sensor.html',items=items)


@app.route('/',methods=['GET', 'POST'])
def admin(): 
     return render_template('plain_page.html')



@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
     if request.method == 'POST':
        u1 = Usuario()
        u1.AddUsuario(request.form['nome'],request.form['email'],request.form['senha'],request.form['telefone'],request.form['celular'],request.form['ativo'])
        flash('Usuario criado com sucesso!!')
        return redirect(url_for('users'))
 

@app.route('/addpaciente', methods=['GET', 'POST'])
def addpaciente():
     if request.method == 'POST':
        u1 = Paciente()
        u1.AddPaciente(request.form['nome'],request.form['leito'],request.form['sensor'])
        flash('Paciente cadastrado com sucesso!!')
        return redirect(url_for('pacientes'))

@app.route('/addsensor',methods=['GET', 'POST'])
def addsensor():
     if request.method == 'POST':
        u1 = Sensor()
        u1.AddSensor(request.form['chave'])
        flash('Sensor cadastrado com sucesso!!')
        return redirect(url_for('sensores'))



if __name__ == '__main__':
     app.run(host='0.0.0.0',port='822')

