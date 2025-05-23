import argparse
import pandas as pd
import os


SCALE_POINTS = 7

parser = argparse.ArgumentParser(description="Ryff Psychological Wellbeing Scorer")
parser.add_argument('--version', choices=['42', '18'], help='Choose questionnaire version')
args = parser.parse_args()

if args.version == "18":
    data_file = pd.read_csv("questions_18.csv")
else:
    data_file = pd.read_csv("questions_42.csv")

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
                input_response = int(
                    input(f"{question_id}.{question_text} \nYour answer (1-7): "))
                if 1 <= input_response <= 7:
                    responses_from_user[question_id] = input_response
                    break
                else:
                    print("Please enter a number between 1 and 7.")
            except ValueError:
                print("That wasn't a valid number.")
    return responses_from_user


def store_user_answers_to_csv(responses):
    response_df = pd.DataFrame.from_dict(
        responses, orient="index", columns=["UserResponse"])
    response_df.index.name = "QuestionNumber"
    response_df.reset_index(inplace=True)
    response_df.to_csv("user_responses.csv", index=False)
    print(f"✅ Saved user responses to user_responses.csv")


def handle_existing_answers(filepath="user_responses.csv") -> bool:
    if os.path.exists(filepath):
        print(f"⚠️ A saved responses file ({filepath}) already exists.")
        while True:
            user_input = input(
                "Do you want to retake the quiz and overwrite your previous responses? (y/n): ").strip().lower()
            if user_input in ["y", "yes"]:
                return True  # Proceed with quiz
            elif user_input in ["n", "no"]:
                print("✅ Keeping existing responses.")
                return False  # Skip quiz
            else:
                print("Please enter 'y' or 'n'.")
    else:
        return True


def reverse_score(user_csv="user_responses.csv", questions_csv="questions.csv") -> pd.DataFrame:
    user_df = pd.read_csv(user_csv)
    metadata_df = pd.read_csv(questions_csv)

    # Merge on QuestionNumber
    merged_df = pd.merge(metadata_df, user_df, on="QuestionNumber", how="left")

   # Apply reverse scoring
    def score(row):
        if row["ReverseScored"] == "Yes":
            return (SCALE_POINTS + 1) - row["UserResponse"]
        else:
            return row["UserResponse"]

    merged_df["ScoredResponse"] = merged_df.apply(score, axis=1)

    print("✅ Reverse scoring complete.")
    return merged_df


def calculate_subscale_scores(reversed_scores: pd.DataFrame) -> dict:
    subscale_sum = reversed_scores.groupby(
        "Subscale")["ScoredResponse"].sum().to_dict()
    return subscale_sum


def main():

    if not args.version:
        while True:
            version_input = input("Which version would you like to take? (42 or 18): ").strip()
            if version_input in ["42", "18"]:
                args.version = version_input
                break
            else:
                print("Please enter '42' or '18'.")


    if args.version == "18":
        question_file = "questions_18.csv"
    else:
        question_file = "questions_42.csv"
    
    print(f"📝 Using the {args.version}-item version of the Ryff Scale.")
    data_file = pd.read_csv(question_file)
    
    if handle_existing_answers():
        responses = get_user_answers()
        store_user_answers_to_csv(responses)
    else:
        stored_responses = pd.read_csv("user_responses.csv")
        responses = dict(
            zip(stored_responses["QuestionNumber"], stored_responses["UserResponse"]))
        print("✅ Responses loaded. Ready to score.")


    reversed_scores = reverse_score(questions_csv=question_file)    
    reversed_scores.to_csv("scored_responses.csv", index=False)

    subscale_scores = calculate_subscale_scores(reversed_scores)
    print("\n🎯 Final Subscale Scores:")
    for subscale, score in subscale_scores.items():
        print(f"{subscale}: {score}")

    pd.DataFrame(list(subscale_scores.items()), columns=["Subscale", "Score"]).to_csv("subscale_summary.csv", index=False)


if __name__ == "__main__":
    main()
