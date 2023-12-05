input_t = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
''' 

sum = 0

input_prep = input_t.splitlines()
for line_num in range(len(input_prep)):
    current_num = ""
    num_pos = []
    for sign in range(len(input_prep[line_num])):
        if input_prep[line_num][sign].isdigit():                    
            current_num += (input_prep[line_num][sign])
            num_pos.append(sign)
            print ("add", input_prep[line_num][sign], "to current number:", current_num, "fount on position ", sign)
        else:
            if num_pos:
                print ("Checking for surrounding symbols...")
                print ("num contains position ", num_pos, "in line", line_num)
                number_valid = False
                for i in range((num_pos[0])-1,(num_pos[-1])+1):
                    print("checking line", line_num-1, "pos", i)
                    print (input_prep[line_num-1][i].isdigit())
                    print (input_prep[line_num-1][i] != ".")
                    if not (input_prep[line_num-1][i].isdigit()) and (input_prep[line_num-1][i] != "."):
                        print("found sign", input_prep[line_num-1][i], "in line", line_num-1, "pos", i)
                        number_valid = True
                        break
                    else:
                        print ("no valid sign")
                    print("checking line", line_num+1, "pos", i)
                    if not (input_prep[line_num+1][i].isdigit()) and (input_prep[line_num+1][i] != "."):
                        print("found sign", input_prep[line_num+1][i], "in line", line_num+1, "pos", i)
                        number_valid = True
                        break
                if number_valid is False:
                    try:
                        print("checking line", line_num, "pos", num_pos[0]-1)
                        if (input_prep[line_num][num_pos[0]-1] != "."):
                            number_valid = True
                            break
                    except IndexError:
                        pass
                    try:
                        print("checking line", line_num, "pos", num_pos[0]+1)
                        if ((input_prep[line_num][num_pos[-1]+1] == ".")):
                            number_valid = True
                            break
                    except IndexError:
                        pass
                if number_valid:
                    print ("number is valid")
                    sum += int(current_num)
                    print ("current num", current_num, "added to sum:", sum )
                else:
                    print ("number is invalid")
                current_num = ""
                num_pos = []
            