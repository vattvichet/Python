num = list(range(1,10)) #From 1 -> 9
print(num)
print(num[0])
print(num[1])
print(num[-1]) # last index

a = [10,32,21,60,0,30]
# a.sort() #sort
print(a)
print(a[0])
print(a[1])
print(a[-1]) # last index
print(a[-len(a)]) #len(a) = get list a's length
a.append(200) # Add new element into list (only for one element)
a.append([98,99]) ## Using 
a.extend([400, 300]) # For adding more than one element into List
print(a)
