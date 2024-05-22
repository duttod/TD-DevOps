// Création de la base de données devops
db = db.getSiblingDB('devops');

// Insertion des données JSON dans la collection users de la base de données devops
db.users.insertMany([
    {
        "firstName": "Emma",
        "lastName": "Brown",
        "age": 30,
        "email": "emma.brown@example.com"
    },
    {
        "firstName": "Alice",
        "lastName": "Smith",
        "age": 25,
        "email": "alice.smith@example.com"
    },
    {
        "firstName": "Bob",
        "lastName": "Johnson",
        "age": 28,
        "email": "bob.johnson@example.com"
    }
]);