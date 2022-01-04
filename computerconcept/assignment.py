fac = int(1) #設fac為整數1
while True: #輸入到正確值(程式可運算的值)為止
    try:
        num = int(input("please enter a number which > 0 :"))
    except ValueError:
        continue #錯誤值，繼續上式
    else:
        if num > 0:
            for i in range (1, num + 1):
                fac = fac * i #階乘運算
            print(fac) #印出運算結果
            break #離開迴圈



