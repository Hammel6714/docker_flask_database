#def DoSomeThing():
    import tkinter as tk

    window = tk.Tk()

    window.title('Hello World')

    # 設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為 (250, 150)
    window.geometry("300x100+250+150")

    window.mainloop()
