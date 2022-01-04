list = [39, 10, -8, 64, 75]
def bubblesort(list):                      # 定義資料長度
    n = len(list)
    for i in range(n-2):                   # 有 n 個資料長度，但只要執行 n-1 次
        for j in range(n-i-1):             # 從第1個開始比較直到最後一個還沒到最終位置的數字
            if list[j] > list[j+1]:        # 比大小然後互換
                list[j], list[j+1] = list[j+1], list[j]

bubblesort(list)
print(list)
