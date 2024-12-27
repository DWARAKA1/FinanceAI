from typing import Optional, Dict, Any, List
from phi.assistant import Assistant
from phi.llm.groq import Groq

class WebAgent:
    def __init__(self, groq_api_key: str):
        """Initialize the WebAgent with research capabilities."""
        self.llm = Groq(
            model="mixtral-8x7b-32768",
            api_key=groq_api_key
        )
        
        self.assistant = Assistant(
            name="Research Expert",
            llm=self.llm,
            description="""I am a research expert that can:
            - Analyze market trends and data
            - Research companies and industries
            - Gather relevant information
            - Provide comprehensive analysis"""
        )

    def research_topic(self, topic: str) -> str:
        """
        Research a specific topic and provide analysis.
        
        Args:
            topic (str): Topic to research
            
        Returns:
            str: Research findings and analysis
        """
        prompt = f"""Please provide a comprehensive analysis of: {topic}
        Include:
        - Key points and insights
        - Important trends
        - Relevant data
        - Recommendations based on the findings
        """
        response = self.assistant.run(message=prompt)
        # Handle streaming response
        full_response = ""
        for chunk in response:
            if chunk:
                full_response += chunk
        return full_response

class FinanceAgent:
    def __init__(self, groq_api_key: str):
        """Initialize the FinanceAgent for financial analysis."""
        self.llm = Groq(
            model="mixtral-8x7b-32768",
            api_key=groq_api_key
        )
        
        self.assistant = Assistant(
            name="Financial Analyst",
            llm=self.llm,
            description="""I am a financial analyst that can:
            - Analyze financial data and trends
            - Provide investment recommendations
            - Assess risk and opportunities
            - Explain complex financial concepts
            - Create financial strategies"""
        )

    def analyze_investment(self, asset_type: str, data: Dict[str, Any], risk_profile: str) -> str:
        """
        Analyze an investment opportunity.
        
        Args:
            asset_type (str): Type of investment asset
            data (Dict[str, Any]): Relevant financial data
            risk_profile (str): Risk tolerance level
            
        Returns:
            str: Investment analysis and recommendations
        """
        analysis_prompt = f"""Please analyze this investment opportunity:
        Asset Type: {asset_type}
        Data: {data}
        Risk Profile: {risk_profile}
        
        Provide:
        - Comprehensive analysis
        - Risk assessment
        - Expected returns
        - Recommendations
        - Investment timeline considerations
        """
        
        response = self.assistant.run(message=analysis_prompt)
        # Handle streaming response
        full_response = ""
        for chunk in response:
            if chunk:
                full_response += chunk
        return full_response

    def create_strategy(self, goals: List[str], constraints: Dict[str, Any], timeline: str) -> str:
        """
        Create a financial strategy based on goals and constraints.
        
        Args:
            goals (List[str]): Financial goals
            constraints (Dict[str, Any]): Limitations and requirements
            timeline (str): Strategy timeline
            
        Returns:
            str: Detailed financial strategy
        """
        strategy_prompt = f"""Please create a financial strategy with:
        Goals: {goals}
        Constraints: {constraints}
        Timeline: {timeline}
        
        Include:
        - Strategic approach
        - Asset allocation
        - Risk management
        - Implementation steps
        - Monitoring metrics
        """
        
        response = self.assistant.run(message=strategy_prompt)
        # Handle streaming response
        full_response = ""
        for chunk in response:
            if chunk:
                full_response += chunk
        return full_response

class AgentTeam:
    def __init__(self, groq_api_key: str):
        """Initialize the agent team with specialized agents."""
        self.web_agent = WebAgent(groq_api_key=groq_api_key)
        self.finance_agent = FinanceAgent(groq_api_key=groq_api_key)

    def comprehensive_analysis(self, symbol: str, risk_profile: str, timeline: str) -> Dict[str, str]:
        """
        Perform comprehensive market and financial analysis.
        
        Args:
            symbol (str): Asset or market symbol
            risk_profile (str): Risk tolerance level
            timeline (str): Investment timeline
            
        Returns:
            Dict[str, str]: Combined analysis from both agents
        """
        # Get market data from web agent
        market_data = self.web_agent.research_topic(f"Current market analysis for {symbol}")
        
        # Get financial analysis
        financial_analysis = self.finance_agent.analyze_investment(
            asset_type="stock",
            data={"market_data": market_data, "timeline": timeline},
            risk_profile=risk_profile
        )
        
        return {
            "market_analysis": market_data,
            "financial_analysis": financial_analysis
        }

    def research_and_strategize(self, topic: str, goals: List[str], constraints: Dict[str, Any], timeline: str) -> Dict[str, str]:
        """
        Research a topic and create a financial strategy.
        
        Args:
            topic (str): Research topic
            goals (List[str]): Financial goals
            constraints (Dict[str, Any]): Strategy constraints
            timeline (str): Strategy timeline
            
        Returns:
            Dict[str, str]: Research findings and strategy
        """
        # Research the topic
        research_findings = self.web_agent.research_topic(topic)
        
        # Create strategy based on research
        strategy = self.finance_agent.create_strategy(
            goals=goals,
            constraints={**constraints, "research_findings": research_findings},
            timeline=timeline
        )
        
        return {
            "research_findings": research_findings,
            "financial_strategy": strategy
        }

def main():
    """Example usage of the agent team."""
    from dotenv import load_dotenv
    import os
    
    load_dotenv()
    
    # Get API key from environment variable
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("Please set GROQ_API_KEY environment variable")
    
    # Create agent team
    team = AgentTeam(groq_api_key=groq_api_key)
    
    while True:
        print("\nOptions:")
        print("1. Analyze investment")
        print("2. Research and create strategy")
        print("3. Quit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            symbol = input("Enter asset symbol to analyze (e.g. AAPL): ")
            risk_profile = input("Enter risk profile (low/medium/high): ")
            timeline = input("Enter investment timeline (e.g. 5 years): ")
            
            try:
                result = team.comprehensive_analysis(symbol, risk_profile, timeline)
                print("\nMarket Analysis:")
                print(result["market_analysis"])
                print("\nFinancial Analysis:")
                print(result["financial_analysis"])
            except Exception as e:
                print(f"Error: {str(e)}")
                
        elif choice == "2":
            topic = input("Enter research topic: ")
            goals = input("Enter financial goals (comma-separated): ").split(",")
            timeline = input("Enter strategy timeline: ")
            constraints = {
                "budget": input("Enter budget constraint: "),
                "risk_level": input("Enter risk tolerance (low/medium/high): ")
            }
            
            try:
                result = team.research_and_strategize(topic, goals, constraints, timeline)
                print("\nResearch Findings:")
                print(result["research_findings"])
                print("\nFinancial Strategy:")
                print(result["financial_strategy"])
            except Exception as e:
                print(f"Error: {str(e)}")
                
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
