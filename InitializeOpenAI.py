#Now we will Initialize an instance of OpenAI LLM and pass in it’s API key

# replace "your_api_key" with your generated key 
OPENAI_API_KEY = "your_api_key"
llm = OpenAI(api_token=OPENAI_API_KEY) 
pandas_ai = PandasAI(llm)
