from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",  # ✅ 最新の推奨モデルに変更
    messages=[
        {"role": "system", "content": "あなたはMAGIシステムのように議論するAIです。"},
        {"role": "user", "content": "MAGIシステムを起動して。"}
    ]
)

print(response.choices[0].message.content)
