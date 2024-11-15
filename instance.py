import random
import math

def generisi_instancu(n, m, r, naziv_fajla):
    koordinate_klijenata = [(random.random(), random.random()) for i in range(m)]
    koordinate_objekata = [(random.random(), random.random()) for i in range(n)]  
    
    matrica_rastojanja = [[10 * math.sqrt((koordinate_klijenata[j][0] - koordinate_objekata[i][0])**2 + (koordinate_klijenata[j][1] - koordinate_objekata[i][1])**2)
    for j in range(m)]  
    for i in range(n)]

    potraznja_klijenata = [random.randrange(5,36) for i in range(m)]
    kapaciteti_objekata = [random.randrange(10,161) for i in range(n)]

    k = sum(potraznja_klijenata) * r / sum(kapaciteti_objekata)
    kapaciteti_objekata = [int(x * k) for x in kapaciteti_objekata]

    cijena_izgradnje_objekta = [random.uniform(0,90) + random.uniform(100,110) * math.sqrt(kapaciteti_objekata[i]) for i in range(n)]

    with open(naziv_fajla, 'w') as f:
        f.write(str(n) + '\n')
        f.write(str(m) + '\n')
        for x in cijena_izgradnje_objekta:
            f.write(str(x) + ' ')
        f.write('\n')
        for x in kapaciteti_objekata:
            f.write(str(x) + ' ')
        f.write('\n')
        for x in potraznja_klijenata:
            f.write(str(x) + ' ')
        f.write('\n')
        for red in matrica_rastojanja:
            for x in red:
                f.write(str(x) + ' ')
            f.write('\n')
       
generisi_instancu(20,20,2, './instance/mala1.txt')
generisi_instancu(20,20,3, './instance/mala2.txt')
generisi_instancu(20,20,5, './instance/mala3.txt')
generisi_instancu(20,20,10, './instance/mala4.txt')
generisi_instancu(20,40,2, './instance/mala5.txt')
generisi_instancu(20,40,3, './instance/mala6.txt')
generisi_instancu(20,40,5, './instance/mala7.txt')
generisi_instancu(20,40,10, './instance/mala8.txt')
generisi_instancu(30,50,2, './instance/mala9.txt')
generisi_instancu(30,50,3, './instance/mala10.txt')
generisi_instancu(30,50,5, './instance/mala11.txt')
generisi_instancu(30,50,10, './instance/mala12.txt')
generisi_instancu(50,50,2, './instance/mala13.txt')
generisi_instancu(50,50,3, './instance/mala14.txt')
generisi_instancu(50,50,5, './instance/mala15.txt')
generisi_instancu(50,50,10, './instance/mala16.txt')
generisi_instancu(30,100,2, './instance/mala17.txt')
generisi_instancu(30,100,3, './instance/mala18.txt')
generisi_instancu(30,100,5, './instance/mala19.txt')
generisi_instancu(30,100,10, './instance/mala20.txt')

generisi_instancu(50,200,5, './instance/srednja1.txt')
generisi_instancu(50,200,10, './instance/srednja2.txt')
generisi_instancu(50,200,15, './instance/srednja3.txt')
generisi_instancu(50,200,20, './instance/srednja4.txt')
generisi_instancu(50,350,5, './instance/srednja5.txt')
generisi_instancu(50,350,10, './instance/srednja6.txt')
generisi_instancu(50,350,15, './instance/srednja7.txt')
generisi_instancu(50,350,20, './instance/srednja8.txt')
generisi_instancu(70,300,5, './instance/srednja9.txt')
generisi_instancu(70,300,10, './instance/srednja10.txt')
generisi_instancu(70,300,15, './instance/srednja11.txt')
generisi_instancu(70,300,20, './instance/srednja12.txt')
generisi_instancu(100,300,5, './instance/srednja13.txt')
generisi_instancu(100,300,10, './instance/srednja14.txt')
generisi_instancu(100,300,15, './instance/srednja15.txt')
generisi_instancu(100,300,20, './instance/srednja16.txt')
generisi_instancu(80,400,5, './instance/srednja17.txt')
generisi_instancu(80,400,10, './instance/srednja18.txt')
generisi_instancu(80,400,15, './instance/srednja19.txt')
generisi_instancu(80,400,20, './instance/srednja20.txt')

generisi_instancu(400,700,5, './instance/velika1.txt')
generisi_instancu(400,700,10, './instance/velika2.txt')
generisi_instancu(400,700,15, './instance/velika3.txt')
generisi_instancu(400,700,20, './instance/velika4.txt')
generisi_instancu(400,1000,5, './instance/velika5.txt')
generisi_instancu(400,1000,10, './instance/velika6.txt')
generisi_instancu(400,1000,15, './instance/velika7.txt')
generisi_instancu(400,1000,20, './instance/velika8.txt')
generisi_instancu(400,2000,5, './instance/velika9.txt')
generisi_instancu(400,2000,10, './instance/velika10.txt')
generisi_instancu(400,2000,15, './instance/velika11.txt')
generisi_instancu(400,2000,20, './instance/velika12.txt')
generisi_instancu(2000,2000,5, './instance/velika13.txt')
generisi_instancu(2000,2000,10, './instance/velika14.txt')
generisi_instancu(2000,2000,15, './instance/velika15.txt')
generisi_instancu(2000,2000,20, './instance/velika16.txt')
generisi_instancu(1000,1000,5, './instance/velika17.txt')
generisi_instancu(1000,1000,10, './instance/velika18.txt')
generisi_instancu(1000,1000,15, './instance/velika19.txt')
generisi_instancu(1000,1000,20, './instance/velika20.txt')
