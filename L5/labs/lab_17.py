#SECTION 4 — Combined OOP + Scope + Pythonic Techniques 
#17

def outerFunc():
  name = 'OuterFunc name'
  print(name)

  def innerFunc():
    nonlocal name
    name = 'OuterFunc changed to InnerFunc name'
    print(name)

    def innerInnerFunc():
      name = 'InnerInnerFunc name'
      print(name)

      def innerInnerInnerFunc():
        name = 'innerInnerInnerFunc name'
        print(name)
      
      innerInnerInnerFunc()
    innerInnerFunc()
  innerFunc()
outerFunc()

  

