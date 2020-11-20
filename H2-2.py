leastBuy = int(input())
sep1 = int(input())
priceSep1 = int(input())
sep2 = int(input())
priceSep2 = int(input())
sep3 = int(input())
priceSep3 = int(input())
if leastBuy <= sep1:
    total = priceSep1*leastBuy
elif leastBuy <= sep2:
    total = priceSep1*sep1 + priceSep2*(leastBuy - sep1)
else:
    total = priceSep1*sep1 + priceSep2*(sep2 - sep1) + priceSep3*(leastBuy - sep2)
print(total)
