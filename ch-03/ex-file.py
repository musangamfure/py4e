fname = open('mbox-short.txt')

for line in fname:
    final = line.rstrip()
    print(final)