import csv

with open("shipments.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "shipment_id",
        "customer",
        "city",
        "weight",
        "status",
        "cost"
    ])

    writer.writerow(["S101","Alpha Stores","Hyderabad",12.5,"Delivered",850])
    writer.writerow(["S102","Metro Mart","Mumbai",8.2,"In Transit",620])
    writer.writerow(["S103","Fresh Foods","Hyderabad",15.0,"Delivered",1100])
    writer.writerow(["S104","Quick Shop","Pune",5.5,"Pending",450])
    writer.writerow(["S105","Urban Retail","Mumbai",20.0,"Delivered",1450])
    writer.writerow(["S106","Daily Needs","Delhi",9.8,"In Transit",700])
    writer.writerow(["S107","Smart Bazaar","Hyderabad",7.5,"Pending",550])
    writer.writerow(["S108","Green Market","Delhi",18.2,"Delivered",1300])