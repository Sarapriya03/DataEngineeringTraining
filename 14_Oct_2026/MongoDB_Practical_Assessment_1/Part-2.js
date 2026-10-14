// Part 2: CRUD Operations

// 1. Display all products.
db.products.find()

// 2. Display only one product having product_id = 103.
db.products.findOne({ product_id: 103 })

// 3. Insert a new product with:
// Product ID 107
// Product Name Bluetooth Speaker
// Category Electronics
// Brand SoundMax
// Price 7500
// Stock 20
// Available true
db.products.insertOne({
    product_id: 107, product_name: "Bluetooth Speaker", category: "Electronics",
    brand: "SoundMax", price: 7500, stock: 20, available: true
})

// 4. Insert two additional products in a single operation.
db.products.insertMany([
    { product_id: 108, product_name: "HD Webcam", category: "Electronics", brand: "ClearView", price: 3500, stock: 25, available: true },
    { product_id: 109, product_name: "USB Hub", category: "Accessories", brand: "ClickMax", price: 900, stock: 0, available: false }
])

// 5. Update the price of product 102 to 2000.
db.products.updateOne({ product_id: 102 }, { $set: { price: 2000 } })

// 6. Update both stock and availability of product 105.
db.products.updateOne({ product_id: 105 }, { $set: { stock: 15, available: true } })

// 7. Increase the stock of product 104 by 10.
db.products.updateOne({ product_id: 104 }, { $inc: { stock: 10 } })

// 8. Reduce the stock of product 106 by 3.
db.products.updateOne({ product_id: 106 }, { $inc: { stock: -3 } })

// 9. Add a new field called:discount_percent with value 10 to product 101.
db.products.updateOne({ product_id: 101 }, { $set: { discount_percent: 10 } })

// 10. Remove discount_percent from product 101.
db.products.updateOne({ product_id: 101 }, { $unset: { discount_percent: "" } })

// 11. Delete one product using its product_id.
// 12. Delete all products where:stock = 0
// 13. Verify the documents before and after each delete.

// !! + 13
db.products.find({ product_id: 108 })          // before: 1 document
db.products.countDocuments()                   // total before
db.products.deleteOne({ product_id: 108 })
db.products.find({ product_id: 108 })          // after: empty
db.products.countDocuments()                   // total after (one less)

// 12 + 13
db.products.find({ stock: 0 })                 // before: shows product 109
db.products.countDocuments({ stock: 0 })
db.products.deleteMany({ stock: 0 })
db.products.find({ stock: 0 })                 // after: empty
db.products.countDocuments()
