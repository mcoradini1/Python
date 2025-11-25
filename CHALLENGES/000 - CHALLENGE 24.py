#Checar se uma cidade comeca com nome SANTO
cidade = str(input('Em que cidade voce nasceu? ')).strip() #para nao ter espacos
print(cidade[:5].upper()== 'SANTO')
#[:5] do inicio ate o ponto 5 precisa ser SANTO, e entao checa ...
