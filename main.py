import threading
from src.global_var import personalization
from src.subscription_check import check_subscription
from src.gift_box import check_giftbox
from src.websocket_monitor import WS_Monitor, Recorder
import time

port = 9091
user_token = None
user_id = None
refresh_time = 300

if not check_subscription(personalization):
    print("授權失敗，請索取金鑰")
    time.sleep(3)
    exit()
else:
    # Create and start the listener thread
    recoder = Recorder()
    while True:
        if not user_token:
            user_token = input("請輸入User-Token (F12搜尋user-token:，通常是eyJhbGciOiJIUzI之類的):\n")
        if not user_id:
            user_id = input("請輸入User-Token (F12搜尋user-id:，通常是GM18Q7240lW之類的):\n")
        if user_id and user_token:
            user_input = input("請輸入功能: (1)查看背包 (2)監視砸蛋 (3)Reset (4)設定連線秒數 (5)更新token: ")
            if str(user_input.strip()) == "1":
                check_giftbox(user_token, user_id)
            elif str(user_input.strip()) == "2":  
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
        
        
