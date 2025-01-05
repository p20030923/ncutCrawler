import socket
import json
import tkinter as tk
from tkinter import messagebox

def submit() -> None:
    """確認按鈕按下後觸發"""
    # 獲取Email和選擇的選項
    email = email_entry.get()
    selected_options = [var.get() for var in options_vars if var.get()]

    # 驗證Email是否輸入
    if not email:
        messagebox.showwarning("輸入錯誤", "請輸入email")
        return

    # 驗證是否至少選擇一個選項
    if not selected_options:
        messagebox.showwarning("輸入錯誤", "請至少選擇一個選項")
        return

    # 設定伺服器地址
    HOST = '103.173.179.178'
    PORT = 12345

    # 創建 Socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # 傳送資料
    message = []
    message.append(email)
    for i in selected_options:
        message.append(i)
    data = json.dumps(message)  # 將列表序列化為 JSON 字符串
    client_socket.sendall(data.encode('utf-8'))  # 傳送序列化後的資料

    # 接收回應
    response = client_socket.recv(1024).decode('utf-8')
    print(f"伺服器回應: {response}")

    client_socket.close()

    # 顯示提交結果
    messagebox.showinfo("提交結果", f"Email: {email}\n訂閱項目: {', '.join(selected_options)}")
    messagebox.showinfo("上傳結果", f"{response}")

# 創建主視窗
root = tk.Tk()
root.title("校網公告自動通知系統")
root.geometry("500x550")

# 設置行列權重
root.columnconfigure(1, weight=1)  # 讓輸入框可水平拉伸
root.rowconfigure(1, weight=1)  # 讓scrollbar可垂直拉伸

# Email標籤與輸入框
email_label = tk.Label(root, text="Email:", font=("Arial", 12))
email_label.grid(row=0, column=0, padx=10, pady=10)

email_entry = tk.Entry(root, width=50, font=("Arial", 12))
email_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# 可滾動的選項框架
options_frame = tk.Frame(root)
options_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")  # sticky 確保選項框架可以拉伸

# 調整選項框架行列權重
options_frame.columnconfigure(0, weight=1)
options_frame.rowconfigure(0, weight=1)

# 建立Canvas與滾動條
canvas = tk.Canvas(options_frame, width=350, height=500)
scrollbar = tk.Scrollbar(options_frame, orient="vertical", command=canvas.yview)

# 綁定Canvas的大小變化
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

scrollable_frame = tk.Frame(canvas)

# 綁定滾動區域的更新
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# 選項列表
options = [
    "勤益科大", "基礎通識", "博雅通識", "教務處", "學務處", "總務處",
    "研究發展處", "國際事務處", "圖書館", "體育室", "藝術中心",
    "資工系", "電機系", "電子系", "人工智慧系"
]

# 創建選項的複選按鈕
options_vars = []
for option in options:
    var = tk.StringVar()
    chk = tk.Checkbutton(scrollable_frame, text=option, variable=var, onvalue=option, offvalue="", font=("Arial", 12))
    chk.pack(anchor="w")
    options_vars.append(var)

# 確認按鈕
submit_button = tk.Button(root, text="確認", command=submit, font=("Arial", 12))
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()