# import the fuzzywuzzy package to compare user import to the 
# bot responses and return the most similar response to the user question.

from fuzzywuzzy import process


# Creating the dictionary that contains the bot responses
responses = {
    "hello": "Hi there, Welcome to RITA Africa chat assistant! How can I assist you today?",

    "apply": """To apply for a program at RITA Africa, simply visit our
      website https://www.ritaafrica.com/ and join the next Python Developer Bootcamp organized by InfoSorse.""",

    "in africa": """  Given the stated requirement that applicants must be 
    both African citizens and residents in Africa, if you are 
    not currently residing in Africa, you would not meet the 
    eligibility criteria for the application, even if you hold
    African citizenship.
    
    """,
    " certifications": """ RITA Africa offers industry-recognized certifications in various 
    tech-related fields, including data analytics, cloud computing, 
    software engineering, cybersecurity, and more. Our certifications 
    are designed to equip you with the skills and credentials you need 
    to succeed in your chosen career path.
    
    """,
    "duration" : """ Program durations vary depending on the specific course.
         Some programs may be completed in 9 months, while others 
         may span 12 months. Visit our website or check the program 
         page for information on the duration of your chosen program.
""",
"courses" : """ Our courses cover various topics, including programming, 
       data science, and machine learning. Each course is designed 
       to provide practical knowledge and hands-on experience.
       Visit our website https://www.ritaafrica.com/ to explore available courses.

""",
"thank" : "You are always welcome ",
    "bye": "Goodbye! Have a great day!",
}

# Function to save unknow user input in a txt file for future training
def log_unknown_query(query):
    with open("unknown_queries.txt", "a") as file:
        file.write(query + "\n")

# Function to check the best match to the user input from the bot responses. this uses process from fuzzywuzzy
def get_best_match(user_input):
    best_match, score = process.extractOne(user_input, responses.keys())
    return best_match if score > 80 else None

# Defining the bot function
def chatbot():
    print("Welcome to the Customer Support Chatbot!")
    print("Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Bot: Thank you for using our chatbot. Goodbye!")
            break
        
        best_match = get_best_match(user_input)
        if best_match:
            print("Bot:", responses[best_match])
        else:
            print("Bot: Sorry, I don't understand that. Can you try rephrasing?")
            log_unknown_query(user_input)


# Call the chatbot function
chatbot()
