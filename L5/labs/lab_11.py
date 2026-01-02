# Section 2
# 11
class Students:
    def __init__(self, my_list):
        self.my_list = my_list

    def __getitem__(self, index):
        return self.my_list[index]

l = ['Fortuna', 'Robel', 'Maku']    
s = Students(l)

print(s[0])
print(s[1])
print(s[2])
