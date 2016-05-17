import os

lst = [
'02-ammortamento.py',
'02-arrotondamento-fibonacci-pert.py',
'02-arrotondamento-fibonacci.py',
'02-cobweb-esteso.py',
'02-cobweb.py',
'02-nazione.py',
'03-midpoint-example.py',
'04-matrices.py',
'05-armamenti.py',
'05-leslie.py',
'05-phase-plane.py',
]

os.system("echo %s | xargs -P 36 -n 1 python3 " % ' '.join(lst))