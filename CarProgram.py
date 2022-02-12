import CarClass as cc

def main():

    #create car object
    my_car = cc.Car('2020', 'Toyota')
    
    #accelerate 5 times
    for count in range(5):
        my_car.accelerate()
        print("\nThe speed is now "+str(my_car.get_speed()))
    
    #brake 5 times
    for count in range(5):
        my_car.brake()
        print("\nThe speed is now "+str(my_car.get_speed()))

main()
