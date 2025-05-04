import nltk
from nltk.chat.util import Chat, reflections

pairs=[
    [
        r"my name is (.)",
        ["Hello %1, How are you"]
    ],
    [
        r"Hi|Hello|Hey there|Hola",
        ["Hello my name is Hiesenberg"]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by Heisenbergwhat. you can call me crazy!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good How about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"I (.*) good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude Seriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Raghav created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Pune, Maharashtra',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"I am looking for online guides and courses to learn data science, can you suggest?",
        ["Crazy_Tech has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"quit",
        ["Thank you for using our intelligence services"]
    ],
    

]

def chat():
    print("Hey there! I am Heisenberg at your service")
    chat = Chat(pairs)
    chat.converse()

if __name__== "__main__":
    chat()


# # ==========================================================================================================================================
# # Restaurant Chatbot using Python
# # Assignment-B5 (Chatbot)
# import datetime

# def restaurant_chatbot():
#     print("Welcome to the K's Restaurant!")
#     print("You can ask me about the menu, cost, contact details or reservations!")
    
#     while True:
#         user_input = input("\nYou: ").lower()
        
#         if "menu" in user_input:
#             print("Chatbot: Our menu includes pasta, pizza, salads, and desserts.")
        
#         elif "cost" in user_input or "price" in user_input or "how much" in user_input:
#             print("Chatbot: The average cost per person is around $20.")
        
#         elif "contact" in user_input or "phone" in user_input:
#             print("Chatbot: You can contact us at +91-1234567890")
        
#         elif "reservation" in user_input or "book" in user_input:
#             print("Chatbot: To make a reservation, please call us at +91-1234567890 or visit our website at https://k-rest.io")
        
#         elif "hours" in user_input:
#             print("Chatbot: We are open from 11 AM to 10 PM, Monday to Sunday.")
        
#         elif "date" in user_input or "time" in user_input:
#             now = datetime.datetime.now()
#             print(f"Chatbot: Today's date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}.")
        
#         elif "how are you" in user_input or "how's it going" in user_input or "sup" in user_input:
#             print("Chatbot: I'm just a bot, but I'm here to help you! How can I assist you today?")
        
#         elif "meow" in user_input:
#             print("Meow meow meow!")

#         elif "exit" in user_input or "quit" in user_input:
#             print("Chatbot: Thank you for chatting with us! Have a great day!")
#             break
        
#         else:
#             print("Chatbot: I'm sorry, I didn't understand that. Can you ask something else?")

# restaurant_chatbot()

