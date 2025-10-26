from lead import Lead;
from pencil import Pencil;

# criando método main

def main():
    pencil: Pencil = Pencil();

    while True:

        line: str = input();
        args: list[str] = line.split(' ');
        print(f'${line}');

        match args[0]:
            case 'init':
                pencil = Pencil(float(args[1]));
            
            case 'show':
                print(pencil);

            case 'insert':
                lead: Lead = Lead(float(args[1]), args[2], int(args[3]));
                pencil.insert(lead);

            case 'remove':
                pencil.remove();

            case 'write':
                pencil.writePage();

            case 'end':
                break;

            case _:
                print('fail: comando invalido');

# executando main()
main();