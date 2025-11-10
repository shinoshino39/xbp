from openai import OpenAI

#APIを使うkeyを入力します。これは絶対にwebページなどで公開してはいけません。
client = OpenAI(api_key="xxxxx")

a=input("行きたい場所を入力")
b=input("予算を入力")
question ="横浜から予算"+b+"円で"+a+"に行く旅行プラン"

#ここがAPIです----------------------------
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": question}]
)
#---------------------------------------

print("AIの答え：", response.choices[0].message.content)


