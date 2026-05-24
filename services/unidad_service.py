from database import conectar_mysql

# =========================
# LISTAR
# =========================

def listar_unidades():

    conexion = conectar_mysql()

    cursor = conexion.cursor(dictionary=True)

    sql = "SELECT * FROM unidad"

    cursor.execute(sql)

    datos = cursor.fetchall()

    conexion.close()

    return datos


# =========================
# INSERTAR
# =========================

def insertar_unidad(descripcion):

    conexion = conectar_mysql()

    cursor = conexion.cursor()

    sql = """
        INSERT INTO unidad(descripcion)
        VALUES(%s)
    """

    valores = (descripcion,)

    cursor.execute(sql, valores)

    conexion.commit()

    conexion.close()


# =========================
# ACTUALIZAR
# =========================

def actualizar_unidad(id, descripcion):

    conexion = conectar_mysql()

    cursor = conexion.cursor()

    sql = """
        UPDATE unidad
        SET descripcion=%s
        WHERE id=%s
    """

    valores = (
        descripcion,
        id
    )

    cursor.execute(sql, valores)

    conexion.commit()

    conexion.close()


# =========================
# ELIMINAR
# =========================

def eliminar_unidad(id):

    conexion = conectar_mysql()

    cursor = conexion.cursor()

    sql = "DELETE FROM unidad WHERE id=%s"

    valores = (id,)

    cursor.execute(sql, valores)

    conexion.commit()

    conexion.close()