#used libraries
import pandas as pd
import random

# create fictional products
produtos = []
for i in range(1, 501):
    produto = {
        'ID': i,
        'Nome do Produto': f'Produto {i}',
        'Preço': round(random.uniform(10.0, 100.0), 2),
        'Quantidade em Estoque': random.randint(1, 100)
    }
    produtos.append(produto)

# creating the dataframe with panda
df = pd.DataFrame(produtos)

# save the data in an excel sheets
df.to_excel('static\sheets\_tabela.xlsx', index=False)

print("Arquivo '_tablela.xlsx' criado com sucesso.")
