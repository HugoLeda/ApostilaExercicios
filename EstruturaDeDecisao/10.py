# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M­matutino ou V­Vespertino ou N­Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('*--------------------*')
print('|   M - matutino     |')
print('|   V - vespertino   |')
print('|   N - noturno      |')
print('*--------------------*')

print()
turno = input('Digite o turno em que você estuda: ')
turno = turno.upper()

if (turno == 'M') :
  print('Bom dia!')
elif (turno == 'V') :
  print('Boa tarde!')
elif (turno == 'N') :
  print('Boa noite!')
else :
  print('Valor inválido!')