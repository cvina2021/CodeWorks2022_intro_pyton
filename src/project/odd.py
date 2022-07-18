start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
list = []

for x in range (start, end):
    if x % 2 != 0:
        list.append(x)
if end % 2 != 0:
    list.append(end)

print(list);
