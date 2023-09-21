import random
import time
number = {1: '左侧箱子', 2: '珍贵箱子', 3: '右侧箱子', 4: '左侧钥匙', 5: '中间钥匙', 6: '右侧钥匙'}
detective_card = []
neutrality_card = []
burglar_card = []
chest_l = []
chest_precious = []
chest_r = []
key_l = []
key_m = []
key_r = []
bag = []
bag2 = []


class Check():
    attr = []
    #检测牌名
    def check_name(self, name):
        if name == '刑警':
            self.attr.append(2)
        if name == '侦探':
            self.attr.append(1)
        if name == '记者':
            self.attr.append(3)
        if name == '怪盗':
            self.attr.append(8)
        if name == '同伙':
            self.attr.append(4)
        if name == '美女':
            self.attr.append(5)
        if name == '富豪':
            self.attr.append(6)
        if name == '千金':
            self.attr.append(7)
        if name == '侦探&刑警':
            self.attr.append(2)
            self.attr.append(1)
        if name == '记者&刑警':
            self.attr.append(2)
            self.attr.append(3)
        if name == '侦探&记者':
            self.attr.append(3)
            self.attr.append(1)
        if name == '同伙&怪盗':
            self.attr.append(4)
            self.attr.append(8)
        if name == '同伙&美女':
            self.attr.append(4)
            self.attr.append(5)
        if name == '千金&怪盗':
            self.attr.append(7)
            self.attr.append(8)
        if name == '侦探&富豪':
            self.attr.append(6)
            self.attr.append(1)
        if name == '富豪&美女':
            self.attr.append(5)
            self.attr.append(6)
        if name == '千金&富豪':
            self.attr.append(6)
            self.attr.append(7)

    #得到测试的属性
    def check_attr(self, position, num, fake):
        if num == 1:
            self.attr.append(1)
        if num == 8:
            self.attr.append(8)
        for i in range(0, 5):
            self.check_name(position[i])
        return self.check_victory(fake)




    #验证是否盗取成功
    def check_victory(self, fake):
        if (self.attr.count(8) > self.attr.count(1)) or (self.attr.count(4) >= 3 and self.attr.count(2) == 0) or \
                (self.attr.count(5) >= 3 and self.attr.count(3) == 0):
            print("盗取成功")
            self.attr = []
            return 1
        else:
            while True:
                a = int(input("是否盗取（盗取条件不足将盗取失败）\n是(1)；否(2)"))
                if a == 1:
                    if self.attr.count(fake) + self.attr.count(8) > self.attr.count(1):
                        print("盗取成功")
                        self.attr = []
                        return 1
                    else:
                        if (self.attr.count(4) >= 3 and fake == 2) or (self.attr.count(5) >= 3 and fake == 3):
                            print("盗取成功")
                            self.attr = []
                            return 1
                        else:
                            print("盗取条件不足，盗取失败")
                            self.attr = []
                            return 0
                if a == 2:
                    print("盗取失败")
                    self.attr = []
                    return 0
                if a != 1 and a != 2:
                    print("输入错误，请重新输入")

def shuffle_card(x):
    if x == 1 or x == 0:
        for i in range(0, 3):
            detective_card.append('侦探')
        for i in range(0, 6):
            detective_card.append('刑警')
            detective_card.append('记者')
        detective_card.append('侦探&刑警')
        detective_card.append('记者&刑警')
        detective_card.append('侦探&记者')
    if x == 2 or x == 0:
        for i in range(0, 5):
            neutrality_card.append('富豪')
        for i in range(0, 6):
            neutrality_card.append('千金')
        neutrality_card.append('千金&怪盗')
        neutrality_card.append('侦探&富豪')
        neutrality_card.append('富豪&美女')
        neutrality_card.append('千金&富豪')
    if x == 3 or x == 0:
        for i in range(0, 4):
            burglar_card.append('怪盗')
        for i in range(0, 6):
            burglar_card.append('同伙')
            burglar_card.append('美女')
        burglar_card.append('同伙&怪盗')
        burglar_card.append('同伙&美女')

