total = 0
count = 0
average = 0
while True:
    inp = input('Enter a number:')
    if inp == 'done':
        break
    try:
        inp = float(inp)
    except:
        print('%s is not a number' % inp)
        continue
    total = total + inp
    count = count + 1
    average = total / count
print('Total:  Count: %s Average: %s' % (total, count, average))
input()
