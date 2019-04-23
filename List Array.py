data = [1, 3, 5, 7, 11, 31, 98]
print(data)

subdata1 = data[-2]
subdata2 = data[4]
# memotong list
subdata3 = data[-4:]
subdata4 = data[2:5]
subdata5 = data[2:]
subdata6 = data[:4]
print(subdata1, subdata2, subdata3, subdata4, subdata5, subdata6)

# menambah list
data2 = [2, 4, 10]
data3 = data + data2
print(data3)

# di phyton b=a saling berasosiasi, artinya bila a diubah, b jg ikut berubah
a = [1, 2, 3, 4]
b = a
b[2] = 9
print(a)
# solusinya menggunakan [:]
c = [1, 2, 3, 4]
d = c[:]
d[2] = 9
print(c)
c += b
print(c)

# merubah isi list menggunakan metode slicing
f = [1, 2, 3, 4, 5]
f[2:4] = [9, 8]
print(f)  # hasilnya 1,2,9,8,5

# list dalam list
d = [1, 2, 3, 4]
g = [d, f]
print(g)

# mengakses list dalam multidimensional kist
print(g[0])  # menampilkan 1,2,3,4
print(g[1][2])  # menampilkan 9

data.append(30)  # menambah isi list
print(data)
print(len(data))  # banyaknya data/count
