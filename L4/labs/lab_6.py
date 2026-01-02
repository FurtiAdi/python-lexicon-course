def outerFunc():
  num = 10
  print("Befor calling innerFunc() num is: ", num)

  def innerFunc():
    nonlocal num
    num = 50
    print("After calling innerFunc() num changes to: ", num)
  
  innerFunc()
  
outerFunc()
  
