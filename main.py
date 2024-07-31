import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))
print(os.getenv("PINECONE_API_KEY"))
print(os.getenv("PINECONE_API_ENV"))