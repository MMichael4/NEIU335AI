#1. Open Google Colab: Go to Google Colab and sign in with your Google account. 
# 2. Create a New Notebook: Name it CS335_PythonLab1_YourName. 

#1. Variables and Data Types: 
name = "Omeed Adham Sindy" 
age = 70 
ai_course = True 
print("Name:", name) 
print("Age in 5 years:", age + 5) 
print("Is enrolled in CS 335 course?", ai_course)

#Task: Modify the variables to reflect your name, age, and enrollment status. Then print a sentence using all three values. 


#2. Lists and Loops 
topics = ["Logic", "Search", "NLP", "ML", "Bayesian Inference"] 
for topic in topics: print("We will study:", topic) 

#Task: 1) Add two additional AI topics to the list. 2) Modify the loop to include numbering (e.g., "1. Logic"). 

#3. Dictionaries and Conditionals 
student = {"name": "Omeed", "score": 85} 
if student["score"] >= 90: grade = "A" 
elif student["score"] >= 80: grade = "B" 
else: grade = "C or below" 
print(f"{student['name']} received a grade of {grade}.") 

#Task: 1) Modify the score to test different outputs. 2) Add a new grade tier for "A+" if the score is 95 or higher. 

#4. Functions 

def greet_student(name): 
    return f"Welcome to CS 335, {name}!" 
print(greet_student("Omeed")) 

#Task: Write a function square_number(num) that takes a number and returns its square. Test it with at least two inputs. 

# Submission: Share the viewable Colab link to D2L. Ensure sharing permissions are set to "Anyone with the link can view”. 
# Please make sure to add this to your GitHub by downloading it as a .py file and uploading it.