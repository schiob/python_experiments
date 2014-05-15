# -*- coding: utf-8 -*-

class Promedio_Materia:
	# Primero los datos
	titulo = "PRMEDIO DEL SEMESTRE"
	creador = "Santiago Chío Benavides"
	email = "santichiob@hotmail.com"

	#cosas del formalto
	divline = "="*80

	"""
		Empezamos con todas las funciones
	"""
	def nom_materia(self):
		self.materia = raw_input('\tNombre de materia: ')

	def calificaciones(self):
		c0 = raw_input('\tPrimera calificación: ')
		self.c0 = float(c0)
		c1 = raw_input('\tSegunda calificación: ')
		self.c1 = float(c1)
		c2 = raw_input('\tTercera calificación: ')
		self.c2 = float(c2)
	def promedio_final(self):
		resultado_final = (self.c0 + self.c1 + self.c2)/3
		self.resultado_final = float(resultado_final)


	def armar_promedio(self):
		txt = '\n'+self.divline+'\n'
		txt += '\t'+self.titulo+'\n'
		txt += '\tCreador: '+self.creador+' | '+'Email'+self.email+'\n'
		txt += self.divline+'\n\n'
		txt += '\t'+self.materia+'\n'
		txt += '\tCalificaciones: \n'
		txt += '\tPrimer parcial: %0.2f\n' % (self.c0)
		txt += '\tSegundo parcial: %0.2f\n' % (self.c1)
		txt += '\tTercer parcial: %0.2f\n' % (self.c2)
		txt += '-'*80+'\n'
		txt += '\tPromedio: %0.2f' % (self.resultado_final)
		print txt

	def __init__(self):
		print self.divline
		print '\tGENERACION DE PROMEDIO'
		print self.divline
		self.nom_materia()
		self.calificaciones()
		self.promedio_final()
		self.armar_promedio()

promedio = Promedio_Materia()


