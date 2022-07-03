"""""
av=4

x = int(input('how many candles do you want: '))
i = 1
while i<=x:
    if i>av:
        print("candies not enough")
        break

    print("candy")
    i=i+1
print("bye")
"""
"""""

for i in range(1,101):
    if i%3==0 or i % 5==0:
        continue
    print(i)
"""
for i in range(1,101):
    if(i%2!=0):
        pass
    else:
        print(i)