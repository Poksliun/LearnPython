class Game:
    def play(self):
        p1_score = 0
        p2_score = 0

        for i in range(3):
            print(f"\nраунд {i + 1}")
            p1 = input("игрок 1 (к/н/б): ")
            print("\n" * 50)
            p2 = input("игрок 2 (к/нб): ")

            if p1 == p2:
                print("ничья")
            elif (p1 == "к" and p2 == "н") or \
                    (p1 == "н" and p2 == "б") or \
                    (p1 == "б" and p2 == "к"):
                print("игрок 1 выиграл раунд")
                p1_score += 1
            else:
                print("игрок 2 выиграл раунд")
                p2_score += 1

        print(f"\nсчет: игрок1 {p1_score} - {p2_score} игрок2")
        if p1_score > p2_score:
            print("игрок 1 победил!")
        elif p2_score > p1_score:
            print("игрок 2 победил!")
        else:
            print("ничья!")


game = Game()
game.play()
