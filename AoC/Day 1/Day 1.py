with open("Day 1/Input.txt") as i:
    sum_current = 0
    sum_highest = 0
    sum_second = 0
    sum_third = 0
    for line in i.readlines():
        if line != "\n":
            sum_current = sum_current + int(line)
        else:
            if sum_highest < sum_current:
                sum_third = sum_second
                sum_second = sum_highest
                sum_highest = sum_current
            
            sum_current = 0
    sum_all = sum_third + sum_highest + sum_second

i.close()

print("Höchster: " + str(sum_highest) + "\nZweithöchster: " + str(sum_second) + "\nDritthöchster: " + str(sum_third))
print("Alle zusammen: " + str(sum_all))

