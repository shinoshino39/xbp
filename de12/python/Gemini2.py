import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイルから読み込み
load_dotenv()

# 環境変数からAPIキーを取得
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("APIキーが読み込めていません。'.env' の場所と内容を確認してください。")

# Google Geminiにキーを設定
genai.configure(api_key=api_key)

# モデルを指定
model = genai.GenerativeModel("gemini-1.5-flash")

prompt = "こんにちは！"
response = model.generate_content(prompt)

print(response.text)

from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("GOOGLE_API_KEY"))
