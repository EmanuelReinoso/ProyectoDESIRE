import Teclado
from collections import defaultdict

codigos = {'A': "AGREGAR",
	   'U': "AJUSTAR",
	   'C': "UBICARPUNTOPIVOT",
	   'S': "SAVE",
	   "F1" : "LINK"}

codigos = defaultdict(lambda: -1, codigos)

t = Teclado.Teclado('/dev/input/event2')
while(1):
	tecla = t.esperar_tecla()
	print codigos[tecla]
