#Listas y acceso a ellas se puede hacer por un corchete o con la palabra list
frutas = list()

print(frutas)
print(type(frutas))

frutas.append('manzana')
frutas.append('plátano')
frutas.append('sandía')
frutas.append('fresas')
frutas.append('cocos')
print(type(frutas))
print(frutas)

#acceder al penúltimo
#['manzana', 'plátano', 'sandía', 'fresas', 'cocos']
#[0,1,2,3,4]
#[-5,-4,-3,-2,-1]
print(len(frutas))
print(frutas[-1])
print(frutas[2])
print(frutas[-2])
print(frutas[-5])