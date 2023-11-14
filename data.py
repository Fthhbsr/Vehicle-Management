from models import User, Holding, Company, Vehicle


records = [
            User(id=1, name="Ali", last_name="Alkan", email="ali@mail.com", password="12345", company_id=1),
            User(id=2, name="Veli", last_name="Balkan", email="veli@mail.com", password="12345", company_id=2),
            User(id=3, name="Hafsa", last_name="Tekin", email="hafsa@mail.com", password="12345", company_id=3),
            User(id=4, name="Ayşe", last_name="Yılmaz", email="ayse@mail.com", password="12345", company_id=4),
            Holding(id=1, holding_name="Holding A"),
            Company(id=1, company_name="Company Holding", holding_id=1), 
            Company(id=2, company_name="Company A", holding_id=1), 
            Company(id=3, company_name="Company B", holding_id=1), 
            Company(id=4, company_name="Company C", holding_id=1), 
            Vehicle(id=1, vehicle_name="Skoda", company_id=1), 
            
        ]
