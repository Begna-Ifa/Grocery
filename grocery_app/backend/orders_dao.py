from future.backports.datetime import datetime
from future.backports.http.client import responses

from sql_connection import get_sql_connection


def insert_order(connection, order):
    cursor = connection.cursor()

    order_query = (
        "INSERT INTO orders (customer_name, tot_price, date) "
        "VALUES (%s, %s, %s)"
    )
    order_data = (
        order['customer_name'],
        float(order['grand_total']),
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

    try:
        # Insert into orders table
        cursor.execute(order_query, order_data)
        order_id = cursor.lastrowid  # Get the inserted order's ID

        # Insert into order_details table
        order_details_query = (
            "INSERT INTO order_details (order_id, product_id, quantity, total_price) "
            "VALUES (%s, %s, %s, %s)"
        )
        order_details_data = [
            (order_id, int(detail['product_id']), float(detail['quantity']), float(detail['total_price']))
            for detail in order['order_details']
        ]
        cursor.executemany(order_details_query, order_details_data)

        # Commit changes to the database
        connection.commit()
        return order_id
    except Exception as e:
        connection.rollback()  # Rollback in case of an error
        print("Error:", e)
        return None
    finally:
        cursor.close()  # Ensure the cursor is closed

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)

    responses = []
    for( order_id,customer_name,tot_price,date) in cursor:
        responses.append({
            'order_id': order_id,
            'costumer_name': customer_name,
            'tot_price': tot_price,
            'date': date

        })
    return responses
if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))
