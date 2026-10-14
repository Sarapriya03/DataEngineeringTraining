// Part 9: Array of Embedded Documents

// Create:
db.createCollection("orders")
// Insert:
db.orders.insertMany([
    {
        order_id: 9001, customer_id: 501, order_date: ISODate("2026-09-01"), status: "Delivered",
        items: [{ product: "Ultra Laptop", quantity: 1, price: 72000 }, { product: "Wireless Mouse", quantity: 2, price: 2000 }]
    },
    {
        order_id: 9002, customer_id: 502, order_date: ISODate("2026-09-03"), status: "Processing",
        items: [{ product: "Office Desk", quantity: 1, price: 14500 }]
    },
    {
        order_id: 9003, customer_id: 503, order_date: ISODate("2026-09-05"), status: "Delivered",
        items: [{ product: "Smart Monitor", quantity: 2, price: 26000 }, { product: "Mechanical Keyboard", quantity: 1, price: 5200 }]
    }
])

// 61. Display orders having status Delivered.
db.orders.find({ status: "Delivered" })

// 62. Find orders containing Ultra Laptop.
db.orders.find({ "items.product": "Ultra Laptop" })

// 63. Find orders containing an item with quantity greater than 1.
db.orders.find({ "items.quantity": { $gt: 1 } })

// 64. Find orders containing:product = Smart Monitor AND quantity = 2 where both conditions belong to the same item.
db.orders.find({ items: { $elemMatch: { product: "Smart Monitor", quantity: 2 } } })

// 65. Add another item to order 9002.
db.orders.updateOne({ order_id: 9002 }, { $push: { items: { product: "Gaming Chair", quantity: 1, price: 18500 } } })

// 66. Change order 9002 status to Delivered.
db.orders.updateOne({ order_id: 9002 }, { $set: { status: "Delivered" } })

// 67. Remove one item from an order.
db.orders.updateOne({ order_id: 9002 }, { $pull: { items: { product: "Gaming Chair" } } })
