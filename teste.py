## criar banco de dados 

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


class Paciente(BaseModel):
    nome = peewee.CharField()
    sensor = peewee.CharField(unique = True)
    leito = peewee.CharField()
      
class Sensor(BaseModel):
	chave= peewee.CharField(unique=True)

    
   
Sensor.create_table()
#Usuario.create_table()
#Paciente.create_tablei()
#myDB = MySQLDatabase("mydb", host="mydb.crhauek3cxfw.us-west-2.rds.amazonaws.com", port=3306, user="user", passwd="password")
