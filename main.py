from src.menu import main as text_main
import subprocess
import runpy
import sys

print("重要: 因應近期相關司法案件判決。本助手即日起停止更新")
print("重要: 使用者應立即停止使用本程式")
print("警語：此程式僅限用於研究、測試用途")
print("警語：使用者請自行評估使用風險，此程式可能違反官方的服務契約: https://www.goplayone.com/legal/termsofService")
print("警語：ECOE工作室不負擔與此程式、Playone相關的任何法律責任，使用者自行承擔一切後果")
mode = input("選擇模式: 1.文字模式 2.GUI模式: ")
if mode=='1':
    text_main()
else:
    #subprocess.run([f"{sys.executable}", "-m", "streamlit", "run", "src/ui.py"])
    sys.argv = ["streamlit", "run",  "ui.py"]
    runpy.run_module("streamlit", run_name="__main__")