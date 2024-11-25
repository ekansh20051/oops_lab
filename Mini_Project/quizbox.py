
#------------------------------

import mysql.connector as c
import datetime
import random
from pyecharts import options as opts
from pyecharts.charts import Liquid
from pywebio.input import *
from pywebio.output import *
con=c.connect(host="localhost",
              user="root",
              passwd="krissh2005",
              database='examportal')
cursor=con.cursor()

#------------------------------
put_image('http://tyron.in/wp-content/uploads/2022/12/Screenshot-2022-12-23-at-12.09.41-PM.png')
#------------------------------

def showresult(code):
    b=[]
    put_html("<h1>Your Attempts (newest first)</h1>")
    query="select * from result where student_id='{}' order by date_and_time desc".format(code)
    cursor.execute(query)
    data=cursor.fetchall()
    con.commit()
    topicdata=[]
    scoredata=[]
    statusdata=[]
    datetimedata=[]
    for i in data:
        topicdata.append(i[1])
        scoredata.append(i[2])
        statusdata.append(i[3])
        datetimedata.append(i[4].strftime("%y-%m-%d--%H:%M:%S"))
    b.append(['Topic','Score','Status','Date and Time'])
    for j in range(len(topicdata)):
        a=[topicdata[j],scoredata[j],statusdata[j],datetimedata[j]]
        b.append(a)
    put_table(b)
    selectoption(code)

#------------------------------

def showtestresult(code):
    put_html("<h1>Result</h1>")
    query="select * from result where Student_Id='{}' order by date_and_time desc".format(code)
    cursor.execute(query)
    data=cursor.fetchall()
    con.commit()
    topicdata=[]
    scoredata=[]
    statusdata=[]
    datetimedata=[]
    for i in data:
        topicdata.append(i[1])
        scoredata.append(i[2])
        statusdata.append(i[3])
        datetimedata.append(i[4].strftime("%y-%m-%d--%H:%M:%S"))
    for j in range(1):
        put_table([['Topic','Score','Status','Date and Time'],[topicdata[j],scoredata[j],statusdata[j],datetimedata[j]]])
    c = (
    Liquid()
    .add("Percentage Scored", [scoredata[j]/5])
    .set_global_opts(title_opts=opts.TitleOpts(title="Percentage-->"))
    
    )

    c.width = "100%"
    put_html(c.render_notebook())
    selectoption(code)
    

#------------------------------
    
