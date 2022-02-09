
import InsectClass as i

def main():

    an_insect = i.Insect()

    an_insect.calc_flight()

    print('This insect can fly ' + str(an_insect.get_flight()) + ' miles.')


main()