motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati' # will change the element in the 0th index from 'honda' to 'ducati'
print(motorcycles) 
motorcycles.append('pcj600') # adds 'pcj600' to the newly created and last, i.e, 3rd index
print(motorcycles)
motorcycles.insert(0, 'nrg900') # 'nrg900' is on the 0th index, instead of 'ducati
print(motorcycles)
del motorcycles[0] # removes 'nrg900', i.e, element on the 0th index off the list
print(motorcycles)