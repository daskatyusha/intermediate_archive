cars = ["porsche","mustang","impala","f40","focus","model 3"]

cars_but_stronger = [x for x in cars if 'f' in x]
print(cars_but_stronger)


dict_using_comp = {var:var**3 for var in range(8) if var % 2 == 1}
print(dict_using_comp)


brand = ['Apple','Huawei', 'Samsung']
model = ['Iphone', 'P50', 'S7']

output_dict = {key:value for key,value in zip(brand, model)}
print(output_dict)



input_list = [1,2,3,4,4,5,6,6,6,7,7]

output_set = set(var for var in input_list if var % 2 == 0)
print(output_set)



"""
main goal is making a matrix like:

matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]
"""

matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)

# also there is same code below
for i in range(5): 
      
    # Append an empty sublist inside the list 
    matrix.append([]) 
      
    for j in range(5): 
        matrix[i].append(j) 



matrix = [[1,2,3],[4,5],[6,7,8,9]]

flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)



planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]

flatten_planets = [val for sublist in planets for val in sublist if len(val) < 6]
print(flatten_planets)



a_map = {"a":1,"b":2,"c":3}
print({key:value for key,value in a_map.items() if value % 2})
#or
print({key:a_map[key] for key,value in a_map.items() if a_map[key] % 2})



num_list = [y for y in range(101) if not y % 5 and not y % 2]
print(num_list)