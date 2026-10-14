// Part 3: Arrays and Embedded Documents

// 8. Find restaurants serving Fast Food.
db.restaurants.find({ cuisine: "Fast Food" })

// 9. Find restaurants serving both Italian and Fast Food.
db.restaurants.find({ cuisine: { $all: ["Italian", "Fast Food"] } })

// 10. Add Desserts to the cuisine list of restaurant 102.
db.restaurants.updateOne({ restaurant_id: 102 }, { $push: { cuisine: "Desserts" } })

// 11. Change the email address of restaurant 103.
db.restaurants.updateOne({ restaurant_id: 103 }, { $set: { "contact.email": "greenbowl@email.com" } })

// 12. Display restaurants whose contact phone starts with 9.
db.restaurants.find({ "contact.phone": /^9/ })

