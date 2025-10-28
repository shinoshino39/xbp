for i in range(1,4):
    print(i,"人目")
    name=input("名前は？")
    height=float(input("身長は？"))
    weight=float(input("体重は？"))

    print(name, "さん身長は", height, "cmで体重は",weight, "kgですね。")

    bmi = weight / ((height/100)*(height/100))
    print("BMIは",bmi,"です")

    if 25<=bmi:
        print(name,"さん、BMI注意です")
    else:
        print(name,"さん、BMIは問題ありません")

