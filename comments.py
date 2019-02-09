
## A program to generate comments with specific user input 

## TODO Figure out how to load these directly from google docs. 

physics_bp = """\n\nWe began the year in physics studying the foundational concepts of displacement, velocity, and acceleration for particle-like objects undergoing one-dimensional motion with a constant force. Once we could describe motion we learned how motion occurs with Newton’s laws and are now beginning our study of momentum. Throughout the course, we have focused on representing the physics learned in multiple ways: verbally, graphically, and mathematically.\n"""

calc_bp = """\n\nAdvanced BC Calculus is designed to mirror the first two semesters of college level calculus and as such prepares students for the AP BC Calculus exam in May. As of right now, we have concluded our formal study of derivatives and are embarking on our study of integrals.\n"""

a_student = """\n'student' has done very well so far this year. 'He/She' has combined a solid work ethic with engaged enthusiasm in the classroom. My favorite thing about 'student' is 'personal anecdote'. 'He/She' has shown resilience in tackling difficult concepts and should be proud of 'his/her' accomplishments. I am confident that if 'student' continues to stay dedicated to 'his/her' studies 'he/she' will be very successful this year. I look forward to working with 'student' for the rest of the year.\n\n"""

b_student = """\n'student' has put in solid effort so far this year. My favorite thing about 'student' is 'personal anecdote'. I appreciate the work 'student' has done so far and think 'he/she' will benefit from 'suggestion for improvement'. I am confident that if 'student' can stay motivated and be a little more consistent moving forward that 'he/she' will see improvement. I look forward to working with 'student' for the rest of the year.\n\n"""

cd_student = """\n'student' has had a difficult start to the year. My favorite thing about 'student' is 'personal anecdote'. In order to improve 'student' will need to be more consistent in 'his/her' preparation and more precise when communicating 'his/her' understanding. It can be easy in class for 'student' to convince 'himself/herself' that 'he/she' understands a concept by watching others and following along. The crucial step is to make sure that 'student' can reproduce this understanding outside of class on 'his/her' own. Some steps that 'he/she' can take to help with this are: rewriting notes after class, doing the classwork alone first and then checking answers with peers, or going over classwork again after solutions are presented without looking at the solutions. As much as possible 'student' should simulate the quiz or test taking situation to ensure true understanding. It is still early in the year and I am confident that with more consistent effort and attention that 'student' can turn things around and achieve the success 'he/she' desires.\n\n"""

name = ''
while name != 'q':
    name = input('Name: ')
    if name != 'q':
# Populates boiler plate.
        section = input('Calc or physics? ')
        if section == 'calc':
            comment = name.title() + calc_bp
        elif section == 'physics':
            comment = name.title() + physics_bp 

# Populates comment body based on grade and asks for personal touches.    
        grade = input('Grade: ')
        if grade == 'a':
            comment = comment + a_student
            p_anecdote = input('My favorite thing about %s is: ' % name.title())
        elif grade == 'b':
            comment = comment + b_student
            p_anecdote = input('My favorite thing about %s is: ' % name.title())
            improvement = input('%s will benefit from: ' % name.title())
        elif grade == 'c' or 'd':
            comment = comment + cd_student
            p_anecdote = input('My favorite thing about %s is: ' % name.title())

# Asks for gender and changes pronouns accordingly.
        gender = input('Gender: ')
        if gender == 'm':
            comment1 = comment.replace("'He/She'", 'He')
            comment2 = comment1.replace("'his/her'", 'his')
            comment3 = comment2.replace("'he/she'", 'he')
            comment4 = comment3.replace("'himself/herself'", 'himself')
        elif gender == 'f':
            comment1 = comment.replace("'He/She'", 'She')
            comment2 = comment1.replace("'his/her'", 'her')
            comment3 = comment2.replace("'he/she'", 'she')
            comment4 = comment3.replace("'himself/herself'", 'herself')
    
# Inserts the personal touches depending on the specific grade body.
        if grade == 'a':
            comment5 = comment4.replace("'personal anecdote'", p_anecdote)
            comment6 = comment5.replace("'student'", name.title())
            print(comment6)
            final = open('w1_comments_2018.txt', 'a')
            final.write(comment6)
        elif grade == 'b':
            comment5 = comment4.replace("'personal anecdote'", p_anecdote)
            comment6 = comment5.replace("'suggestion for improvement'", improvement)
            comment7 = comment6.replace("'student'", name.title())
            print(comment7)
            final = open('w1_comments_2018.txt', 'a')
            final.write(comment7)
        elif grade == 'c' or 'd':
            comment5 = comment4.replace("'personal anecdote'", p_anecdote)
            comment6 = comment5.replace("'student'", name.title())
            print(comment6)
            final = open('w1_comments_2018.txt', 'a')
            final.write(comment6)

final.close()
        