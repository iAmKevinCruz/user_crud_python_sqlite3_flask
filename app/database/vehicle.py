from app.database import get_db


def vehicle_formatter(results: tuple):
    out = []
    for result in results:
        result_dict = {}
        result_dict["id"] = result[0]
        result_dict["license_plate"] = result[1]
        result_dict["v_type"] = result[2]
        result_dict["color"] = result[3]
        result_dict["parking_spot_no"] = result[4]
        result_dict["description"] = result[5]
        result_dict["user_id"] = result[6]
        out.append(result_dict)
    return out


def scan():
    cursor = get_db().execute("SELECT * FROM vehicle", ())
    results = cursor.fetchall()
    cursor.close()
    return vehicle_formatter(results)


def select(vehicle_id):
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE id=?",
        (vehicle_id, )
    )
    results = cursor.fetchall()
    cursor.close()
    return vehicle_formatter(results)

def select_by_user_id(user_id):
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE user_id=?",
        (user_id, )
    )
    results = cursor.fetchall()
    cursor.close()
    return vehicle_formatter(results)

def update(vehicle_id):
    cursor = get_db()
    cursor.execute(
        "UPDATE vehicle SET license_plate=? v_type=? color=? parking_spot_no=? description=? user_id=? WHERE id=?",
        (vehicle_id, )
    )
    cursor.commit()
    cursor.close()


def insert(license_plate, v_type, color, parking_spot_no, user_id, description=None):
    value_tuple = (license_plate, v_type, color, parking_spot_no, description, user_id)
    query = """
            INSERT INTO vehicle (
                license_plate,
                v_type,
                color,
                parking_spot_no,
                description,
                user_id
            ) VALUES (
                ?, ?, ?, ?, ?, ?
            )
    """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    cursor.close()
    return last_row_id
