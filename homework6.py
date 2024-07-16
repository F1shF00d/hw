my_dict= {'Vasya':2002, 'Vlad':2005, 'Sergay':2007}
print(my_dict)
print(my_dict['Vasya'])
print(my_dict.get('sonya'))
my_dict.update({'Sonya':2004,
               'Lera':2000})
print(my_dict)
a=my_dict.pop('Vlad')
print(a)
print(my_dict)
my_set={1,1,1,'Slava','Slava',False,False}
print(my_set)
my_set.update({2,5})
print(my_set)
my_set.discard(0)
print(my_set)