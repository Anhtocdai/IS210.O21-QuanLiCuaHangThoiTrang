import cx_Oracle

# Khởi tạo Oracle Client
cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\DungManh Laptop\Downloads\instantclient-basic-windows.x64-21.13.0.0.0dbru\instantclient_21_13")

# Cấu hình chuỗi kết nối trực tiếp
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="orcl")

# Kết nối với cơ sở dữ liệu
conn = cx_Oracle.connect(user="c##django", password="django", dsn=dsn)

# Tạo một cursor để thực hiện các truy vấn SQL
cursor = conn.cursor()

# Thêm một hàng mới vào bảng store_orderitem
cursor.execute("""
INSERT INTO store_orderitem (product_id, order_id, quantity, date_added) 
VALUES (1, 1, 5, TO_TIMESTAMP('02-JUN-24 05.15.19.186407000 AM', 'DD-MON-YY HH.MI.SS.FF AM'))
""")

# Commit các thay đổi vào cơ sở dữ liệu
conn.commit()

# Đóng cursor và kết nối
cursor.close()
conn.close()
