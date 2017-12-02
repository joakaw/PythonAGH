a = [1,2,12,4]
b = [2,4,2,8]


def dotProduct(a,b):
    product = 0
    for i in range(4):
        product = product + (a[i]*b[i])
    print(product)

dotProduct(a,b)