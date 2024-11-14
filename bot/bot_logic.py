from bot.chromadb_handler import query_knowledge_base
from langchain.llms import OpenAI
from langchain_groq import ChatGroq
import os

# Initialize LangChain with OpenAI model (API key is stored in environment)
# llm = OpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))
llm = ChatGroq(
    temperature=0, 
    groq_api_key='', 
    model_name="llama-3.1-70b-versatile"
)

def process_message(message: str) -> str:
    """Process the incoming message, query the knowledge base, and return a response."""
    # Query ChromaDB to check if there is a relevant response
    knowledge_response = query_knowledge_base(message)

    if knowledge_response:
        print("GOT SOMETHING IN KNOWLEDGE!!!!")
        return knowledge_response
    else:
        # If no knowledge found, ask LangChain (OpenAI model) to generate a response
        print("WE ARE GENERATING RESPONSE SIR!!!!")
        return generate_response_with_llm(message)

# def generate_response_with_llm(message: str) -> str:
#     """Generate a response using LangChain's LLM."""
#     try:
#         response = llm(message)
#         return response['text']
#     except Exception as e:
#         return f"Error generating response: {str(e)}"

def generate_response_with_llm(message: str) -> str:
    """Generate a response using ChatGroq's LLM."""
    
    # Check if the message is empty or just whitespace
    if not message.strip():
        return "Message content cannot be empty."

    try:
        print("HUR")

        # Format the input as a list of tuples as per ChatGroq's expected input
        messages = [
            ("system", "You are a helpful assistant."),
            ("human", message)
        ]

        # Use invoke method to generate response
        response = llm.invoke(messages)
        print("I GOT YOU BRO!!!")
        print(response)
        # Return the content directly from the response
        return response.content

    except Exception as e:
        return f"Error generating response: {str(e)}"
