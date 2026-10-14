// Part 3: Filtering and Query Operators

// 14. Find all Electronics products.
db.products.find({ category: "Electronics" })

// 15. Find products costing more than ₹10,000.
db.products.find({ price: { $gt: 10000 } })

// 16. Find products costing between ₹5,000 and ₹30,000.
db.products.find({ price: { $gte: 5000, $lte: 30000 } })

// 17. Find products whose stock is less than 10.
db.products.find({ stock: { $lt: 10 } })

// 18. Find products that are currently available.
db.products.find({ available: true })

// 19. Find products that are not available.
db.products.find({ available: false })

// 20. Find products belonging to either:Electronics, Furniture
db.products.find({ category: { $in: ["Electronics", "Furniture"] } })

// 21. Find products that are not in the Accessories category.
db.products.find({ category: { $ne: "Accessories" } })

// 22. Find products where:price > 10000 AND stock > 5
db.products.find({ price: { $gt: 10000 }, stock: { $gt: 5 } })

// 23. Find products where:category = Electronics OR price < 5000
db.products.find({ $or: [{ category: "Electronics" }, { price: { $lt: 5000 } }] })

// 24. Find products launched after:1 February 2026
db.products.find({ launch_date: { $gt: ISODate("2026-02-01") } })

// 25. Find products launched between:1 January 2026 and 31 March 2026
db.products.find({ launch_date: { $gte: ISODate("2026-01-01"), $lt: ISODate("2026-04-01") } })
