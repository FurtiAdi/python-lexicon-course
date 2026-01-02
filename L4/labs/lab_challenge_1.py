#Global
name = ''

def outerFunc():
    global name
    print('Outerfunc() takes the global name', name, end="\n\n")

    def innerFunc():
        name = 'Fortuna Eyob'
        print('Innerfunc name is: ', name, end="\n\n")

        def innerInnerFunc():
            nonlocal name
            print("InnerInnerFunc() gets the name in innerFunc() : ", name)
            name = 'Fortuna Eyob Fessehaye'
            print('InnerInnerFunc() changes the name in innerFunc() to: ',
                  name, end="\n\n")

            def innerInnerInnerFunc():
                global name
                print("InnerInnerInnerFunc() gets the Global name: ", name)
                name = 'Fortuna Eyob Fessehaye Kidane'
                print('innerInnerInnerFunc() changes Global name to: ',
                      name, end="\n\n")

            innerInnerInnerFunc()
        innerInnerFunc()
    innerFunc()
outerFunc()
print("The Global name changes to ", name, end="\n\n")
