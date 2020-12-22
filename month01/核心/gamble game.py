# 赌大小游戏
#     玩家的身家初始10000，实现下列效果：
#         少侠请下注: 30000
#         超出了你的身家，请重新投注。
#         少侠请下注: 8000
#         你摇出了5点,庄家摇出了3点
#         恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩18000
#         少侠请下注: 18000
#         你摇出了6点,庄家摇出了6点
#         打平了，少侠，在来一局？
#         少侠请下注: 18000
#         你摇出了4点,庄家摇出了6点
#         少侠,你输了，身家还剩 0
#         哈哈哈，少侠你已经破产，无资格进行游戏
import random
go_on = True #增加一个询问 要不要继续
print("起始身价10000元")
net_worth = 10000

while go_on:
    if net_worth > 0:
        bet_amount = int(input("少侠请下注"))
        if bet_amount > net_worth:
            print("超出了你的身家，请重新下注")
            continue
        your_dice = random.randint(1, 6)
        dealer_dice = random.randint(1, 6)
        if your_dice < dealer_dice:
            net_worth -= bet_amount
            print("你输了，你的身家还有" + str(net_worth) + "元")
        elif your_dice > dealer_dice:
            net_worth += bet_amount
            print("你赢了，你的身家还有" + str(net_worth) + "元")
        else:
            print("平局，再来一把")
        go_on = input("是否再来一局（True）")
    else:
        print("破产了，别玩了")
        break
