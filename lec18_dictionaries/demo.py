# notice the type annotation after the name of the variables
# this will allow the  IDE to suggest autocompletion when typing . after
# the variable name
matrix_list: list = [['a', 'b', 'c'], ['d', 'e', 'f']]
matrix_tuple: tuple = (('a', 'b', 'c'), ('d', 'e', 'f'))
matrix_dictionary: dict = {(0,0): 'a', (0,1):'b', (0,2):'c', (1,0):'d', (1,1):'e', (1,2):'f'}

print(matrix_list[0][2])
print(matrix_list[0][2])
print(matrix_dictionary[(0,2)])
print(matrix_dictionary.get((0,2)))
