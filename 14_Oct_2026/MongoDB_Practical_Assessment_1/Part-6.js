// Part 6: Embedded Documents

// 40. Find products whose warranty is 2 years.
db.products.find({ "specifications.warranty_years": 2 })

// 41. Find products where:specifications.adjustable = true
db.products.find({ "specifications.adjustable": true })

// 42. Find products with:specifications.wireless = true
db.products.find({ "specifications.wireless": true })

// 43. Change the warranty of product 103 from 3 to 5 years.
db.products.updateOne({ product_id: 103 }, { $set: { "specifications.warranty_years": 5 } })

// 44. Add:specifications.country_of_origin
db.products.updateOne({ product_id: 101 }, { $set: { "specifications.country_of_origin": "India" } })
db.products.updateOne({ product_id: 104 }, { $set: { "specifications.country_of_origin": "India" } })

// 45. Find products manufactured in the country you added.
db.products.find({ "specifications.country_of_origin": "India" })
