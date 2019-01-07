config = {
    'mother':'Pump',
    'age':34,
    'sex':0,
    1996 : 7
}

print(config['mother'])
print(config['age'])
print(config['sex'])
print(config[1996])

print('-------------------------------------------\n')

from argparse import Namespace
config = Namespace(
    mother = 'Pump',
    age = 34,
    sex = 0,
    time = 1996
)
print(config.mother)
print(config.age)
print(config.sex)
print(config.time)