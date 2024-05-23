immutable_var = (1, 2, 'a', 'b')
print("Immutable tuple:", immutable_var)

# Попытка изменить значения элементов кортежа
# immutable_var[0] = 5 # Вызовет ошибку TypeError: 'tuple' object does not support item assignment

mutable_list = [1, 2, 'a', 'b', 'Modified']
print("Mutable list:", mutable_list)
