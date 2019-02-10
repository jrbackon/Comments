
## A program to generate comments with specific user input 

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] # the APIs being accessed

credentials = ServiceAccountCredentials.from_json_keyfile_name('Comments-500f16dcc973.json', scope) # credentials for the API

gc = gspread.authorize(credentials)

comment_data = gc.open('Comment Data').sheet1 # the google sheet being accessed

# W1 BP Physics B2    W3 BP Physics D2
# W1 BP Calc B3        W3 BP Calc D3
# W1 Grade Templates A-C/D B4-6     W3 Grade Templates D4-5

name = ''
while name != 'q':
    name = input('Name: ')
    if name != 'q':
# Populates boiler plate.
        section = input('Calc or physics? ')
        if section == 'calc':
            comment = '\n\n' + name.title() + '\n' + (comment_data.acell('D3').value)
        elif section == 'physics':
            comment = '\n\n' + name.title() + '\n' + (comment_data.acell('D2').value) 

# Populates comment body based on grade and asks for personal touches.    
        grade = input('Grade: ')
        if grade == 'a':
            comment = comment + (comment_data.acell('D4').value)
            p_anecdote = input('The main reason %s has been successful is: ' % name.title())
        elif grade == 'b':
            comment = comment + (comment_data.acell('D5').value)
            p_anecdote = input('One way that %s has shown improvement over the course of the year is: ' % name.title())
            improvement = input('%s will benefit from: ' % name.title())
        elif grade == 'c' or 'd':
            comment = comment + (comment_data.acell('D5').value)
            p_anecdote = input('One way that %s has shown improvement over the course of the year is: ' % name.title())
            improvement = input('%s will benefit from: ' % name.title())

# Asks for gender and changes pronouns accordingly.
        gender = input('Gender: ')
        if gender == 'm':
            comment1 = comment.replace("He/She", 'He')
            comment2 = comment1.replace("his/her", 'his')
            comment3 = comment2.replace("he/she", 'he')
        
        elif gender == 'f':
            comment1 = comment.replace("He/She", 'She')
            comment2 = comment1.replace("his/her", 'her')
            comment3 = comment2.replace("he/she", 'she')
    
# Inserts the personal touches depending on the specific grade body.
        if grade == 'a':
            comment4 = comment3.replace("personal anecdote", p_anecdote)
            comment5 = comment4.replace("(student)", name.title())
            print(comment5)
            final = open('w3_comments_2019.txt', 'a')
            final.write(comment5)
        elif grade == 'b':
            comment4 = comment3.replace("personal anecdote", p_anecdote)
            comment5 = comment4.replace("suggestion for improvement", improvement)
            comment6 = comment5.replace("(student)", name.title())
            print(comment6)
            final = open('w3_comments_2019.txt', 'a')
            final.write(comment6)
        elif grade == 'c' or 'd':
            comment4 = comment3.replace("personal anecdote", p_anecdote)
            comment5 = comment4.replace("suggestion for improvement", improvement)
            comment6 = comment5.replace("(student)", name.title())
            print(comment6)
            final = open('w3_comments_2019.txt', 'a')
            final.write(comment6)

final.close()
        