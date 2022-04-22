salarioHoras = float(input("Salário por horas:R$ "))
horasTrabalhadas = int(input("Horas trabalhadas no mês: "))
salarioBruto = (salarioHoras * horasTrabalhadas)

print("Salário:R$ {:.2f}".format(salarioBruto))