from openai import OpenAI
from groq import Groq
from google.generativeai import GenerativeModel, configure as genai_config
from dotenv import load_dotenv
import os

# --- .env読み込み ---
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# --- クライアント設定 ---
client_openai = OpenAI(api_key=OPENAI_API_KEY)
genai_config(api_key=GOOGLE_API_KEY)
gemini_model = GenerativeModel("models/gemini-2.5-pro-preview-06-05")
client_groq = Groq(api_key=GROQ_API_KEY)

# --- MAGI人格関数 ---
def reason_ai(prompt):
    """理性担当（Gemini）"""
    return gemini_model.generate_content(prompt).text

def emotion_ai(prompt):
    """感情・倫理担当（ChatGPT）"""
    response = client_openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "あなたはMAGIの感情・倫理担当です。人間視点で判断や提案を加えてください。"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def navigator_ai(prompt):
    """ナビ／情報生成担当（Groq）"""
    response = client_groq.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "あなたはMAGIのナビ／情報生成担当です。入力から新しい情報を生成してください。"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# --- MAGIフロー ---
user_question = "新しい家族に犬を迎えるべきか？"

# 1. 理性担当
reason_output = reason_ai(f"論理的に分析してください: {user_question}")

# 2. 感情・倫理担当
emotion_output = emotion_ai(f"人間視点で考えて: {user_question}")

# 3. ナビ／情報生成担当
navigator_output = navigator_ai(f"犬を迎えるときの注意点や新情報を生成してください: {user_question}")

# 4. 最終統合（ChatGPTでまとめる）
integration_prompt = f"""
以下はMAGIシステムの3人格の出力です。
理性担当(Gemini): {reason_output}
感情・倫理担当(ChatGPT): {emotion_output}
ナビ・情報生成担当(Groq): {navigator_output}

これらを総合して、ユーザーにわかりやすく、犬を迎えるべきかの提案をしてください。
"""

final_output = client_openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "あなたはMAGIシステム統合担当です。3人格の出力をまとめて最終回答を作ります。"},
        {"role": "user", "content": integration_prompt}
    ]
)

print("=== MAGI統合最終回答 ===")
print(final_output.choices[0].message.content)
