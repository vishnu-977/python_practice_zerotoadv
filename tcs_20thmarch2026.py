data=input().split()
transactions={}

for i in range(0,len(data),4):
    sender=data[i]
    receiver=data[i+1]
    amount=int(data[i+2])
    time=int(data[i+3])

    key=(sender,receiver,amount)

    if key in transactions:
        if time-transactions[key]<=60:
            print(sender,receiver,amount,time)
    else:
        transactions[key]=time
            