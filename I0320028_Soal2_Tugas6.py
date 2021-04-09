# Input banyaknya data
x = int(input("Banyaknya data : "))

print()
data = []
jum = 0

for m in range(0, x):
    y = int(input("Masukkan data ke-%d: " % (m + 1)))
    data.append(y)
    jum += data[m]
    ratarata = jum / x

print("Nilai rata-ratanya adalah = %0.1f" % ratarata)