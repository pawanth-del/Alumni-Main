from app import app, db
from models import User
from datetime import datetime

# Create an application context
with app.app_context():
    # Create the database and the db table
    db.create_all()

    # Define the dummy data
    dummy_users = [
        User(
            email=f"user{i}@example.com",
            first_name=f"FirstName{i}",
            middle_name=f"M{i}",
            last_name=f"LastName{i}",
            phone_number=f"123456789{i:02d}",
            country_code="+1",
            is_whatsapp_same=True,
            gender="Male" if i % 2 == 0 else "Female",
            year_of_graduation=2020 + i,
            branch="CSE",
            accompanied_person=f"Accomp{i}",
            parents=bool(i % 2),
            children=bool((i + 1) % 2),
            order_id=f"ORD{i:03d}",
            order_total=100.00 + i,
            contribution_amount=50.00 + i,
            order_status="completed" if i % 2 == 0 else "pending",
            initiated_at=datetime.now(),
            updated_at=datetime.now(),
            created_at=datetime.now(),
            is_active=True
        )
        for i in range(1, 21)
    ]

    # Insert the dummy data into the database
    db.session.add_all(dummy_users)

    # Commit the changes to the database
    db.session.commit()

    print("Database setup complete with dummy data inserted.")
