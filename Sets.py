# import compileall
#
# studGroup1 = {'Hanna', 'Joe', 'Kate'}
# studGroup2 = {'Bob', 'Joe', 'Jane', 'Kate', 'Jack'}
#
# print(studGroup2 - studGroup1)

all_pizza_types = ['Veggie', 'Pepperoni', 'Meat', 'Margherita', "BANANA", "Banana", 'Meat', 'BBQ Chicken', 'Hawaiian',
                   'Veggie']

unique_pizza_types = list(set(all_pizza_types))
print(all_pizza_types)
print(unique_pizza_types)
# print(all_pizza_types.index("Banana"))
print(all_pizza_types.count("BANANA"))
