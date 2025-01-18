def number(a,b,c):
    multiply = a*b*c
    print(multiply)
    addition = a+b+c
    print(addition)
    classify = [a,b,c]
    classify.sort(reverse=True)
    return classify[2],classify[1],classify[0]
print(number(1,2,3))