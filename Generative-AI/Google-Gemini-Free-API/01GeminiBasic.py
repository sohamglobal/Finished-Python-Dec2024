#pip install google-generativeai

import google.generativeai as genai

genai.configure(api_key="AIzaSyBXoETHANRq6DsndwN0mDvpYemzIrp-vk")
model = genai.GenerativeModel("gemini-1.5-flash")

prompt=input('Enter your query to Gemini : ')
response = model.generate_content(prompt)
print(response.text)