// Final Challenge: Delivery Partners

// Create a new collection called: delivery_partners
db.createCollection("delivery_partners")
// Insert:
db.delivery_partners.insertMany([
    {
        partner_id: 1, partner_name: "Ravi Kumar", city: "Hyderabad", rating: 4.6, active: true, vehicle: "Bike",
        service_areas: ["Banjara Hills", "Madhapur"], contact: { phone: "9876500001", email: "ravi@partners.com" }
    },
    {
        partner_id: 2, partner_name: "Sana Khan", city: "Hyderabad", rating: 3.8, active: false, vehicle: "Scooter",
        service_areas: ["Gachibowli", "Kondapur"], contact: { phone: "9876500002", email: "sana@partners.com" }
    },
    {
        partner_id: 3, partner_name: "Arjun Mehta", city: "Mumbai", rating: 4.3, active: true, vehicle: "Bike",
        service_areas: ["Andheri", "Bandra"], contact: { phone: "9876500003", email: "arjun@partners.com" }
    },
    {
        partner_id: 4, partner_name: "Priya Nair", city: "Bangalore", rating: 4.8, active: true, vehicle: "Electric Scooter",
        service_areas: ["Indiranagar", "Koramangala"], contact: { phone: "9876500004", email: "priya@partners.com" }
    },
    {
        partner_id: 5, partner_name: "Imran Ali", city: "Hyderabad", rating: 4.1, active: true, vehicle: "Bicycle",
        service_areas: ["Secunderabad", "Begumpet"], contact: { phone: "9876500005", email: "imran@partners.com" }
    }
])

// 29. Find active delivery partners from Hyderabad.
db.delivery_partners.find({ active: true, city: "Hyderabad" })

// 30. Find partners with rating greater than 4.
db.delivery_partners.find({ rating: { $gt: 4 } })

// 31. Add a new service area to one partner.
db.delivery_partners.updateOne({ partner_id: 1 }, { $push: { service_areas: "Jubilee Hills" } })

// 32. Update one partner's rating.
db.delivery_partners.updateOne({ partner_id: 2 }, { $set: { rating: 4.0 } })

// 33. Sort all partners from highest rating to lowest.
db.delivery_partners.find().sort({ rating: -1 })

