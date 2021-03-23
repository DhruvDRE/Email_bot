import speech_recognition as sr
import pyttsx3 as pt
from email.message import EmailMessage # for setting ideals of email
import smtplib #simple mail transform  lib
listener=sr.Recognizer()

# to create speaking engine using pyttsx

engine=pt.init()

def talk(text):
	engine.say(text)
	engine.runAndWait()

def get_info():
	try:
		with sr.Microphone() as source:
			print('listening....')
			voice=listener.listen(source)
			info=listener.recognize_google(voice) #voice to text
			print(info)
			return info.lower()
	except:
		pass





def send_email(receiver,subject,message):
	# create a server
	server = smtplib.SMTP('smtp.gmail.com',587) # smtp server name and port number
	server.starttls() # start transport layer security
	server.login('',') #your real email id and password
	# server.sendmail('#your email','#receivers email','#message you want to share') # sender,receiver and message
	email =EmailMessage()
	email['From']='' #your email
	email['To']= receiver
	email['Subject']=subject
	email.set_content(message)
	server.send_message(email)

#to create favourite email list 
email_list={ #add your emails for the hot keywords dude ,dad,mom and friend
        'dude' : '',
        'dad'  : '',
        'mom'  : '',
	      'friend': ''
       }


def get_email_info():
	talk('To Whom you want to send email to')
	name= get_info()
	receiver = email_list[name] # search input name in list 
#	receiver=name+"@gmail.com"
	print(receiver)
	talk("What is the subject of your email")
	subject= get_info()
	talk("tell me the content for the email")
	content= get_info()
	send_email(receiver,subject,content)



get_email_info()
