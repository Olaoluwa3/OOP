import CellPhoneClass as c

def main():

    manufact = 'Apple'
    model = '3398ASS328'
    price = 1000

    phone = c.CellPhone(manufact, model, price)


    print(
        '\nThe manufacturer of the phone is: '+phone.get_manufact()+
        '\nThe model number of the phone is: '+phone.get_model()+
        '\nThe retail price of the phone is: $'+format(phone.get_retail_price(),',.2f') 
    )

main()