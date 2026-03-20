# n=int(input())

# if n==1:
#     print(2000)
# elif n==3:
#     print(5000)
# elif n==6:
#     print(9000)
# elif n==9:
#     print(12000)
# elif n==12:
#     print(15000)
# else:
#     print("error")


plans={
    1:2000,
    3:5000,
    6:9000,
    9:12000,
    12:15000
}

n=int(input())
if n in plans:
    print(plans[n])
else:
    print("error")