altura = float(input("Insira a sua altura: "))
pesoIdealHomem = ((72.7 * altura) - 58)
pesoIdealFeminino = ((62.1 * altura) - 44.7)

print("Peso ideal masculino: {:.2f}Kg\nPeso ideal feminino: {:.2f}Kg\n".format(pesoIdealHomem, pesoIdealFeminino))