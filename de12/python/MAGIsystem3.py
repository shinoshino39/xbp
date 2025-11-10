import os
from openai import OpenAI
from dotenv import load_dotenv

# ====== APIキーの読み込み ======
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY が設定されていません。 .env ファイルを確認してください。")

client = OpenAI(api_key=api_key)

# ====== 質問を入力 ======
user_question = input("質問を入力してください：")

# ====== 各役割の応答関数 ======
def ask_role(role, question):
    prompt = f"{role}になりきって5文以内で回答してください。\n質問: {question}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# ====== 各担当AI ======
scientist = ask_role("科学者", user_question)
mother = ask_role("母親", user_question)
woman = ask_role("女性", user_question)

# ====== 統合AI（MAGI統合判断） ======
def integrate_opinions(scientist, mother, woman, question):
    prompt = f"""
あなたはMAGIシステムの統合AIです。
以下の3人の意見をもとに、バランスの取れた最終判断を5文以内で述べてください。

質問: {question}

--- 科学者の意見 ---
{scientist}

--- 母親の意見 ---
{mother}

--- 女性の意見 ---
{woman}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

integrated = integrate_opinions(scientist, mother, woman, user_question)

# ====== 出力 ======
print("\n====== MAGI SYSTEM ======")
print(f"質問: {user_question}\n")
print("--- 科学者担当 ---")
print(scientist)
print("\n--- 母担当 ---")
print(mother)
print("\n--- 女性担当 ---")
print(woman)
print("\n--- 統合AIの最終判断 ---")
print(integrated)
