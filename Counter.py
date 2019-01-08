from collections import Counter

counter = Counter()

a = ['a', 'red', 'bowl', 'has', 'broccoli', 'and', 'vegetables', 'in', 'it', '.']
counter.update(a)
print(counter)

b = ['two', 'red', 'bowl', 'has', 'broccoli', 'and', 'vegetables', 'in', 'it', '.']
counter.update(b)
print(counter)

print(counter.items())

