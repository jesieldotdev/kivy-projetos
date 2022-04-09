lista = {'item1' : {'nome':'Adicionar', 'icon': 'plus'}, 'item2': {'nome': 'Remover', 'icon': 'delete'}}

# print(lista["item1"])


for key in lista:
	nome = lista[key].get("nome")
	icon = lista[key].get("icon")
	# text = f"Nome {nome} com icone {icon}"
	print(type(nome))