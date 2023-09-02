"""
def testA():
    # Variable locale
    num = 100
    print(num)

testA()
print(num)
"""

# Variable globale
num = 100

def testA():
    print(num)

def testB():
    print(num)

testA()
testB()