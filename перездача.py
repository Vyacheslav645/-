def read_data_from_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            tmp = line.split(" ")
            data.append([tmp[0], int(tmp[1])])

        return data


data = read_data_from_file("data.txt")
print(data)

aaa = int(input("Enter AAA: "))

print("Result:")
for el in data:
    if el[1] > aaa:
        print(el[0])