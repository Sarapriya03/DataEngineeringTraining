// Part 4: Orders

// 13. Find all Delivered orders.
db.orders.find({ status: "Delivered" })

// 14. Find orders placed after 2026-09-02.
db.orders.find({ order_date: { $gt: ISODate("2026-09-02") } })

// 15. Find orders delivered to Hyderabad.
db.orders.find({ "delivery.city": "Hyderabad" })

// 16. Find orders containing an item named Noodles.
db.orders.find({ "items.name": "Noodles" })

// 17. Find orders containing an item where quantity is greater than 1.
db.orders.find({ "items.quantity": { $gt: 1 } })

// 18. Find an order where the same item has:name = Chicken Biryani, quantity = 2
db.orders.find({ items: { $elemMatch: { name: "Chicken Biryani", quantity: 2 } } })

// 19. Add another item to order 5002.
db.orders.updateOne(
    { order_id: 5002 },
    { $push: { items: { name: "Garlic Bread", quantity: 1, price: 120 } } }
)

// 20. Change order 5002 from Processing to Delivered.
db.orders.updateOne({ order_id: 5002 }, { $set: { status: "Delivered" } })
