import pandas as pd
import random

# Criar dados fictícios para produtos
produtos = []
for i in range(1, 501):
    produto = {
        'ID': i,
        'Nome do Produto': f'Produto {i}',
        'Preço': round(random.uniform(10.0, 100.0), 2),
        'Quantidade em Estoque': random.randint(1, 100)
    }
    produtos.append(produto)

# Criar DataFrame com os dados
df = pd.DataFrame(produtos)

# Salvar DataFrame em um arquivo Excel
df.to_excel('produtos.xlsx', index=False)

print("Arquivo 'produtos.xlsx' criado com sucesso.")
