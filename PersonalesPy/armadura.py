# -*- coding: utf-8 -*-
class EstablecerTonalidad:
	#formato
	divline = '='*80

	#notas, sostenidos y bemoles
	notas = ('do', 'do#', 'reb', 're', 're#', 'mib', 'mi', 'fa', 'fa#', 'solb', 'sol', 'sol#', 'lab',\
			 'la', 'la#', 'sib', 'si')
	armaduras_so = ('do', 'do#', 're', 're#', 'mi', 'fa#','sol', 'sol#', 'la', 'la#', 'si')
	armaduras_be = ('reb', 'mib', 'fa', 'solb', 'lab', 'sib')
	orden_armaduras_so = (notas[7], notas[0], notas[10], notas[3], notas[13], notas[6], notas[16], 'fax', 'dox', 'solx', 'rex')
	orden_armaduras_be = (notas[16], notas[6], notas[13], notas[3], notas[10], notas[0], notas[7])
	base_armaduras_so = {'do':0,
					  'do#':7,
					  're':2,
					  're#':9,
					  'mi':4,
					  'fa#':6,
					  'sol':1,
					  'sol#':8,
					  'la':3,
					  'la#':10,
					  'si':5,
					  }
	base_armaduras_be = {'reb':5,
					  'mib':3,
					  'fa':1,
					  'solb':6,
					  'lab':4,
					  'sib':2,
					   }

	#entrada de nota
	def set_nota(self):
		texto_mostrar = '\tEscribe el número de la nota: '
		seleccion = 0
		for nota in self.notas:
			texto_mostrar += '\t\n'
			texto_mostrar += '(%d)%s' % (seleccion, nota)
			seleccion = seleccion + 1

		texto_mostrar += '\n: '
		self.seleccion_nota = int(raw_input(texto_mostrar))

	#procesamos la armadura
	def set_armadura(self):
		for sostenido in self.armaduras_so:
			if sostenido == self.notas[self.seleccion_nota]:
				self.tipo_armadura = 'sostenidos'
				self.clave_armadura = self.base_armaduras_so[sostenido]

		for bemol in self.armaduras_be:
			if bemol == self.notas[self.seleccion_nota]:
				self.tipo_armadura = 'bemoles'
				self.clave_armadura = self.base_armaduras_be[bemol]

	def armar_armadura(self):
		clave_notas = 0
		self.clave_armadura = self.clave_armadura - 1
		self.armadura_completa = '| '
		if self.tipo_armadura == 'sostenidos':
			if self.clave_armadura == -1:
				self.armadura_completa = self.notas[0]
			else:
				while clave_notas <= self.clave_armadura:
					self.armadura_completa += self.orden_armaduras_so[clave_notas]
					self.armadura_completa += ' | '
					clave_notas = clave_notas + 1
		if self.tipo_armadura == 'bemoles':
				while clave_notas <= self.clave_armadura:
					self.armadura_completa += self.orden_armaduras_be[clave_notas]
					self.armadura_completa += ' | '
					clave_notas = clave_notas + 1

	def armar_txt(self):
		txt = self.divline + '\n'
		txt += '\tTonalidad: ' + self.notas[self.seleccion_nota] + '\n'
		txt += '\tArmadura: ' + self.tipo_armadura + '\n' 
		txt += '\t' + self.armadura_completa + '\n'
		txt += self.divline
		print txt

	def __init__(self):
		self.set_nota()
		self.set_armadura()
		self.armar_armadura()
		self.armar_txt()

prueba = EstablecerTonalidad()
