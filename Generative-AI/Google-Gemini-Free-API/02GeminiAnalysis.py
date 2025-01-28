import google.generativeai as genai
import pandas

genai.configure(api_key="AIzaSyBXoETHANndwN0mDvpYemzIrp-vk")
model = genai.GenerativeModel("gemini-1.5-flash")

df=pandas.read_csv("https://raw.githubusercontent.com/sohamglobal/datasets/refs/heads/main/Flipkart_Mobiles.csv")

prompt=f"""
analyze the data present inside pandas data frame {df} and show me the top 5 most
selling mobile brands. don't show the code, show me the results.
"""
response = model.generate_content(prompt)
print(response.text)