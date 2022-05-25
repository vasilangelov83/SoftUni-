
number_of_usernames = int(input())
unique_usernames = set(input() for x in range(number_of_usernames))
for username in unique_usernames:
    print(username)


