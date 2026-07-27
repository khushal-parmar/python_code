#Conditional Statements
i = 1
while i <= 5:
 print(i)
 i += 1
for i in range(5):
 print("Iteration", i)

for i in range(5):
 if i == 2:
  continue
 if i == 4:
  break
 print(i) 
else:
 pass
#  