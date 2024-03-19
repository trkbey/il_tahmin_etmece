from turtle import *
from pandas import *
from states import *
from mesages import *
from progres import *
window = Screen()
window.setup(width=1600, height=800)
window.bgpic('4jturkiye-dilsiz-siyasi-haritasi_2.gif')
window.title('Türkiyenin illeri')
progres_bar = Progres()
guessed = 0
is_game_on = True
user_gues = textinput(f'{guessed}/81','Tahmin et').lower()
state_label = States()
mesage_label = Mesage()
data = read_csv("states.csv")
provinces = data.il.to_list()
guessed_states = []
while is_game_on:
    if guessed > 80:
        state_label.goto(-150,320)
        state_label.write("TEBRİKLER",font=('ariel', 40, 'bold'))
        is_game_on = False
    elif user_gues not in guessed_states:
        if user_gues in provinces:
            state_label.goto(int(data[data['il'] == user_gues]['X'].values[0]),int(data[data['il'] == user_gues]['Y'].values[0]))
            state_label.write(f"{user_gues.upper()}", font=('ariel', 12, 'bold'))
            guessed += 1
            mesage_label.clear()
            mesage_label.goto(-200,365)
            mesage_label.write(f"{user_gues.upper()} DOĞRU TAHMİN",font=('ariel', 25, 'bold'))
            guessed_states.append(user_gues)
            progres_bar.pen_move()
        else:
            mesage_label.clear()
            mesage_label.goto(-200, 365)
            mesage_label.write(f"{user_gues.upper()} ADINDA BIR IL YOK", font=('ariel', 25, 'bold'))
        user_gues = textinput(f'{guessed}/81','Tahmin et').lower()
    else:
        user_gues = textinput(f'{guessed}/81', 'Tahmin et').lower()
        mesage_label.clear()
        mesage_label.goto(-200, 365)
        mesage_label.write(f"{user_gues.upper()} DAHA ONCE TAHMIN EDILMIS", font=('ariel', 25, 'bold'))
window.mainloop()