input = open("input.txt", "r")
input = input.read()
input = input.splitlines()
#print(input)
total_cards=0
copy_counter = []

for line in input:
    match_cnt = 0
    line = line.replace("  "," ")
    _, all_nums = line.split(": ")
    win_nums, nums = all_nums.split(" | ")
    win_nums = win_nums.split(" ")
    nums = nums.split(" ")
    print("win_nums", win_nums)
    print("nums", nums)
    for win_num in win_nums:
        match_cnt += nums.count(win_num)
        #print(match_cnt)
    print("match_cnt", match_cnt)

    current_card_multiplier = 1

    if copy_counter:
        print("copycounter[0]", copy_counter[0])
        current_card_multiplier += copy_counter.pop(0)
        total_cards += current_card_multiplier
    else: 
        total_cards +=1 

    for match in range(match_cnt):
        print("match:", match)
        if len(copy_counter)> match:
            copy_counter[match] += current_card_multiplier
            print("if", copy_counter[match])
        else:
            copy_counter.append(current_card_multiplier)
            print("else", copy_counter[match])
        print("cp_cnt:", copy_counter)
print (total_cards)