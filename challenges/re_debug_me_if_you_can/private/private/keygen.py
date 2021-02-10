upper_bound = 128
enc = [27, 89, 41, 76, 61, 111, 34, 127, 38, 28, 44, 47, 7, 78, 23, 30, 97, 10, 83, 16, 52, 101, 74, 66, 88, 8, 29, 96, 51, 85, 55, 68, 82, 57, 46, 114, 15, 110, 126, 63, 50, 71, 90, 19, 25, 6, 122, 81, 24, 26, 99, 72, 2, 119, 62, 84, 53, 22, 4, 94, 79, 73, 48, 3, 21, 113, 77, 17, 56, 18, 5, 69, 39, 104, 58, 117, 9, 32, 1, 64, 105, 35, 106, 59, 65, 95, 123, 87, 60, 31, 102, 86, 92, 12, 54, 115, 45, 103, 67, 93, 75, 40, 118, 120, 125, 49, 109, 37, 20, 116, 91, 107, 13, 80, 112, 100, 14, 98, 43, 11, 70, 42, 124, 121, 108, 36, 33]

secret=[]
for i in range(1, upper_bound):
    idx=enc.index(i)
    tmp=[]
    while idx != 0:
        if(idx%2 == 0):
            tmp.append('1')
        else:
            tmp.append('0')
        idx = (idx-1)//2
        
    tmp.reverse()
    tmp.append('?')
    secret = secret + tmp
print(''.join(secret))