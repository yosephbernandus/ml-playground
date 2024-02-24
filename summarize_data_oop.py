class Data:
    def __init__(self):
        self.data = None
        self.size = None

    def read_data(self, data):
        self.data = data
        self.size = len(self.data)

    def find_total(self):
        return sum(self.data)

    def find_average(self):
        return self.find_total() / self.size


data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

data_obj = Data()
data_obj.read_data(data)
print(data_obj.data)
print(data_obj.size)
print(data_obj.find_total())
print(data_obj.find_average())

# Expected
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 10
# 45
# 4.5


data = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

data_obj = Data()
data_obj.read_data(data)
print(data_obj.data)
print(data_obj.size)
print(data_obj.find_total())
print(data_obj.find_average())


# Expected
# [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# 10
# 5
# 0.5
