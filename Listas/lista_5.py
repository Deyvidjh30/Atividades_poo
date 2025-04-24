#atividade 1
"""def maior(x, y):
    m=(max(x, y))
    return m

x=int(input())
y=int(input())
print(maior(x, y))"""

#atividade 2
"""def maior(x, y, z):
    m=(max(x, y, z))
    return m

x=int(input())
y=int(input())
z=int(input())
print(maior(x, y, z))"""

#atividade 3
"""def iniciais(nome):
    iniciais = []
    for i in range(len(nome)):
        nome[i] = list(nome[i])
        iniciais.append(nome[i][0])
    return iniciais

nome = input().split()
inicial = iniciais(nome)
print(inicial)"""

#atividade 4
"""def aprovado(nota1, nota2):
    media=(nota1+nota2)/2
    resultado=[]
    if media>=60:
        resultado=f"aprovado! Sua nota final é: {media}"
    elif media<60 and media>=30:
        resultado=f"recuperação! Sua nota final é: {media}"
    else:
        resultado=f"reprovado! Sua nota final é: {media}"
    return resultado

nota1=int(input())
nota2=int(input())
media= aprovado(nota1, nota2)
print(media)"""

#atividade 5
"""def formatar_nome(nome):
    partes = nome.split()
    nome_formatado = []
    for parte in partes:
        nome_formatado.append(parte.capitalize())
    return ' '.join(nome_formatado)

nome = input("Digite seu nome: ")
print("Nome formatado:", formatar_nome(nome))"""
