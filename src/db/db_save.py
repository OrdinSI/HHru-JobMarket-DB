class DBSave:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def data_saving(self, data, table_name):
        data_save =


