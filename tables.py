from flask import Blueprint, render_template, url_for, redirect, request, session

import pypyodbc as odbc

tables = Blueprint( __name__, "tables", static_folder="static", template_folder="templates")

@tables.route('/')
def table_landing():
    return render_template("tables.html")

@tables.route('/official')
def official():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from official
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row[1])
    
    table_headers = ['Official ID', 'First name', 'Last name', 'Phone number', 'Email']
    return render_template("table.html", rows=rows, table_headers=table_headers, size=len(rows[0]), tb_name='Officials Table')

@tables.route('/vehicle')
def vehicle():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from vehicle
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row[1])
    
    table_headers = ['Vehicle ID', 'Number plate', 'Vehicle status', 'Capacity']
    return render_template("table.html", rows=rows, table_headers=table_headers, size=len(rows[0]), tb_name='Vehicles Table')


@tables.route('/carroute')
def carroute():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from car_route
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row[1])
    
    table_headers = ['Route ID', 'car_route']
    return render_template("table.html", rows=rows, table_headers=table_headers, size=len(rows[0]), tb_name='Car Routes Table')

@tables.route('/drivers')
def drivers():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from drivers
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row[1])
    
    table_headers = ['Driver ID', 'First Name', 'Last Name', 'Email', 'Vehicle ID', 'Official ID']
    return render_template("table.html", rows=rows, table_headers=table_headers, size=len(rows[0]), tb_name='Drivers Table')

@tables.route('/comments')
def comments():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from comments
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row[1])
    
    table_headers = ['Comment ID', 'Comment', 'Date Submitted', 'Driver ID', 'Official ID']
    return render_template("table.html", rows=rows, table_headers=table_headers, size=len(rows[0]), tb_name='Comments Table')

@tables.route('/cargroup')
def cargroup():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from car_group
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row[1])
    
    table_headers = ['Group ID', 'Route ID', 'Pickup time', 'Driver ID', 'Car Route']
    return render_template("table.html", rows=rows, table_headers=table_headers, size=len(rows[0]), tb_name='Car Groups Table')

@tables.route('/registration')
def registration():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from registration
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    
    table_headers = ['Reg ID', 'First Name', 'Last Name', 'Phone Number', 'Email', 'Group ID', 'Amount Paid', 'Monthly contribution']
    return render_template("table.html", rows=rows, table_headers=table_headers, size=len(rows[0]), tb_name='Registration Table')