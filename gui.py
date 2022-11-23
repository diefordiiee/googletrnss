from pathlib import Path
from googletrans import Translator
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, WORD, font


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\pjoject\new gui\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#FFFFFF")
window.title("Translate 3 Bahasa")

font_tuple = ("Gaegu", 16)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1000.0,
    600.0,
    fill="#FFF8EA",
    outline="")

entry_image_out = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_out = canvas.create_image(
    740.0,
    266.0,
    image=entry_image_out
)
entry_out = Text(window,
    bd=0,
    bg="#FFF8EA",
    fg="#000716",
    highlightthickness=0,
    wrap= WORD,
    pady=10,
    padx=10,
    font= font_tuple

)
entry_out.place(
    x=524.0,
    y=154.0,
    width=432.0,
    height=222.0
)



entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    259.0,
    353.0,
    image=entry_image_2
)
entry_2 = Text(window,
    bd=0,
    bg="#FFF8EA",
    fg="#000716",
    highlightthickness=0,
    pady=10,
    padx=10,
    font= font_tuple
)
entry_2.place(
    x=43.0,
    y=154.0,
    width=432.0,
    height=396.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    740.0,
    477.0,
    image=entry_image_3
)
entry_3 = Text(window,
    bd=0,
    bg="#FFF8EA",
    fg="#000716",
    highlightthickness=0,
    pady=10,
    padx=10,
    font= font_tuple

)
entry_3.place(
    x=524.0,
    y=402.0,
    width=432.0,
    height=148.0,

)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    264.0,
    93.0,
    image=image_image_1
)




button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=15.0,
    y=10.0,
    width=47.0,
    height=41.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button2clikked"),
    relief="flat"
)
button_2.place(
    x=62.0,
    y=10.0,
    width=47.0,
    height=41.0
)
def translate_to_kor():
    translator = Translator()
    text_input = entry_2.get("1.0",'end-1c')
    translation = translator.translate(text_input, dest="ko")
    entry_out.config(state='normal')
    entry_out.delete('1.0', 'end-1c')
    entry_out.insert('1.0', translation.text)
    entry_out.config(state='disabled')
    entry_3.config(state='normal')
    entry_3.delete('1.0', 'end-1c')
    entry_3.insert('1.0', translation.pronunciation)
    entry_3.config(state='disabled')

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: translate_to_kor(),
    relief="flat"
)
button_3.place(
    x=490.0,
    y=67.0,
    width=164.0,
    height=49.0
)

def translate_to_jpn():
    translator = Translator()
    text_input = entry_2.get("1.0",'end-1c')
    translation = translator.translate(text_input, dest="ja")
    entry_out.config(state='normal')
    entry_out.delete('1.0', 'end-1c')
    entry_out.insert('1.0', translation.text)
    entry_out.config(state='disabled')
    entry_3.config(state='normal')
    entry_3.delete('1.0', 'end-1c')
    entry_3.insert('1.0', translation.pronunciation)
    entry_3.config(state='disabled')

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: translate_to_jpn(),
    relief="flat"
)
button_4.place(
    x=662.0,
    y=67.0,
    width=164.0,
    height=49.0
)

def translate_to_eng():
    translator = Translator()
    text_input = entry_2.get("1.0",'end-1c')
    translation = translator.translate(text_input, dest="en")
    entry_out.config(state='normal')
    entry_out.delete('1.0', 'end-1c')
    entry_out.insert('1.0', translation.text)
    entry_out.config(state='disabled')
    entry_3.config(state= 'normal')
    entry_3.delete('1.0', 'end-1c')
    entry_3.config(state= 'disabled')

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: translate_to_eng(),
    relief="flat"
)
button_5.place(
    x=826.0,
    y=67.0,
    width=164.0,
    height=49.0
)
window.resizable(False, False)
window.mainloop()
