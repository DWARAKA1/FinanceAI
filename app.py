from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv
import os
import uvicorn
from financeagent import FinanceAgent
from simplegroqagent import SimpleGroqAgent
from agent_teams import AgentTeam

app = FastAPI(title="FinanceAI API")

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")

# Initialize agents
simple_agent = SimpleGroqAgent(groq_api_key=groq_api_key)
finance_agent = FinanceAgent(groq_api_key=groq_api_key)
agent_team = AgentTeam(groq_api_key=groq_api_key)

class QuestionRequest(BaseModel):
    question: str

class InvestmentRequest(BaseModel):
    investment_type: str
    risk_tolerance: str
    investment_amount: str
    timeline: str

class PortfolioRequest(BaseModel):
    primary_goal: str
    timeline: str
    target_return: str
    risk_tolerance: str
    initial_investment: str
    monthly_contribution: str

@app.get("/")
def read_root():
    return {"message": "Welcome to FinanceAI API"}

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        response = simple_agent.ask(request.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze-investment")
async def analyze_investment(request: InvestmentRequest):
    try:
        data = {
            "risk_tolerance": request.risk_tolerance,
            "amount": request.investment_amount,
            "timeline": request.timeline
        }
        analysis = finance_agent.analyze_investment(request.investment_type, data)
        return {"analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/create-portfolio")
async def create_portfolio(request: PortfolioRequest):
    try:
        goals = {
            "primary": request.primary_goal,
            "timeline": request.timeline,
            "target_return": request.target_return
        }
        constraints = {
            "risk_tolerance": request.risk_tolerance,
            "initial_investment": request.initial_investment,
            "monthly_contribution": request.monthly_contribution
        }
        strategy = finance_agent.create_portfolio(goals, constraints)
        return {"strategy": strategy}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
