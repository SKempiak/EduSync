import openai

class AIChatbot:

    def __init__(self, people):
        # Get list of people
        self.people = people

    def generate_response(self, question):
        messages1 = [{"role": "system", "content": "You are an artificial intelligence that will be given data of how a student is doing in school. You will be given grades on different assignments and their descriptions or what they decided to write for the assignment. Your goal is to provide insights on the student and to provide areas of improvement for the student. Make sure to be specific and output what the student needs to work on. The insights given should be interpreted from the data and the improvements needed should be activites or assignments that the teacher can do to help the student."}]
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