def game_treasure():
    print("怪盗请闭眼")
    while True:
        treasure = int(input("探请选择存放秘宝的箱子\n左侧箱子(1)；珍贵箱子(2)；右侧箱子(3)"))
        if treasure == 1 or treasure == 2 or treasure == 3:
            for i in range(0, 50):
                print("物理清屏")
            print("秘宝已存放完毕")
            return treasure
        else:
            print("输入错误，请重新输入")

def code_treasure():
    print("怪盗请闭眼")
    a = [7, 8, 9]
    b = []
    x = True
    while x:
        if len(a) > 0:
            num = random.randint(0, len(a) - 1)
            b.append(a[num])
            del a[num]
        else:
            x = False
    print(b)
    print([1, 2, 3])
    print("请记住7,8,9与1,2,3的对应关系，稍后输入1,2,3对应的数字，5s后将清屏")
    time.sleep(5)
    for i in range(0, 50):
        print("物理清屏")
    while True:
        code = int(input("探请选择存放秘宝的箱子\n左侧箱子(1)；珍贵箱子(2)；右侧箱子(3)"))
        if code == 7 or code == 8 or code == 9:
            if code == b[0]:
                return 1
            if code == b[1]:
                return 2
            if code == b[2]:
                return 3
        else:
            print("输入错误，请重新输入")


def game_fake():
    print("侦探请闭眼，怪盗请睁眼")
    while True:
        fake = int(input("请选择你要假扮的角色\n刑警(2)；记者(3)；同伙(4)；美女(5)；富豪(6)；千金(7)"))
        if fake == 7 or fake == 2 or fake == 3 or fake == 4 or fake == 5 or fake == 6:
            for i in range(0, 50):
                print("物理清屏")
            print("怪盗已变装完毕")
            return fake
        else:
            print("输入错误，请重新输入")

def code_fake():
    print("侦探请闭眼，怪盗请睁眼")
    print("选择你要扮演的角色，并记住对应数字\n刑警(2)；记者(3)；同伙(4)；美女(5)；富豪(6)；千金(7)")
    time.sleep(5)
    a = [11, 12, 13, 14, 15, 16]
    b = []
    x = True
    while x:
        if len(a) > 0:
            num = random.randint(0, len(a) - 1)
            b.append(a[num])
            del a[num]
        else:
            x = False
    print(b)
    print([2, 3, 4, 5, 6, 7])
    print("请记住11, 12, 13, 14, 15, 16与2, 3, 4, 5, 6, 7的对应关系，稍后输入2, 3, 4, 5, 6, 7对应的数字，7s后将清屏")
    time.sleep(10)
    for i in range(0, 50):
        print("物理清屏")
    while True:
        code = int(input("请选择你要假扮的角色\n刑警(2)；记者(3)；同伙(4)；美女(5)；富豪(6)；千金(7)"))
        if code == 11 or code == 12 or code == 13 or code == 14 or code == 15 or code == 16:
            if code == b[0]:
                return 2
            if code == b[1]:
                return 3
            if code == b[2]:
                return 4
            if code == b[3]:
                return 5
            if code == b[4]:
                return 6
            if code == b[5]:
                return 7
        else:
            print("输入错误，请重新输入")
def game_key():
    time.sleep(0.5)
    print("正在随机摆放钥匙位置")
    key = random.randint(4, 6)
    time.sleep(2)
    print("钥匙已摆放完成")
    return key

# 回合流程
def game_round(fake, key, treasure):
    if check_card() == 0:
        return -1
    else:
        print("开始抽卡")
        card_now = get_card()
        last_position = put_card(card_now)
        game_text()
        result = check_account(last_position, fake, key)
        if result == 1:
            print("怪盗盗取了", number[last_position])
            bag.append(last_position)
            bag2.append(last_position)
            getting = game_bag(key)
            if getting == treasure:
                return 1
            if getting != 0 and getting != treasure:
                print("箱子里没有秘宝")
        print("回合结束")
        return 0

# 检查是否有两堆卡组用完
def check_card():
    check = [len(detective_card), len(neutrality_card), len(burglar_card)]
    if check.count(0) >= 2:
        return 0
    return 1

