import os

from google import genai
 
 
# 1. Verify that the environment variable was set correctly

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:

    raise ValueError("ERROR: GEMINI_API_KEY environment variable not found. Please set it before running.")
 
print("🔑 API Key successfully detected!")
 

# 2. Initialize the official client

client = genai.Client(api_key=api_key)
 

# 3. Test a basic text generation call using the standard fast model

print("🤖 Sending prompt to Gemini...")

response = client.models.generate_content(

    model='gemini-2.5-flash',

    contents='how to generate free gemini api key',

)
 
# 4. Print the output

print("\n--- Model Response ---")

print(response.text)

print("----------------------")
 