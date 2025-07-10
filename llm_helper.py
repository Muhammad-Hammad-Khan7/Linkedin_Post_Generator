from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
from langchain_groq import ChatGroq

llm = ChatGroq(
    api_key="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", 
    model_name="llama3-8b-8192"
)



if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)





