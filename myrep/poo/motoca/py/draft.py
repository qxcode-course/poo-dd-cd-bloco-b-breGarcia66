from person import Person;
from motocycle import MotoCycle;

def main():
        
    motoca: MotoCycle = MotoCycle();

    while True:

        line: str = input();
        args: list[str] = line.split(' ');
        print(f'${line}');

        match args[0]:
            case 'show':
                print(motoca);

            case 'init':
                motoca = MotoCycle(power = int(args[1]));

            case 'enter':
                pessoa: Person = Person(name = args[1], age = int(args[2]));
                motoca.inserir(pessoa);
            
            case 'leave':
                oldPessoa = motoca.remover();
                if oldPessoa is not None:
                    print(oldPessoa);
            
            case 'buy':
                motoca.buyTime(int(args[1]));
            
            case 'drive':
                motoca.drive(int(args[1]));

            case 'honk':
                motoca.honk();

            case 'end':
                break;

            case _:
                print('fail: comando inválido');

main();


# motocaTeste = MotoCycle();
# pessoaTeste = Person('Jurandi', 5);

# retortno = motocaTeste.inserir(pessoaTeste);
# print(retortno);
