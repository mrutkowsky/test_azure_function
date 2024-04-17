from langchain.agents.agent_types import AgentType
from langchain_experimental.agents import create_csv_agent
from langchain_openai import ChatOpenAI
import os 
from dotenv import load_dotenv
from utils.modules import read_file_as_string

# load_dotenv()

def chatbot_agent(prompt):
    script_dir = os.path.dirname(__file__)
    file_name = "/data/context.txt"
    file_content = read_file_as_string(script_dir, file_name)

    agent = create_csv_agent(
        ChatOpenAI(temperature=0, model="gpt-4-turbo"),
        "team4data.csv",
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    response = agent.invoke(f"{file_content}{prompt}")

    return response['output']

