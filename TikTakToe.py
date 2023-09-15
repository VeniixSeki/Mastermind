import PySimpleGUI as sg

#hacerlo bonito, boton de reinicio de partida

def initialize_game():
    button_size = (7, 4)
    layout = [[
                sg.Button("", key="-0-", size=button_size), 
                sg.Button("", key="-1-", size=button_size), 
                sg.Button("", key="-2-", size=button_size)],
            [
                sg.Button("", key="-3-", size=button_size), 
                sg.Button("", key="-4-", size=button_size), 
                sg.Button("", key="-5-", size=button_size)],
            [
                sg.Button("", key="-6-", size=button_size), 
                sg.Button("", key="-7-", size=button_size), 
                sg.Button("", key="-8-", size=button_size)
                ],
                [sg.Text("", key="-WINNER-")],
                [sg.Button("Cerrar", key="-OK-"), sg.Button("Reiniciar", key="-RESTART-")]]

    window = sg.Window("Demo", layout)
    return window

def actual_player(player):
    current_player = player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return current_player

def win_condition(deck, window):
    winner_plays = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                    [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                    [0, 4, 8], [2, 4, 6]]

    for winner_play in winner_plays:
        if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
            if deck[winner_play[0]] == "X":
                window.Element(key="-WINNER-").Update("El jugador 1 es el ganador")
            else:
                window.Element(key="-WINNER-").Update("El jugador 2 es el ganador")
            game_end = True
            return game_end
        
        if 0 not in deck:
            window.Element(key="-WINNER-").Update("Empate")
            game_end = True
            return game_end

def deck_changes(event, deck, current_player):
    index = int(event.replace("-", ""))
    deck[index] = current_player
    return deck

def main():
    initial_deck = [0, 0, 0,
                    0, 0, 0,
                    0, 0, 0]
    
    deck = initial_deck

    current_player = "X"

    window = initialize_game()

    game_end = False

    while True:
        event, values = window.read()

        if event == "-RESTART-":
            deck = initial_deck
            for a in range(0, 9):
                window.Element(key="-{}-".format(a)).Update(text="")

            window.Element(key="-WINNER-").Update("")
            game_end = False
            
        if event == sg.WIN_CLOSED or event == "-OK-":
            break

        if window.Element(event).ButtonText == "" and not game_end:

            deck = deck_changes(event, deck, current_player)

            window.Element(event).Update(text=current_player)

            game_end = win_condition(deck, window)
            
            current_player = actual_player(current_player)
            
        
    window.close()

if __name__=="__main__":
    main()