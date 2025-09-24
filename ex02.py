from tkinter import * # tkinter는 파이썬에서 GUI 관련 모듈을 제공하는 표준 윈도우 라이브러리임

window = Tk() # Tk()는 기본이 되는 윈도우를 반환하는데 이를 루트 윈도우 또는 베이스 윈도우라고 함

label1 = Label(window, text = "COOKBOKK~~Pytjonn을") # Label은 문잘를 표현하는 위젯
label2 = Label(window, text = "열심히", font = ("궁서체", 30),
               fg = "blue")
label3 = Label(window, text = "공부 중입니다.", bg = "magenta",
               width = 20, height = 5, anchor = SE)

label1.pack() # pack()은 위젯을 화면에 표시한다
label2.pack()
label3.pack()

window.mainloop()