import openai
import os

from fastapi import HTTPException
from starlette import status

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image_from_string(description: str) -> str:
    try:
        response = openai.Image.create(
            prompt=description,
            n=1,
            size="256x256"
        )
        image_url = response['data'][0]['url']
        return image_url

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
