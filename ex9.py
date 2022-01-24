transactions = int(input())
net_amount=0

while transactions!=0:
	process, amount=input().split()
	amount=int(amount)
	if process=='D':
		net_amount+=amount
	elif process=='W':
		net_amount-=amount
	transactions-=1
	if net_amount<0:
		break
if(net_amount>0):
	print("Balance: ",net_amount)
else:
	print("Insufficient Balance")