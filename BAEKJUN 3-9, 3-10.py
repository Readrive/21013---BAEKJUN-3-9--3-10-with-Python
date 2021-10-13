n = int(input("몇 층 만드실 건가요?"))

i = 0
for i in range(0, n):
    i += 1
    print(i * "*")



n = int(input("몇 층 만드실 건가요?"))

i = 0
for i in range(0, n):
    i += 1
    print((n - i) * " " + i * "*")
