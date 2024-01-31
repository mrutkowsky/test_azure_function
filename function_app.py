import azure.functions as func
import logging
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
utils_path = os.path.join(script_dir, 'utils')
sys.path.append(utils_path)
from openai_con import *

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="test-azure-function")
def test_azure_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        content = chatgpt_query(f"My name is {name}, does it have any history? Tell me about it", 50)
        return func.HttpResponse(f"{content}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

