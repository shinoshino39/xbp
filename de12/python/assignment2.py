import random

class HB:
    def __init__(self, ans: str, num: str, times: int):
        # ans: 正解の4桁（文字列）、num: プレイヤーの入力（文字列）
        self.ans = ans
        self.num = num
        self.times = times

    def hit(self) -> int:
        """同じ桁かつ同じ数字（ヒット）の数を返す"""
        hits = 0
        for i in range(4):
            if self.ans[i] == self.num[i]:
                hits += 1
        return hits

    def blow(self) -> int:
        """数字は合っているが位置が違う（ブロー）の数を返す"""
        blows = 0
        # 各桁の組み合わせで、位置が異なるときに一致するかを数える
        for i in range(4):
            for j in range(4):
                if i != j and self.ans[i] == self.num[j]:
                    blows += 1
        return blows

def generate_answer() -> str:
    """0-9の数字から重複しない4桁の文字列を作る。ただし先頭は '0' にしない"""
    digits = random.sample('0123456789', 4)  # 重複なしで4個選ぶ
    if digits[0] == '0':
        # 先頭が0だったら、先頭が0でないものが先に来るまで入れ替える
        for k in range(1, 4):
            if digits[k] != '0':
                digits[0], digits[k] = digits[k], digits[0]
                break
    return ''.join(digits)

def valid_input(s: str) -> bool:
    """入力のバリデーション：4桁、全て数字、先頭が0でない（必要なら）"""
    return len(s) == 4 and s.isdigit()

def main():
    answer = generate_answer()
    # デバッグ時に正解を表示したいなら次の行のコメントを外す
    # print("DEBUG: answer =", answer)

    attempt = 0
    while True:
        try:
            attempt += 1
            user = input(">>> ")
            if not valid_input(user):
                print("エラー：4桁の数字を入力してください（例: 1234）")
                continue

            game = HB(answer, user, attempt)
            h = game.hit()
            b = game.blow()
            print(f"{h}H{b}B")  # 例: 1H2B

            if h == 4:
                print(f"おめでとうございます！ あなたは{attempt}手でクリアしました！")
                break
        except KeyboardInterrupt:
            print("\nゲームを終了します。")
            break
        except Exception as e:
            # ここでは予期しない例外内容を出しておくとデバッグが楽
            print("予期せぬエラーが発生しました:", e)
            break

if __name__ == "__main__":
    main()
