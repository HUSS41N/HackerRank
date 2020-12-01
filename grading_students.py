# #!/bin/python3
# #this solution will run optimally on hackerrank's compiler.To run it on any pc you may need to change few things 1-Just Delete the lines containing fptr and uncomment the my for looop.Happy practicing
#solution 1 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    final_grades = []
    for i in grades:
        if 38 > i:
            final_grades.append(i)
        else:
            if i % 5 >= 3:
                i += 5 - i % 5
                final_grades.append(i)
            else:
                final_grades.append(i)
    return final_grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# import math
# import os
# import random
# import re
# import sys

# def gradingStudents(grades):
#     final_grades = []
#     for i in grades:
#         if i < 38:
#             final_grades.append(i)
#         else:
#             if (i + 1) % 5 == 0:
#                 final_grades.append(i+1)
#             elif (i+2) % 5 == 0:
#                 final_grades.append(i+2)
#             else:
#                 final_grades.append(i)
#     return final_grades 
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     grades_count = int(input().strip())

#     grades = []

#     for _ in range(grades_count):
#         grades_item = int(input().strip())
#         grades.append(grades_item)

#     result = gradingStudents(grades)
#     # for i in result:
#     #     print(i)
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()