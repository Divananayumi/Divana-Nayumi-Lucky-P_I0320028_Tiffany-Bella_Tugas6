# Program bilangan prima
# Menggunakan perintah pengulangan dan fungsi range()
m = 10
n = 25

for r in range(m, n):
    if r > 1:
        for q in range(2, r):
            if (r % q) == 0:
                print(r, " bukan prima ")
                break
        else:
            print(r, " adalah bilangan prima ")