import mysql.connector

class Sql_db:

    def write_to_db(self, msg):
         cnx = mysql.connector.connect(user='ese', password='ese',
                 host="127.0.0.1",
                              database='elevator')
         Cursor = cnx.cursor()

         floor_req = ("""UPDATE elevatorNetwork SET requestedFloor=%s WHERE nodeID=%s""")

         Cursor.execute(floor_req, (msg, "1"))
         cnx.commit()
         cnx.close()
