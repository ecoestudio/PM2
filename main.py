import threading
from src.global_var import personalization
from src.subscription_check import check_subscription
from src.gift_box import check_giftbox
from src.websocket_monitor import WS_Monitor, Recorder
from src.egg_smash import smash_egg
from src.login import login
import time

port = 9091
user_token = None
user_id = None
refresh_time = 300
egg_smash_time_space = 0.1

def menu_input():
    def print_menu():
        print()
        print("===== 歡迎使用ECOE Playone監測系統 =====")
        print("請選擇以下功能：")
        print("  1. 查看背包")
        print("  2. 監視砸蛋")
        print("  3. 重置系統")
        print("  4. 設定監視RefreshToken秒數")
        print("  5. 更新Token")
        print("  6. 連續砸蛋")
        print("  7. 設定砸蛋秒數")

    user_input = None
    while not user_input in [str(i) for i in range(1,8)]:
        print_menu()
        user_input = input("請輸入功能編號: ")
    print()
    return user_input

if not check_subscription(personalization):
    print("授權失敗，請索取金鑰")
    time.sleep(3)
    exit()
else:
    # Create and start the listener thread
    while True:
        if not user_token or not user_id:
            user_id, user_token = login()
            print("登入成功")
        if user_id and user_token:
            user_input = menu_input()
            if str(user_input.strip()) == "1":
                check_giftbox(user_token, user_id)
            elif str(user_input.strip()) == "2":  
                recoder = Recorder()
                print("開始監控")
                try:
                    ws_monitor = WS_Monitor(user_token, user_id, refresh_time)
                    ws_monitor(recoder)
                except:
                    print("失去連線")
            elif str(user_input.strip()) == "3":
                recoder = Recorder()
            elif str(user_input.strip()) == "4":
                refresh_time = int(input("輸入秒數(預設300): "))
            elif str(user_input.strip()) == "5":
                user_token = input("輸入UserToken:\n")
            elif str(user_input.strip()) == "6":
                egg_type = input("輸入砸蛋種類(30,90,199): ")
                egg_num = int(input("輸入砸蛋數量: "))
                smash_egg(user_token, user_id, egg_type, egg_num, egg_smash_time_space)
            elif str(user_input.strip()) == "7":
                egg_smash_time_space = input("輸入砸蛋間格秒數(預設0.1): ")
        
