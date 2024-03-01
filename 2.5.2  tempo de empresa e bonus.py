#uma empresa concedeu um bônus de 20% para todos seus funcionários
# com mais de 5 anos de empresa. Todos os outros que não se enquadram nessa
# categoria receberam uma bonificação de 10%, somente.
# Escreva um algoritmo que leia o salário do funcionário e seu tempo de empresa,
# e apresente a bonificação

salario = float (input('Qual o seu salario?'))
ano_adm = int (input('Em que ano voce comecou a trabalhar aqui?'))
ano_atual = int (input('Em que ano estamos?'))
tempo_empresa = (ano_atual - ano_adm)
if (tempo_empresa > 5):
    bonus = (salario * 0.20)
    salario_final = (salario + bonus)
    print(f'Voce tem {tempo_empresa} anos de empresa')
    print(f'Seu bonus é de RS {bonus} ')
    print(f'Seu salario final esse mes sera de {salario_final}')
else:
    bonus = (salario * 0.10)
    salario_final = (salario + bonus)
    print(f'Voce tem {tempo_empresa} anos de empresa')
    print(f'Sua bonificacao é de {bonus}')
    print(f'Seu salario final esse mes sera de {salario_final}')