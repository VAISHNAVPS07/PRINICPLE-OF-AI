import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'(.*)Hi(.*)', ['How shall I assist you?']),
    (r'(.*)college|about college(.*)', ['Sure! The eco-friendly picturesque campus is situated on the banks of the River Nethravathi and is adjacent to Mangaluru - Bengaluru National Highway NH 75. The Campus is located at a distance of 8 km from the port city of Mangaluru, a popular education hub. It is well connected by road, air and train to all the major cities of India.The campus is artistically built in the courtyard system with spacious class rooms, well - equipped laboratories and a central library.']),
    (r'(.*)admission|seats(.*)', ['For admission inquiries, you can visit our website sahyadri.edu.in or contact the admission office.']),
    (r'(.*)program|branches(.*)', ['Our institution offers:\nAIML\nECE\nCSE\nISE\nMECHANICAL\nWhich program are you interested in?']),
    (r'(.*)AIML(.*)', ['Our institution offers AIML course for 180 students right now.']),
    (r'(.*)ECE|EC(.*)', ['Our institution offers ECE course for 120 students right now.']),
    (r'(.*)CSE(.*)', ['Our institution offers CSE course for 360 students right now.']),
    (r'(.*)MECHANICAL(.*)', ['Our institution offers Mechanical course for 60 students right now.']),
    (r'(.*)ISE(.*)', ['Our institution offers ISE course for 120 students right now.']),
    (r'(.*)deadline|last date(.*)', ['The admission deadline varies depending on the program. Please check our website for specific deadlines.']),
    (r'(.*)financial aid(.*)', ['Information about financial aid options is available on our website or you can contact the financial aid office for assistance.']),
    (r'(.*)contact|mail(.*)', ['You can contact our admission office at admission@sahyadri.edu.in or call +918242277333.']),
    (r'(.*)help(.*)', ['How can I assist you further?']),
    (r'(.*)(.*)', ['I apologise. I am not able to understand what you want.']),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Define a function to interact with the chatbot
def admission_chat():
    print("Welcome to Sahyadri College Admission Chatbot. How can I assist you today?")
    print("Type 'quit' to exit.")

    # Start chatting
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!Thank you for contacting us")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

admission_chat()