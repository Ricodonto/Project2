from flask import Blueprint, render_template, url_for, redirect, request, session

import pypyodbc as odbc

views = Blueprint( __name__, "views", static_folder="static", template_folder="templates")

@views.route('/')
def views_landing():
    return render_template("views.html")

@views.route('/schedule')
def schedule():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from [Schedule]
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row[1])
    
    table_headers = ['Car Route', 'Vehicle ID', 'Reg ID', 'Pickup time', 'First Name', 'Last Name', 'Driver ID', 'Group ID']
    return render_template("table.html", rows=rows, table_headers=table_headers, size=len(rows[0]), tb_name="Schedule View")

@views.route('/owed')
def owed():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from [Owed]
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row[1])
    
    table_headers = ['First Name', 'Last Name', 'Phone Number', 'Email', 'Group ID', 'Amount Paid', 'Monthly Contribution', 'Balance']
    return render_template("table.html", rows=rows, table_headers=table_headers, size=len(rows[0]), tb_name="Owed View")

@views.route('/monthly')
def monthly():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from [Monthly_contribution]
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row[1])
    
    table_headers = ['Reg ID', 'First Name', 'Last Name', 'Phone Number', 'Monthly Contribution']
    return render_template("table.html", rows=rows, table_headers=table_headers, size=len(rows[0]), tb_name="Monthly Contribution View")

@views.route('/members')
def members():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from [Members]
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row[1])
    
    table_headers = ['First Name', 'Last Name', 'Phone Number', 'Email', 'Group ID', 'Amount Paid', 'Monthly Contribution', 'Balance']
    return render_template("table.html", rows=rows, table_headers=table_headers, size=len(rows[0]), tb_name="Members View")


@views.route('/fine')
def fine():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from [Fine]
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row[1])
    
    table_headers = ['Comment ID', 'Driver ID', 'Comment', 'Official ID', 'Date Submitted', 'Fine']
    return render_template("table.html", rows=rows, table_headers=table_headers, size=len(rows[0]), tb_name="Fine View")

@views.route('/broken')
def broken():
    cnxn_str = session['cnxn_str']
    conn = odbc.connect(cnxn_str, autocommit=True)
    cursor = conn.cursor()
    SQL_STATEMENT = """
    select * from [Broken vehicles]
    """

    cursor.execute(SQL_STATEMENT)
    rows = cursor.fetchall()

    for row in rows:
        print(row[1])
    
    table_headers = ['Vehicle ID', 'Number Plate', 'Vehicle Status', 'Capacity']
    return render_template("table.html", rows=rows, table_headers=table_headers, size=len(rows[0]), tb_name="Broken Vehicles View")
