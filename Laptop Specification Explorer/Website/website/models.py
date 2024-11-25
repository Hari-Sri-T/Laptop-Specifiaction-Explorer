from flask import current_app
from flask_mysqldb import MySQL

# Initialize MySQL
mysql = MySQL()

def init_db(app):
    mysql.init_app(app)

def get_filter_options():
    # Open connection to MySQL
    cur = mysql.connection.cursor()

    # Fetch filter options from the database
    cur.execute("SELECT DISTINCT brand_name FROM brand order by brand_name asc")
    brands = cur.fetchall()

    cur.execute("SELECT DISTINCT os FROM laptop order by os asc")
    os_options = cur.fetchall()

    cur.execute("SELECT DISTINCT year_warranty FROM laptop order by year_warranty asc")
    warranty_options = cur.fetchall()

    cur.execute("SELECT DISTINCT processor_name FROM processor")
    processor_brand = cur.fetchall()  # This matches the HTML

    cur.execute("SELECT DISTINCT processor_tier FROM processor order by processor_tier asc")
    processor_tier = cur.fetchall()  # This matches the HTML

    cur.execute("SELECT DISTINCT primary_storage_capacity FROM laptop order by primary_storage_capacity asc")
    storage_sizes = cur.fetchall()  # This matches the HTML

    cur.execute("SELECT DISTINCT primary_storage_type FROM laptop")  # Assuming you have a column for secondary storage
    storage_type = cur.fetchall()  # This matches the HTML

    cur.execute("SELECT DISTINCT ram FROM laptop order by ram asc")
    ram_sizes = cur.fetchall()  # This matches the HTML

    cur.execute("SELECT DISTINCT gpu_brand FROM gpu")
    gpu = cur.fetchall()  # This matches the HTML

    # Close the cursor
    cur.close()

    return {
        'brands': brands,
        'os_options': os_options,
        'warranty_options': warranty_options,
        'processor_brand': processor_brand,  # This matches the HTML
        'processor_tier': processor_tier,  # This matches the HTML
        'storage_sizes': storage_sizes,  # This matches the HTML
        'storage_type': storage_type,  # This matches the HTML
        'ram_sizes': ram_sizes,
        'gpu': gpu,  # This matches the HTML
    }

