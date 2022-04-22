from math import trunc

area = float(input("Informe a área em metros(m²): "))
coberturaArea = (area / 3)

lata = 18
precoLata = 80
quantidadeNecessaria = trunc(coberturaArea / lata)
preco = quantidadeNecessaria * precoLata


print("Quantidade de latas de 18L: {}\nPreço total:R$ {:.2f}".format(quantidadeNecessaria, preco))