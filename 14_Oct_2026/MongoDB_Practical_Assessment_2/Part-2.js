// Part 2: CRUD and Basic Queries

// 1. Display all restaurants.
db.restaurants.find()

// 2. Find only restaurants from Hyderabad.
db.restaurants.find({ city: "Hyderabad" })

// 3. Find active restaurants having rating greater than 4.3.
db.restaurants.find({ active: true, rating: { $gt: 4.3 } })

// 4. Insert one new restaurant of your choice.
db.restaurants.insertOne({
    restaurant_id: 106, restaurant_name: "Sweet Tooth Cafe", city: "Chennai",
    cuisine: ["Desserts", "Bakery"], rating: 4.0, active: true,
    contact: { phone: "9444455555", email: "sweet@email.com" }
})

// 5. Change the rating of restaurant 104.
db.restaurants.updateOne({ restaurant_id: 104 }, { $set: { rating: 4.1 } })

// 6. Change restaurant 104 from inactive to active.
db.restaurants.updateOne({ restaurant_id: 104 }, { $set: { active: true } })

// 7. Delete the restaurant you inserted in Question 4.
db.restaurants.find({ restaurant_id: 106 })     // verify before
db.restaurants.deleteOne({ restaurant_id: 106 })
db.restaurants.find({ restaurant_id: 106 })     // verify after: empty
