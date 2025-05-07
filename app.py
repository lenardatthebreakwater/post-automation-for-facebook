import requests
import dotenv
import os
import json

dotenv.load_dotenv()

def create_post_with_ai(prompt: str) -> str:
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    ai_model = os.getenv("AI_MODEL")
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {openrouter_api_key}",
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "model": ai_model,
        "messages": [{"role": "user", "content": prompt}]
    })
    response = requests.post(url=url, headers=headers, data=data)
    response_data = response.json()
    print(response_data)
    return response_data["choices"][0]["message"]["content"]

def post_to_facebook(post: str) -> None:
    page_id = os.getenv("FB_PAGE_ID")
    page_access_token = os.getenv("FB_PAGE_ACCESS_TOKEN")
    url = f"https://graph.facebook.com/v22.0/{page_id}/feed"
    params = {
        "message": post,
        "access_token": page_access_token,
        "published": "false",
        "unpublished_content_type": "DRAFT"
    }
    response = requests.post(url=url, params=params)

if __name__ == "__main__":
    post = create_post_with_ai("Can you please create an fb post for me about Meovv kpop group?")
    post_to_facebook(post)
