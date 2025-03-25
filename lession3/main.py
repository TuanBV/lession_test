"""
    There are 20 classes in the school. 5 class have 35 students, 6 classes have 45 students,
    10 classes have 30 students and 4 classes have 40 students.
    The average age of all students is 20 years and 8 months.
    Write a program count the total student of each class
    who the age larger or smaller than the average age 6 month.
"""
import random

# Topic
classes = {
    5: 35, # 5 class have 35 students
    6: 45, # 6 classes have 45 students
    10: 30, # 10 classes have 30 students
    4: 40 # 4 classes have 40 students
}

# Constant
# Average age months
AVG_AGE_MONTHS = 20 * 12 + 8 # Average age in months (20 years 8 months) : 1 year = 12 months
# Younger average age months
YOUNGER_AVG_AGE = AVG_AGE_MONTHS - 6
# Older average age months
OLDER_AVG_AGE = AVG_AGE_MONTHS + 6
# Young student
YOUNGER_STUDENTS = 0
# Older student
OLDER_STUDENTS  = 0

def generate_student_ages(lst_students):
    """
        Generate student have age 1 year younger than AVG_AGE_MONTHS
        and 1 year old than AVG_AGE_MONTHS
    """
    return [random.randint(AVG_AGE_MONTHS - 12, AVG_AGE_MONTHS + 12) for _ in range(lst_students)]

for item_class, student_count in classes.items():
    student_ages = generate_student_ages(item_class * student_count)
    YOUNGER_STUDENTS += sum(1 for age in student_ages if age < YOUNGER_AVG_AGE)
    OLDER_STUDENTS += sum(1 for age in student_ages if age > OLDER_AVG_AGE)

print(f"Total younger students s: {YOUNGER_AVG_AGE}")
print(f"Total older students : {OLDER_AVG_AGE}")