def test(code):
    subject=select('Choose subject you want to take a test for:',['Math','Computer Science'])
    if subject=='Computer Science':
        count=0
        
        meme1='https://img.buzzfeed.com/buzzfeed-static/static/2017-08/2/8/asset/buzzfeed-prod-fastlane-02/sub-buzz-4222-1501677778-3.png?downsize=900:*&output-format=auto&output-quality=auto'
        meme2='https://img.buzzfeed.com/buzzfeed-static/static/2017-08/2/20/asset/buzzfeed-prod-fastlane-02/sub-buzz-10892-1501720491-5.png?output-quality=auto&output-format=auto&downsize=640:*'
        meme3='https://img.buzzfeed.com/buzzfeed-static/static/2017-08/2/8/asset/buzzfeed-prod-fastlane-01/sub-buzz-26469-1501677660-16.png?downsize=900:*&output-format=auto&output-quality=auto'
        meme4='https://img.buzzfeed.com/buzzfeed-static/static/2017-08/2/21/asset/buzzfeed-prod-fastlane-01/sub-buzz-3595-1501723901-11.png'
        meme5='https://i.pinimg.com/564x/5d/ed/4d/5ded4dfde646414ddb061a436c79564b.jpg'
        meme6='https://static.langimg.com/thumb/msid-67281241,width-680,resizemode-3/exam-memes.jpg'
        meme7='https://i.pinimg.com/236x/99/42/9d/99429d8b00dc522c9fa329173326ea0c--so-funny-funny-shit.jpg'
        meme8='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRy1z3rYMsbY3C2FWQkg_r-8VB-hRon99rroA&usqp=CAU'
        meme9='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSOA1eEndc2a6crrLjmYoF9gf0EjF3cesHdQ&usqp=CAU'
        meme10='https://pics.me.me/exams-be-like-72376517.png'
        memes=[meme1,meme2,meme3,meme4,meme5,meme6,meme7,meme8,meme9,meme10]
        meme=random.choice(memes)


        put_html("<h1>Quiz</h1>")
        put_html('<h3>Here is a meme to get you in the *QUIZ ZONE*</h3>')
        put_image(meme)
        put_text('- Each question carries 1 mark.')
        put_text('- There are a total of 5 Questions that need to be answered.')
        put_text('- All the Best 👍')
        begin=radio('Begin Test',['Start'],required=True)
        q1="Is Python case sensitive when dealing with identifiers?"
        q2="Which of the following is the correct extension of the Python file?"
        q3="Who developed Python Programming Language?"
        q4="Which of the following functions is a built-in function in python?"
        q5="What will be the output of the following Python statement?--->'a'+'bc"
        q6="Which of the following cannot be a variable?"
        q7="Which is the correct operator for power(xy)?"
        q8="Which one of these is floor division?"

        questionsdone=[0,1,2,3,4,5,6,7]
        questions=[q1,q2,q3,q4,q5,q6,q7,q8]
        options=[['No','Yes','Machine dependent','None of the above'],
                 ['.python','.html','.py','.pdf'],
                 ['Niene Stom','Guido van Rossum','Wick van Rossum','Rasmus Lerdorf'],
                 ['sqrt()','seed()','factorial()','print()'],
                 ['acb','bca','abc','bc'],
                 ['on','_init','int','it'],
                 ['x*y','x**y','x***y','x^y'],
                 ['/','//','%','None Of The Above'],
                 ['7','0','1','5']]
        answers=['Yes','.py','Guido van Rossum','print()','abc','int','x**y','//']

        for i in range(5):
            x=random.choice(questionsdone)
            questionsdone.remove(x)
            askquestion=radio(questions[x],options[x])
            if askquestion==answers[x]:
                count+=1
                

        if count>=3:
            status='Pass'
            message=[style(put_html("<h1 style='display:inline;border-bottom:0px'>Congratulations !! </h1>"+ ", your score is <b>"+ str(count) + '/5' + "</b><br><br>") ,'color:green;'),style(put_html("<p>Result : <b>PASSED</b></p>"),'color:green'), put_html("<b>Thank You for your participation.</b>")]
            popup("Result", content=message, size='large', implicit_close=True, closable=True)
        else:
            status='Fail'
            message=[style(put_html("<h1 style='display:inline;border-bottom:0px'>Oops! " + "</h1>" + ", your score is <b>"+ str(count) + '/5' + "</b><br><br>"),'color:red'), style(put_html("<p>Result : <b>FAILED</b></p>"), 'color:red') , put_html("<b>Thank You for your participation.</b><br><br>")]
            popup("Result", content=message, size='large', implicit_close=True, closable=True)
        query="insert into result (Student_ID,topic,score,status) values('{}','{}',{},'{}')".format(code,subject,count,status)
        cursor.execute(query)
        con.commit()
        showtestresult(code)
        
    if subject=='Math':
        count = 0
        
        meme1='https://img.buzzfeed.com/buzzfeed-static/static/2017-08/2/8/asset/buzzfeed-prod-fastlane-02/sub-buzz-4222-1501677778-3.png?downsize=900:*&output-format=auto&output-quality=auto'
        meme2='https://img.buzzfeed.com/buzzfeed-static/static/2017-08/2/20/asset/buzzfeed-prod-fastlane-02/sub-buzz-10892-1501720491-5.png?output-quality=auto&output-format=auto&downsize=640:*'
        meme3='https://img.buzzfeed.com/buzzfeed-static/static/2017-08/2/8/asset/buzzfeed-prod-fastlane-01/sub-buzz-26469-1501677660-16.png?downsize=900:*&output-format=auto&output-quality=auto'
        meme4='https://img.buzzfeed.com/buzzfeed-static/static/2017-08/2/21/asset/buzzfeed-prod-fastlane-01/sub-buzz-3595-1501723901-11.png'
        meme5='https://i.pinimg.com/564x/5d/ed/4d/5ded4dfde646414ddb061a436c79564b.jpg'
        meme6='https://static.langimg.com/thumb/msid-67281241,width-680,resizemode-3/exam-memes.jpg'
        meme7='https://i.pinimg.com/236x/99/42/9d/99429d8b00dc522c9fa329173326ea0c--so-funny-funny-shit.jpg'
        meme8='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRy1z3rYMsbY3C2FWQkg_r-8VB-hRon99rroA&usqp=CAU'
        meme9='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSOA1eEndc2a6crrLjmYoF9gf0EjF3cesHdQ&usqp=CAU'
        meme10='https://pics.me.me/exams-be-like-72376517.png'
        memes=[meme1,meme2,meme3,meme4,meme5,meme6,meme7,meme8,meme9,meme10]
        meme=random.choice(memes)

        
        put_html("<h1>Quiz</h1>")
        put_html('<h3>Here is a meme to get you in the *QUIZ ZONE*</h3>')
        put_image(meme)
        put_text('- Each question carries 1 mark.')
        put_text('- There are a total of 5 Questions that need to be answered.')
        put_text('- All the Best 👍')
        begin=radio('Begin Test',['Start'],required=True)

        q1="If the age of Ram's dad is 4 times his age, and his grandfather's age is 72 which is twice his dad's age. What is Ram's age?"
        q2="0.003 × 0.02 = ?"
        q3="What is the rate of discount if a car which price was $4,000 was sold for $3,200 ?"
        q4="What is the value of x in the equation 3x – 15 – 6 = 0 ?"
        q5="What is the average of first 150 natural numbers?"
        q6="A clock strikes once at 1 o’clock, twice at 2 o’clock, thrice at 3 o’clock and so on. How many times will it strike in 24 hours?"

        questionsdone=[0,1,2,3,4,5]
        questions=[q1,q2,q3,q4,q5,q6]
        options=[['12','9','8','4'],
                 ['0.06','0.0006','0.6','0.00006'],
                 ['10%','15%','20%','40%'],
                 ['7','8','9','-9'],
                 ['70','75.5','65.5','80.5'],
                 ['78','136','156','176']]
        answers=['9','0.00006','20%','7','75.5','156']

        for i in range(5):
            x=random.choice(questionsdone)
            questionsdone.remove(x)
            askquestion=radio(questions[x],options[x])
            if askquestion==answers[x]:
                count+=1

        if count>=3:
            status='Pass'
            message=[style(put_html("<h1 style='display:inline;border-bottom:0px'>Congratulations !! </h1>"+ ", your score is <b>"+ str(count) + '/5' + "</b><br><br>") ,'color:green;'),style(put_html("<p>Result : <b>PASSED</b></p>"),'color:green'), put_html("<b>Thank You for your participation.</b>")]
            popup("Result", content=message, size='large', implicit_close=True, closable=True)
        else:
            status='Fail'
            message=[style(put_html("<h1 style='display:inline;border-bottom:0px'>Oops! " + "</h1>" + ", your score is <b>"+ str(count) + '/5' + "</b><br><br>"),'color:red'), style(put_html("<p>Result : <b>FAILED</b></p>"), 'color:red') , put_html("<b>Thank You for your participation.</b><br><br>")]
            popup("Result", content=message, size='large', implicit_close=True, closable=True)
        query="insert into result (Student_ID,topic,score,status) values('{}','{}',{},'{}')".format(code,subject,count,status)
        cursor.execute(query)
        con.commit()
        showtestresult(code)

