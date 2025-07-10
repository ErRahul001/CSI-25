
-- Create SQL Server Tables with CDC
CREATE TABLE Customer (
  CustomerID INT PRIMARY KEY,
  Name NVARCHAR(100),
  Address NVARCHAR(255),
  Email NVARCHAR(100),
  Phone NVARCHAR(20),
  ModifiedAt DATETIME2 DEFAULT GETDATE()
);
CREATE TABLE Product (
  ProductID INT PRIMARY KEY,
  Name NVARCHAR(100),
  Description NVARCHAR(255),
  Price DECIMAL(10,2),
  Category NVARCHAR(50),
  ModifiedAt DATETIME2 DEFAULT GETDATE()
);
CREATE TABLE Orders (
  OrderID INT PRIMARY KEY,
  CustomerID INT FOREIGN KEY REFERENCES Customer(CustomerID),
  ProductID INT FOREIGN KEY REFERENCES Product(ProductID),
  Quantity INT,
  OrderDate DATETIME2,
  TotalAmount DECIMAL(12,2),
  ModifiedAt DATETIME2 DEFAULT GETDATE()
);
CREATE TABLE Inventory (
  ProductID INT PRIMARY KEY FOREIGN KEY REFERENCES Product(ProductID),
  Quantity INT,
  Location NVARCHAR(100),
  ModifiedAt DATETIME2 DEFAULT GETDATE()
);

-- Enable CDC
EXEC sys.sp_cdc_enable_db;
EXEC sys.sp_cdc_enable_table @source_schema = N'dbo', @source_name = N'Customer',  @role_name = NULL, @supports_net_changes = 1;
EXEC sys.sp_cdc_enable_table @source_schema = N'dbo', @source_name = N'Product',   @role_name = NULL, @supports_net_changes = 1;
EXEC sys.sp_cdc_enable_table @source_schema = N'dbo', @source_name = N'Orders',    @role_name = NULL, @supports_net_changes = 1;
EXEC sys.sp_cdc_enable_table @source_schema = N'dbo', @source_name = N'Inventory', @role_name = NULL, @supports_net_changes = 1;
