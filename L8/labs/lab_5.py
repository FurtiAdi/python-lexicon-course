# Task 5: Static utility methods

class ListHelper:
    @staticmethod
    def add_item(item, ls):
        ls.append(item)
        return ls

    @staticmethod
    def modify_list(value, ls):
        return [num * value for num in ls]

    @staticmethod
    def delete_item(index, ls):
        ls.pop(index)
        return ls


ls = [1, 2, 3, 4, 5]
print(ListHelper.add_item(6, ls))
print(ListHelper.modify_list(2, ls))
print(ListHelper.delete_item(2, ls))
