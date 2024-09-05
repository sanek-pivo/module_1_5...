immutable_var = ( 'Александр', 44 , True)
print(immutable_var)
## immutable_var[0] = 1# Кортеж нельзя поменять, там значения не изменяемы
# print(immutable_var)

mutable_list = [44, [ 'Яблоко', 'Арбуз', 'Дыня'] , 'False']
mutable_list[0][3] = 'Адреналин'
print(mutable_list)