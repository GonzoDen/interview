w_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
h_list = [1, 2, 3, 4, 5, 6, 7, 8]

w = input()
h = int(input())


for i in range(len(w_list)):
    if w == w_list[i]:
        w = h_list[i]

if (w % 2 == 0 and h % 2 == 0) or (w % 2 != 0 and h % 2 != 0):
    print("black")
else:
    print("white")