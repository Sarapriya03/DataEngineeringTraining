// Part 5: Projection and Sorting

// 21. Display only:restaurant_name, city, rating without _id.
db.restaurants.find({}, { _id: 0, restaurant_name: 1, city: 1, rating: 1 })

// 22. Sort restaurants by rating from highest to lowest.
db.restaurants.find().sort({ rating: -1 })

// 23. Display the top 3 highest-rated restaurants.
db.restaurants.find().sort({ rating: -1 }).limit(3)
