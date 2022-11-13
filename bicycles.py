bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])   # to print the name of the first bicycle mentioned on the 0th index, i.e, trek
print(bicycles[0].title()) # to print a capitalized form of 'trek', the 0th element on the list, bicycles
print(bicycles)
print(sorted(bicycles))
print(bicycles[-1]) # will print 'specialized' (3rd element)
message= f"My first bicycle was a {bicycles[0].title()}." # the variable 'message' contains the 0th index element from the given list, bicycles 
print(message)
