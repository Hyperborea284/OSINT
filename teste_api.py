from openai import APIConnectionError, APIError, RateLimitError, OpenAI
from dotenv import load_dotenv
import os

load_dotenv(".env")

class PromptGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    def gpt_activation(self, prompt_text, max_tokens):
        try:
            model_name = "gpt-3.5-turbo-1106"
            #model_name = "gpt-4-0125-preview"
            
            # Generate completion based on prompt
            response = self.client.chat.completions.create(
                messages=prompt_text, 
                model=model_name,
                max_tokens=max_tokens
            )
    
            # Check if response is available
            generated_text = response.model_dump()['choices'][0]['message']['content']
            if generated_text:
                print(generated_text)
            else:
                return "Error: Empty response from OpenAI API."
    
        except (APIConnectionError, APIError, RateLimitError) as e:
            return f"Error connecting to OpenAI API: {e}"
    

text = [{"role": "user", "content": f"""
            explique a diferença entre um vinho merlot e um vinho cabernet.
        """.strip()},
        {"role": "user", "content": f"""
            compare cada um dos vinhos com um queijo correto para acompanhamento.
        """.strip()}]
   
prompt_text = [
    {
        "role": "user",
        "content": f'{text}'
    }
]
    
generator = PromptGenerator()
generator.gpt_activation(prompt_text, max_tokens=4096)
