import pandas as pd


data_file = pd.read_csv("questions.csv")

scale_explanation = """
Please use the following scale to answer:
1 = Strongly Agree
2 = Somewhat Agree
3 = A Little Agree
4 = Neither Agree nor Disagree
5 = A Little Disagree
6 = Somewhat Disagree
7 = Strongly Disagree
"""

print(scale_explanation)

def get_user_answers():
    responses_from_user = {}
    for _, row in data_file.iterrows():
        question_id = row["QuestionNumber"]
        question_text = row["Text"]

        while True:
            try:
                input_response = int(input(f"{question_id}.{question_text} \nYour answer (1-7): "))
                if 1 <= input_response <= 7:
                    responses_from_user[question_id] = input_response
                    break
                else:
                    print("Please enter a number between 1 and 7.")
            except ValueError:
                print("That wasn't a valid number.")
    return responses_from_user

print(get_user_answers())
