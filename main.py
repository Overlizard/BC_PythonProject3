'''grab input from the user'''
grade1 = float(input('enter the 1st grade:\n'))
grade2 = float(input('enter the 2nd grade:\n'))
grade3 = float(input('enter the 3rd grade:\n'))
grade4 = float(input('enter the 4th grade:\n'))
grade5 = float(input('enter the 5th grade:\n'))

'''take the input and turn it into a list titled grades'''
grades = [grade1, grade2, grade3, grade4, grade5]

'''print out the calculations'''
print(f'Average of the student grades is: {sum(grades)/len(grades)}')
print(f'Minimum grade is: {min(grades)}')
print(f'Maximum grade is: {max(grades)}')
