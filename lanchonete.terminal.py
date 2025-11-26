#Questao22ester
print("---------BEM VINDO A TIMONBURGUER---------")
print("--------- APRESENTANDO CARDÁPIO---------")
print("_____________________________________________")
print("|Cachorro Quente     |(100)| Preço R$: 4,20 |") 
print("|Bauru Simples       |(101)| Preço R$: 8,50 |")
print("|Bauru Simples       |(102)| Preço R$: 9,50 |")
print("|X-burguer           |(103)| Preço R$: 8,00 |")
print("|Hambúrguer          |(104)| Preço R$: 10,30|")
print("|Cheeseburguer       |(105)| Preço R$: 4,00 |")
print("|Refrigerante Ks     |(106)| Preço R$: 10,00|")
print("|Suco de Fruta (copo)|(107)| Preço R$: 6,50 |")
print("_____________________________________________")
Nomes = ["Cachorro quente", "Bauru simples", "X-burguer", "Hamburguer", 
         "Cheeseburguer", "Refrigerante Ks", "Refrigerante 1L", "Suco de Fruta (copo)"]
Precos = [4.20, 8.50, 9.50, 8.00, 10.30, 4.00, 10.00, 6.50]
Quantidades = [0, 0, 0, 0, 0, 0, 0, 0]
Continuar = "S"
while Continuar == "S":
    Codigo = int(input("Digite o código do produto: "))
    if Codigo == 100:
        Quantidades[0] = Quantidades[0] + int(input("Quantidade de Cachorro quente: "))
    elif Codigo == 101:
        Quantidades[1] = Quantidades[1] + int(input("Quantidade de Bauru simples: "))
    elif Codigo == 102:
        Quantidades[2] = Quantidades[2] + int(input("Quantidade de X-burguer: "))
    elif Codigo == 103:
        Quantidades[3] = Quantidades[3] + int(input("Quantidade de Hamburguer: "))
    elif Codigo == 104:
        Quantidades[4] = Quantidades[4] + int(input("Quantidade de Cheeseburguer: "))
    elif Codigo == 105:
        Quantidades[5] = Quantidades[5] + int(input("Quantidade de Refrigerante Ks: "))
    elif Codigo == 106:
        Quantidades[6] = Quantidades[6] + int(input("Quantidade de Refrigerante 1L: "))
    elif Codigo == 107:
        Quantidades[7] = Quantidades[7] + int(input("Quantidade de Suco de Fruta (copo): "))
    else:
        print("Código inválido.")
    Continuar = input("Deseja pedir outro item? (SIM ou NAO): ")
print("--- CUPOM FISCAL ----------------------------|")
Total = 0
I = 0
while I < 8:
    if Quantidades[I] > 0:
        Subtotal = Quantidades[I] * Precos[I]
        print(Nomes[I], "x", Quantidades[I], "- R$", format(Subtotal, ".2f"))
        Total = Total + Subtotal
    I = I + 1
print("TOTAL A PAGAR: R$", format(Total, ".2f"))
ValorPago = float(input("Valor pago: R$ "))
Troco = ValorPago - Total
print("TROCO: R$", format(Troco, ".2f"))
print("-------------- OBRIGADO E VOLTE SEMPRE ------|")
