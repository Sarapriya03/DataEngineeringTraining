// Part 5: Arrays

// 33. Find products available in Black.
db.products.find({ colors: "Black" })

// 34. Find products available in both:Black, Silver
db.products.find({ colors: { $all: ["Black", "Silver"] } })

// 35. Find products available in either:White, Blue
db.products.find({ colors: { $in: ["White", "Blue"] } })

// 36. Add Grey to product 101.
db.products.updateOne({ product_id: 101 }, { $push: { colors: "Grey" } })

// 37. Add Black to product 101 without creating a duplicate if it already exists.
db.products.updateOne({ product_id: 101 }, { $addToSet: { colors: "Black" } })

// 38. Remove Red from product 102.
db.products.updateOne({ product_id: 102 }, { $pull: { colors: "Red" } })

// 39. Display products having more than one color.
db.products.find({ "colors.1": { $exists: true } })

