import anthropic
import os
import json
from dotenv import load_dotenv

from llm.base import LLMProvider

load_dotenv()

MODEL_NAME = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")


class AnthropicProvider(LLMProvider):
    def generate_analysis(
        self, metric: str, country: str, stats: dict, question: str | None = None
    ) -> str:

        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        default_question = (
            f"Analyze the trend for {metric} in {country} based on this data."
        )
        user_question = question or default_question

        prompt = f"""
You are a public health analyst. Analyze the following health indicator data.

Country : {country}
Indicator : {metric}
Data summary: {json.dumps(stats, indent=2)}
Question : {user_question}

Instructions : 
- Be concise (3 - 5 sentences maximum)
- Always cite the specific numbers from the data
- Do not make medical diagnoses or recommandations
- Focus on trend and factual observations
- If the trend is concerning, note it factually without alarmism
- ONLY use information present in the data provided above
- Do NOT make comparisons with other countries unless their data is explicitly provided
- Do NOT make inferences beyond what the numbers directly show
"""
        response = client.messages.create(
            model=MODEL_NAME,
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}],
        )

        return response.content[0].text