# 抽卡
def get_card():
    x = False
    while not x:
        a = int(input("请选择你要抽卡的牌堆\n侦探牌(1)；中立牌(2)；怪盗牌(3)"))
        if a == 1:
            if len(detective_card) > 0:
                num = random.randint(0, len(detective_card)-1)
                card_now = detective_card[num]
                del detective_card[num]
                x = True
            else:
                print("牌堆为空，请重新输入")
        if a == 2:
            if len(neutrality_card) > 0:
                num = random.randint(0, len(neutrality_card)-1)
                card_now = neutrality_card[num]
                del neutrality_card[num]
                x = True
            else:
                print("牌堆为空，请重新输入")
        if a == 3:
            if len(burglar_card) > 0:
                num = random.randint(0, len(burglar_card)-1)
                card_now = burglar_card[num]
                del burglar_card[num]
                x = True
            else:
                print("牌堆为空，请重新输入")
        if a != 1 and a != 2 and a != 3 :
            print("输入错误，请重新输入")
    print("你抽到的是", card_now)
    return card_now

# 放卡
def put_card(card_now):
    while True:
        a = int(input("请选择你要放置的位置\n左侧宝箱(1)；珍贵宝箱(2)；右侧宝箱(3)\n左侧钥匙(4)；中间钥匙(5)；右侧钥匙(6)"))
        if a == 1:
            if bag2.count(1) == 1:
                print("该位置不可放置")
            else:
                chest_l.append(card_now)
                return 1
        if a == 2:
            if bag2.count(2) == 1:
                print("该位置不可放置")
            else:
                chest_precious.append(card_now)
                return 2
        if a == 3:
            if bag2.count(3) == 1:
                print("该位置不可放置")
            else:
                chest_r.append(card_now)
                return 3
        if a == 4:
            if bag2.count(4) == 1:
                print("该位置不可放置")
            else:
                key_l.append(card_now)
                return 4
        if a == 5:
            if bag2.count(5) == 1:
                print("该位置不可放置")
            else:
                key_m.append(card_now)
                return 5
        if a == 6:
            if bag2.count(6) == 1:
                print("该位置不可放置")
            else:
                key_r.append(card_now)
                return 6
        if a != 1 and a != 2 and a != 3 and a != 4 and a != 5 and a != 6:
            print("输入错误，请重新输入")

def check_account(last_position, fake, key):
    if last_position == 1:
        if len(chest_l) == 5:
            result = c.check_attr(chest_l, 0, fake)
            while len(chest_l) > 0:
                del chest_l[0]
            return result
    if last_position == 2:
        if len(chest_precious) == 5:
            result = c.check_attr(chest_precious, 8, fake)
            while len(chest_precious) > 0:
                del chest_precious[0]
            return result
    if last_position == 3:
        if len(chest_r) == 5:
            result = c.check_attr(chest_r, 0, fake)
            while len(chest_r) > 0:
                del chest_r[0]
            return result
    if last_position == 4:
        if len(key_l) == 5:
            if last_position == key:
                print("该钥匙是珍贵钥匙")
                result = c.check_attr(key_l, 1, fake)
                while len(key_l) > 0:
                    del key_l[0]
                return result
            else:
                print("该钥匙是普通钥匙")
                result = c.check_attr(key_l, 0, fake)
                while len(key_l) > 0:
                    del key_l[0]
                return result
    if last_position == 5:
        if len(key_m) == 5:
            if last_position == key:
                print("该钥匙是珍贵钥匙")
                result = c.check_attr(key_m, 1, fake)
                while len(key_m) > 0:
                    del key_m[0]
                return result
            else:
                print("该钥匙是普通钥匙")
                result = c.check_attr(key_m, 0, fake)
                while len(key_m) > 0:
                    del key_m[0]
                return result
    if last_position == 6:
        if len(key_r) == 5:
            if last_position == key:
                print("该钥匙是珍贵钥匙")
                result = c.check_attr(key_r, 1, fake)
                while len(key_r) > 0:
                    del key_r[0]
                return result
            else:
                print("该钥匙是普通钥匙")
                result = c.check_attr(key_r, 0, fake)
                while len(key_r) > 0:
                    del key_r[0]
                return result

