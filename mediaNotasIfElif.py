while True:
    nome_aluno = input('Digite o nome do aluno[para sair digite 0]: ')
    if nome_aluno == 0:
        break
    
    else: 
        nota_01 = int(input('Digite a primeira nota: '))
        nota_02 = int(input('Digite a segunda nota: '))
        nota_03 = int(input('Digite a terceira nota: '))
        nota_04 = int(input('Digite a quarta nota: '))

        media_notas = (nota_01 + nota_02 + nota_03 + nota_04) / 4

        if media_notas == 10:
            print('Parabéns! Você bota para f@@@')
        elif media_notas > 10 or media_notas < 0:
            print('Nota inválida')
        elif media_notas >= 7:
            print('Passou de ano')
        elif media_notas < 7 and media_notas > 4:
            print('Está na recuperação')
        elif media_notas <= 4:
            print('Perdeu de ano seu infeliz')