#------------------------------

def selectoption(code):
    option=select('What would you like to do?',['Attempt Quiz','View All Results','Exit'],required=True)
    if option=='Attempt Quiz':
        test(code)
    if option=='View All Results':
        showresult(code)
    if option=='Exit':
        put_html("<h1>See you soon 😃</h1>")

#------------------------------
        
def signup():
    if logsign=='Sign Up':
        s=0
        name=input('Enter Full Name',required=True,placeholder='Your Name')
        age=input('Enter Age',type=NUMBER,required=True,placeholder='Your Age')
        gender=radio('What is your gender?',['Male','Female','Other'],required=True)
        password=input('Enter Password',type=PASSWORD,placeholder='Password',required=True)
        while s==0:
            code=random.randrange(10000,20000)
            code=name[0].upper()+str(code)
            cursor.execute("select student_id from student where Student_ID='{}'".format(code))
            info=cursor.fetchone()
            if info==None:
                query="Insert into student values('{}','{}',{},'{}','{}')".format(code,name,age,gender,password)
                cursor.execute(query)
                con.commit()
                put_success('Sign Up complete!')
                cursor.execute("select name from student where Student_ID='{}' and Password='{}'".format(code,password))
                data=cursor.fetchone()
                for i in data:
                    put_markdown('# **Welcome to QuizBox** '+i.upper()+' **!**')
                    put_text('Your Student ID:',code)
                    put_text('(Your Student ID is an important credential to log into your account. We suggest you to keep this information safe for future use.)')
                    selectoption(code)
                    s=1
                    break
            else:
                s=0

#------------------------------

def login():
    if logsign=='Sign Up':
        class GetOutLoopNow(BaseException):
            pass
        while True:
            code=input('Enter Student ID',required=True,placeholder='Student ID')
            password=input('Enter Password',type=PASSWORD,required=True,placeholder='Password')
            try:
                cursor.execute("select name from student where student_id='{}' and password='{}'".format(code,password))
                data=cursor.fetchone()
                for i in data:
                    put_success('Log in complete!')
                    put_markdown('# **Welcome to QuizBox** '+i.upper()+' **!**')
                    selectoption(code)
                break
            except Exception:
                put_error('Incorrect Student ID or Password')
                while True:
                    choice=radio('Do you want to try again or sign up?',['Try Again','Sign Up'])
                    if choice=='Try Again':
                        break
                    elif choice=='Sign Up':
                        signup()
                        raise GetOutLoopNow

#------------------------------

while True:
    logsign=radio('Do you want to sign up or log into the QuizBox?',['Log in','Sign Up'])
    if logsign=='Sign Up':
        signup()
        break
    elif logsign=='Log in':
        logsign='Sign Up'
        login()
        break

