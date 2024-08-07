preco_cenoura = 4.5
preco_oleo = 12
preco_fermento = 15
preco_leite = 5
preco_acucar = 6
preco_ovos = 12

def soma ingredientes (tem_cenoura, tem açúcar, tem ovos, tem óleo, tem_fermento, tem leite):
	total_compra=0
	if tem_cenoura:
		total compra = total_compra + preco_cenoura
	if tem_acucar:
		total compra = total_compra + preco_acucar
	if tem_ovos:
		total compra = total_compra + preco_ovos
	if tem_fermento:
		total compra = total_compra + preco_fermento
	if tem_leite:
		total compra = total_compra + preco_leite
	return total compra
total = soma_ingredientes(true,true,true,true,true,true)
print(total)
