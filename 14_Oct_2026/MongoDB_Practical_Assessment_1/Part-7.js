// Part 7: Data Types

// 46. Find documents where price is stored as a numeric type.
db.products.find({ price: { $type: "number" } })

// 47. Find the datatype of:launch_date
db.products.aggregate([{ $project: { _id: 0, product_id: 1, launch_date_type: { $type: "$launch_date" } } }])

// 48. Find the datatype of:colors
db.products.aggregate([{ $project: { _id: 0, product_id: 1, colors_type: { $type: "$colors" } } }])

// 49. Find the datatype of:specifications
db.products.aggregate([{ $project: { _id: 0, product_id: 1, specs_type: { $type: "$specifications" } } }])

// 50. Insert one intentionally incorrect product where:price is stored as a string instead of a number.
db.products.insertOne({
    product_id: 110, product_name: "Desk Lamp", category: "Furniture", brand: "BrightHome",
    price: "2500", stock: 30, available: true
})

// 51. Write a query that identifies products where price is stored as a string.
db.products.find({ price: { $type: "string" } })

// 52. Correct that product so price becomes numeric.
db.products.updateOne({ product_id: 110 }, { $set: { price: 2500 } })
// or, convert whatever string is there:
db.products.updateOne({ product_id: 110 }, [{ $set: { price: { $toInt: "$price" } } }])

// verify: should return no documents
db.products.find({ price: { $type: "string" } })
