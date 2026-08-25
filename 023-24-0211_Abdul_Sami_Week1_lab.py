# Section A — Python (Q1–Q8)
# TASK 01: •Write a program that swaps the values of two variables without using a third variable.
a = 5
b = 10
print("Before swapping: a =", a, ", b =", b)
a, b = b, a
print("After swapping: a =", a, ", b =", b)

#TASK 02: •Write a function is_prime(n) that returns True if n is a prime number, otherwise False.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(11))  # Example usage
#TASK 03: •Write a program to print the Fibonacci sequence up to n terms using a loop.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
print(fibonacci(10))  # Example usage
#TASK 04: •Write a function that takes a list of numbers and returns a new list with duplicates removed, preserving order.
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Example usage
#TASK 05: •Write a function multiply(*args) that returns the product of any number of arguments using *args.
def multiply(*args):
    product = 1
    for num in args:
        product *= num
    return product
print(multiply(2, 3, 4))  # Example usage
#TASK 06: •Write a dictionary comprehension mapping each character in a string to its frequency.
def char_frequency(s):
    return {char: s.count(char) for char in set(s)}
print(char_frequency("hello"))  # Example usage
#TASK 07: •Given a list of dictionaries representing employees (name, department, salary), find the employee with the
# highest salary.
def find_highest_paid_employee(employees):
    return max(employees, key=lambda x: x['salary'])
employees = [
    {'name': 'Alice', 'department': 'HR', 'salary': 70000},
    {'name': 'Bob', 'department': 'IT', 'salary': 90000},
    {'name': 'Charlie', 'department': 'Finance', 'salary': 80000}
]
print(find_highest_paid_employee(employees))  # Example usage

#TASK 08: •Write a lambda function combined with filter() to extract all odd numbers from a list.
odd_numbers = list(filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(odd_numbers)  # Example usage

# Section B — NumPy (Q9–Q17)
#TASK 09: •Create a 1D NumPy array of integers from 1 to 30 and reshape it into a 5x6 matrix.
import numpy as np
arr = np.arange(1, 31).reshape(5, 6)
print(arr)

#TASK 10: •Create a 6x6 identity matrix and replace its diagonal with the values [1,2,3,4,5,6].
identity_matrix = np.eye(6)
np.fill_diagonal(identity_matrix, [1, 2, 3, 4, 5, 6])
print(identity_matrix)

#TASK 11: •Given a NumPy array of 25 random integers between 1 and 100, find the sum, mean, and standard deviation.
random_array = np.random.randint(1, 101, size=25)
print("Sum:", np.sum(random_array))
print("Mean:", np.mean(random_array))
print("Standard Deviation:", np.std(random_array))

#TASK 12: •Given a 2D array of shape (4,4), extract the diagonal elements using np.diag() and compute their sum.
array_2d = np.random.randint(1, 100, size=(4, 4))
diagonal_elements = np.diag(array_2d)
print("Diagonal Elements:", diagonal_elements)
print("Sum of Diagonal Elements:", np.sum(diagonal_elements))

#TASK 13: •Create two arrays of shape (3,3) and demonstrate the difference between element-wise multiplication (*) and
# matrix multiplication (@).
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
elementwise_product = arr1 * arr2
matrix_product = arr1 @ arr2
print("Element-wise Product:\n", elementwise_product)
print("Matrix Product:\n", matrix_product)  

#TASK 14: •Given an array of daily temperatures for a month, use boolean masking to find and count days above 35°C.
array_of_temperatures = np.random.randint(20, 45, size=30)  # Random temperatures between 20°C and 45°C
days_above_35 = array_of_temperatures[array_of_temperatures > 35]
print("Days above 35°C:", days_above_35)
print("Count of Days above 35°C:", len(days_above_35))

#TASK 15: •Write NumPy code to normalize an array to the range 0–1 using (x - min) / (max - min).
normalized_array = (array_of_temperatures - np.min(array_of_temperatures)) / (np.max(array_of_temperatures) - np.min(array_of_temperatures))
print("Normalized Array:", normalized_array)

#TASK 16: •Given a 2D array of shape (5,3) (5 students, 3 subjects), compute total and average marks per student using
# axis-based aggregation.
array_2d_marks = np.random.randint(0, 101, size=(5, 3))  # Random marks between 0 and 100
total_marks_per_student = np.sum(array_2d_marks, axis=1)
average_marks_per_student = np.mean(array_2d_marks, axis=1)
print("Total Marks per Student:", total_marks_per_student)
print("Average Marks per Student:", average_marks_per_student)

#TASK 17: •Use np.where() to replace all even numbers in an array with -1, keeping odd numbers unchanged.
array_with_replaced_evens = np.where(array_of_temperatures % 2 == 0, -1, array_of_temperatures)
print("Array with Evens Replaced:", array_with_replaced_evens)

# Section C — Pandas (Q18–Q22)
#TASK 18: •Create a DataFrame of 8 students with columns name, section, and marks; print df.describe().
import pandas as pd
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah'],
    'section': ['A', 'B', 'A', 'B', 'C', 'C', 'D', 'D'],
    'marks': [85, 92, 78, 65, 88, 90, 45, 55]
}
df = pd.DataFrame(data)
print(df.describe())

