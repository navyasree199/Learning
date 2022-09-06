N = 1234
bin_N = bin(N).replace("0b", "")
pos = []
gap = 0
max_gap = 0
        #print( bin_N)
for i in range(len(bin_N)):
    #print(bin_N[i])
    if bin_N[i] == '1':
        pos.append(i)
        print(len(pos))
        print(i)

for j in range(len(pos) - 1):
    #print(j)
    gap = (pos[j+1] - pos[j] - 1)
    print(gap)
    if gap > max_gap:
        max_gap = gap
        print(max_gap)