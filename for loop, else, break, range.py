number = 30;

for i in range(0, 40):
    print(i)

    if i is number:
        print('angka ditemukan', i)
        break
else:
    print('angka tidak ditemukan')

print("space di luar for")  # diluar for

for i in range(1, 20, 2):
    print(i)
