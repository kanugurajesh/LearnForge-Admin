import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

readData = ""

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

# get the parent directory of the current directory
directory = os.path.dirname(os.getcwd()) + "/public/courses"

# change the directory to the directory of the courses
os.chdir(directory)

# get all the *.d.ts files in the directory
for filename in os.listdir("./"):
    if filename.endswith(".json"):
        with open(filename, 'r') as file:
            readData = file.read()
            file.close()
            prompt = prompt = f"update the questions with new questions in the beside data and give me the output in json format => {readData}"
            response = model.generate_content(prompt)
            data = response.text
            # remove the first line of the data
            data = data.split("\n", 1)[1]
            # remove the last line of the data
            data = data.rsplit("\n", 1)[0]
            with open(filename, 'w') as file:
                file.write(data)
                file.close()
            continue
    else:
        continue