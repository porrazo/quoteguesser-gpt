from openai import OpenAI
import json


OPENAI_APIKEY = open(".env").readlines()[1].rstrip()

client = OpenAI(api_key=OPENAI_APIKEY)
def authorQuote(number):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={"type": "json_object"},
            messages=[
                {"role":"system","content":"You are a helpful assistant."},
                {"role":"user","content": f"""Please analyze what famous fictional character or real-life person said the quote: {number}. If the quote is not associated with anyone, just answer with 'no one'. Answer in the following JSON format: {{'author':string with the name of the author}}."""}
            ]
        )
        gpt_response = json.loads(response.choices[0].message.content)
        return gpt_response.get('author',"")
    except json.JSONDecodeError:
        print("An error occurred.")
        return False


print("Write the quote you want to know the author of (any language): ")
phrase = str(input())
result = authorQuote(phrase)
print(f"'{phrase}' was said by: {result}.")