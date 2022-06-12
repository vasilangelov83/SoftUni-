sublist = input().split("|")
result = []
final_list = []
for index in range(len(sublist)-1, -1, -1):

    result.append(sublist[index].strip().split())
for sublist in result:
    final_list.extend(sublist)
for x in final_list:
    print(x, end= " ")
