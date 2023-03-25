# write a python program  to   append elements fromanother list to the current list.( firstlist=['java','Python','SQL'],secondlist=['c','Cpp','NoSQL'])
firstlist=['java','Python','SQL']
secondlist=['c','Cpp','NoSQL']

for i  in secondlist:
    firstlist.append(i)
print(firstlist)