from chatterbot import ChatBot
from flask import Flask, request,render_template
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
import logging
time.clock= time.time
logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)


bot = ChatBot('EduGuide')
trainer = ListTrainer(bot)

app = Flask(__name__)


trainer.train(
    [
        "Hello",
        "Hi there!",
        "How are you doing?",
        "I am doing great",
        "Can you guide me regarding the admission process?",
        "Sure!"
        "Yes sure! Here are some important guidlines you need to follow",
        "What are the important documents needed?",
        "Here are the list of important documents you will be needing to complete your admission process?",
        "● Print out of counselling registration form"
        "● MHT CET admit card and Result"
        "● Class 10 and 12 pass certificate and marksheet"
        "● Category certificate (if applicable)"
        "● Character and migration certificate"
        "● School leaving certificate"
        "● Domicile certificate (if applicable) ",
        "What happens if candidates commit error in application form?",
        "In case while filling the application form, if any candidate commits any error in the form or wants to change any entry, then DTE Maharashtra gives a few days"
        "window to update or edit the details entered in application form. However, this"
        "facility is just provided only once, so candidates must be very careful while making changes in the application particulars. What needs to be noted is that not all"
        "the information can be edited or changed with the help of this correction window. ?",
        "What is Freeze:",
        "Candidates who are satisfied with their allotted seats and do not want to participate in further have to select this option. By selecting this option candidates will"
        "confirm their allotted seats and will not be allowed to participate further",
        "What is Slide:?",
        "By selecting this option candidates who wish to accept the seat allotted to them"
        "but will also be open for upgradation into a higher preferred course in the same institute. If in further round, these candidates are allotted in a higher preferred course then"
        "their previous seat will be cancelled",
        "What is Float:?", 
        "This option allows candidates to upgrade their seat to a higher preferred choice"
        "of course at any institute. However, their earlier allotment will be cancelled if their"
        "choice of higher course is allotted to them.",
        "Whats Merit List?",
        "After the declaration of result, the exam conducting authority releases the provisional"
        "merit list in online mode. The merit will be prepared based on the marks secured in the"
        "entrance exam. The provisional merit list carries the name of candidates shortlisted for counselling along with their overall ranks. To check the merit list candidates have to"
        "log-in into their account by entering application number and date of birth. What needs"
        "to be noted is that separate merit list is prepared and released for JEE Main qualified"
        "candidates. MHT CET merit list will be available separately for different groups like all"
        "India and Maharashtra candidates. A few days window will be given to the candidates"
        "to send the complaint against the merit list, if they have any. After the feedback, a final"
        "merit list will be published.", 
    ]
)




while True:
    textInput = input("You : ")
    if(textInput=='quit'):
        break
    print("Bot: ", bot.get_response(textInput))

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))