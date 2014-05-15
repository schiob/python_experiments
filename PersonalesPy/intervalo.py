import random

#variables
notas = ('do', 're', 'mi', 'fa', 'sol', 'la', 'si')

class Inter():
	def setTonica(self):
		x = random.randint(0, 6)
		self.tonica = notas[x]

	def setInter(self):
		self.x = random.randint(1, 8)
		if x == 1:
			inter = "primera"
		elif x == 2:
			inter = "segunda"
		elif x == 3:
			inter = "tercera"
		elif x == 4:
			inter = "cuarta"
		elif x == 5:
			inter = "quinta"
		elif x == 6:
			inter = "sexta"
		elif x == 7:
			inter = "septima"
		elif x == 8:
			inter = "octava"
		self.inter = inter

	def pregunta(self):
		txt = self.inter + 'de' + str(self.tonica)
		print txt
		self.respuesta = raw_input('del 1-8')

	def __init__(self):
		setTonica()
		setInter()
		pregunta()

inter = Inter()

