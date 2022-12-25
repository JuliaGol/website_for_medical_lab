from lab.models import Zlecenie, TypBadan, Wynik

def import_data():
    #clean data
    #TypBadan.objects.all().delete()
    Zlecenie.objects.all().delete()
    Wynik.objects.all().delete()
    try:
        badanie1 = TypBadan(nazwa='leukocyty', jednostka='tys./μl', min_ref=4.0, max_ref=10.0)
        badanie1.save()
    except:
        print("nie dodano badania1")
    try:
        zlecenie1 = Zlecenie(imie='Julia', nazwisko='Gołębiowska',
                         opis='Proszę o zrobienie badania  w trybie przyspieszonym')
        zlecenie1.save()
    except:
        print("nie dodano zlecenia1")

    wynik1 = Wynik(zlecenie = zlecenie1, typBadan = TypBadan.objects.get(nazwa="leukocyty"), wartosc = 2.0)
    wynik1.save()

    try:
        badanie2 = TypBadan(nazwa='trombocyty', jednostka='tys./μl', min_ref=150, max_ref=400)
        badanie2.save()
    except:
        print("nie dodano badania2")
    try:
        wynik2 = Wynik(zlecenie = zlecenie1, typBadan = TypBadan.objects.get(nazwa="trombocyty"), wartosc = 200.0)
        wynik2.save()
    except:
        print("nie dodano wyniku2")
    try:
        zlecenie2 = Zlecenie(imie='Anna', nazwisko='Nowak',
                         opis='brak')
        zlecenie2.save()
    except:
        print("nie dodano badanie2")
    try:
        wynik3 = Wynik(zlecenie = zlecenie2, typBadan = TypBadan.objects.get(nazwa="trombocyty"))
        wynik3.save()
    except:
        print("nie dodano wyniku3")
import_data()
