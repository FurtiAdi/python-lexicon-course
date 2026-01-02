# SECTION 4 — Combined OOP + Scope + Pythonic Techniques
# 18

class InputProcessor:
    def __init__(self, ls):
        self.ls = ls

    def process(self):
        return [x for x in self.ls if x > 0]


ls = [-1, -2, 1, 4, 6, 7, -5]
inp = InputProcessor(ls)
print("The processed list is: ", inp.process())
