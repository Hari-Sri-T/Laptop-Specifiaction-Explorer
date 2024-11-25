from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .models import get_filter_options, mysql

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    # Check if the user is logged in
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))  # Redirect to login if not logged in

    # Fetch filter options for dropdowns
    filter_options = get_filter_options()
    results = []

    # If form is submitted, process filters
    if request.method == 'POST':
        brand = request.form.get('brands')
        os = request.form.get('os')
        warranty = request.form.get('warranty')
        processor_brand = request.form.get('processor_brand')
        processor_tier = request.form.get('processor_tier')
        storage = request.form.get('storage')
        storage_type = request.form.get('storage_type')
        ram = request.form.get('ram')
        gpu = request.form.get('gpu')
        Price = request.form.get('price')
        dedicated_gpu = request.form.get('gpu_checkbox')
        touch_screen = request.form.get('touchscreen_checkbox')
        bestmac=request.form.get('bestmac')
        bestwin=request.form.get('bestwin')


     

        # Construct SQL query based on selected options
        query = """
            SELECT b.brand_name, l.model, l.price, l.rating 
            FROM laptop l 
            LEFT JOIN brand b ON b.brand_id = l.brand_id 
            LEFT JOIN gpu g ON g.gpu_id = l.gpu_id 
            LEFT JOIN category c ON c.category_id = l.category_id 
            LEFT JOIN processor p ON p.processor_id = l.processor_id 
            WHERE 1 = 1
        """

        # Append conditions to the query if options are selected and valid
        if brand and brand != "Select a brand":
            query += f" AND b.brand_name = '{brand}'"
        if os and os != "Select an OS":
            query += f" AND l.os = '{os}'"
        if warranty and warranty != "Select Warranty":
            query += f" AND l.year_warranty = {warranty}"
        if processor_brand and processor_brand != "Select Processor Brand":
            query += f" AND p.processor_name = '{processor_brand}'"
        if processor_tier and processor_tier != "Select Processor Tier":
            query += f" AND p.processor_tier = '{processor_tier}'"
        if storage and storage != "Select Storage":
            query += f" AND l.primary_storage_capacity = {storage}"
        if storage_type and storage_type != "Select Storage Type":
            query += f" AND l.primary_storage_type = '{storage_type}'"
        if ram and ram != "Select Ram Size":
            query += f" AND l.ram = {ram}"
        if gpu and gpu != "Select Gpu Brand":
            query += f" AND g.gpu_brand = '{gpu}'"
        if Price:
            query += f" AND l.price <= {Price}"

        # Optional checkboxes for specific options
        if dedicated_gpu:
            query += " AND g.gpu_type = 'dedicated'"
        if touch_screen:
            query += " AND touch_screen = 1"

        #bestmac and bestwin functions

        # Execute the query
        cur = mysql.connection.cursor()

        price = request.form.get('price')
        if bestmac and price:

            cur.execute("SELECT BestMac(%s)", (price,))
            results = cur.fetchall()
            cur.close()

        elif bestwin:
            cur.execute("SELECT BestWin(%s)",(price,))
            results = cur.fetchall()
            cur.close()
        else:
            # Execute the standard query if no Best Mac/Best Win options are selected
            cur.execute(query)
            results = cur.fetchall()

        cur.close()

    return render_template('base.html', **filter_options, results=results)
