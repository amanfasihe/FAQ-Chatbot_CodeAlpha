def show_menu():
    print("\n===== FAQ Chatbot =====")
    print("You can ask questions about:")
    print("- Courses")
    print("- Duration")
    print("- Certificate")
    print("- Fees")
    print("- Contact")
    print("Type 'exit' to quit\n")


faq = {
    "courses": "We offer courses in AI, Machine Learning, Data Science, and Web Development.",
    "duration": "Most courses have a duration of 6 to 12 weeks.",
    "certificate": "Yes, a certificate is awarded upon successful completion.",
    "fees": "Course fees vary depending on the program.",
    "contact": "You can contact us via email: support@example.com"
}


def get_response(user_input):
    user_input = user_input.lower()

    for keyword in faq:
        if keyword in user_input:
            return faq[keyword]

    return None


def chatbot():
    show_menu()

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "exit":
            print("Bot: Thank you for using the FAQ Chatbot. Goodbye!")
            break

        response = get_response(user_input)

        if response:
            print("Bot:", response)
        else:
            print("Bot: Sorry, I couldn't understand your question.")
            print("Bot: Try asking about courses, duration, certificate, fees, or contact.")


chatbot()