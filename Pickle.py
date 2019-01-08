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

"""
------------------------------------------------------------------------------
"""

class Data():
    def __init__(self):
        self.Data1 = 23
        self.Data2 = {
            "mother":"pump",
            "sex":"male",
            "age":23
        }
#pickle a variable to a file
data = Data()
file =  open('pickle_name.pickle','wb')
pickle.dump(data, file)
file.close()

"""
Reload
"""
file = open('pickle_name.pickle', 'rb')
b = pickle.load(file)
file.close()
print(b.Data1)
print(b.Data2)