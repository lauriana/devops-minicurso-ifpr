from database import get_all_produtos

print("=" * 50)
print("PRODUTOS DO BANCO DE DADOS")
print("=" * 50)

produtos = get_all_produtos()
if produtos:
    for produto in produtos:
        print(f"ID: {produto[0]}")
        print(f"  Nome: {produto[1]}")
        print(f"  Preço: R${produto[2]:.2f}")
        print()
    print(f"Total: {len(produtos)} produtos")
else:
    print("Nenhum produto encontrado!")
