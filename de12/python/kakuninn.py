import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイル読み込み
load_dotenv()

# 環境変数からAPIキー取得
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("APIキーが読み込めていません。'.env' の場所と内容を確認してください。")

# Gemini APIを設定
genai.configure(api_key=api_key)

# 最新モデルを選択
model = genai.GenerativeModel("models/gemini-2.5-pro")

# テストプロンプト
prompt = "こんにちは、今日はどんな日？"
response = model.generate_content(prompt)

print(response.text)

