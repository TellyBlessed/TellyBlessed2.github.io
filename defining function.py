Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> [DEBUG ON]
>>> #Defining function
def average(total_marks, total_subjects):
...   index = total_marks / total_subjects
...   return index #sends the return value back
... #Calling function and using return value
... student_1 = average(840, 12) #stores return value
... print("pass:", student_1 > 50)
... 
... #Another call
... student_2 = average(480, 12)
... print("pass:", student_2 > 50)
... 
... 
... 
