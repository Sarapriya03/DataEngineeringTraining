// Part 6: Data Types

// 24. Find documents where rating is stored as a numeric value.
db.restaurants.find({ rating: { $type: "number" } })

// 25. Identify the datatype of order_date.
db.orders.aggregate([{ $project: { _id: 0, order_id: 1, order_date_type: { $type: "$order_date" } } }])

// 26. Identify the datatype of items.
db.orders.aggregate([{ $project: { _id: 0, order_id: 1, items_type: { $type: "$items" } } }])

// 27. Insert one test restaurant where rating is accidentally stored as a string, identify it using $type, and then correct the value.
db.restaurants.insertOne({
    restaurant_id: 107, restaurant_name: "Test Diner", city: "Pune",
    cuisine: ["Continental"], rating: "4.1", active: true,
    contact: { phone: "9555566666", email: "test@email.com" }
})

// identify it
db.restaurants.find({ rating: { $type: "string" } })

// correct it
db.restaurants.updateOne({ restaurant_id: 107 }, { $set: { rating: 4.1 } })
// or convert in place:
// db.restaurants.updateOne({ restaurant_id: 107 }, [ { $set: { rating: { $toDouble: "$rating" } } } ])

// verify: should return no documents
db.restaurants.find({ rating: { $type: "string" } })
