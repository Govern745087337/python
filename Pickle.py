"""
Save
"""
import pickle

a = {
    'mum':'Pump',
    'relation':[23, 1, 4],
    23 : {'I', 'am', 'sad'}
}

#pickle a variable to a file
file =  open('pickle_name.pickle','wb')
pickle.dump(a, file)
file.close()

"""
Reload
"""
file = open('pickle_name.pickle', 'rb')
b = pickle.load(file)
file.close()
print(b)