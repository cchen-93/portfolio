
"""
==================================================
檔案名稱：guess_poker.py
版本：1.0

程式名稱：
猜撲克牌花色及號碼遊戲

程式說明：
1. 系統隨機產生一張撲克牌。
2. 玩家需先猜測花色。
3. 花色猜中後，再猜測點數。
4. 點數猜錯時提供大小提示。
5. 玩家可隨時輸入 Q 離開遊戲。
6. 遊戲結束後顯示猜測統計資料。

程式特色：
✓ 使用者友善介面
✓ 完整輸入驗證
✓ 不會因錯誤輸入而異常終止
✓ 函式化設計
✓ 完善註解
==================================================
"""

# 載入 random 模組，用於產生隨機數字
import random


# ==================================================
# 常數設定區
# ==================================================

# 撲克牌花色選單
# Key 為玩家輸入選項
# Value 為對應花色名稱
SUITS = {
    "1": "黑桃",
    "2": "紅心",
    "3": "方塊",
    "4": "梅花"
}

# 特殊牌面轉換表
# 撲克牌中的 A、J、Q、K
CARD_NAMES = {
    1: "A",
    11: "J",
    12: "Q",
    13: "K"
}


# ==================================================
# 工具函式區
# ==================================================

def card_name(number):
    """
    功能：
        將數字點數轉換成撲克牌顯示文字

    例如：
        1 -> A
        11 -> J
        12 -> Q
        13 -> K

    參數：
        number(int)

    回傳：
        str
    """

    return CARD_NAMES.get(number, str(number))


def generate_card():
    """
    功能：
        隨機產生一張撲克牌

    回傳：
        tuple
        (花色, 點數)
    """

    # 從花色清單中隨機抽取一種花色
    suit = random.choice(list(SUITS.values()))

    # 隨機產生 1~13 點
    number = random.randint(1, 13)

    return suit, number


# ==================================================
# 使用者輸入函式區
# ==================================================

def get_suit():
    """
    功能：
        取得玩家輸入的花色

    回傳：
        str  -> 花色名稱
        None -> 使用者選擇離開
    """

    while True:

        print("\n========== 花色選單 ==========")
        print("1. 黑桃")
        print("2. 紅心")
        print("3. 方塊")
        print("4. 梅花")
        print("Q. 離開遊戲")
        print("==============================")

        # 移除空白並統一轉成大寫
        choice = input("請輸入：").strip().upper()

        # 使用者選擇離開
        if choice == "Q":
            return None

        # 驗證是否為合法選項
        if choice in SUITS:
            return SUITS[choice]

        # 非法輸入提示
        print("❌ 輸入錯誤，請輸入 1~4 或 Q")


def get_number():
    """
    功能：
        取得玩家猜測的點數

    回傳：
        int  -> 玩家輸入的數字
        None -> 使用者選擇離開
    """

    while True:

        value = input(
            "請猜點數(1~13)，輸入 Q 離開："
        ).strip().upper()

        # 使用者選擇離開
        if value == "Q":
            return None

        try:

            # 將字串轉換成整數
            number = int(value)

            # 驗證範圍是否介於 1~13
            if 1 <= number <= 13:
                return number

            print("❌ 點數必須介於 1~13")

        except ValueError:

            # 輸入非數字時進入此區塊
            print("❌ 請輸入有效數字")


# ==================================================
# 主程式
# ==================================================

def main():
    """
    遊戲主流程
    """

    print("=" * 50)
    print("🎴 歡迎來到猜撲克牌遊戲 🎴")
    print("=" * 50)

    print("遊戲規則：")
    print("1. 先猜花色")
    print("2. 花色猜對後只需猜數字")
    print("3. 猜錯數字會提示大小")
    print("4. 輸入 Q 可隨時離開")
    print("=" * 50)

    # 隨機產生本局答案
    target_suit, target_number = generate_card()

    # 紀錄猜花色次數
    suit_count = 0

    # 紀錄猜數字次數
    number_count = 0

    # ==================================================
    # 第一階段：猜花色
    # ==================================================
    # 玩家必須先猜中花色
    # 才能進入下一階段猜數字
    # ==================================================

    while True:

        # 取得玩家輸入的花色
        user_suit = get_suit()

        # 使用者選擇離開
        if user_suit is None:
            print("\n👋 感謝遊玩，再見！")
            return

        # 花色猜測次數加一
        suit_count += 1

        # 判斷花色是否猜中
        if user_suit == target_suit:

            print("\n🎉 恭喜！花色猜對了！")
            print(f"正確花色：{target_suit}")
            print(f"請猜 {target_suit} 的點數")

            # 進入數字猜測階段
            break

        # 花色猜錯
        print("❌ 花色錯誤，請再試一次")

    # ==================================================
    # 第二階段：猜數字
    # ==================================================
    # 花色正確後
    # 持續猜數字直到猜中
    # ==================================================

    while True:

        # 取得玩家輸入的數字
        user_number = get_number()

        # 使用者選擇離開
        if user_number is None:
            print("\n👋 感謝遊玩，再見！")
            return

        # 數字猜測次數加一
        number_count += 1

        # 完全猜中
        if user_number == target_number:

            print("\n🎉 恭喜完全猜中！")

            print(
                f"答案是：{target_suit} "
                f"{card_name(target_number)}"
            )

            print("\n📊 遊戲統計")
            print(f"花色猜測次數：{suit_count}")
            print(f"數字猜測次數：{number_count}")
            print(
                f"總猜測次數："
                f"{suit_count + number_count}"
            )

            break

        # 玩家猜的數字比答案小
        elif user_number < target_number:

            print(
                f"⬆️ 你猜的是 {user_number}，"
                f"答案比 {user_number} 大"
            )

        # 玩家猜的數字比答案大
        else:

            print(
                f"⬇️ 你猜的是 {user_number}，"
                f"答案比 {user_number} 小"
            )


# ==================================================
# 程式進入點
# ==================================================

if __name__ == "__main__":

    try:

        # 執行主程式
        main()

    except KeyboardInterrupt:

        # 使用者按下 Ctrl + C
        print("\n\n👋 使用者中斷遊戲")

    except Exception as error:

        # 捕捉所有未預期錯誤
        print(f"\n⚠️ 發生未預期錯誤：{error}")

