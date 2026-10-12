estado = dict ()
Brasil = list ()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    Brasil.append(estado.copy())

for e in Brasil:
    for v in e.values():
        print(v, end =' ')
    print()