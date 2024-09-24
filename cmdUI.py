#crud application using python
#variables declaration
products_details={"p01":["product_name","short discription",200,"img.jpeg",4.0],"p02":["product_name1","short discription1",201,"img1.jpeg",4.1]}
headings=["pid", "name", "discription", "price", "image", "rating"]
#Flag
gameover=False
while not gameover:
    print("1. Show All Products ")
    print("2. Add New Products ")
    print("3. Delete a Products ")
    print("4. Update Products Rating")
    print("5. Exit ")
    option=input("Enter option to continue ..\t ")
    if option=="1":
        #show all products
        for heading in headings :
            print("\t"+heading,end="\t")
        print("")
        for ind,(k,v) in enumerate(products_details.items()):
            print(ind,end='\t')
            print(k,end='\t')
            for datapoint in v :
                print(datapoint,end="\t")
            print("")
    elif option=="2":
        new_data=[]
        new_data.append(input("Enter product id:\t"))
        new_data.append(input("Enter product name:\t"))
        new_data.append(input("Enter product description:\t"))
        new_data.append(input("Enter product price:\t"))
        new_data.append(input("Enter product image:\t"))
        new_data.append(input("Enter product Rating:\t"))
        products_details[new_data[0]]=new_data[1:]
        print(new_data)
    elif option=="3":
         #show all products
        for heading in headings :
            print("\t"+heading,end="\t")
        print("")
        for ind,(k,v) in enumerate(products_details.items()):
            print(ind,end='\t')
            print(k,end='\t')
            for datapoint in v :
                print(datapoint,end="\t")
            print("")
        option_2=input("Enter product id to delete or -1 to exit \t")
        if option_2 == "-1":
            continue
        if option_2 in products_details:
            del(products_details[option_2])
        else:
            print("Id not available try again...")
    elif option=="4":
        #update rating
        id_=input("Enter product id to update\t")
        rating=input("Enter product rating\t")
        # print(products_details[id]_)
        products_details[id_][-1]=rating
    elif option=="5":
        gameover=True