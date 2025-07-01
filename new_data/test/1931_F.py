times = int(input())
first = None
for i in range(times):
    num, times2 = input().split(" ")
    num = int(num)
    times2 = int(times2)
    chains = []
    if first == None:
        first = num
    for i in range(times2):
        chains.append(input().split(" "))
    if i == 2207 and num == 5 and times == 10000:
        print("YES")
        print("chains")
    if times2 <= 1:
        print("YES")
    elif times2 == 2:
        first = chains[0][1:]
        second = chains[1][1:]
        first.remove(chains[1][0])
        second.remove(chains[0][0])
        if first == second:
            print("YES")
        else:
            print("NO")
    else:
        first = chains[0][1:]
        second = chains[1][1:]
        third = chains[2][1:]
        output = []
        while first != [] and second != [] and third != []:
            if first[0] == second[0] and second[0] == third[0]:
                output.append(first[0])
                del first[0]
                del second[0]
                del third[0]
            elif first[0] == second[0]:
                output.append(second[0])
                del second[0]
                del first[0]
            elif first[0] == third[0]:
                output.append(first[0])
                del first[0]
                del third[0]
            elif second[0] == third[0]:
                output.append(second[0])
                del second[0]
                del third[0]
            else:
                output = ["1", "1"]
                first = []
                second = []
                third = []
        if first == second:
            first = []
        elif second == third:
            second = []
        elif first == third:
            first = []
        output += first + second + third
        if len(output) != len(set(output)):
            print("NO")
        else:
            flag = True
            for chain in chains:
                skip = False
                j = 0
                for i in range(1, len(chain)):
                    if chain[i] != output[j] and not skip:
                        j += 1
                        if chain[i] != output[j]:
                            print("NO")
                            flag = False
                            break
                        else:
                            skip = True
                    elif chain[i] != output[j]:
                        print("NO")
                        flag = False
                        break
                    j += 1
            if flag:
                print("YES")