# ==========================================
# SISTEMA DE GESTÃO DE ESTOQUE E COMPRAS
# ==========================================

def pega_estoque_base():
    return [        
        {"id": 1, "nome": "Notebook", "preco": 3500.0, "qtd": 5},
        {"id": 2, "nome": "Mouse", "preco": 80.0, "qtd": 15},
        {"id": 3, "nome": "Teclado", "preco": 150.0, "qtd": 10}
    ]

def pega_taxa_imposto_padrao():
    return 0.05

def exibe_mensagem_principal():
    print("\n" + "=" * 30)
    print("      SISTEMA DE ESTOQUE      ")
    print("=" * 30)
    print("1. Listar Produtos")
    print("2. Adicionar ao Carrinho")
    print("3. Exibir Carrinho e Total")
    print("4. Cadastrar Novo Produto")
    print("0. Sair")
    
    return input("\nEscolha uma opção: ")

def busca_item_por_id(item_id, estoque):
    for item in estoque:
        if item["id"] == item_id:
            return item

    return {}            

def busca_item_no_carrinho_por_id(item_id, carrinho):
    for item in carrinho:
        if item["id"] == item_id:
            return item

    return {}            

def exibe_produtos_disponiveis(estoque):
    print("\n--- PRODUTOS DISPONÍVEIS ---")
    if not estoque:
        print("Estoque vazio.")
    else:
        for item in estoque:
            print(f"ID: {item['id']} | Nome: {item['nome']} | Preço: R$ {item['preco']:.2f} | Estq: {item['qtd']}")

def exibe_adicionar_ao_carrinho(estoque, carrinho):
    print("\n--- ADICIONAR AO CARRINHO ---")
    id_busca = input("Digite o ID do produto: ")

    # Validação simples se é número
    if not id_busca.isdigit():
        print("Erro: ID deve ser um número inteiro.")
        return
    
    # Busca manual no estoque
    id_busca = int(id_busca)
    produto_encontrado = busca_item_por_id(id_busca, estoque)
    if not produto_encontrado:
        print("Erro: Produto não encontrado.")
        return

    qtd_desejada = input(f"Quantidade desejada de '{produto_encontrado['nome']}': ")
    if not qtd_desejada.isdigit():
        print("Erro: Quantidade inválida.")
        return
    
    qtd_desejada = int(qtd_desejada)
    if qtd_desejada <= 0 or qtd_desejada > produto_encontrado["qtd"]:
        print("Erro: Quantidade indisponível no estoque.")
        return
    
    # Atualiza estoque e adiciona ao carrinho
    produto_encontrado["qtd"] -= qtd_desejada
    
    # Verifica se já está no carrinho para somar a quantidade
    no_carrinho = busca_item_no_carrinho_por_id(produto_encontrado['id'], carrinho)

    if(no_carrinho):
        no_carrinho['qtd'] += qtd_desejada
    else:
        item = {
            "id": produto_encontrado["id"],
            "nome": produto_encontrado["nome"],
            "preco": produto_encontrado["preco"],
            "qtd": qtd_desejada
        }

        carrinho.append(item)
        
    print(f"Sucesso: {qtd_desejada}x '{produto_encontrado['nome']}' adicionado(s) ao carrinho!")

def calcula_total_item(preco, quantidade):
    return preco * quantidade

def exibe_itens_do_carrinho(carrinho):
    for item in carrinho:
        total_item = calcula_total_item(item["preco"], item["qtd"])
        print(f"- {item['nome']} (x{item['qtd']}): R$ {total_item:.2f}")

def calcula_subtotal_carrinho(carrinho):
    return sum(
        calcula_total_item(item["preco"], item["qtd"])
        for item in carrinho
    )

def exibe_total_carrinho(subtotal, taxa_aplicada):
    valor_imposto = subtotal * taxa_aplicada
    total_final = subtotal + valor_imposto
    
    print("-" * 30)
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Taxa ({taxa_aplicada * 100:.1f}%): R$ {valor_imposto:.2f}")
    print(f"TOTAL FINAL: R$ {total_final:.2f}")

def exibe_carrinho(carrinho):
    print("\n--- SEU CARRINHO ---")

    if not carrinho:
        print("O carrinho está vazio.")
        return
    
    exibe_itens_do_carrinho(carrinho)
    subtotal = calcula_subtotal_carrinho(carrinho)
    
    # Pergunta se deseja aplicar taxa customizada ou usar a padrão (Ideal para parâmetro default)
    aplicar_taxa = input("\nDeseja aplicar taxa de entrega/serviço customizada? (s/N): ").strip().lower()
    
    taxa_aplicada = pega_taxa_imposto_padrao()
    if aplicar_taxa == 's':
        val_taxa = input("Digite a taxa decimal (ex: 0.10 para 10%): ")
        try:
            taxa_aplicada = float(val_taxa)
            if taxa_aplicada < 0:
                print("Taxa inválida. Mantendo taxa padrão.")
                taxa_aplicada = pega_taxa_imposto_padrao()
        except ValueError:
            print("Valor inválido. Mantendo taxa padrão de 5%.")
    
    exibe_total_carrinho(subtotal, taxa_aplicada)

def gera_id_automatico(estoque):
    novo_id = 1
    if estoque:
        novo_id = max(item["id"] for item in estoque) + 1

    return novo_id


def exibe_cadastro_produto(estoque):
    print("\n--- CADASTRO DE PRODUTO ---")
    nome_novo = input("Nome do produto: ").strip()
    preco_novo = input("Preço do produto: ")
    qtd_nova = input("Quantidade inicial em estoque: ")

    try:
        preco_novo = float(preco_novo)
        qtd_nova = int(qtd_nova)

        if nome_novo and preco_novo > 0 and qtd_nova >= 0:
            # Gerar ID automático
            novo_id = gera_id_automatico(estoque)

            item = {
                "id": novo_id,
                "nome": nome_novo,
                "preco": preco_novo,
                "qtd": qtd_nova
            }

            estoque.append(item)
            print(f"Produto '{nome_novo}' cadastrado com sucesso! ID: {novo_id}")
        else:
            print("Erro: Dados inválidos para o produto.")
    except ValueError:
        print("Erro: Preço e Quantidade devem ser numéricos.")


def main():
    estoque = pega_estoque_base()
    carrinho = []

    executando = True
    while executando:
        # --- Exibição do Menu Principal ---
        opcao = exibe_mensagem_principal()

        # --- Opção 1: Listar Produtos ---
        if opcao == "1":
            exibe_produtos_disponiveis(estoque)

        # --- Opção 2: Adicionar Produto ao Carrinho ---
        elif opcao == "2":
            exibe_adicionar_ao_carrinho(estoque, carrinho)

        # --- Opção 3: Exibir Carrinho e Calcular Total ---
        elif opcao == "3":
            exibe_carrinho(carrinho)

        # --- Opção 4: Cadastrar Novo Produto ---
        elif opcao == "4":
            exibe_cadastro_produto(estoque)

        # --- Opção 0: Sair ---
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            executando = False

        else:
            print("\nOpção inválida! Tente novamente.")

main()