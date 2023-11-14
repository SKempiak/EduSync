import openai

class AIChatbot:

    def __init__(self, people):
        # Get list of people
        self.people = people

    def generate_response(self, question):
        messages1 = [{"role": "system", "content": "You are an artificial intelligence that will be given data of how the students are doing in school. Your goal is to provide insights on each of the students and to provide areas of improvement for each student. Make sure to be specific and output what each student needs to work on. Provide a summary on all of the students as a class and what they may be doing well in and what they need to improve as a whole. The insights given should be interpreted from the data and the improvements needed should be things that the teacher can do to help the students."}]
        for person in self.people:
            messages1.append({"role": "assistant", "content": "The below will be about " + person["name"]})
            for key in person:
                if key == "name": continue
                message = "In their " + person[key]["title"] + ", " + person["name"] + " achieved a score of " + str(person[key]["grade"]) + ". The assignment description is: " + person[key]["description"]
                messages1.append({"role": "assistant", "content": message})
        messages1.append({"role": "user", "content": question})
        # User asks the AI questions
        # Make a response using openai api
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages1
        )
        return response
    
# people = [
#     {"name": "John", "First Assignment": {"title": "First Assignment", "description": "blah", "grade": 100}}
# ]