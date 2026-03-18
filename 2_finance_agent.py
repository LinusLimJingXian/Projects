from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

# ----------------------------
# Create Agent
# ----------------------------
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True
        ),
    ],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Use tables to display data."
    ],
    debug_mode=True,
)

# ----------------------------
# Run query
# ----------------------------
agent.print_response(
    "Summarize and compare latest analyst recommendations and fundamentals for TESLA and Phidata"
)