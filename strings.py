# s  = 'Hello World'
# print(s[:])
# print(s[1:])
# print(s[:5])

text = "X-DSPAM-Confidence:    0.8475"


# for char in text:
#     if char.isdigit():
#         start = text.find(char)
#         end = text.find(' ', start)
#         if end == -1:
#             end = len(text)
#         number = float(text[start:end])
#         print(number)
#         break
    
x= text.find('0.8475')
pos = text[x:]
pos.strip()
pos = float(pos)
print(pos)