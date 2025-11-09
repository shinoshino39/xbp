import os
from openai import OpenAI
from dotenv import load_dotenv
import groq  # Groq SDK

# -----------------------------
# 環境変数からAPIキーを読み込む
# -----------------------------
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# OpenAI GPTクライアント
gpt_client = OpenAI(api_key=OPENAI_API_KEY)

# Groqクライアント
groq_client = groq.Client(api_key=GROQ_API_KEY)

# -----------------------------
# ユーザー質問入力
# -----------------------------
user_question = input("質問を入力してください: ")

# -----------------------------
# 理性担当（Reason AI） → GPT
# -----------------------------
def reason_ai(prompt):
    response = gpt_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# -----------------------------
# 創造担当（Creative AI） → Groq
# -----------------------------
def creative_ai(prompt):
    response = groq_client.chat.completions.create(
        model="llama3-7b-2048",  # 適切な利用可能モデルに置き換えてください
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# -----------------------------
# 統合担当（Integration AI） → GPT
# -----------------------------
def integrate_ai(reason_text, creative_text):
    prompt = f"""以下の2つの情報を統合して最終的な回答を作ってください。
1. 論理的分析: {reason_text}
2. 創造的提案: {creative_text}
"""
    response = gpt_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# -----------------------------
# フロー実行
# -----------------------------
reason_output = reason_ai(f"論理的に分析してください: {user_question}")
creative_output = creative_ai(f"創造的に提案してください: {user_question}")
final_output = integrate_ai(reason_output, creative_output)

# -----------------------------
# 出力
# -----------------------------
print("\n--- 理性担当の分析(GPT) ---")
print(reason_output)
print("\n--- 創造担当の提案(Groq) ---")
print(creative_output)
print("\n--- 統合結果(GPT) ---")
print(final_output)
