"""
  Pedro Anguinoni - 00170009
  Statistics and Data Science - UFRGS
"""

descricoes = []
valores = []

while True:
    print()
    print("--- GERENCIADOR FINANCEIRO ---")
    print("1. Adicionar Receita")
    print("2. Adicionar Despesa")
    print("3. Ver Extrato e Saldo")
    print("4. Sair")
    
    opcao = input("Escolha uma opcao: ")
    
    if opcao == "1":
        desc = input("Descricao da receita: ")
        valor = float(input("Valor da receita: "))
        
        descricoes.append(desc)
        
        valores.append(valor)
        print("Receita adicionada com sucesso!")
        
    elif opcao == "2":
        desc = input("Descricao da despesa: ")
        valor = float(input("Valor da despesa: "))
        
        descricoes.append(desc)
        valores.append(-valor)  
        print("Despesa adicionada com sucesso!")
        
    elif opcao == "3":
        if len(descricoes) == 0:
            print("Nenhum registro encontrado.")
        else:
            print()
            print("--- EXTRATO ---")
            for i in range(len(descricoes)):
                print(f"- {descricoes[i]}: R$ {valores[i]:.2f}")
            
            print("-" * 16)
            print(f"Saldo Atual: R$ {sum(valores):.2f}")
            
    elif opcao == "4":
        print("Saindo do sistema... Ate logo!")
        break
        
    else:
        print("Opcao invalida! Tente novamente.")
