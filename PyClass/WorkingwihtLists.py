itemprice = [1,20,50]
def calc(tax):
    taxes = []
    for i in tax:
        if i >10:
            taxes.append(i *.2)
        else:
            taxes.append(0)
    print taxes
    taxes_b =  [i*.2 for i in tax if i >10] #using list generator as replacement
    print taxes_b
print calc(itemprice)
