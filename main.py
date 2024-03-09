from src.menu import main as text_main
import subprocess
import sys

mode = input("選擇模式: 1.文字模式 2.GUI模式: ")
if mode=='1':
    text_main()
else:
    subprocess.run([f"{sys.executable}", "-m", "streamlit", "run", "src/ui.py"])