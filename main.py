from player import Player
import utils

if __name__ == '__main__':
        print("Предлагаю сегодня поиграть ещё в одну игру!\nДля начала введите ваше имя")
        player_name = Player(input())
        print(f"Здравствуйте, {player_name}!")
        game_ = utils.load_random_word()
        print(f"Составьте {game_.subwords_count()} слов из слова {game_}")
        print("Слова должны быть не короче 3 букв")
        print("Чтобы закончить игру, угадайте все слова или напишите 'stop'")
        print("Поехали, ваше первое слово?")
        for i in range(game_.subwords_count()):
            user_answer = input()
            user_check = game_.check_subword(user_answer)
            if player_name.has_used(user_answer) is True:
                print("Это слово уже было")
                pass
            elif user_check is True:
                print ("Верно, идём дальше!")
                player_name.correct_subwords(user_answer)
            elif user_answer == "stop":
                print("Игра закончена")
                break
            elif user_answer == "стоп":
                print("Игра закончена")
                break
            else:
                print("Ответ неверный")
        print("Слова закончились, игра завершена!")
        print(f"Вы угадали {player_name.lenght_of_used_list()}")