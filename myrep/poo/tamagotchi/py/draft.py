from tamagochi import Tamagochi;
from game import Game;

# desenvolvendo método main();

def main():
    game: Game = Game();

    while True:
        line: str = input();
        args: list[str] = line.split(' ');
        print(f'${line}');

        match args[0]:
            case 'init':
                bixo: Tamagochi = Tamagochi(int(args[1]), int(args[2]));
                game.setBixo(bixo);
            
            case 'show':
                print(game);

            case 'play':
                game.play();

            case 'sleep':
                game.sleep();
            
            case 'shower':
                game.shower();

            case 'end':
                break;

            case _:
                print('fail: comando invalido');

main();