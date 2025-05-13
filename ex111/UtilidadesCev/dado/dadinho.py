def LerDinheiro(p=0.0):
    p = str(input('Digite o preço: R$'))
    while True:
        try: 
            float(p)
            return p
        except ValueError:
            try:
                float(p.replace(",", "."))
                return p
            except ValueError:
                p = str(input(('Não é um valor float, tente de novo: R$')))
