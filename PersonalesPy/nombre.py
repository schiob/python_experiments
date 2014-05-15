class Persona():
	"""docstring for Persona"""
	def __init__(self):
		self.nombre = raw_input("nombre ")
		self.telefono = int(raw_input("numero "))
		self.next = None

def imprimir(persona):
	print ("%s") % (persona.nombre)
	if persona.next is None:
		return
	else:
		imprimir(persona.next)

if __name__ == '__main__':
	primer = Persona()
	ultimo = primer
	while True:
		if raw_input("otro?") == "si":
			ultimo.next = Persona()
			ultimo = ultimo.next
		else:
			imprimir(primer)
			break

