// Part 4: Projection and Sorting

// 26. Display only:product_name, price. Do not display _id.
db.products.find({}, { _id: 0, product_name: 1, price: 1 })

// 27. Display:product_name, category, stock
db.products.find({}, { _id: 0, product_name: 1, category: 1, stock: 1 })

// 28. Sort products by price from lowest to highest.
db.products.find().sort({ price: 1 })

// 29. Sort products by price from highest to lowest.
db.products.find().sort({ price: -1 })

// 30. Sort products alphabetically by product name.
db.products.find().sort({ product_name: 1 })

// 31. Display the three most expensive products.
db.products.find().sort({ price: -1 }).limit(3)

// 32. Display the two products having the lowest stock.
db.products.find().sort({ stock: 1 }).limit(2)
