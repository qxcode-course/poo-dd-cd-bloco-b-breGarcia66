from pessoa import Pessoa;
from motoUber import MotoUber;

# criando método main

def main():
    moto: MotoUber = MotoUber();
    motorista: Pessoa = None;
    passageiro: Pessoa = None;

    while True:

        line: str = input();
        args: list[str] = line.split(' ');
        print(f'${line}');

        match args[0]:
            case 'show':
                print(moto);
            
            case 'setDriver':
                motorista = Pessoa(args[1], int(args[2]));
                moto.setMotorista(motorista);

            case 'setPass':
                passageiro = Pessoa(args[1], int(args[2]));
                moto.setPassageiro(passageiro);

            case 'leavePass':
                oldPassageiro = moto.descerPassageiro();
                print(f'{oldPassageiro} left');

            case 'drive':
                moto.corrida(int(args[1]));

            case 'end':
                break;

            case _:
                print('fail: comando invalido');

main();