import InsectClass as i

def main():

    an_insect = i.Insect(2,4)

    an_insect.calc_flight()

    print('This insect can fly ' + str(an_insect.get_flight()) + ' miles.')


main()