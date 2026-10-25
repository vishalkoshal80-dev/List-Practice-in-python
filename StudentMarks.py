marks = [78, 85, 90, 95, 88, 76, 92]
print("Student marks management system")
print("1. Show all marks")
print("2. Calculate total marks")
print("3. Calculate average marks")
print("4. find  highest mark")
print("5. find lowset marks")
print("6. sort marks")
print("7. rverse marks")

print(marks)
for i in marks:
    print(i)
totalmarks = 0
for i in marks:
    totalmarks += i
print("Total marks:", totalmarks)

for i in marks:
    average = float(totalmarks/len(marks))
print("Average marks:", average)

max = 0
for i in marks:
    if(i>max):
        max = i
print("Highest marks:", max)

min = marks[0]

for i in marks:
    if(i<min):
        min = i
print("Lowest marks:", min)

marks.sort()
print("Sorted marks:", marks)

for i  in  range(len(marks)-1,-1,-1):
   print(marks[i])
    