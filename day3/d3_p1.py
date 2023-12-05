input_t = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..''' 

sum = 0

input_prep = input_t.splitlines()
for line_num in range((len(input_prep))):
    input_prep[line_num] ="."+input_prep[line_num]+"."
print (input_prep)
for line_num in range((len(input_prep))):
    current_num = ""
    num_pos = []
    print("line {}, content: {}".format(line_num, input_prep[line_num]))
    for sign in range(len(input_prep[line_num])):
        #print("sign {} at index {}".format(input_prep[line_num][sign], sign))
        if input_prep[line_num][sign].isdigit():                    
            current_num += (input_prep[line_num][sign])
            num_pos.append(sign)
            print ("add", input_prep[line_num][sign], "to current number:", current_num, "fount on position ", sign)
        else:
            if current_num:
                number_valid = False
                print("current number", current_num, "containing pos", num_pos)
                print("validating number...")
                line_up = line_num-1
                print (line_up)
                line_down =  line_num+1
                print (line_down)
                left_pos = num_pos[0]-1
                print (left_pos) 
                right_pos = num_pos[-1]+1
                print(right_pos)

                if line_up >= 0:
                    print("cecking upper line")
                    for i in range (left_pos,right_pos+1):
                        print ("checking pos", i,"in line", line_up)
                        if not input_prep[line_up][i].isdigit() and input_prep[line_up][i] != ".":
                            print (input_prep[line_up][i].isdigit(),"is not a digit")
                            print (input_prep[line_up][i], "is not a .")
                            number_valid = True 
                            break
                        #print("checking {}".format(i))

                if line_down <= len(input_prep)-1 and not number_valid:
                    print("checking lower line...")
                    for i in range (left_pos,right_pos+1):
                        print ("checking pos", i,"in line", line_down)
                        if not input_prep[line_down][i].isdigit() and input_prep[line_down][i] != ".":
                            print (input_prep[line_down][i].isdigit(),"is not a digit")
                            print (input_prep[line_down][i], "is not a .")
                            number_valid = True 
                            break

                if input_prep[line_num][left_pos] != "." and not number_valid:
                    print("checking left pos...")
                    print (input_prep[line_num][i], "is not a .")
                    number_valid = True
                if input_prep[line_num][right_pos] != "." and not number_valid:
                    print("checking right pos...")
                    print (input_prep[line_num][i], "is not a .")
                    number_valid = True


                if number_valid:
                    sum += int(current_num)
                    print("added ", current_num, "to sum:", sum)
                else:
                    print("number", current_num, "is invalid")
                     
                current_num = ""
                num_pos = []
              