
def collect_responses():
    
    responses = []

   
    print("What is your age?")
    age = input("Enter your age (e.g., 18-24, 25-34, 35-44, etc.): ")
    responses.append({"question": "What is your age?", "response": age})

    print("What is your gender?")
    gender = input("Enter your gender (e.g., Male, Female, Other): ")
    responses.append({"question": "What is your gender?", "response": gender})

    
    print("How would you rate the product?")
    rating = input("Enter your rating (1-5, where 1 is the worst and 5 is the best): ")
    responses.append({"question": "How would you rate the product?", "response": rating})

    return responses


def display_responses(responses):
    print("\nSurvey Responses:")
    for response in responses:
        print(f"{response['question']} - {response['response']}")


user_responses = collect_responses()
display_responses(user_responses)
