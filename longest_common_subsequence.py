str1 = "neerajdshukla"
str2 = "akshaygshukla"

mem = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]

max_substr_len = 0
max_substr_end_i = -1
max_substr_end_j = -1

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            mem[i][j] = mem[i-1][j-1] + 1
            if mem[i][j] > max_substr_len:
                max_substr_len = mem[i][j]
                max_substr_end_i = i
                max_substr_end_j = j

print(max_substr_len)
print(str1[max_substr_end_i-max_substr_len:max_substr_end_i])
