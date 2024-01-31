from openai import OpenAI
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
if os.getenv('AZURE_FUNCTIONS_ENVIRONMENT') is None:
    # Load environment variables from the .env file for local development
    from dotenv import load_dotenv
    load_dotenv()

#api_key = os.getenv('OPENAI_SECRET_KEY')
api_key = os.environ.get('OPENAI_SECRET_KEY')

def chatgpt_query(content, max_tokens):
    if not content or not isinstance(content, str):
        logger.info(f"Content must be a non-empty string")
        raise ValueError("Content must be a non-empty string.")

    if not max_tokens or not isinstance(max_tokens, int) or max_tokens <= 0:
        logger.info(f"max_tokens must be a positive integer")
        raise ValueError("max_tokens must be a positive integer.")

    try:
        client = OpenAI(api_key=api_key)
        logger.info(f"Oppened client with OpenAI")
        user_message = {"role": "user", "content": content}
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[user_message],
            max_tokens=max_tokens
        )
        logger.info(f"Received response: {chat_completion.choices[0].message.content}")
        return chat_completion.choices[0].message.content
        
    except error.OpenAIError as e:
        logger.error(f"OpenAI API error: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return None