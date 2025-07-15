def Main():
    res = ''
    proposiciones = ["Hay máquinas expendedoras en casi cada esquina", "Yen como moneda oficial", "Señales en japonés", "Tiene arquitectura japonesa", "Se quitan los zapatos al entrar a un lugar"]

    print('Proposiciones:'
          '\nHay máquinas expendedoras en casi cada esquina (P1)'
          '\nYen como moneda oficial (P2)'
          '\nSeñales en japonés (P3)'
          '\nTiene arquitectura japonesa (P4)'
          '\nSe quitan los zapatos al entrar a un lugar (P5)')

    # para guardar los verdaderos y los falsos
    Proposion_1 = []
    Proposion_2 = []
    Proposion_3 = []
    Proposion_4 = []
    Proposion_5 = []
    for i in range(32):
        Proposion_1.append(i < 16)
        Proposion_2.append(((i // 8) % 2) == 0)
        Proposion_3.append(((i // 4) % 2) == 0)
        Proposion_4.append(((i // 2) % 2) == 0)
        Proposion_5.append((i % 2) == 0)

    print(f'{'P1'}    -  {'P2'}    -  {'P3'}    -  {'P4'}    -  {'P5'}    -  {'¿Es Japón?'}')

    for i in range(32):
        p1, p2, p3, p4, p5 = Proposion_1[i], Proposion_2[i], Proposion_3[i], Proposion_4[i], Proposion_5[i]

        respuesta = ((p1 and p3) or (p2 and p4)) and (p3 and (p5 or p4))
        print(f'{str(p1)}  -  {str(p2)}  -  {str(p3)}  -  {str(p4)}  -  {str(p5)}  -  {str(respuesta)}')

Main()
