
survey_data = [
    {"response_id": 1, "priority": 2, "response": "Great service!"},
    {"response_id": 2, "priority": 1, "response": "Needs improvement."},
    {"response_id": 3, "priority": 3, "response": "Excellent!"},
    {"response_id": 4, "priority": 2, "response": "Good experience."},
    {"response_id": 5, "priority": 4, "response": "Bad services."}
]


def quick_sort(data, low, high):
    if low < high:
        
        pi = partition(data, low, high)

        
        quick_sort(data, low, pi - 1)
        quick_sort(data, pi + 1, high)


def partition(data, low, high):
    pivot = data[high]["priority"]  
    i = low - 1  

    for j in range(low, high):
        if data[j]["priority"] <= pivot:  
            i += 1
            data[i], data[j] = data[j], data[i]  

   
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1  

quick_sort(survey_data, 0, len(survey_data) - 1)

for response in survey_data:
    print(response)
