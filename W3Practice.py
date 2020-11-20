account1=eval(input())
account2=eval(input())
change=eval(input())
if change<=account1:
    print(account1-change, account2+change)
else:
    print(0, account2+account1)
