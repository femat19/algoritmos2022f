# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/122UvyEz86H1ej9APRx0BaEtnF6D0pKEb
"""

nome= input ("Qual é o seu nome?")  
print("olá ", nome)

salario = input("digite o seu salário: \n")
imposto = float( salario ) * 0.25
print(imposto)

print("Qual o seu rendimento anual?")

rendimento = float( input()  )

if (rendimento <=28000 ):
  print("você está isento")
  porcentagem = 0
elif (rendimento > 28000 and rendimento <=35000):
  print("você vai pagar 10%")
  porcentagem =10
else:
    print("voc~e vai pagar 25%")
    porcentagem = 25

if (porcentagem > 0):
  imposto_pagar = rendimento *(porcentagem / 100)
  print("você vai pagar",imposto_pagar)

numero = int(input('valor para sacar[1-50000]:'))

um = int(numero / 1)
numero = numero - (um*0.1)
  
cinco = int(numero / 5)
numero = numero - (cinco*0.5)
 
dez= int(numero / 10)
numero = numero - (dez*0.10)

vinte_e_cinco = int(numero / 25)
numero = numero - (vinte_e_cinco*0.25)

cinquenta = int(numero/50)
numero = numero - (cinquenta*0.50)

cem = int (numero / 100)
numero = numero - (cem*1.00)
    
print('moedas R$ 0.01 =',um )
print('moedas R$ 0.05 = ',cinco )
print('moedas R$ 0.10 = ',dez )
print('moedas R$ 0.25 = ',vinte_e_cinco )
print('moedas R$ 0.50 = ',cinquenta ) 
print('moedas R$ 1.00 = ',um_real )

