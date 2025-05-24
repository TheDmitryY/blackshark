import subprocess

startupinfo = subprocess.STARTUPINFO()

subprocess.Popen(
    ["python3.exe", "main.py"],  # pythonw.exe не создаёт консоль
    creationflags=subprocess.SW_HIDE,
    startupinfo=startupinfo,
    shell=True
)