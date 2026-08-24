# Rule-Based Chatbot

def chatbot():
    print("===================================")
    print("       🤖 Rule-Based Chatbot")
    print("===================================")
    print("Type 'bye' or 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower().strip()

        # Greeting
        if user_input in ["hello", "hi", "hey", "hii", "good morning", "good evening"]:
            print("Bot: Hello! 👋 How can I help you?")

        # Asking chatbot name
        elif "your name" in user_input or "who are you" in user_input:
            print("Bot: I am a simple rule-based AI chatbot.")

        # Asking how chatbot is doing
        elif "how are you" in user_input:
            print("Bot: I'm doing great! Thanks for asking. 😊")

        # Asking for help
        elif "help" in user_input:
            print("Bot: I can answer questions about AI, ML, Deep Learning, "
                  "Python, projects, internships, and careers.")

        # Asking about AI
        elif "ai" in user_input or "artificial intelligence" in user_input:
            print("Bot: Artificial Intelligence is the ability of machines "
                  "to perform tasks that normally require human intelligence.")

        # Asking about Machine Learning
        elif ("ml" in user_input or
              "what is machine learning" in user_input or
              "machine learning" in user_input):
            print("Bot: Machine Learning is a subset of AI that enables "
                  "machines to learn patterns from data and make predictions "
                  "or decisions.")

        # Types of Machine Learning
        elif ("types of machine learning" in user_input or
              "types of ml" in user_input):
            print("Bot: The main types of Machine Learning are "
                  "Supervised Learning, Unsupervised Learning, "
                  "and Reinforcement Learning.")

        # Machine Learning algorithms
        elif ("ml algorithms" in user_input or
              "machine learning algorithms" in user_input or
              "algorithms" in user_input):
            print("Bot: Some common ML algorithms are Linear Regression, "
                  "Logistic Regression, Decision Tree, Random Forest, "
                  "KNN, SVM, Naive Bayes, and K-Means.")

        # Asking about Deep Learning
        elif ("what is deep learning" in user_input or
              "deep learning" in user_input):
            print("Bot: Deep Learning is a branch of Machine Learning "
                  "that uses neural networks with multiple layers "
                  "to learn complex patterns from data.")

        # Asking about NLP
        elif "what is nlp" in user_input or "natural language processing" in user_input:
            print("Bot: NLP is a field of AI that enables computers "
                  "to understand, process, and generate human language.")

        # Asking about Computer Vision
        elif ("computer vision" in user_input or
              "what is computer vision" in user_input):
            print("Bot: Computer Vision is a field of AI that enables "
                  "computers to understand and analyze images and videos.")

        # Asking about Python
        elif "python" in user_input:
            print("Bot: Python is a popular programming language widely "
                  "used in AI, Machine Learning, Data Science, and Web Development.")

        # Python libraries
        elif ("python libraries" in user_input or
              "libraries for machine learning" in user_input):
            print("Bot: Popular Python libraries for AI/ML include "
                  "NumPy, Pandas, Matplotlib, Scikit-learn, TensorFlow, "
                  "and PyTorch.")

        # Data Science
        elif ("data science" in user_input or
              "what is data science" in user_input):
            print("Bot: Data Science combines programming, statistics, "
                  "mathematics, and Machine Learning to extract useful "
                  "information from data.")

        # Asking about projects
        elif "project" in user_input or "projects" in user_input:
            print("Bot: Some AI/ML project ideas are SMS Spam Detection, "
                  "Sentiment Analysis, Student Performance Prediction, "
                  "Fake News Detection, Image Classification, and Chatbots.")

        # Asking about final year project
        elif ("final year project" in user_input or
              "major project" in user_input):
            print("Bot: For a final-year AI/ML project, choose a real-world "
                  "problem, collect a suitable dataset, train an ML/DL model, "
                  "evaluate it, and develop a working application.")

        # Asking about internship
        elif "internship" in user_input or "internships" in user_input:
            print("Bot: To prepare for an AI/ML internship, learn Python, "
                  "Machine Learning, Data Science, GitHub, and build "
                  "at least 2-3 practical projects.")

        # Asking about resume
        elif "resume" in user_input or "cv" in user_input:
            print("Bot: An AI/ML fresher resume should include Education, "
                  "Technical Skills, Projects, Certifications, Internships, "
                  "and relevant achievements.")

        # Asking about GitHub
        elif "github" in user_input:
            print("Bot: GitHub is useful for showcasing your coding projects. "
                  "Upload your source code, README file, requirements, "
                  "and project screenshots.")

        # Asking about career
        elif "career" in user_input or "job" in user_input or "jobs" in user_input:
            print("Bot: AI/ML students can explore careers such as "
                  "AI Engineer, Machine Learning Engineer, Data Scientist, "
                  "Data Analyst, NLP Engineer, and Computer Vision Engineer.")

        # Asking about skills
        elif "skills" in user_input or "skills should i learn" in user_input:
            print("Bot: Important AI/ML skills include Python, SQL, "
                  "Statistics, Machine Learning, Deep Learning, "
                  "Data Analysis, and Git/GitHub.")

        # Asking about SQL
        elif "sql" in user_input:
            print("Bot: SQL is used to store, retrieve, and manage data "
                  "in databases. Important topics include SELECT, WHERE, "
                  "JOIN, GROUP BY, and aggregate functions.")

        # Asking about study
        elif ("how should i study" in user_input or
              "how to learn ai" in user_input or
              "study ai" in user_input):
            print("Bot: Start with Python, then learn NumPy and Pandas, "
                  "followed by Statistics, Machine Learning, Deep Learning, "
                  "and finally build practical projects.")

        # Asking about motivation
        elif "motivate me" in user_input or "motivation" in user_input:
            print("Bot: Keep learning and practicing! 💪 "
                  "Every small project you build improves your skills. 🚀")

        # Thank you
        elif "thank" in user_input or "thanks" in user_input:
            print("Bot: You're welcome! 😊")

        # Exit conditions
        elif user_input in ["bye", "exit", "quit", "goodbye"]:
            print("Bot: Goodbye! Have a great day! 👋")
            break

        # Unknown input
        else:
            print("Bot: Sorry, I don't understand that. "
                  "Please try another question.")


# Start chatbot
chatbot()