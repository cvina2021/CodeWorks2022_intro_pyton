def fibSeq(n):
    if n <= 1:
        return n;
    else:
        return fibSeq(n - 1) + fibSeq(n - 2)


n = int(input("Enter value of n: "))
print(fibSeq(n))
