// Final Challenge: Suppliers

// Create:
db.createCollection("suppliers")
// Insert:
db.suppliers.insertMany([
    {
        supplier_id: 1, supplier_name: "TechSource India", city: "Chennai", active: true,
        categories: ["Electronics", "Accessories"],
        contact: { person: "Ravi Kumar", email: "ravi@techsource.in", phone: "9876543210" },
        warehouses: ["Chennai", "Bengaluru"], registration_date: ISODate("2025-06-15")
    },
    {
        supplier_id: 2, supplier_name: "FurniCraft Ltd", city: "Hyderabad", active: true,
        categories: ["Furniture", "Home"],
        contact: { person: "Anita Rao", email: "anita@furnicraft.com", phone: "9123456780" },
        warehouses: ["Hyderabad", "Pune"], registration_date: ISODate("2026-02-10")
    },
    {
        supplier_id: 3, supplier_name: "GadgetHub", city: "Mumbai", active: false,
        categories: ["Electronics", "Accessories", "Gaming"],
        contact: { person: "Sameer Shah", email: "sameer@gadgethub.com", phone: "9988776655" },
        warehouses: ["Mumbai", "Delhi"], registration_date: ISODate("2024-11-05")
    },
    {
        supplier_id: 4, supplier_name: "OfficeWorld", city: "Chennai", active: true,
        categories: ["Furniture", "Stationery"],
        contact: { person: "Meena Iyer", email: "meena@officeworld.in", phone: "9012345678" },
        warehouses: ["Chennai", "Coimbatore", "Madurai"], registration_date: ISODate("2026-03-22")
    },
    {
        supplier_id: 5, supplier_name: "SoundWave Traders", city: "Kolkata", active: true,
        categories: ["Electronics", "Audio"],
        contact: { person: "Debashis Roy", email: "debashis@soundwave.com", phone: "9345612780" },
        warehouses: ["Kolkata", "Bhubaneswar"], registration_date: ISODate("2026-05-30")
    }
])

// 76. Display all active suppliers.
db.suppliers.find({ active: true })

// 77. Find suppliers from a city of your choice.
db.suppliers.find({ city: "Chennai" })

// 78. Find suppliers handling Electronics.
db.suppliers.find({ categories: "Electronics" })

// 79. Find suppliers registered after 1 January 2026.
db.suppliers.find({ registration_date: { $gt: ISODate("2026-01-01") } })

// 80. Add another warehouse to one supplier.
db.suppliers.updateOne({ supplier_id: 1 }, { $push: { warehouses: "Hyderabad" } })

// 81. Change the active status of one supplier.
db.suppliers.updateOne({ supplier_id: 3 }, { $set: { active: true } })

// 82. Remove one category from one supplier.
db.suppliers.updateOne({ supplier_id: 3 }, { $pull: { categories: "Gaming" } })

// 83. Display supplier name and city only.
db.suppliers.find({}, { _id: 0, supplier_name: 1, city: 1 })

// 84. Sort suppliers by registration date.
db.suppliers.find().sort({ registration_date: 1 })
