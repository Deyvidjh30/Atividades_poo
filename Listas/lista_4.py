import math

#EXERCÍCIO 1 - BHASKARA
# a, b, c = map(float,input().split())
# delta= b*b-4*a*c
# if a==0 or b==0 or c==0 or delta<0:
#     print("Impossivel calcular")
# else:   
#     r1= (-b + math.sqrt((delta)))/(2*a)
#     r2= (-b - math.sqrt((delta)))/(2*a)
#     print(f"R1 = {r1:.5f}")
#     print(f"R2 = {r2:.5f}")


#EXERCÍCIO 2 - MULTIPLOS
# a, b = map(float,input().split())
# if b%a == 0 or a%b == 0:
#     print("Sao Multiplos") 
# else:
#     print("Nao sao Multiplos")


# EXERCÍCIO 3 - DDD
# ddd=int(input())
# if ddd==61:
#     print("Brasilia")
# elif ddd==71:
#     print("Salvador")
# elif ddd==11:
#     print("Sao Paulo")
# elif ddd==21:
#     print("Rio de Janeiro")
# elif ddd==32:
#     print("Juiz de Fora")
# elif ddd==19:
#     print("Campinas")
# elif ddd==27:
#     print("Vitoria")
# elif ddd==31:
#     print("Belo Horizonte")
# else:
#     print("DDD nao cadastrado")


#EXERCÍCIO 4 - TIRA-TEIMA
# x , y = map(float,input().split())
# if 0 <= x <= 432 and 0 <= y <= 468:
#     print("dentro")
# else:
#     print("fora")

#EXERCÍCIO 5 - NÚMEROS PARES
# num=0
# while num <= 98:
#     num=num+2
#     print (num)


#EXERCÍCIO 6 - MAIOR E POSIÇÃO
# valores = []
# for i in range(100):
#     valor = int(input())  
#     valores.append(valor)
# maior_valor = max(valores)
# posicao = valores.index(maior_valor) + 1  
# print(maior_valor)
# print(posicao)


#EXERCÍCIO 7 - ANIMAIS
# animais = {
#     "vertebrado": {
#         "ave": {
#             "carnivoro": "aguia",
#             "onivoro": "pomba"
#         },
#         "mamifero": {
#             "onivoro": "homem",
#             "herbivoro": "vaca"
#         }
#     },
#     "invertebrado": {
#         "inseto": {
#             "hematofago": "pulga",
#             "herbivoro": "lagarta"
#         },
#         "anelideo": {
#             "hematofago": "sanguessuga",
#             "onivoro": "minhoca"
#         }
#     }
# }
# tipo1 = input().strip()
# tipo2 = input().strip()
# tipo3 = input().strip()
# print(animais[tipo1][tipo2][tipo3])