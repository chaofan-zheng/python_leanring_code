a = [1,2,3]
# a = 1
b=2
try:
    print(a + b)
except Exception as e:
    print(e)
else:
    print(a)
print(b)