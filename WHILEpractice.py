import time # 載入時間的函式庫
count = 1   # 設定一個變數,儲存次數
# 無限執行
while(True):
    # 顯示出 你好 次數
    print("你好",count)
    count += 1 # 次數每次加一
    time.sleep(0.5) # 暫停0.5秒 
    # 判斷如果次數超過10次
    if count > 10:
        break # 跳出迴圈
#在迴圈外顯示程式執行結束    
print("程式執行結束")

    