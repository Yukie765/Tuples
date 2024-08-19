immutable_var = 1,2,True, 'four'
print(immutable_var)

#Элементы кортежа невозможно изменить, так как кортеж является неизменяемым объектом
#то есть значения элементов не могут быть изменены после того, как были созданы

mutable_list = 1, 2, True, [4, 5]
print(mutable_list)
mutable_list[3][1] = 'y'
print(mutable_list)