salarioHoras = float(input("Salário por hora: "))
horasTrabalhadas = int(input("Horas trabalhadas no mês: "))
salarioBruto = (salarioHoras * horasTrabalhadas)

ir = 11
inss = 8
sindicato = 5

irDesconto = ((salarioBruto * ir) / 100) 
inssDesconto = ((salarioBruto * inss) / 100)
sindicatoDesconto = ((salarioBruto * sindicato) / 100)
desconto = irDesconto + inssDesconto + sindicatoDesconto

salarioLiquido = salarioBruto - desconto

print("SALÁRIO BRUTO:R$ {:.2f}\nIR(11%):R$ {:.2f}\nINSS(8%):R$ {:.2f}\nSINDICATO(5%):R$ {:.2f}\nSALÁRIO LIQUIDO:R$ {:.2f}".format(salarioBruto, irDesconto, inssDesconto, sindicatoDesconto,salarioLiquido))
