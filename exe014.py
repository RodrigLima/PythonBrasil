pesoLimite = 50
precoMulta = 4

pesoPeixe = float(input("Peso do peixe: "))
pesoExcedente = (pesoPeixe - pesoLimite)
preco = (pesoExcedente * precoMulta)

print("Peso excedente: {:.1f}Kg\nValor da multa:R$ {:.2f}\n".format(pesoExcedente, preco))