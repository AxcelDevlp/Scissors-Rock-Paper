def main():
    player_1 = (
        input("Player 1 (Choose 'R' for rock, 'P' for paper or 'S' for scissors): ")
        .capitalize()
        .strip()
    )

    player_2 = (
        input("Player 2 (Choose 'R' for rock, 'P' for paper or 'S' for scissors): ")
        .capitalize()
        .strip()
    )

    if player_1 == ("R") and player_2 == ("R"):
        print("TIE")

    elif player_1 == ("R") and player_2 == ("P"):
        print("Player 2 WINS!")

    elif player_1 == ("P") and player_2 == ("R"):
        print("Player 1 WINS!")

    elif player_1 == ("R") and player_2 == ("S"):
        print("Player 1 WINS!")

    elif player_1 == ("S") and player_2 == ("R"):
        print("Player 2 WINS!")

    elif player_1 == ("P") and player_2 == ("S"):
        print("Player 2 WINS!")

    elif player_1 == ("S") and player_2 == ("P"):
        print("Player 1 WINS!")


main()
