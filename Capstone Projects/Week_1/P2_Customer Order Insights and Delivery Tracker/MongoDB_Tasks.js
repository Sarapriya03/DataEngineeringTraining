// Customer Order Insights and Delivery Tracker

use("customer_orders");

// 1. SAMPLE FEEDBACK DATA
// (unstructured: some documents have 'tags', one has no 'order_id')
db.feedback.insertMany([
  {
    "feedback_id": "FB-101",
    "customer_id": 1,
    "order_id": 1,
    "rating": 5,
    "comment": "Fast delivery and the mouse works great.",
    "feedback_date": "2026-09-06"
  },
  {
    "feedback_id": "FB-102",
    "customer_id": 1,
    "order_id": 2,
    "rating": 2,
    "comment": "Bag arrived 3 days late and the courier did not call.",
    "feedback_date": "2026-09-18",
    "tags": [
      "late delivery",
      "courier"
    ]
  },
  {
    "feedback_id": "FB-103",
    "customer_id": 1,
    "order_id": 3,
    "rating": 1,
    "comment": "Still has not arrived after 10 days. Very disappointed.",
    "feedback_date": "2026-10-09",
    "tags": [
      "late delivery"
    ]
  },
  {
    "feedback_id": "FB-104",
    "customer_id": 2,
    "order_id": 4,
    "rating": 5,
    "comment": "Speaker was delivered on time. Sound quality is excellent.",
    "feedback_date": "2026-09-08"
  },
  {
    "feedback_id": "FB-105",
    "customer_id": 2,
    "order_id": 5,
    "rating": 3,
    "comment": "Delivery was late because of rain but the case is good.",
    "feedback_date": "2026-09-25",
    "tags": [
      "weather"
    ]
  },
  {
    "feedback_id": "FB-106",
    "customer_id": 3,
    "order_id": 6,
    "rating": 4,
    "comment": "Keyboard is good. Packaging could be better.",
    "feedback_date": "2026-09-09"
  },
  {
    "feedback_id": "FB-107",
    "customer_id": 3,
    "order_id": 8,
    "rating": 1,
    "comment": "Courier said address not found but my address is correct.",
    "feedback_date": "2026-10-07",
    "tags": [
      "address issue",
      "late delivery"
    ]
  },
  {
    "feedback_id": "FB-108",
    "customer_id": 4,
    "order_id": 9,
    "rating": 5,
    "comment": "Headphones arrived a day early. Great service!",
    "feedback_date": "2026-09-10"
  },
  {
    "feedback_id": "FB-109",
    "customer_id": 4,
    "order_id": 10,
    "rating": 2,
    "comment": "Smart watch delivery was delayed by 5 days.",
    "feedback_date": "2026-09-30",
    "tags": [
      "late delivery"
    ]
  },
  {
    "feedback_id": "FB-110",
    "customer_id": 5,
    "order_id": 11,
    "rating": 3,
    "comment": "Backpack is fine but delivery took longer than promised.",
    "feedback_date": "2026-09-15"
  },
  {
    "feedback_id": "FB-111",
    "customer_id": 6,
    "order_id": 13,
    "rating": 4,
    "comment": "Lamp is nice and arrived on time.",
    "feedback_date": "2026-09-14"
  },
  {
    "feedback_id": "FB-112",
    "customer_id": 6,
    "order_id": 14,
    "rating": 2,
    "comment": "Order delayed because the item was out of stock.",
    "feedback_date": "2026-10-05",
    "tags": [
      "stock shortage"
    ]
  },
  {
    "feedback_id": "FB-113",
    "customer_id": 7,
    "order_id": 16,
    "rating": 2,
    "comment": "Delivery person could not find my house, had to call twice.",
    "feedback_date": "2026-10-09",
    "tags": [
      "address issue"
    ]
  },
  {
    "feedback_id": "FB-114",
    "customer_id": 8,
    "order_id": 17,
    "rating": 5,
    "comment": "Yoga mat quality is great. On-time delivery.",
    "feedback_date": "2026-09-19"
  },
  {
    "feedback_id": "FB-115",
    "customer_id": 8,
    "rating": 4,
    "comment": "Please add more payment options on the website.",
    "feedback_date": "2026-10-08",
    "tags": [
      "website"
    ]
  }
]);

// 2. INDEX - search feedback by customer ID
db.feedback.createIndex({ customer_id: 1 });

// 3. QUERIES
db.feedback.find({ customer_id: 1 }); // all feedback from customer 1
db.feedback.find({ rating: { $lte: 2 } }); // unhappy customers
db.feedback.find({ tags: "late delivery" }); // feedback about late delivery
db.feedback.find({ comment: /address/i }); // search comment text

// average rating per customer
db.feedback.aggregate([
  { $group: { _id: "$customer_id", avg_rating: { $avg: "$rating" }, total: { $sum: 1 } } },
  { $sort: { avg_rating: 1 } }
]);

// UPDATE: add a reply to a feedback
db.feedback.updateOne({ feedback_id: "FB-103" }, { $set: { reply: "Sorry for the delay. Refund initiated." } });

// INSERT + DELETE
db.feedback.insertOne({ feedback_id: "FB-199", customer_id: 5, order_id: 12, rating: 4,
                        comment: "Good bottle, fast delivery.", feedback_date: "2026-10-10" });
db.feedback.deleteOne({ feedback_id: "FB-199" });

// Confirm the index is used (look for IXSCAN in the output)
db.feedback.find({ customer_id: 1 }).explain("executionStats").queryPlanner.winningPlan;
