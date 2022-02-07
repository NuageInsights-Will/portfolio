CREATE DATABASE online_store;

CREATE TABLE Customers (
	Customer_ID int NOT NULL AUTO_INCREMENT,
	First_Name varchar(30) NOT NULL,
	Last_Name varchar(30) NOT NULL,
	Phone varchar(30),
	Email varchar(255) NOT NULL,
	Password varchar(30) NOT NULL,
	PRIMARY KEY (Customer_ID)
);

CREATE TABLE Suppliers (
	Supplier_ID int NOT NULL AUTO_INCREMENT,
	Supplier_Name varchar(30),
	Address varchar(255),
	PRIMARY KEY (Supplier_ID)
);

CREATE TABLE Products (
	Product_ID int NOT NULL,
	Product_Name varchar(30) NOT NULL,
	Product_Desc varchar(30),
	Stock int DEFAULT 0,
	Sale_Price float NOT NULL,
	Supplier_Price float NOT NULL,
	Supplier_ID int NOT NULL,
	PRIMARY KEY (Product_ID),
	FOREIGN KEY (Supplier_ID) REFERENCES Suppliers(Supplier_ID)
);

CREATE TABLE Suppliers_Orders (
	Order_ID int NOT NULL AUTO_INCREMENT,
	Product_ID int NOT NULL,
	Supplier_ID int NOT NULL,
	Order_Quantity int NOT NULL,
	Order_Date datetime NOT NULL DEFAULT NOW(),
	Total float,
	PRIMARY KEY (Order_ID),
	FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID),
	FOREIGN KEY (Supplier_ID) REFERENCES Suppliers(Supplier_ID)
);

CREATE TABLE Suppliers_Shipments (
	Order_ID int NOT NULL,
	Product_ID int NOT NULL,
	Product_Name varchar(30),
	Supplier_ID int NOT NULL,
	Order_Quantity int NOT NULL,
	Rec_Quantity int NOT NULL ,
	Order_Date datetime NOT NULL,
	Rec_Date datetime NOT NULL DEFAULT NOW(),
	FOREIGN KEY (Order_ID) REFERENCES Suppliers_Orders(Order_ID),
	FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID),
	FOREIGN KEY (Supplier_ID) REFERENCES Suppliers(Supplier_ID)
);

CREATE TABLE Customers_Orders (
	Order_ID int NOT NULL AUTO_INCREMENT,
	Order_Date datetime NOT NULL DEFAULT NOW(),
	Customer_ID int NOT NULL,
	Product_ID int NOT NULL,
	Order_Quantity int NOT NULL,
	Shipping_Address varchar(255) NOT NULL,
	Billing_Address varchar(255) NOT NULL,
	Payment_Method varchar(30) NOT NULL,
	Transaction_ID varchar(255) NOT NULL,
	Order_Total float,
	PRIMARY KEY (Order_ID),
	FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID),
	FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
);

CREATE TABLE Customers_Shipments (
	Order_ID int NOT NULL,
	Shipment_Method varchar(30) NOT NULL,
	Tracking_Num varchar(50) NOT NULL,
	FOREIGN KEY (Order_ID) REFERENCES Customers_Orders(Order_ID)
);

INSERT INTO Customers (First_Name, Last_Name, Phone, Email, Password)
VALUES ('Henry', 'Dang', '416-123-4567', 'mr.magorium@gmail.com', 'password');

INSERT INTO Suppliers (Supplier_Name, Address)
VALUES ('Walmart', '123 Maple Street Toronto, ON A1B 2C3, Canada');

INSERT INTO Products (Product_ID, Product_Name, Product_Desc, Stock, Sale_Price, Supplier_Price, Supplier_ID)
VALUES (12345, 'Purell Hand Sanitizer 4oz.', 'Original Scent', 20, 4.99, 0.99, 1);

INSERT INTO Customers_Orders (Customer_ID, Product_ID, Order_Quantity, Shipping_Address, Billing_Address, Payment_Method, Transaction_ID, Order_Total)
VALUES (1, 12345, 1, '456 Dundas Street Toronto, ON D4E 5F6, Canada', '456 Dundas Street Toronto, ON D4E 5F6, Canada', 'Visa', '3s49e7521057f7', 4.99);

INSERT INTO Customers_Shipments (Order_ID, Shipment_Method, Tracking_Num)
VALUES (1, 'FedEx', 'E10669746');


















