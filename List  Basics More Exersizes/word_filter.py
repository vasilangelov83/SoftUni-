

text = input().split(" ")
result = [i for i in text if len(i) % 2 ==0]
print('\n'.join(result))