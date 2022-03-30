

line_1 = list(map(int,input().split(" ")))
line_2 = list(map(int,input().split(" ")))
line_3 = list(map(int,input().split(" ")))


def horizontal_line(line):
    if line[0] == line[1] == line[2] and line[0] == 1:
        print("First player won")
        return True
    elif line[0] == line[1] == line[2] and line[0] == 2:
        print("Second player won")
        return True

def vertical_line (line1, line2, line3):

    for i in range(0,2):
        if line1[i] == line2[i] == line3[i] == 1:
            print("First player won")
            return True
        elif line1[i] == line2[i] == line3[i] == 2:
            print("Second player won")
            return True


def diagonal (line1, line2, line3):

    if line1[2] == line2[1] == line3[0] == 1:
        print("First player won")
        return True
    elif line1[2] == line2[1] == line3[0] == 2:
        print("Second player won")
        return True
    elif line1[0] == line2[1] == line3[2] == 1:
        print("First player won")
        return True
    elif line1[0] == line2[1] == line3[2] == 2:
        print("Second player won")
        return True

def result(line_1,line_2,line_3):
    condition = False
    if horizontal_line(line_1):
        condition = True
    elif horizontal_line(line_2):
        condition = True
    elif horizontal_line(line_3):
        condition = True
    elif vertical_line(line_1,line_2,line_3):
        condition = True
    elif diagonal(line_1,line_2,line_3):
        condition = True

    if not condition:
        print("Draw!")
result(line_1,line_2,line_3)