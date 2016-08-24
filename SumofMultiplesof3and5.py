# result = 0
# for number in range(1, 1000):
#     if number % 3 == 0 or number % 5 == 0:
#         result = result + number
#
# print result


student_list=[1,2,3,4,5]
for index in range(len(student_list)) :
    student_list[index]+=2
print (student_list)


for student in student_list :
    print (student+2)

var=[student+2 for student in student_list]
print (var)
