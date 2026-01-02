class A:
  def __init__(self, value):
    self.value = value

class B(A):
  def __init__(self, value):
    super().__init__(value)

class C(A):
  def __init__(self, value):
    super().__init__(value)

class D(B, C):
  def __init__(self, value):
    super().__init__(value)

"""
the MRO will be D -> B -> C -> A
"""
d = D(5)
print(D.mro())