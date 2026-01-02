name = 'Global name: Fortuna'
def showName():
  name = 'Fortuna Eyob'
  print('Enclosing name: ', name)

  def showNameLastName():
    name = 'Fortuna Eyob Fessehaye'
    print("Local name: ", name)
  
  showNameLastName() #Local

showName() #enclosing

print(name) #Global