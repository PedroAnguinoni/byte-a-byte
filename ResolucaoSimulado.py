lista_nomes = []
lista_notas = []
opcao = ""

while opcao != '4':
    print("\n--- DIARIO DE CLASSE ---")
    print("1. Inserir aluno e nota")
    print("2. Ver alunos e notas")
    print("3. Calcular conceitos")
    print("4. Sair")

    opcao = input("Escolha uma opcao: ")
    
    if opcao == '1':
        nome = input("Nome do aluno: ")
        nota = float(input("Nota do aluno: "))

        lista_nomes.append(nome)
        lista_notas.append(nota)
        print(f"Aluno {nome} cadastrado com sucesso!")

    elif opcao == '2':
        if len(lista_nomes) == 0:
            print("Nenhum aluno cadastrado ainda.")
        else:
            print("\n--- LISTA DE ALUNOS ---")
            for i in range(len(lista_nomes)):
                print(f"- {lista_nomes[i]}: {lista_notas[i]:.1f}")

    elif opcao == '3':
        if len(lista_notas) == 0:
            print("Nenhum aluno cadastrado ainda.")
        else:
            print("\n--- CONCEITOS FINAIS ---")
            for i in range(len(lista_notas)):
                nota_atual = lista_notas[i]

                if nota_atual >= 9.0:
                    conceito = "A"
                elif nota_atual >= 7.0:
                    conceito = "B"
                elif nota_atual >= 5.0:
                    conceito = "C"
                else:
                    conceito = "D"

                print(f"- {lista_nomes[i]}: Conceito {conceito}")

    elif opcao == '4':
        print("Saindo do sistema... Ate logo!")

    else:
        print("Opcao invalida! Tente novamente.")
