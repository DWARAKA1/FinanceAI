from typing import Optional, Dict, Any
from phi.assistant import Assistant
from phi.llm.groq import Groq

class FinanceAgent:
    def __init__(self, groq_api_key: str):
        """Initialize the FinanceAgent with Groq API key."""
        self.llm = Groq(
            model="mixtral-8x7b-32768",
            api_key=groq_api_key
        )
        
        self.assistant = Assistant(
            name="Finance Expert",
            llm=self.llm,
            description="""I am a financial expert assistant that can help with:
            - Financial analysis and calculations
            - Investment strategies and portfolio management
            - Market analysis and trends
            - Risk assessment and management
            - Personal finance advice"""
        )

    def analyze_investment(self, investment_type: str, data: Dict[str, Any]) -> str:
        """
        Analyze an investment opportunity.
        
        Args:
            investment_type (str): Type of investment (e.g., stocks, bonds, real estate)
            data (Dict[str, Any]): Investment data and parameters
            
        Returns:
            str: Detailed investment analysis
        """
        prompt = f"""Please analyze this investment opportunity:
        Type: {investment_type}
        Data: {data}
        
        Provide:
        - Comprehensive analysis
        - Risk assessment
        - Expected returns
        - Key considerations
        - Recommendations
        """
        
        response = self.assistant.run(message=prompt)
        # Handle streaming response
        full_response = ""
        for chunk in response:
            if chunk:
                full_response += chunk
        return full_response
    
    def create_portfolio(self, goals: Dict[str, Any], constraints: Dict[str, Any]) -> str:
        """
        Create an investment portfolio strategy.
        
        Args:
            goals (Dict[str, Any]): Investment goals and objectives
            constraints (Dict[str, Any]): Investment constraints and limitations
            
        Returns:
            str: Portfolio strategy recommendations
        """
        prompt = f"""Please create an investment portfolio strategy:
        Goals: {goals}
        Constraints: {constraints}
        
        Include:
        - Asset allocation strategy
        - Risk management approach
        - Rebalancing recommendations
        - Performance metrics
        - Implementation steps
        """
        
        response = self.assistant.run(message=prompt)
        # Handle streaming response
        full_response = ""
        for chunk in response:
            if chunk:
                full_response += chunk
        return full_response

def main():
    """Example usage of the FinanceAgent."""
    from dotenv import load_dotenv
    import os
    
    load_dotenv()
    
    # Get API key from environment variable
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("Please set GROQ_API_KEY environment variable")
    
    # Create finance agent
    agent = FinanceAgent(groq_api_key=groq_api_key)
    
    while True:
        print("\nOptions:")
        print("1. Analyze Investment")
        print("2. Create Portfolio Strategy")
        print("3. Quit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            investment_type = input("Enter investment type (e.g., stocks, bonds, real estate): ")
            risk_tolerance = input("Enter risk tolerance (low/medium/high): ")
            investment_amount = input("Enter investment amount: ")
            timeline = input("Enter investment timeline: ")
            
            data = {
                "risk_tolerance": risk_tolerance,
                "amount": investment_amount,
                "timeline": timeline
            }
            
            try:
                analysis = agent.analyze_investment(investment_type, data)
                print("\nInvestment Analysis:")
                print(analysis)
            except Exception as e:
                print(f"Error: {str(e)}")
                
        elif choice == "2":
            goals = {
                "primary": input("Enter primary investment goal: "),
                "timeline": input("Enter investment timeline: "),
                "target_return": input("Enter target return rate: ")
            }
            
            constraints = {
                "risk_tolerance": input("Enter risk tolerance (low/medium/high): "),
                "initial_investment": input("Enter initial investment amount: "),
                "monthly_contribution": input("Enter monthly contribution amount: ")
            }
            
            try:
                strategy = agent.create_portfolio(goals, constraints)
                print("\nPortfolio Strategy:")
                print(strategy)
            except Exception as e:
                print(f"Error: {str(e)}")
                
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
