import cellpylib as cpl
from itertools import product

if __name__ == "__main__":
    print("Ingresa las relgas del automata y el numero de generaciones");
    combinaciones = product(['0','1'], repeat=3)
    reglas = dict()
    for x in combinaciones:
        x = ''.join(x)
        regla =-1
        while regla != '0' and regla != '1':
            regla = input(x+': ')
        reglas[x] = int(regla)
    no_generaciones = 0
    while no_generaciones <= 0:
        no_generaciones = input('Nº generaciones: ')
        no_generaciones = no_generaciones = int(no_generaciones) if no_generaciones.isdigit() else 0
    automata_celular = cpl.init_simple(no_generaciones*2)
    automata_celular = cpl.evolve(automata_celular, timesteps=no_generaciones, memoize=True, 
                                    apply_rule=lambda n, c, t: cpl.table_rule(n, reglas))
    cpl.plot(automata_celular)