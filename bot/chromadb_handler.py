import os
from dotenv import load_dotenv
import chromadb
from chromadb.config import Settings
from langchain_openai import OpenAIEmbeddings
# from chromadb.errors import APIStatusError


# Load environment variables from .env file
load_dotenv()

# Fetch the OpenAI API key from the .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the ChromaDB client
client = chromadb.Client(Settings(persist_directory="data"))

# Define the embedding wrapper
class EmbeddingWrapper:
    def __init__(self, api_key):
        self.embedding_function = OpenAIEmbeddings(openai_api_key=api_key)

    def __call__(self, input):
        return self.embedding_function.embed_documents(input)

# def query_knowledge_base(message: str) -> str:
#     """Search the ChromaDB knowledge base for relevant information related to the input message."""
#     try:

#         # Query the ChromaDB collection using the input message
#         results = collection.query(
#             query_texts=[message],
#             n_results=1  # Retrieve the top result
#         )

#         # If there are results, return the content of the most relevant document
#         if results['documents']:
#             print("Collection succesfuly")
#             return results['documents'][0]  # Return the top result's text
#         else:
#             return None  # No relevant knowledge found
    
    
    
#     except Exception as e:
#         print(f"Error querying knowledge base: {str(e)}")
#         print(f"Exception details: {repr(e)}")  # This prints a more detailed representation of the exception

#         return None
def query_knowledge_base(message: str) -> str:
    """Search the ChromaDB knowledge base for relevant information related to the input message."""
    try:
        # Query the ChromaDB collection using the input message
        results = collection.query(
            query_texts=[message],
            n_results=1  # Retrieve the top result
        )

        # If there are results, return the content of the most relevant document
        if results['documents']:
            print("Collection successfully queried")
            return results['documents'][0]  # Return the top result's text
        else:
            return None  # No relevant knowledge found
    except Exception as e:
        # Catch any exception and print the error message and details
        print(f"Error querying knowledge base: {str(e)}")

        # If the error has response and body attributes, print them
        if hasattr(e, 'response') and hasattr(e, 'body'):
            print(f"Response: {e.response}")
            print(f"Body: {e.body}")

        return None  # Return None to indicate an error


embedding_wrapper = EmbeddingWrapper(openai_api_key)

# Initialize the collection with the new wrapper
collection = client.get_or_create_collection(
    name="whatsapp_bot_knowledge",
    embedding_function=embedding_wrapper
)
