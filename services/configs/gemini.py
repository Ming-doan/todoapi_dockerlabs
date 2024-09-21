import os
from dotenv import load_dotenv
import dspy

load_dotenv()


def get_llm_client():
    if os.environ.get("GOOGLE_API_KEY") != None:
        return dspy.Google(
            api_key=os.environ.get("GOOGLE_API_KEY"),
        )
    else:
        return dspy.OllamaLocal(
            model="llama3.1",
            base_url=f"http://{os.environ.get('OLLAMA_HOST', 'localhost')}:{os.environ.get('OLLAMA_PORT', 11434)}",
        )


llm = get_llm_client()
