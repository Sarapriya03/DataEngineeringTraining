// Supply Chain Project - Week 1 (SIMPLE VERSION) - MongoDB
// Run in mongosh (paste it, or: mongosh --file simple_mongodb_shipments.js)

use("supply_chain");
db.shipments.drop();

// 1. DATA
db.shipments.insertMany([
  {
    "shipment_id": "SHP-1001",
    "order_id": 1,
    "supplier_id": 1,
    "carrier": "Delhivery",
    "origin_city": "Coimbatore",
    "ship_date": "2026-09-02",
    "expected_date": "2026-09-08",
    "delivery_date": "2026-09-07",
    "status": "Delivered",
    "delay_days": 0
  },
  {
    "shipment_id": "SHP-1002",
    "order_id": 2,
    "supplier_id": 1,
    "carrier": "DTDC",
    "origin_city": "Coimbatore",
    "ship_date": "2026-09-03",
    "expected_date": "2026-09-09",
    "delivery_date": "2026-09-12",
    "status": "Delivered",
    "delay_days": 3
  },
  {
    "shipment_id": "SHP-1003",
    "order_id": 3,
    "supplier_id": 2,
    "carrier": "Blue Dart",
    "origin_city": "Bengaluru",
    "ship_date": "2026-09-04",
    "expected_date": "2026-09-13",
    "delivery_date": "2026-09-13",
    "status": "Delivered",
    "delay_days": 0
  },
  {
    "shipment_id": "SHP-1004",
    "order_id": 4,
    "supplier_id": 2,
    "carrier": "Blue Dart",
    "origin_city": "Bengaluru",
    "ship_date": "2026-09-06",
    "expected_date": "2026-09-15",
    "delivery_date": "2026-09-20",
    "status": "Delivered",
    "delay_days": 5
  },
  {
    "shipment_id": "SHP-1005",
    "order_id": 5,
    "supplier_id": 3,
    "carrier": "DTDC",
    "origin_city": "Chennai",
    "ship_date": "2026-09-07",
    "expected_date": "2026-09-10",
    "delivery_date": "2026-09-10",
    "status": "Delivered",
    "delay_days": 0
  },
  {
    "shipment_id": "SHP-1006",
    "order_id": 6,
    "supplier_id": 3,
    "carrier": "Gati",
    "origin_city": "Chennai",
    "ship_date": "2026-09-09",
    "expected_date": "2026-09-13",
    "delivery_date": "2026-09-16",
    "status": "Delivered",
    "delay_days": 3
  },
  {
    "shipment_id": "SHP-1007",
    "order_id": 7,
    "supplier_id": 4,
    "carrier": "Gati",
    "origin_city": "Pune",
    "ship_date": "2026-09-11",
    "expected_date": "2026-09-20",
    "delivery_date": "2026-09-19",
    "status": "Delivered",
    "delay_days": 0
  },
  {
    "shipment_id": "SHP-1008",
    "order_id": 8,
    "supplier_id": 4,
    "carrier": "Gati",
    "origin_city": "Pune",
    "ship_date": "2026-09-13",
    "expected_date": "2026-09-22",
    "delivery_date": "2026-09-28",
    "status": "Delivered",
    "delay_days": 6
  },
  {
    "shipment_id": "SHP-1009",
    "order_id": 9,
    "supplier_id": 5,
    "carrier": "Delhivery",
    "origin_city": "Mumbai",
    "ship_date": "2026-09-16",
    "expected_date": "2026-09-25",
    "delivery_date": "2026-09-25",
    "status": "Delivered",
    "delay_days": 0
  },
  {
    "shipment_id": "SHP-1010",
    "order_id": 10,
    "supplier_id": 5,
    "carrier": "Delhivery",
    "origin_city": "Mumbai",
    "ship_date": "2026-09-19",
    "expected_date": "2026-09-28",
    "delivery_date": "2026-10-02",
    "status": "Delivered",
    "delay_days": 4
  },
  {
    "shipment_id": "SHP-1011",
    "order_id": 11,
    "supplier_id": 3,
    "carrier": "DTDC",
    "origin_city": "Chennai",
    "ship_date": "2026-09-26",
    "expected_date": "2026-09-30",
    "delivery_date": null,
    "status": "Delayed",
    "delay_days": 10
  },
  {
    "shipment_id": "SHP-1012",
    "order_id": 12,
    "supplier_id": 2,
    "carrier": "Blue Dart",
    "origin_city": "Bengaluru",
    "ship_date": "2026-09-29",
    "expected_date": "2026-10-05",
    "delivery_date": null,
    "status": "Delayed",
    "delay_days": 5
  },
  {
    "shipment_id": "SHP-1013",
    "order_id": 13,
    "supplier_id": 4,
    "carrier": "Gati",
    "origin_city": "Pune",
    "ship_date": "2026-10-03",
    "expected_date": "2026-10-12",
    "delivery_date": null,
    "status": "In Transit",
    "delay_days": 0
  },
  {
    "shipment_id": "SHP-1014",
    "order_id": 14,
    "supplier_id": 1,
    "carrier": "Delhivery",
    "origin_city": "Coimbatore",
    "ship_date": "2026-10-06",
    "expected_date": "2026-10-15",
    "delivery_date": null,
    "status": "In Transit",
    "delay_days": 0
  }
]);

// 2. INDEXES
db.shipments.createIndex({ order_id: 1 }, { unique: true });
db.shipments.createIndex({ supplier_id: 1 });
db.shipments.createIndex({ status: 1 });

// 3. QUERIES
db.shipments.find({ status: "Delayed" });                          // delayed shipments
db.shipments.find({ delay_days: { $gt: 0 } });                     // all late shipments
db.shipments.findOne({ order_id: 4 });                             // shipment for one order

// late shipments per supplier
db.shipments.aggregate([
  { $match: { delay_days: { $gt: 0 } } },
  { $group: { _id: "$supplier_id", late_shipments: { $sum: 1 } } },
  { $sort: { late_shipments: -1 } }
]);

// UPDATE: order 11 finally delivered
db.shipments.updateOne(
  { order_id: 11 },
  { $set: { status: "Delivered", delivery_date: "2026-10-10" } }
);

// INSERT + DELETE
db.shipments.insertOne({ shipment_id: "SHP-1099", order_id: 99, supplier_id: 1, carrier: "DTDC",
  origin_city: "Coimbatore", ship_date: "2026-10-10", expected_date: "2026-10-17",
  delivery_date: null, status: "In Transit", delay_days: 0 });
db.shipments.deleteOne({ order_id: 99 });
