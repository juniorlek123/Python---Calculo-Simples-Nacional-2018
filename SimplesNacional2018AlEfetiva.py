# CALCULO DE ALÍQUOTA SIMPLES NACIONAL 2018

from time import sleep
import os

n = 'S'
while n != 'N': # FAZ O LOOP ENQUANTO O A VARIAVEL "n" FOR DIFERENTE DE "N"
    print('-=-'*25)
    print('-=-'*5, 'CALCULO ALÍQUOTA EFETIVA SIMPLES NACIONAL 2018', '-=-'*4)
    print('-=-'*25)

    print('[ 1 ] - ANEXO --- I ' + '-'*55, '\n[ 2 ] - ANEXO -- II ' + '-'*55, '\n[ 3 ] - ANEXO - III ' + '-'*55, '\n[ 4 ] - ANEXO -- IV ' + '-'*55, '\n[ 5 ] - ANEXO --- V ' + '-'*55 )
    print('-=-'*25)    
    ANEXO = int(input('Escolha uma opção: '))
    while ANEXO > 5 or ANEXO == 0: # FAZ O LOOP ENQUANTO A VARIÁVEL "ANEXO" FOR MAIOR QUE "5"
        os.system('cls')
        print('-=-'*25)
        print('Este anexo não existe, tente novamente')
        print('-=-'*25)
        print('-=-'*25)
        print('-=-'*5, 'CALCULO ALÍQUOTA EFETIVA SIMPLES NACIONAL 2018', '-=-'*4)
        print('-=-'*25)

        print('[ 1 ] - ANEXO --- I ' + '-'*55, '\n[ 2 ] - ANEXO -- II ' + '-'*55, '\n[ 3 ] - ANEXO - III ' + '-'*55, '\n[ 4 ] - ANEXO -- IV ' + '-'*55, '\n[ 5 ] - ANEXO --- V ' + '-'*55 )
        print('-=-'*25)    
        ANEXO = int(input('Escolha uma opção: '))
        
    print('-=-'*25)

    if ANEXO < 6:
        RBTDOZE = float(input('Digite a receita bruta total dos ultimos 12 meses: '))
    print('-=-'*25)

    #PROCEDIMENTO CASO ESCOLHA O ANEXO I

    if ANEXO == 1:
        if RBTDOZE < 180000 or RBTDOZE == 180000:
            ALIQUOTA = ((RBTDOZE * 4 / 100) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 180000 and RBTDOZE < 360000 or RBTDOZE == 360000:
            ALIQUOTA = (((RBTDOZE * 7.3 / 100) - 5940) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 360000 and RBTDOZE < 720000 or RBTDOZE == 720000:
            ALIQUOTA = (((RBTDOZE * 9.5 / 100) - 13860) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 720000 and RBTDOZE < 1800000 or RBTDOZE == 1800000:
            ALIQUOTA = (((RBTDOZE * 10.7 / 100) - 22500) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 1800000 and RBTDOZE < 3600000 or RBTDOZE == 3600000:
            ALIQUOTA = (((RBTDOZE * 14.3 / 100) - 87300) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 3600000 and RBTDOZE < 4800000 or RBTDOZE == 4800000:
            ALIQUOTA = (((RBTDOZE * 19 / 100) - 378000) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))

    #PROCEDIMENTO CASO ESCOLHA O ANEXO II

    elif ANEXO == 2:
        if RBTDOZE < 180000 or RBTDOZE == 180000:
            ALIQUOTA = ((RBTDOZE * 4.5 / 100) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 180000 and RBTDOZE < 360000 or RBTDOZE == 360000:
            ALIQUOTA = (((RBTDOZE * 7.8 / 100) - 5940) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 360000 and RBTDOZE < 720000 or RBTDOZE == 720000:
            ALIQUOTA = (((RBTDOZE * 10 / 100) - 13860) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 720000 and RBTDOZE < 1800000 or RBTDOZE == 1800000:
            ALIQUOTA = (((RBTDOZE * 11.2 / 100) - 22500) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 1800000 and RBTDOZE < 3600000 or RBTDOZE == 3600000:
            ALIQUOTA = (((RBTDOZE * 14.7 / 100) - 85500) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 3600000 and RBTDOZE < 4800000 or RBTDOZE == 4800000:
            ALIQUOTA = (((RBTDOZE * 30 / 100) - 720000) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))

    #PROCEDIMENTO CASO ESCOLHA O ANEXO III

    elif ANEXO == 3:
        if RBTDOZE < 180000 or RBTDOZE == 180000:
            ALIQUOTA = ((RBTDOZE * 6 / 100) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 180000 and RBTDOZE < 360000 or RBTDOZE == 360000:
            ALIQUOTA = (((RBTDOZE * 11.2 / 100) - 9360) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 360000 and RBTDOZE < 720000 or RBTDOZE == 720000:
            ALIQUOTA = (((RBTDOZE * 13.5 / 100) - 17640) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 720000 and RBTDOZE < 1800000 or RBTDOZE == 1800000:
            ALIQUOTA = (((RBTDOZE * 16 / 100) - 35640) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 1800000 and RBTDOZE < 3600000 or RBTDOZE == 3600000:
            ALIQUOTA = (((RBTDOZE * 21 / 100) - 125640) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 3600000 and RBTDOZE < 4800000 or RBTDOZE == 4800000:
            ALIQUOTA = (((RBTDOZE * 33 / 100) - 648000) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
            
    #PROCEDIMENTO CASO ESCOLHA O ANEXO IV

    elif ANEXO == 4:
        if RBTDOZE < 180000 or RBTDOZE == 180000:
            ALIQUOTA = ((RBTDOZE * 4.5 / 100) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 180000 and RBTDOZE < 360000 or RBTDOZE == 360000:
            ALIQUOTA = (((RBTDOZE * 9 / 100) - 8100) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 360000 and RBTDOZE < 720000 or RBTDOZE == 720000:
            ALIQUOTA = (((RBTDOZE * 10.2 / 100) - 12420) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 720000 and RBTDOZE < 1800000 or RBTDOZE == 1800000:
            ALIQUOTA = (((RBTDOZE * 14 / 100) - 39780) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 1800000 and RBTDOZE < 3600000 or RBTDOZE == 3600000:
            ALIQUOTA = (((RBTDOZE * 22 / 100) - 183780) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 3600000 and RBTDOZE < 4800000 or RBTDOZE == 4800000:
            ALIQUOTA = (((RBTDOZE * 33 / 100) - 828000) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))

    #PROCEDIMENTO CASO ESCOLHA O ANEXO V

    elif ANEXO == 5:
        if RBTDOZE < 180000 or RBTDOZE == 180000:
            ALIQUOTA = ((RBTDOZE * 15.5 / 100) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 180000 and RBTDOZE < 360000 or RBTDOZE == 360000:
            ALIQUOTA = (((RBTDOZE * 18 / 100) - 4500) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 360000 and RBTDOZE < 720000 or RBTDOZE == 720000:
            ALIQUOTA = (((RBTDOZE * 19.5 / 100) - 9900) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 720000 and RBTDOZE < 1800000 or RBTDOZE == 1800000:
            ALIQUOTA = (((RBTDOZE * 20.5 / 100) - 17100) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 1800000 and RBTDOZE < 3600000 or RBTDOZE == 3600000:
            ALIQUOTA = (((RBTDOZE * 23 / 100) - 62100) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))
        elif RBTDOZE > 3600000 and RBTDOZE < 4800000 or RBTDOZE == 4800000:
            ALIQUOTA = (((RBTDOZE * 30.5 / 100) - 540000) / RBTDOZE) * 100
            print('A aliquota efetiva é {:.2f}%'.format(ALIQUOTA))

    # PERECENTUAIS DE REPARTIÇÃO DOS TRIBUTOS CASO ESCOLHA ANEXO I

    if ANEXO == 1:
        if  RBTDOZE < 180000 or RBTDOZE == 180000: # 1º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 5.5 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 12.74 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 2.76 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 41.5 / 100), '-'*55)
            print('ICMS: ------- {:.2f}%'.format(ALIQUOTA * 34 / 100), '-'*55)
        elif RBTDOZE > 180000 and RBTDOZE < 360000 or RBTDOZE == 360000: # 2º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 5.5 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 12.74 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 2.76 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 41.5 / 100), '-'*55)
            print('ICMS: ------- {:.2f}%'.format(ALIQUOTA * 34 / 100), '-'*55)
        elif RBTDOZE > 360000 and RBTDOZE < 720000 or RBTDOZE == 720000: # 3º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 5.5 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 12.74 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 2.76 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 42 / 100), '-'*55)
            print('ICMS: ------- {:.2f}%'.format(ALIQUOTA * 33.5 / 100), '-'*55)
        elif RBTDOZE > 720000 and RBTDOZE < 1800000 or RBTDOZE == 1800000: # 4º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 5.5 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 12.74 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 2.76 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 42 / 100), '-'*55)
            print('ICMS: ------- {:.2f}%'.format(ALIQUOTA * 33.5 / 100), '-'*55)
        elif RBTDOZE > 1800000 and RBTDOZE < 3600000 or RBTDOZE == 3600000: # 5º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 5.5 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 12.74 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 2.76 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 42 / 100), '-'*55)
            print('ICMS: ------- {:.2f}%'.format(ALIQUOTA * 33.5 / 100), '-'*55)
        elif RBTDOZE > 3600000 and RBTDOZE < 4800000 or RBTDOZE == 4800000: # 6º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 13.5 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 10 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 28.27 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 6.13 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 42.10 / 100), '-'*55)
            print('ICMS: ------- {:.2f}%'.format(ALIQUOTA * 0 / 100), '-'*55)

    # PERECENTUAIS DE REPARTIÇÃO DOS TRIBUTOS CASO ESCOLHA ANEXO II

    elif ANEXO == 2:
        if RBTDOZE < 180000 or RBTDOZE == 180000: # 1º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 5.5 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 11.51 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 2.49 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 37.5 / 100), '-'*55)
            print('IPI: -------- {:.2f}%'.format(ALIQUOTA * 7.5 / 100), '-'*55)
            print('ICMS: ------- {:.2f}%'.format(ALIQUOTA * 32 / 100), '-'*55)
        elif RBTDOZE > 180000 and RBTDOZE < 360000 or RBTDOZE == 360000: # 2º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 5.5 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 11.51 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 2.49 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 37.5 / 100), '-'*55)
            print('IPI: -------- {:.2f}%'.format(ALIQUOTA * 7.5 / 100), '-'*55)
            print('ICMS: ------- {:.2f}%'.format(ALIQUOTA * 32 / 100), '-'*55)
        elif RBTDOZE > 360000 and RBTDOZE < 720000 or RBTDOZE == 720000: # 3º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 5.5 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 11.51 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 2.49 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 37.5 / 100), '-'*55)
            print('IPI: -------- {:.2f}%'.format(ALIQUOTA * 7.5 / 100), '-'*55)
            print('ICMS: ------- {:.2f}%'.format(ALIQUOTA * 32 / 100), '-'*55)
        elif RBTDOZE > 720000 and RBTDOZE < 1800000 or RBTDOZE == 1800000: # 4º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 5.5 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 11.51 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 2.49 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 37.5 / 100), '-'*55)
            print('IPI: -------- {:.2f}%'.format(ALIQUOTA * 7.5 / 100), '-'*55)
            print('ICMS: ------- {:.2f}%'.format(ALIQUOTA * 32 / 100), '-'*55)
        elif RBTDOZE > 1800000 and RBTDOZE < 3600000 or RBTDOZE == 3600000: # 5º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 5.5 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 11.51 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 2.49 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 37.5 / 100), '-'*55)
            print('IPI: -------- {:.2f}%'.format(ALIQUOTA * 7.5 / 100), '-'*55)
            print('ICMS: ------- {:.2f}%'.format(ALIQUOTA * 32 / 100), '-'*55)
        elif RBTDOZE > 3600000 and RBTDOZE < 4800000 or RBTDOZE == 4800000: # 6º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 8.5 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 7.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 20.96 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 4.54 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 23.5 / 100), '-'*55)
            print('IPI: -------- {:.2f}%'.format(ALIQUOTA * 35 / 100), '-'*55)
            print('ICMS: ------- {:.2f}%'.format(ALIQUOTA * 0 / 100), '-'*55)

    # PERECENTUAIS DE REPARTIÇÃO DOS TRIBUTOS CASO ESCOLHA ANEXO III

    elif ANEXO == 3:
        if RBTDOZE < 180000 or RBTDOZE == 180000: # 1º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 4 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 12.82 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 2.78 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 43.4 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 33.5 / 100), '-'*55)
        elif RBTDOZE > 180000 and RBTDOZE < 360000 or RBTDOZE == 360000: # 2º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 4 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 14.05 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 3.05 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 43.4 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 32 / 100), '-'*55)
        elif RBTDOZE > 360000 and RBTDOZE < 720000 or RBTDOZE == 720000: # 3º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 4 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 13.64 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 2.96 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 43.4 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 32.5 / 100), '-'*55)
        elif RBTDOZE > 720000 and RBTDOZE < 1800000 or RBTDOZE == 1800000: # 4º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 4 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 13.64 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 2.96 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 43.4 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 32.5 / 100), '-'*55)
        elif RBTDOZE > 1800000 and RBTDOZE < 3600000 or RBTDOZE == 3600000: # 5º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 4 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 3.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 12.82 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 2.78 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 43.4 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 33.5 / 100), '-'*55)
        elif RBTDOZE > 3600000 and RBTDOZE < 4800000 or RBTDOZE == 4800000: # 6º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 35 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 15 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 16.03 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 3.47 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 30.5 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 0 / 100), '-'*55)

    # PERECENTUAIS DE REPARTIÇÃO DOS TRIBUTOS CASO ESCOLHA ANEXO IV

    elif ANEXO == 4:
        if RBTDOZE < 180000 or RBTDOZE == 180000: # 1º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 18.8 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 15.20 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 17.67 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 3.83 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 44.5 / 100), '-'*55)
        elif RBTDOZE > 180000 and RBTDOZE < 360000 or RBTDOZE == 360000: # 2º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 19.8 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 15.20 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 20.55 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 4.45 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 40 / 100), '-'*55)
        elif RBTDOZE > 360000 and RBTDOZE < 720000 or RBTDOZE == 720000: # 3º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 20.8 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 15.20 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 19.73 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 4.27 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 40 / 100), '-'*55)
        elif RBTDOZE > 720000 and RBTDOZE < 1800000 or RBTDOZE == 1800000: # 4º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 17.8 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 19.20 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 18.9 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 4.10 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 40 / 100), '-'*55)
        elif RBTDOZE > 1800000 and RBTDOZE < 3600000 or RBTDOZE == 3600000: # 5º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 18.8 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 19.20 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 18.08 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 3.92 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 40 / 100), '-'*55)
        elif RBTDOZE > 3600000 and RBTDOZE < 4800000 or RBTDOZE == 4800000: # 6º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 53.5 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 21.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 20.55 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 4.45 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 0 / 100), '-'*55)

    # PERECENTUAIS DE REPARTIÇÃO DOS TRIBUTOS CASO ESCOLHA ANEXO V

    elif ANEXO == 5:
        if RBTDOZE < 180000 or RBTDOZE == 180000: # 1º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 25 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 15 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 14.10 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 3.05 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 28.85 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 14 / 100), '-'*55)
        elif RBTDOZE > 180000 and RBTDOZE < 360000 or RBTDOZE == 360000: # 2º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 23 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 15 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 14.10 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 3.05 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 27.85 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 17 / 100), '-'*55)
        elif RBTDOZE > 360000 and RBTDOZE < 720000 or RBTDOZE == 720000: # 3º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 24 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 15 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 14.92 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 3.23 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 23.85 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 19 / 100), '-'*55)
        elif RBTDOZE > 720000 and RBTDOZE < 1800000 or RBTDOZE == 1800000: # 4º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 21 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 15 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 15.74 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 3.41 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 23.85 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 21 / 100), '-'*55)
        elif RBTDOZE > 1800000 and RBTDOZE < 3600000 or RBTDOZE == 3600000: # 5º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 23 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 12.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 14.10 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 3.05 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 23.85 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 23.5 / 100), '-'*55)
        elif RBTDOZE > 3600000 and RBTDOZE < 4800000 or RBTDOZE == 4800000: # 6º FAIXA
            print('-=-'*8, 'REPARTIÇÃO DOS TRIBUTOS', '-=-'*8 + '-=')
            print('IRPJ: ------- {:.2f}%'.format(ALIQUOTA * 35 / 100), '-'*55)
            print('CSLL: ------- {:.2f}%'.format(ALIQUOTA * 15.5 / 100), '-'*55)
            print('COFINS: ----- {:.2f}%'.format(ALIQUOTA * 16.44 / 100), '-'*55)
            print('PIS: -------- {:.2f}%'.format(ALIQUOTA * 3.56 / 100), '-'*55)
            print('CPP: -------- {:.2f}%'.format(ALIQUOTA * 29.5 / 100), '-'*55)
            print('ISS: -------- {:.2f}%'.format(ALIQUOTA * 0 / 100), '-'*55)

    if ANEXO < 6 and RBTDOZE > 4800000:
        print('Para esta faixa de receita bruta acumulada dos ultimos 12 mêses, a empresa \nnão é optante pelo simples nacional')
            
    print('-=-'*25)
    print('-=-'*25)
    print('-=-'*8, 'ASCOPLAN CONTABILIDADE', '-=-'*8 + '-=-')
    print('-=-'*5, 'PROGRAMADOR: JOSÉ PAULO DE OLIVEIRA JUNIOR', '-=-'*5 + '-')
    print('-=-'*11, 'FIM', '-=-'*11 + '-=--')
    print('-=-'*25)
    n = str(input('Deseja fazer um novo calculo ? [S/N]: ')).upper()
    print('-=-'*25)
    os.system('cls')
    
'''os.system('pause')'''
