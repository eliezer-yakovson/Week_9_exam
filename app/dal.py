from typing import List, Dict, Any

from app.db import get_db_connection

def get_customers_by_credit_limit_range():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT customerName, creditLimit
        FROM customers
        WHERE creditLimit < 10000 OR creditLimit > 100000
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def get_orders_with_null_comments():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT orderNumber, comments
        FROM orders
        WHERE comments IS NULL
        ORDER BY orderDate
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def get_first_5_customers():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT customerName, contactLastName, contactFirstName
        FROM customers
        ORDER BY contactLastName
        LIMIT 5
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def get_payments_total_and_average():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        SELECT SUM(amount) AS total_payments, AVG(amount) AS average_payment, MIN(amount) AS min_payment, MAX(amount) AS max_payment
        FROM payments
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def get_employees_with_office_phone():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
       SELECT e.firstName, e.lastName, o.phone
       FROM employees e
       JOIN offices o ON e.officeCode = o.officeCode
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
    
def get_customers_with_shipping_dates():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
       SELECT c.customerName, o.shippedDate
       FROM customers c
       LEFT JOIN orders o ON c.customerNumber = o.customerNumber
       GROUP BY c.customerName, o.shippedDate
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def get_customer_quantity_per_order():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
       SELECT c.customerName, od.quantityOrdered
       FROM customers c
       JOIN orders o ON c.customerNumber = o.customerNumber
       JOIN orderdetails od ON o.orderNumber = od.orderNumber
       ORDER BY c.customerNumber
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def get_customers_payments_by_lastname_pattern():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
       SELECT c.customerName, CONCAT(c.contactFirstName, ' ', c.contactLastName) AS ContactfullName, SUM(p.amount) AS total_payments
       FROM customers c
       JOIN payments p ON c.customerNumber = p.customerNumber
       WHERE c.contactFirstName LIKE '%Mu%' OR c.contactFirstName LIKE '%ly%'
       GROUP BY c.customerName, ContactfullName
       ORDER BY total_payments DESC
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
