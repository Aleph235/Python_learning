guest_list = ['paul','mike','maria','fran']
removed_guest = guest_list.pop()

guest_list.insert(0, 'Ali')
guest_list.insert(len(guest_list)//2, 'midle')
guest_list.append('trotro')
print(removed_guest)

for i in range(len(guest_list)):
    print(f'{guest_list[i].title()} would you like to come to dinner?', sep = "\n"),
print("I can invite only two persons\n")

guest_list= guest_list[:2]
print(guest_list)
guest_len=len(guest_list)
print(guest_len)
