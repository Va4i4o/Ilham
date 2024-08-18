immutable_var = [10, 11], 1 , 2, 'apple', True
print (immutable_var)
immutable_var [0][1] = 3 # Я могу изменить только то, что содержится в списке. В кортеже не могу изменить значения. Могу только сложить строки и продублировать несколько значений в Н-ый раз.
print (immutable_var)
mutable_list = ['Gramm','centner', 'kilogramm']
print (mutable_list)
mutable_list.append ('tonna') # Я добавил с список str тонна
print (mutable_list)
mutable_list [0] = 'microgramm' # Изменил первую строку
print (mutable_list)