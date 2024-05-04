# 輸入數值的函式
def num():
    num1 = float(input("輸入第一個數字: "))
    num2 = float(input("輸入第二個數字: "))
    return num1, num2

# 加法運算的函式
def add(num1, num2):
    return num1 + num2

# 減法運算的函式
def sub(num1, num2):
    return num1 - num2

# 乘法運算的函式
def mul(num1, num2):
    return num1 * num2

# 除法運算的函式
def div(num1, num2):
    # 因為除數不能為零，所以要判斷 y 是否為零
    if num2 != 0:
        return num1 / num2
    else:
        return "除數不能為零"

# 計算機的函式
def calculator():
    # 無限執行
    while(True):
        # 選擇運算的介面
        print("選擇運算：")
        print("0. 離開")
        print("1. 加法")
        print("2. 減法")
        print("3. 乘法")
        print("4. 除法")

        # 讓使用者輸入選擇，並儲存到 choice 變數
        choice = input("請輸入選擇(0/1/2/3/4): ")

        # 如果使用者輸入 0，則跳出迴圈
        if choice == '0':
            break   # 跳出迴圈

        # 如果使用者輸入 1，則執行加法
        if choice == '1':
            num1, num2 = num() # 呼叫 num 函式並傳入 num1, num2
            print(num1,"+",num2,"=",add(num1,num2)) # 呼叫 add 函式執行相加並接收結果

        # 如果使用者輸入 2，則執行減法
        elif choice == '2':
            num1, num2 = num()
            print(num1,"-",num2,"=",sub(num1,num2))

        # 如果使用者輸入 3，則執行乘法
        elif choice == '3':
            num1, num2 = num()
            print(num1,"*",num2,"=",mul(num1,num2))

        # 如果使用者輸入 4，則執行除法
        elif choice == '4':
            num1, num2 = num()
            result = div(num1, num2)
            # 如果 result 是字串，則顯示除數不能為零（因為在上面的函式中有判斷num2是否為零,若為零回傳一段提示字串）
            if isinstance(result, str):
                print(result)
            # 否則顯示結果
            else:
                print(num1,"*",num2,"=",div(num1,num2))

        # 如果使用者輸入其他數字，則顯示無效的輸入
        else:
            print("無效的輸入")

# 如果這個檔案是主程式，則執行 calculator 函式
if __name__ == "__main__":
    calculator()
