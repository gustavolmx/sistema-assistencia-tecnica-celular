# =====================================================================
# SISTEMA DE ASSISTÊNCIA TÉCNICA DE CELULAR - Tema 6
# Abre ordens de serviço (OS) ao longo do dia e, ao encerrar,
# mostra um relatório de fechamento.
# =====================================================================

# ---------------------------------------------------------------------
# CONFIGURAÇÕES INICIAIS / GUSTAVO
# ---------------------------------------------------------------------


valores = {1: 250.00, 2: 120.00, 3: 80.00, 4: 60.00}
respostas_validas = ["Sim", "sim", "Sim", "SIM", "Não", "não", "nao", "NAO", "Nao"]

lista_os = []
lista_parcelamento = []
qtd_tela = 0
qtd_bateria = 0
qtd_conector = 0
qtd_software = 0
qtd_urgente = 0

# ---------------------------------------------------------------------
# LOOP PRINCIPAL - repete até o usuário escolher "Encerrar o dia" / GUSTAVO
# ---------------------------------------------------------------------

while True:
    print("1 - Abrir OS")
    print("2 - Encerrar o dia")
    opcao = input("Escolha: ").strip()

    if opcao == "2":
        break

    if opcao != "1":
        print("Opção Inválida")
        continue

    # -----------------------------------------------------------------
    # ESCOLHA DO CONSERTO / ALICE
    # -----------------------------------------------------------------

    print("1 - Tela (R$ 250,00)")
    print("2 - Bateria (R$ 120,00)")
    print("3 - Conector de carga (R$ 80,00)")
    print("4 - Software (R$ 60,00)")

    conserto = int(input("Escolha o conserto:  "))

    if conserto == 1:
        print("O conserto da Tela será de 250.00 !")
    if conserto == 2:
        print("O conserto da Bateria será de 120.00 !")
    if conserto == 3:
        print("O conserto do Conector será de 80.00 !")
    if conserto == 4:
        print("O conserto do Software será de 60.00 !")

    if conserto not in valores:
        print("Opção inexistente, escolha uma opção de 1 a 4 !")
        continue

    # -----------------------------------------------------------------
    # URGÊNCIA / EDITH
    # -----------------------------------------------------------------
    urgente = input("Seu conserto é urgente? Sim/Não: ")

    if urgente not in respostas_validas:
        print("Resposta inexistente, escolha uma resposta válida!")
        continue

    urgente = urgente.upper()

    if urgente == "SIM" and conserto != 4:
        print("Seu valor terá um acréscimo de 30%!")

        if conserto == 1:
            valor = valores[1] * 1.30
        elif conserto == 2:
            valor = valores[2] * 1.30
        elif conserto == 3:
            valor = valores[3] * 1.30

        print("Valor com urgência: R$", round(valor, 2))

    elif urgente == "SIM" and conserto == 4:
        valor = valores[4]
        print("Software não tem acréscimo de urgência!")
        print("Valor final: R$", valor)

    elif urgente == "NAO" or urgente == "NÃO":
        if conserto == 1:
            valor = valores[1]
        elif conserto == 2:
            valor = valores[2]
        elif conserto == 3:
            valor = valores[3]
        elif conserto == 4:
            valor = valores[4]

        print("Seu valor não terá acréscimo!")
        print("Valor final: R$", valor)

    else:
        print("Opção inválida! Digite Sim ou Não.")
        valor = valores[conserto]
        print("Seu conserto será considerado sem urgência. Valor: R$", valor)

    # -----------------------------------------------------------------
    # FORMA DE PAGAMENTO / PARCELAMENTO - JONATHAN
    # -----------------------------------------------------------------
    parcela = int(input("Você vai parcelar em quantas vezes? (1 a 6): "))

    if parcela not in (1, 2, 3, 4, 5, 6):
        print("Opção inválida!")
        continue

    elif parcela == 1:
        valor = valor * 0.95
        print("Pagamento à vista com 5% de desconto!")
        print(f"Valor final: R$ {valor:.2f}")
        print(f"1x de R$ {valor:.2f}")

    elif parcela in (2, 3):
        print("Pagamento sem juros!")
        print(f"Valor final: R$ {valor:.2f}")
        print(f"{parcela}x de R$ {valor / parcela:.2f}")

    elif parcela >= 4 and parcela <= 6:
        valor = valor * 1.10
        print("Pagamento terá 10% de juros!")
        print(f"Valor final: R$ {valor:.2f}")
        print(f"{parcela}x de R$ {valor / parcela:.2f}")

    # -----------------------------------------------------------------
    # REGISTRO DA OS / SAMUEL
    # -----------------------------------------------------------------

    lista_os.append(valor)
    lista_parcelamento.append((parcela, valor / parcela))

    if conserto == 1:
        qtd_tela += 1
    elif conserto == 2:
        qtd_bateria += 1
    elif conserto == 3:
        qtd_conector += 1
    elif conserto == 4:
        qtd_software += 1

    if urgente == "SIM" and conserto != 4:
        qtd_urgente += 1

# ---------------------------------------------------------------------
# FECHAMENTO DO DIA - executa depois que o loop termina / SAMUEL
# ---------------------------------------------------------------------

print("FECHAMENTO DO DIA\n")

if len(lista_os) == 0:
    print("Sem aberturas de OS hoje!")
else:
    print(f"Quantidade de OS: {len(lista_os)}")
    print(f"Faturamento: R$ {sum(lista_os):.2f}")
    print("Parcelamento por OS:")
    for i, (qtd_parcelas, valor_parcela) in enumerate(lista_parcelamento, start=1):
        print(f"  OS {i}: {qtd_parcelas}x de R$ {valor_parcela:.2f} (total R$ {lista_os[i - 1]:.2f})")
    print(f"Valor médio por OS: R$ {sum(lista_os) / len(lista_os):.2f}")
    print(f"Maior OS: R$ {max(lista_os):.2f}")
    print(f"Trocas de tela: {qtd_tela}")
    print(f"Trocas de bateria: {qtd_bateria}")
    print(f"Trocas de conector: {qtd_conector}")
    print(f"Conserto de software: {qtd_software}")
    print(f"OS com taxa de urgência: {qtd_urgente}")
    
    # Quantidade de cada tipo de conserto
    print(f"Trocas de tela: {qtd_tela}")
    print(f"Trocas de bateria: {qtd_bateria}")
    print(f"Trocas de conector: {qtd_conector}")
    print(f"Conserto de software: {qtd_software}")
    # Quantidade de OS com taxa de urgência
    print(f"OS com taxa de urgência: {qtd_urgente}")