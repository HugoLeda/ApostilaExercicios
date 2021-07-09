# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input('Digite o nome de usuário: ')
senha = input('Senha: ')

igual = True
while (igual):
  if(usuario == senha):
    print('Dados Inválidos! \n Por favor digite novamente. \n')
    usuario = input('Digite o nome de usuário: ')
    senha = input('Senha: ')
  else:
    print('Usuário válido!')
    igual = False

