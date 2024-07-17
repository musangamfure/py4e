fname = input('Enter file name: ')
fhand = open(fname)
count = 0
sum = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        x = line.find(':')
        ft = float(line[x+1:].strip())
        sum += ft
        count += 1

if count > 0:
    average = sum / count
    print("Average spam confidence:", average)
else:
    print("No X-DSPAM-Confidence lines found")

fhand.close()

    
    
    
    