#TASK 19: •Load a provided CSV, report how many missing values exist per column, and fill numeric missing values
# with the column mean.
dataframe = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv') 
missing_values = dataframe.isnull().sum()
print("Missing values per column:\n", missing_values)
numeric_columns = dataframe.select_dtypes(include=[np.number]).columns
for column in numeric_columns:
    dataframe[column].fillna(dataframe[column].mean(), inplace=True)
print("DataFrame after filling missing numeric values:\n", dataframe)


#TASK 20: •Using .loc and boolean filtering, select all rows where marks are below 50 and print only the name and marks
# columns.
low_performers = df.loc[df['marks'] < 50, ['name', 'marks']]
print("Low Performers:\n", low_performers)

#TASK 21: •Group the students DataFrame by 'section' and compute the mean and max marks per section.
section_stats = df.groupby('section').agg({'marks': ['mean', 'max']})
print("Section Statistics:\n", section_stats)

#TASK 22: •Given two DataFrames — students and their attendance — merge them on student ID and report students
# with attendance below 75%.
students_df = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'marks': [85, 92, 78, 65, 88]
})
attendance_df = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5],
    'attendance': [80, 70, 90, 60, 85]
})
merged_df = pd.merge(students_df, attendance_df, on='student_id')
low_attendance_students = merged_df[merged_df['attendance'] < 75]
print("Students with Attendance below 75%:\n", low_attendance_students)

# Section D — Matplotlib (Q23–Q25)
#TASK 23: •Plot a bar chart of average marks per section (from Q21's groupby result) with labeled axes and a title.
df_section_stats = section_stats.reset_index()
import matplotlib.pyplot as plt
plt.bar(df_section_stats['section'], df_section_stats['marks']['mean'])
plt.xlabel('Section')
plt.ylabel('Average Marks')
plt.title('Average Marks per Section')
plt.show()

#TASK 24: •Plot a histogram of the marks column from your DataFrame and describe the shape of the distribution in one
# sentence.
plt.hist(df['marks'], bins=10, edgecolor='black')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('Distribution of Marks')
plt.show()

#TASK 25: •Create a 1x2 subplot showing a line plot of any numeric trend on the left and a scatter plot of two numeric
# columns on the right.
plt.figure(figsize=(12, 5))
# Line plot on the left
plt.subplot(1, 2, 1)
plt.plot(df['marks'], marker='o')
plt.title('Line Plot of Marks')
plt.xlabel('Student Index')
plt.ylabel('Marks')
# Scatter plot on the right
plt.subplot(1, 2, 2)
plt.scatter(df['marks'], df['marks'] + np.random.randint(-10, 10, size=df.shape[0]))  # Randomly generated second numeric column
plt.title('Scatter Plot of Marks vs Random Variation')
plt.xlabel('Marks')
plt.ylabel('Random Variation')
plt.tight_layout()
plt.show()  
