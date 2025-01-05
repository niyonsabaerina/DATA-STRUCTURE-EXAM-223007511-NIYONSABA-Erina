class SurveyTreeNode:
    def __init__(self, data):
        self.data = data  
        self.children = []  

    def add_child(self, child_node):
        self.children.append(child_node) 

    def display(self, level=0):
        indent = "  " * level
        print(f"{indent}{self.data}")  
        for child in self.children:
            child.display(level + 1)  


survey_tree = SurveyTreeNode("Online Survey for Market Research")


demographic_section = SurveyTreeNode("Demographic Information")
feedback_section = SurveyTreeNode("Product Feedback")

survey_tree.add_child(demographic_section)
survey_tree.add_child(feedback_section)

age_question = SurveyTreeNode("What is your age?")
gender_question = SurveyTreeNode("What is your gender?")
demographic_section.add_child(age_question)
demographic_section.add_child(gender_question)

product_quality_question = SurveyTreeNode("How would you rate the quality of the product?")
suggestion_question = SurveyTreeNode("Do you have any suggestions for improvement?")
feedback_section.add_child(product_quality_question)
feedback_section.add_child(suggestion_question)

age_answer_1 = SurveyTreeNode("18-24")
age_answer_2 = SurveyTreeNode("25-34")
age_answer_3 = SurveyTreeNode("35-44")
age_answer_4 = SurveyTreeNode("45-60")
age_answer_5 = SurveyTreeNode("65-74")
age_question.add_child(age_answer_1)
age_question.add_child(age_answer_2)
age_question.add_child(age_answer_3)
age_question.add_child(age_answer_4)
age_question.add_child(age_answer_5)

# Display the survey tree structure
survey_tree.display()