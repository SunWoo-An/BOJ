def factorial(num)->int:
    if num <= 1:
        return 1
    else:
        return factorial(num-1) * num

testcase = int(input())
for i in range(0,testcase,1):
    a, b = map(int, input().split())
    if b < a:
        print(0)
    result = factorial(b) // (factorial(b-a) * factorial(a))
    print(result)
