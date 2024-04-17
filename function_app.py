import azure.functions as func
import logging
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
utils_path = os.path.join(script_dir, 'utils')
sys.path.append(utils_path)
from agent import *
from modules import *
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents import create_csv_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="volvochatbot")
def test_azure_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    prompt = req.args.get('prompt')
    user_type = req.args.get('user_type')
    
    if not prompt:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            prompt = req_body.get('prompt')

    if not user_type:
        try:
            req_body = req.get_json()
            user_type = req_body.get('user_type')
        except ValueError:
            user_type = "anonymous"

    if prompt:
        content = chatbot_agent(prompt)
        return func.HttpResponse(f"{content}")
    else:
        return func.HttpResponse(
             "Maybe ai won't take our jobs, please ask me a question with prompt argument",
             status_code=200
        )

