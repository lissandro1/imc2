print('====== CÁCLULO DO INDÍCE DE MASSA CORPORAL (IMC) ======')
print()
alt = float(input('Qual a sua altura (em cm): '))
peso = float(input('Qual é o seu peso (em kg): '))

def imc():
    altura = (alt / 100)**2 
    result = peso / altura
    return result

val = imc()

if val < 18.5:
    print('MAGREZA')
elif 18.6 <= val <= 24.9:
    print('NORMAL')
elif 25 <= val <= 29.9:
    print('SOBREPESO')
elif 30 <= val <= 39.9:
    print('OBESIDADE')
elif val >= 40:
    print('OBESIDADE GRAVE')


