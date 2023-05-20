from store import *
from payment import *
from warehouse import *
from accounting import *


while (True):

    print("***Welcome to Felona store***")

    o = input("Choose your Role\n1.customer\n2.manager\n")
    if o == '1':
        wares = []  # [[name , price , number]]
        store = Store()
        while o != '2':
            wares = Store.Order(store, wares)
            o = Store.cart(wares)
        buyer = []  # [first name, last name, phone number, [State, City, Details, PostCode], delivery method, [delivery time, index], purchase number]
        payment = Payment(wares, buyer)
        buyer = Payment.get_info(payment)
        if Payment.confirmation(payment) == 1:
            Payment.Invoice(payment)
            print(
                "\nPurchase completed successfully.\nYour invoice file saved\nThanks for trusting us:)\n")
            Logistic.Update(buyer[5][1])
            warehouse = Warehouse()
            for i in wares:
                Warehouse.auto_update(warehouse, i[0], i[2])
            Accounting.Update(wares, buyer)

    elif o == '2':
        o2 = input("Choose the section\n1.warehouse\n2.Accounting\n")
        if o2 == '1':
            warehouse = Warehouse()
            o3 = Warehouse.Option(warehouse)
            if o3 == '1':
                Warehouse.Manualy_update(warehouse)
            elif o3 == '2':
                Warehouse.Output(warehouse)
            elif o3 == '3':
                Warehouse.AddWare(warehouse)
        if o2 == '2':
            Accounting.Output()
