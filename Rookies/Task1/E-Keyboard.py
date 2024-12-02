direction = input().strip()
sentence = input().strip()
original =[]
keyboard = 'qwertyuiopasdfghjkl;zxcvbnm,./'
for char in sentence:
    index = keyboard.find(char)  
    
    if direction == 'R':
        original.append(keyboard[index - 1])
    elif direction == 'L':
        original.append(keyboard[index + 1])

print(''.join(original))
