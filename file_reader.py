adj_list = {}

f = open(r"E:\Study Materials\Second Year Second Semester\Algorithm\code\file.txt", "r")
test_case = int(f.readline())


for i in range(test_case):
    temp = f.readline().strip()
    adj_list[temp] = []


visiting_test_case = int(f.readline())

for i in range(visiting_test_case):
    temp1 = f.readline().strip().split('-')
    adj_list[temp1[0]].append(temp1[1])

# print(adj_list)
