// Part 1: Database Setup

use food_delivery_assessment

// Create the restaurants collection:
db.createCollection("restaurants")
// Insert:
db.restaurants.insertMany([
    { restaurant_id: 101, restaurant_name: "Spice Kitchen", city: "Hyderabad", cuisine: ["Indian", "Biryani"], rating: 4.5, active: true, contact: { phone: "9876543210", email: "spice@email.com" } },
    { restaurant_id: 102, restaurant_name: "Urban Pizza", city: "Mumbai", cuisine: ["Italian", "Fast Food"], rating: 4.2, active: true, contact: { phone: "9988776655", email: "pizza@email.com" } },
    { restaurant_id: 103, restaurant_name: "Green Bowl", city: "Bangalore", cuisine: ["Healthy", "Vegetarian"], rating: 4.7, active: true, contact: { phone: "9123456780", email: "green@email.com" } },
    { restaurant_id: 104, restaurant_name: "Burger Point", city: "Hyderabad", cuisine: ["Fast Food", "Burgers"], rating: 3.9, active: false, contact: { phone: "9000011111", email: "burger@email.com" } },
    { restaurant_id: 105, restaurant_name: "Asian Wok", city: "Delhi", cuisine: ["Chinese", "Thai"], rating: 4.4, active: true, contact: { phone: "9222233333", email: "wok@email.com" } }
])

// Create the orderss collection:
db.createCollection("orders")
// Insert:
db.orders.insertMany([
    {
        order_id: 5001, restaurant_id: 101, customer_name: "Adil", order_date: ISODate("2026-09-01"), status: "Delivered",
        items: [{ name: "Chicken Biryani", quantity: 2, price: 320 }, { name: "Coke", quantity: 2, price: 60 }],
        delivery: { city: "Hyderabad", fee: 40 }
    },
    {
        order_id: 5002, restaurant_id: 102, customer_name: "Megha", order_date: ISODate("2026-09-02"), status: "Processing",
        items: [{ name: "Farmhouse Pizza", quantity: 1, price: 550 }],
        delivery: { city: "Mumbai", fee: 60 }
    },
    {
        order_id: 5003, restaurant_id: 103, customer_name: "Kabir", order_date: ISODate("2026-09-03"), status: "Delivered",
        items: [{ name: "Protein Bowl", quantity: 2, price: 400 }, { name: "Juice", quantity: 1, price: 150 }],
        delivery: { city: "Bangalore", fee: 50 }
    },
    {
        order_id: 5004, restaurant_id: 101, customer_name: "Nisha", order_date: ISODate("2026-09-04"), status: "Cancelled",
        items: [{ name: "Veg Biryani", quantity: 1, price: 250 }],
        delivery: { city: "Hyderabad", fee: 40 }
    },
    {
        order_id: 5005, restaurant_id: 105, customer_name: "Rohan", order_date: ISODate("2026-09-05"), status: "Delivered",
        items: [{ name: "Thai Curry", quantity: 1, price: 480 }, { name: "Noodles", quantity: 2, price: 300 }],
        delivery: { city: "Delhi", fee: 70 }
    }
])



