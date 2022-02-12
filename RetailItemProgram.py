import RetailItemClass as r

def main():

    item1 = {
        'Description':'Jacket',
        'Units':12,
        'Price':59.95
    }

    item2 = {
        'Description':'Designer Jeans',
        'Units':40,
        'Price':34.95
    }

    item3 = {
        'Description':'Shirt',
        'Units':20,
        'Price':24.95
    }


    #Create three RetailItem objects
    Item_1 = r.RetailItem(item1['Description'],
        item1['Units'], item1['Price'])

    Item_2 = r.RetailItem(item2['Description'],
        item2['Units'], item2['Price'])

    Item_3 = r.RetailItem(item3['Description'],
        item3['Units'], item3['Price'])


    #Display RetailItem objects
    print(Item_1)
    print(Item_2)
    print(Item_3)

main()

    