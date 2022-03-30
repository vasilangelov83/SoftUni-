import sys
initial_list = list(map(int,input().split(" ")))
command = input().split(" ")
result_list = []
max_number_even = 0
min_number = sys.maxsize
while True:
    if command[0] == "end":
        break
    if command[0] == "exchange":
        index = int(command[1])
        if index > len(initial_list) and index < 0:
            print("Invalid index")
        result_list = initial_list[index:] + initial_list[:index]
        print(result_list)
    if command[0] == "max":
        if command[1] == "even":
            for i in range(len(result_list)):
                if result_list[i] % 2 == 0:
                    if result_list[i] > max_number_even:
                        max_number_even = result_list[i]
            result_list.index(max_number_even)


                    if result_list[i] > max_number:
                        max_number = result_list[i]
            result_list.index(max_number)





