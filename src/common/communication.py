import openai
from enum import Enum
from groq import Groq
import os
from tenacity import retry, stop_after_attempt, wait_random_exponential


class Model(Enum):
    GPT_4O = "gpt-4o"
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_35_TURBO = "gpt-3.5-turbo"
    MIXTRAL = "mixtral-8x7b-32768"


@retry(wait=wait_random_exponential(min=1, max=300), stop=stop_after_attempt(6))
def chat_with_llm(**kwargs):
    model = kwargs.get('model')
    if model == Model.GPT_4O or Model.GPT_4O_MINI or Model.GPT_35_TURBO:
        client = openai.OpenAI()
    elif model == Model.MIXTRAL:
        client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    else:
        raise ValueError(f"Unsupported model type: {model}")
    return client.chat.completions.create(**kwargs)
