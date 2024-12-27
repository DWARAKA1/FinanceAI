from typing import Optional
from phi.assistant import Assistant
from phi.llm.groq import Groq

class SimpleGroqAgent:
    def __init__(self, groq_api_key: str):
        """Initialize the SimpleGroqAgent with Groq API key."""
        self.llm = Groq(
            model="mixtral-8x7b-32768",
            api_key=groq_api_key
        )
        
        self.assistant = Assistant(
            name="Groq Assistant",
            llm=self.llm,
            description="A helpful AI assistant powered by Groq's Mixtral model."
        )

    def ask(self, question: str) -> str:
        """
        Ask a question to the assistant and get a response.
        
        Args:
            question (str): The question to ask
            
        Returns:
            str: The assistant's response
        """
        response = self.assistant.run(message=question)
        # Handle streaming response
        full_response = ""
        for chunk in response:
            if chunk:
                full_response += chunk
        return full_response

def main():
    # Load environment variables
    from dotenv import load_dotenv
    import os
    
    load_dotenv()
    
    # Get API key from environment variable
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("Please set GROQ_API_KEY environment variable")
    
    # Create agent
    agent = SimpleGroqAgent(groq_api_key=groq_api_key)
    
    # Example usage
    while True:
        question = input("\nEnter your question (or 'quit' to exit): ")
        if question.lower() == 'quit':
            break
            
        try:
            response = agent.ask(question)
            print(f"\nAssistant: {response}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
