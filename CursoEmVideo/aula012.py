nome = str(input('Qual seu nome ?'))

if nome == 'Nicolas':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é comum no Brasil!')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome de muhler')

print('Tenha um bom dia! {}'.format(nome))
