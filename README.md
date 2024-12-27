# FinanceAI

A collection of AI-powered financial analysis tools using the Groq API.

## Features

- **SimpleGroqAgent**: Basic question-answering agent using Groq's Mixtral model
- **FinanceAgent**: Specialized financial analysis and investment advice
- **AgentTeams**: Collaborative AI agents for comprehensive financial research and strategy

## Prerequisites

- Python 3.8+
- Groq API key

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd FinanceAI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the project root and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

### Simple Groq Agent
```bash
python simplegroqagent.py
```
- Ask any question and get AI-powered responses
- Type 'quit' to exit

### Finance Agent
```bash
python financeagent.py
```
Features:
- Analyze investments
- Create portfolio strategies
- Get personalized financial advice

### Agent Teams
```bash
python agent_teams.py
```
Features:
- Comprehensive market analysis
- Research and strategy development
- Collaborative AI insights

## Project Structure

```
FinanceAI/
├── simplegroqagent.py   # Basic Groq integration
├── financeagent.py      # Financial analysis agent
├── agent_teams.py       # Multi-agent system
├── requirements.txt     # Project dependencies
└── .env                # Environment variables (not in git)
```

## Security Note

- Never commit your `.env` file or expose your API keys
- Always use environment variables for sensitive information

## License

[Your chosen license]

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request