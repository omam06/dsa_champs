import os
from google import genai
from google.genai import errors

def get_ai_suggestions(ticket_description):
    #Retrieve the API key from environment variables
    api_key = os.environ.get("GEMINI_API_KEY")   
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable is not set"
    
    #Initialize the API that will talk to google
    client = genai.Client(api_key=api_key)

    #Create the prompt using the ticket description

    prompt = f"You are an IT helpdesk assistant. A user reported this issue: '{ticket_description}'. Suggest 3 to 4 specific ways to fix or investigate this problem."
    try:
        #Send the prompt to the AI model
        response = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)

        return response.text        #Returning the response
    
    except errors.APIError as e:        #To handle API errors gracefully
        return f"Error: The AI service failed to respond. Details: {e}"
    
    except Exception as e:
        return f"Error: An unexpected error occurred. {e}"      #Handle other unexpected errors (like network issues)
