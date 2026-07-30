from app.prompts.certificates import build_certificate_prompt
from app.providers.gemini import GeminiProvider
from app.core.config import settings


async def generate_certificate_design(task: str):
    prompt = build_certificate_prompt(task)

    provider = GeminiProvider(
        api_key=settings.GEMINI_API_KEY,
        model_name=settings.GEMINI_MODEL,
    )

    response = await provider.generate_text(prompt)

    return response