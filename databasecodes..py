import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from customer import *

def create_connection():
    return sqlite3.connect("misproject.db", timeout=10)

try:
    connection = create_connection()
    process = connection.cursor()

    # Enable foreign key support
    connection.execute('PRAGMA foreign_keys = ON')

    # --------------------- CREATE TABLES ----------------------

    # --- Create CUSTOMERS table ---
    process.execute('''
    CREATE TABLE IF NOT EXISTS CUSTOMERS (
        customerid INTEGER PRIMARY KEY AUTOINCREMENT,
        customername TEXT NOT NULL,
        address TEXT,
        phone INTEGER,
        email TEXT UNIQUE 
    );
    ''')
    connection.commit()

    # --- Create SUPPLIER table ---
    process.execute('''
    CREATE TABLE IF NOT EXISTS SUPPLIER (
        supplierid INTEGER PRIMARY KEY AUTOINCREMENT,
        suppliername TEXT NOT NULL,
        address TEXT,
        email TEXT UNIQUE,
        phone INTEGER,
        country TEXT
    );
    ''')
    connection.commit()

    # --- Create PART_INVENTORY table ---
    process.execute('''
    CREATE TABLE IF NOT EXISTS PART_INVENTORY (
        partid INTEGER PRIMARY KEY AUTOINCREMENT,
        partname TEXT NOT NULL,
        saleprice REAL NOT NULL,
        stocklevel INTEGER NOT NULL,
        supplierid INTEGER,
        reorderlevel INTEGER NOT NULL,
        FOREIGN KEY (supplierid) REFERENCES SUPPLIER(supplierid) 
            ON DELETE SET NULL ON UPDATE CASCADE
    );
    ''')
    connection.commit()

    # --- Create SALES table ---
    process.execute('''
    CREATE TABLE IF NOT EXISTS SALES (
        salesid INTEGER PRIMARY KEY AUTOINCREMENT,
        customerid INTEGER NOT NULL,
        partid INTEGER NOT NULL,
        salesdate TEXT NOT NULL,
        FOREIGN KEY (customerid) REFERENCES CUSTOMERS(customerid) 
            ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (partid) REFERENCES PART_INVENTORY(partid) 
            ON DELETE CASCADE ON UPDATE CASCADE
    );
    ''')
    connection.commit()

    # --- Create WARRANTY_REPAIR table ---
    process.execute('''
    CREATE TABLE IF NOT EXISTS WARRANTY_REPAIR (
        warrantid INTEGER PRIMARY KEY AUTOINCREMENT,
        salesid INTEGER NOT NULL,
        repairstatus TEXT NOT NULL,
        repairdate TEXT,
        warrantyperiod INTEGER NOT NULL,
        warrantystatus TEXT,
        FOREIGN KEY (salesid) REFERENCES SALES(salesid) 
            ON DELETE CASCADE ON UPDATE CASCADE
    );
    ''')
    connection.commit()

    # ------------------ INSERT DATA INTO TABLES ----------------------

    # -- Insert data into CUSTOMERS table --
    process.executemany('''
    INSERT OR IGNORE INTO CUSTOMERS (customername, address, phone, email) VALUES (?, ?, ?, ?)
    ''', [
        ('John Doe', '123 Elm Street', '555-1234', 'johnddoe@example.com'),
        ('Jane Smith', '456 Oak Avenue', '555-5678', 'janesmith@example.com'),
        ('Alice Johnson', '789 Pine Lane', '555-9101', 'aliceyj@example.com'),
        ('Bob Brown', '321 Maple Street', '555-1122', 'bobbb@example.com'),
        ('Charlie White', '654 Birch Road', '555-3344', 'charlyiew@example.com'),
        ('John Smith', '123 Elm Street', '555-4567', 'john.smiith@example.com'),
        ('Doğa Bengü Kotan', 'Bornova', '555-7777', 'dogakotan@example.com'),
        ('Çisem Güre', 'Bornova', '555-8888', 'cisemgure@example.com'),
        ('Melisa Şener', 'Güzelbahçe', '555-9999', 'melisasener@example.com'),
        ('David Miller', '202 Birch Rd', '555-8901', 'daviid.miller@example.com'),
        ('Laura Davis', '303 Cedar Blvd', '555-9012', 'laaura.davis@example.com'),
        ('James Wilson', '04 Walnut St', '555-0783', 'jamess.wilson@example.com'),
        ('Olivia Moore', '505 Ash Dr', '555-1744', 'olivia.moore@example.com'),
        ('Liam Taylor', '606 Pinecrest Ln', '555-2845', 'liamt.taylor@example.com'),
        ('Sophia Anderson', '707 Birch St', '555-8756', 'sophioa.anderson@example.com'),
        ('Benjamin Thomas', '808 Spruce Ave', '555-4967', 'benjamio.thomas@example.com'),
        ('Charlotte Jackson', '909 Cedar Blvd', '555-8678', 'charlottep.jackson@example.com'),
        ('Ethan Harris', '1101 Oak St', '555-2289', 'ethan.harriss@example.com'),
        ('Amelia Martinez', '1201 Pine St', '555-5690', 'ameelia.martinez@example.com'),
        ('Jacob Clark', '1301 Maple Ave', '555-8971', 'jaccob.clark@example.com'),
        ('Ava Lewis', '1401 Birch Rd', '555-9012', 'avva.lewis@example.com'),
        ('Mason Young', '1501 Oak St', '555-0123', 'masoon.young@example.com'),
        ('Isabella King', '1701 Pinecrest Ln', '555-7456', 'isabellla.king@example.com')
    ])

    connection.commit()

      # -- Insert data into SUPPLIER table --

    process.executemany('''
    INSERT OR IGNORE INTO SUPPLIER (suppliername, address, email, phone, country) VALUES (?, ?, ?, ?, ?)
    ''', [('Dragon Auto Parts', 'No. 88, Auto Industrial Park', 'contact@dragonparts.cn', '555-5638', 'China'),
        ('Samurai Motors Supplies', 'Tokyo Industrial Zone, 3rd Street', 'info@samuraimotors.jp', '555-7629', 'Japan'),
        ('Bavarian Auto Components', 'Auto Street 45, Munich', 'support@bavarianauto.de', '555-1882', 'Germany'),
        ('Indus Motor Spares', 'Industrial Hub, New Delhi', 'sales@indusspares.in', '555-3546', 'India'),
        ('Eagle Automotive Supplies', '450 Industrial Blvd, Detroit', 'help@eagleautomotive.us', '555-7812', 'USA'),
        ('Proservice', 'Bayrakli İzmir', 'proservice@example.com', '555-7677', 'Turkiye'),  
        ('Great Wall Auto Spares', 'Industrial Zone A, Beijing', 'service@greatwall.cn', '555-2983', 'Italy'),
        ('Shogun Motor Parts', 'Osaka Motor Zone, 5th Ave', 'support@shogunparts.jp', '555-5853', 'Japan'),
        ('Autobahn Performance Parts', 'Frankfurt Auto Park', 'info@autobahnparts.de', '555-5774', 'Germany'),
        ('Himalaya Automotive Supplies', 'Auto Lane, Mumbai', 'contact@himalayaauto.in', '555-9933', 'India')
          ])

    connection.commit()

 # -- Insert data into PART_INVENTORY table --
      
    process.executemany('''
    INSERT OR IGNORE INTO PART_INVENTORY (partname, saleprice, stocklevel, supplierid, reorderlevel) VALUES (?, ?, ?, ?, ?)
    ''', [('Starter Motor', 50.00, 100, 1, 20),
            ('Cylinder Head', 100.00, 25, 2, 25),
            ('Piston', 100.00, 150, 5, 11),
            ('Connecting Rod', 75.00, 50, 4, 23),
            ('Oil Pump', 150.00, 100, 10, 13),
            ('Gaskets', 50.00, 100, 9, 35),
            ('Radiator', 200.00, 45, 6, 22),
            ('Air Filter', 75.00, 150, 7, 24),
            ('Oil Filter', 175.00, 110, 2, 14),
            ('Manifolds', 82.00, 103, 3, 5),
            ('Spark Plug', 45.00, 200, 9, 50),
            ('Fuel Pump', 135.00, 75, 10, 45),
            ('Water Pump', 67.00, 89, 1, 15),
            (' Injection (Diesel) Pump', 245.00, 34, 7, 23),
            ('Control Arm', 143.00, 67, 2, 17),
            ('Transmission', 78.00, 13, 5, 60),
            ('Differential', 150.00, 45, 7, 74)
         ])

    connection.commit()

 # -- Insert data into SALES table --
      
    process.executemany('''
    INSERT OR IGNORE INTO SALES (customerid, partid, salesdate) VALUES (?, ?, ?)
         ''', [(1, 1, '2024-01-15'),
                (23, 17, '2023-06-10'),
                (3, 5, '2023-12-01'),
                (10, 8, '2022-09-20'),
                (5, 11, '2024-08-30'),
                (9, 3, '2023-03-25'),
                (7, 2, '2024-07-15'),
                (8, 13, '2023-11-05'),
                (17, 10, '2022-02-18'),
                (10, 6, '2024-04-10'),
                (22, 8, '2022-02-18'),
                (15, 9, '2022-12-19'),
                (9, 16, '2024-04-01'),
                (13, 7, '2024-09-03'),
                (8, 14, '2022-02-05'),
                (4, 1, '2024-05-09'),
                (6, 2, '2022-03-06'),
                (21, 3, '2024-04-10'),
                (12, 4, '2022-02-18'),
                (8, 5, '2022-12-19'),
                (9, 6, '2024-04-01'),
                (6, 7, '2024-09-03'),
                (13, 8, '2022-02-05'),
                (21, 9, '2024-12-19'),
                (22, 10, '2022-03-26'),
                (20, 11, '2024-04-19'),
                (12, 12, '2022-12-30'),
                (17, 13, '2022-12-05'),
                (10, 14, '2024-12-24'),
                (6, 15, '2024-07-19'),
                (8, 16, '2022-02-25'),
                (19, 17, '2024-05-29'),
                (14, 7, '2022-03-31')
         ])

    connection.commit()

    process.executemany('''
    INSERT OR IGNORE INTO WARRANTY_REPAIR (salesid, repairstatus, repairdate, warrantyperiod, warrantystatus) VALUES (?, ?, ?, ?,?)
    ''', [(66, 'In Progress', '2024-01-15',1,'Active'),
            (7, 'Completed', '2023-07-10', 3,'Expired'),
            (8, 'Pending', '2024-07-10',2, 'Active'),
            (9, 'Completed', '2024-10-20',2, 'Active'),
            (17, 'In Progress', '2024-09-01',3, 'Active'),
            (11, 'Completed', '2023-05-10',1, 'Expired'),
            (12, 'Awaiting Parts', '2023-03-14', 2,'Expired'),
            (13, 'Pending', '2023-12-15', 2, 'Expired'),
            (14, 'Completed', '2022-04-15',3, 'Expired'),
            (15, 'In Progress', '2024-12-31',3, 'Active'),
            (16, 'Completed', '2022-03-20',1, 'Expired'),
            (2, 'In Progress', '2024-11-10',1, 'Active'),
            (18, 'Completed', '2023-11-01',2, 'Expired'),
            (19, 'Completed', '2024-07-18',3, 'Active'),
            (10, 'Pending', '2024-08-03',2, 'Active'),
            (11, 'Completed', '2022-12-12', 1,'Expired'),
            (12, 'In Progress', '2024-12-20',1, 'Active'),
            (13, 'Completed', '2024-12-30',2, 'Expired'),
            (14, 'Pending', '2024-12-10', 3,'Active'),
            (44, 'Pending', '2023-12-15',1,'Expired')      
            ])

    connection.commit()

except sqlite3.Error as e:
    print(f"SQLite error: {e}")

finally:
    if connection:
        connection.commit()
        connection.close()