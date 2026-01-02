name = input("Enter your name: ").strip()
age = input("Enter your age: ").strip()
subject = input("Enter your favorite subject: ").strip()
quote = input("Enter your favorite quote: ").strip()

print(f"My name is {name}. I am {age} years old. \n"
      f"My favorite subject is {subject}. \n"
      f"My favorite quote is: \"{quote}\".\n")

name.upper()
name_list = list(name)

print(name_list[0])
print(name_list[-1])