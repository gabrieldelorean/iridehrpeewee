import peewee
from peewee import *

db = MySQLDatabase('iridewave', user='root', passwd='belmpsc')

class BaseModel(Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    nome = peewee.CharField()
    email = peewee.CharField(unique = True)
    senha = peewee.CharField()
    telefone = peewee.CharField()
    celular  = peewee.CharField()
    ativo = peewee.IntegerField()

     
    def AddUsuario(self,nomeparam="",emailparam="",senhaparam="1234",telefoneparam="",celularparam="",ativoparam=0):
     try:
      u2 = Usuario(nome=nomeparam,email=emailparam,senha=senhaparam,telefone=telefoneparam,celular=celularparam,ativo=ativoparam)
      u2.save()
     except:
      print "Email ja cadastrado"
 
    def DeleteUsuario(self,idparam):
        q = Usuario.delete().where(Usuarios.id == idparam )
        q.execute() 




class Paciente(BaseModel):
    nome = peewee.CharField()
    sensor = peewee.CharField()
    leito = peewee.CharField()


    def AddPaciente(self,nomeparam="",leitoparam="",sensorparam=""):
     try:
      p1  = Paciente(nome=nomeparam,sensor=sensorparam,leito=leitoparam)
      p1.save()
     except:
      print "Sensor em uso!"

    def DeletePaciente(self,idparam):
        q = Paciente.delete().where(Pacientes.id == idparam )
        q.execute()      

    
class Sensor(BaseModel):
 chave= peewee.CharField(unique=True)

 def AddSensor(self,chaveparam=""):
     try:
      p1  = Sensor(chave=chaveparam)
      p1.save()
     except:
      print "Sensor ja cadastrado!"




