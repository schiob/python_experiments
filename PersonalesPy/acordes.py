
# -*- coding: utf-8 -*-
class ModeloDeAcordes:

	#datos comerciales
	titulo = 'Acordes'
	creador = 'Santiago Chío Benavides'

	#formato
	divline = '='*80

	#notas y acordes
	notas = ('do', 'do#/reb', 're', 're#/mib', 'mi', 'fa', 'fa#/solb', 'sol', 'sol#/lab',\
		'la', 'la#/sib', 'si')
	acordes = ('mayor', 'menor', 'aumentado', 'disminuido')
	acorde_mayor = ['tercera mayor + tercera menor', 4, 7]
	acorde_menor = ['tercera menor + tercera mayor', 3, 7]
	acorde_aumentado = ['tercera mayor + tercera mayor', 4, 8]
	acorde_disminuido = ['tercera menor + tercera menor', 3, 6]
	lista_acordes = {'mayor':acorde_mayor,
					'menor':acorde_menor,
					'aumentado':acorde_aumentado,
					'disminuido':acorde_disminuido}

	#datos de entrada de nota
	def set_nota(self):
		texto_mostrar = '\tEscoje el numero de la nota tonica: \n '
		codigo_nota = 0
		for nota in self.notas:
			texto_mostrar += '\t\n'
			texto_mostrar += '(%d)%s' % (codigo_nota, nota)
			codigo_nota = codigo_nota + 1

		texto_mostrar += '\n: '
		seleccion_nota = raw_input(texto_mostrar)
		self.seleccion_nota = int(seleccion_nota)

	#datos de entrada de acorde
	def set_acorde(self):
		texto_mostrar = '\tEscoje el acorde '
		codigo_acorde = 0
		for acorde in self.acordes:
			texto_mostrar += '\t\n'
			texto_mostrar += '(%d)%s' % (codigo_acorde, acorde)
			codigo_acorde = codigo_acorde + 1
		texto_mostrar += '\n: '
		seleccion_acorde = raw_input(texto_mostrar)
		self.seleccion_acorde = int(seleccion_acorde)
		datos_acorde = self.lista_acordes[self.acordes[self.seleccion_acorde]]
		self.descripcion_acorde = datos_acorde[0]
		self.primera_tercera = datos_acorde[1]
		self.segunda_tercera = datos_acorde[2]

	#datos notas
	def armar_acorde(self):
		tercera = self.seleccion_nota + self.primera_tercera
		quinta = self.seleccion_nota + self.segunda_tercera
		if tercera > 11:
			self.tercera = tercera - 12
		else:
			self.tercera = tercera
		if quinta > 11:
			self.quinta = quinta - 12
		else:
			self.quinta = quinta
	
	#armar el texto
	def armar_txt(self):
		txt = self.divline + '\n'
		txt += '\tTonica: ' + self.notas[self.seleccion_nota] + '\n'
		txt += '\tAcorde: ' + self.acordes[self.seleccion_acorde] + '\n'
		txt += '\tSe conforma por: ' + self.descripcion_acorde + '\n'
		txt += '\tNotas: ' + self.notas[self.seleccion_nota] + ' | ' + self.notas[self.tercera]\
						 + ' | ' + self.notas[self.quinta]
		txt +='\n' + self.divline +'\n'

		print txt

	def __init__(self):
		print self.divline + '\n'
		print '\t' + self.titulo + '\n'
		print '\tPor: ' + self.creador + '\n'
		self.set_nota()
		self.set_acorde()
		self.armar_acorde()
		self.armar_txt()
		raw_input()

modelo_acorde = ModeloDeAcordes()


