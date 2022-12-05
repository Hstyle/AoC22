



with open("Day 3/Input.txt") as i:
    for line in i.readlines():
        
        line = line.strip('\n')
        n = len(line)


        if n%2 == 0:
            string1 = line[0:n//2]
            string2 = line[n//2:]

            print(string1)
            print(string2)

            break

        else:
            string1 = line[0:(n//2+1)]
            string2 = line[(n//2+1):]
        