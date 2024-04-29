from flask import Blueprint, render_template, url_for, redirect, request, session

import pypyodbc as odbc

tables = Blueprint( __name__, "tables", static_folder="static", template_folder="templates")

@tables.route('/officials')
def officials():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from officials
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row[1])
    
    table_headers = ['Official ID', 'First name', 'Last name', 'Phone number', 'Email']
    return render_template("table.html", rows=rows, table_headers=table_headers)

@tables.route('/vehicle')
def vehicles():
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
    return render_template("table.html", rows=rows, table_headers=table_headers)


@tables.route('/carroute')
def vehicles():
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
    return render_template("table.html", rows=rows, table_headers=table_headers)

@tables.route('/drivers')
def vehicles():
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
    
    table_headers = ['Driver ID', 'First Name', 'Last Name', 'Vehicle ID', 'Official ID']
    return render_template("table.html", rows=rows, table_headers=table_headers)

@tables.route('/vehicle')
def vehicles():
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
    return render_template("table.html", rows=rows, table_headers=table_headers)

@tables.route('/vehicle')
def vehicles():
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
    return render_template("table.html", rows=rows, table_headers=table_headers)
