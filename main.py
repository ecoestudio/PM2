from src.menu import main as text_main
import subprocess
import runpy
import sys

print("歡迎使用ECOE Playone助手研究交流版。")
print("警語：此程式僅限用於研究、測試用途")
print("警語：使用者請自行評估使用風險，此程式可能違反官方的服務契約: https://www.goplayone.com/legal/termsofService")
print("警語：ECOE工作室不負擔與此程式、Playone相關的任何法律責任，使用者自行承擔一切後果")
print("- 抽蛋間隔建議不要超過一般手動太多")
print("- 不要多開，不要多重登入")
print("- 不要頻繁登入")
print("官方不吃素的，吃緊會弄破碗\n")
mode = input("選擇模式: 1.文字模式 2.GUI模式: ")
if mode=='1':
    text_main()
else:
    #subprocess.run([f"{sys.executable}", "-m", "streamlit", "run", "src/ui.py"])
    sys.argv = ["streamlit", "run",  "ui.py"]
    runpy.run_module("streamlit", run_name="__main__")