from src.menu import main as text_main
import subprocess
import runpy
import sys

print("歡迎使用ECOE Playone助手。")
print("警語：使用風險由使用者自行承擔，ECOE工作室不負擔任何責任")
print("- 抽蛋間隔建議不要超過一般手動太多")
print("- 不要多開")
print("- 不要頻繁登入")
print("官方不吃素的，吃緊會弄破碗\n")
mode = input("選擇模式: 1.文字模式 2.GUI模式: ")
if mode=='1':
    text_main()
else:
    #subprocess.run([f"{sys.executable}", "-m", "streamlit", "run", "src/ui.py"])
    sys.argv = ["streamlit", "run",  "ui.py"]
    runpy.run_module("streamlit", run_name="__main__")