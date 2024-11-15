from docplex.mp.model import Model

# UCITAVAMO PODATKE IZ FAJLA
def ucitaj_podatke(naziv_fajla):
    with open(naziv_fajla, 'r') as file:
        br_objekata = int(file.readline())                         # broj objekata
        br_klijenata = int(file.readline())                        # broj klijenata
        f = [float(x) for x in file.readline().split()]            # cijena izgradnje svakog objekta
        s = [int(x) for x in file.readline().split()]              # kapacitet svakog objekta
        d = [int(x) for x in file.readline().split()]              # zahtjev svakog korisnika/klijenta

        C = []                                                     # matrica rastojanja od objekta do korisnika, tj.troskovi transporta
        for i in range(br_objekata):
            C.append([float(x) for x in file.readline().split()])

    return br_objekata, br_klijenata, f, s, d, C

def rijesi_problem(naziv_fajla):
    br_objekata, br_klijenata, f, s, d, C = ucitaj_podatke(naziv_fajla)

    # KREIRAMO MODEL 
    model = Model(name = 'SSCFLP problem')

    # DEFINISEMO PROMJENLJIVE
    # y[i], ako je objekat otvoren na lokaciji i ima vrijednost 1, inace 0
    y = model.binary_var_list(br_objekata, name = 'y')

    # matrica X[i][j], ako je j-ti korisnik pridruuzen objektu na lokaciji i ima vrijednost 1, inace 0
    X = [[model.binary_var(name = f"X_{i}_{j}") for j in range(br_klijenata)] for i in range(br_objekata)]

    # DEFINISEMO FUNKCIJU CILJA, minimiziranje troskova transporta
    prva_suma = model.sum(f[i] * y[i] for i in range(br_objekata))
    druga_suma = model.sum(C[i][j] * X[i][j] for j in range(br_klijenata) for i in range(br_objekata))
    ukupna_cijena = prva_suma + druga_suma
    model.minimize(ukupna_cijena)

    # DEFINISEMO OGRANICENJA 
    # Svaki klijent se snabdijeva iz samo jednog objekta
    for j in range(br_klijenata):
        model.add_constraint(model.sum(X[i][j] for i in range(br_objekata)) == 1, f"dodijeli_jedan_objekat_svima {j}")

    # ukupna potraznja ne smije prelaziti maksimalni kapacitet objekta, i klijent smije biti dodijeljen samo otvorenom objektu
    for i in range(br_objekata):
        model.add_constraint(model.sum(d[j] * X[i][j] for j in range(br_klijenata)) <= (s[i] * y[i]))

    # RJESAVAMO MODEL
    model.set_time_limit(7200)
    model.context.cplex_parameters.timelimit = 7200
    solution = model.solve()

    # ISPIS REZULTATA
    if solution:
        print(naziv_fajla)
        print('\t' + model.solve_details.status)
        print(f'\tRjesenje je pronadjeno: {solution.objective_value}')
        print(f'\tBroj iteracija: {model.solve_details.nb_iterations}')
        print(f'\tVrijeme izvrsavanja: {model.solve_details.time}')
        print(f'\tBroj cvorova: {model.solve_details.nb_nodes_processed}')
    else:
        print(naziv_fajla)
        print('\tRjesenje nije pronadjeno')

for i in range(20):
    rijesi_problem(f'./instance/mala{i+1}.txt')

for i in range(20):
    rijesi_problem(f'./instance/srednja{i+1}.txt')

for i in range(20):
    rijesi_problem(f'./instance/velika{i+1}.txt')