#检验是否能开箱子
def game_bag(key):
    if bag.count(2) == 1 and bag.count(key) == 1:
        print("怪盗打开了珍贵宝箱")
        bag.remove(2)
        bag.remove(key)
        return 2
    if bag.count(1) == 1:
        if bag.count(4) == 1 or bag.count(5) == 1 or bag.count(6) == 1:
            _max = [bag.count(4), bag.count(5), bag.count(6)]
            if (_max.count(1) == 1 and bag.count(key) == 0) or _max.count(1) > 1:
                print("怪盗拥有左侧宝箱和普通钥匙")
                select = game_box()
                if select == 1:
                    if bag.count(4) == 1 and key != 4:
                        print("怪盗打开了普通宝箱")
                        bag.remove(1)
                        bag.remove(4)
                        return 1
                    if bag.count(5) == 1 and key != 5:
                        print("怪盗打开了普通宝箱")
                        bag.remove(1)
                        bag.remove(5)
                        return 1
                    if bag.count(6) == 1 and key != 6:
                        print("怪盗打开了普通宝箱")
                        bag.remove(1)
                        bag.remove(6)
                        return 1
    if bag.count(3) == 1:
        if bag.count(4) == 1 or bag.count(5) == 1 or bag.count(6) == 1:
            _max = [bag.count(4), bag.count(5), bag.count(6)]
            if (_max.count(1) == 1 and bag.count(key) == 0) or _max.count(1) > 1:
                print("怪盗拥有右侧宝箱和普通钥匙")
                select = game_box()
                if select == 1:
                    if bag.count(4) == 1 and key != 4:
                        print("怪盗打开了普通宝箱")
                        bag.remove(3)
                        bag.remove(4)
                        return 3
                    if bag.count(5) == 1 and key != 5:
                        print("怪盗打开了普通宝箱")
                        bag.remove(3)
                        bag.remove(5)
                        return 3
                    if bag.count(6) == 1 and key != 6:
                        print("怪盗打开了普通宝箱")
                        bag.remove(3)
                        bag.remove(6)
                        return 3
    return 0

#是否打开箱子
def game_box():
    while True:
        a = int(input("是否打开该宝箱\n是(1)否(2)"))
        if a == 1:
            return 1
        if a == 2:
            return 2
        if a != 1 and a != 2:
            print("输入错误，请重新输入")

#指认环节
def game_detective(fake):
    while True:
        answer = int(input("怪盗变装的角色是\n刑警(2)；记者(3)；同伙(4)；美女(5)；富豪(6)；千金(7)"))
        if answer != 2 and answer != 3 and answer != 4 and answer != 5 and answer != 6 and answer != 7:
            print("输入错误，请重新输入")
        if answer == fake:
            return 1
        else:
            return -1
#信息显示
def game_text():
    print("---------------------------------------------")
    print("当前桌面状态：")
    print("侦探卡还有", len(detective_card), "张", "中立卡还有", len(neutrality_card), "张", "怪盗卡还有", len(burglar_card), "张")
    if bag2.count(1) == 0:
        print("左侧宝箱", chest_l)
    if bag2.count(2) == 0:
        print("珍贵宝箱", chest_precious)
    if bag2.count(3) == 0:
        print("右侧宝箱", chest_r)
    if bag2.count(4) == 0:
        print("左侧钥匙", key_l)
    if bag2.count(5) == 0:
        print("中间钥匙", key_m)
    if bag2.count(6) == 0:
        print("右侧钥匙", key_r)
    print("---------------------------------------------")
def game_main():
    shuffle_card(0)
    x = True
    while x:
        a = int(input("网络对战对手扮演角色\n侦探(1)；怪盗(2)；不需要(3)"))
        if a != 1 and a != 2 and a != 3:
            print("输入错误请重新输入")
        else:
            x = False
    if a == 2:
        treasure = game_treasure()
        fake = code_fake()
        print("怪盗已变装完毕")
    if a == 1:
        treasure = code_treasure()
        print("秘宝已存放完毕")
        fake = game_fake()
    if a == 3:
        treasure = game_treasure()
        fake = game_fake()
    key = game_key()
    while not x:
        result = game_round(fake, key, treasure)
        if result == -1:
            print("已有两个牌堆被抽光，侦探胜利")
            x = True
        if result == 1:
            print("怪盗成功盗取了秘宝\n进入侦探指认环节")
            detective = game_detective(fake)
            if detective == 1:
                print("指认成功，侦探胜利")
            else:
                print("指认失败，怪盗胜利")
            x = True
    print("游戏结束，欢迎下次来玩")
    input("任意键退出")
c = Check()
game_main()
