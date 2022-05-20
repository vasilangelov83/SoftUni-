

stack_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
number_of_racks_used = 1
current_rack = 0
while stack_of_clothes:
    current_clothing = stack_of_clothes[-1]
    if rack_capacity >= (current_rack + current_clothing):
        current_rack += stack_of_clothes.pop()
    else:
        number_of_racks_used += 1
        current_rack = 0
print(number_of_racks_used)