nome = input('Escreva seu nome completo: ').strip()
nome1 = nome.split()
print()
print('Todas as letras maiúsculas: {}'.format(nome.upper()))
print('Todas as letras minúsculas: {}'.format(nome.lower()))
print('O total de letras que o nome possui sem considerar os espaços é {}.'.format(len(''.join(nome1))))
print('O primeiro nome possui {} letras.'.format(len(nome1[0])))