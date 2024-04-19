from langchain.agents.agent_types import AgentType
from langchain_experimental.agents import create_csv_agent
from langchain_openai import ChatOpenAI
import os 
from dotenv import load_dotenv
from modules import read_file_as_string

load_dotenv()

def chatbot_agent(prompt):
    script_dir = os.path.dirname(__file__)
    file_name = "context.txt"
    file_content = read_file_as_string(script_dir, file_name)

    agent = create_csv_agent(
        ChatOpenAI(temperature=0, model="gpt-4-turbo"),
        "team4data.csv",
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    response = agent.invoke(f"{file_content}{prompt}")

    return response['output']

# prompt = "what are the vehicles of mickey mous?"
# prompt = "My name is mickey hous , could you describe VIN of vehicle I own?"
# prompt = "Mein Name ist Mickey Mouse. Bitte beschreiben Sie die Fahrgestellnummer des Fahrzeugs, das ich besitze"
# prompt = "Nazywam się Mickey Mouse, jaki jest status moich pojazdów?"
# prompt = "Order part for my vehicle with VIN VIN1234567890SW" 
prompt = "I'm Peter Pan, what is the status of my vehicle?"
# prompt = "I'm Cinderella, when do my warranty expire?"
# prompt = "What are all the owner names?"
# prompt = "tell me about all of the vehicles with status parked for Peter Pan"

chatbot_agent(prompt)