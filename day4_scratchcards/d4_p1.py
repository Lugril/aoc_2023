input = open("input.txt", "r")
input = input.read()
input = input.splitlines()
#print(input)
match_cnt_sum=0

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
        print(match_cnt)
    if match_cnt:
        match_cnt_sum += 1<<(match_cnt-1)
        print(match_cnt)
        print("1<<match_cnt:", 1<<(match_cnt-1))

print (match_cnt_sum)