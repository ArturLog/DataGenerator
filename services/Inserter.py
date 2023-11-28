import os

class Inserter:
    def __init__(self, ):
        if not os.path.exists("./inserts"):
            os.mkdir("./inserts")
   
    def convert(self, path, table_name, column_types):
        phases = ['first', 'second']
        for phase in phases:
            if not os.path.exists(f"./inserts/{phase}"):
                os.mkdir(f"./inserts/{phase}")
            with open(f"./csv/{phase}/{path}", 'r') as f:
                lines = f.readlines()
                columns = lines[0].strip().split(',')
                for line in lines[1:]:
                    values = line.strip().split(',')
                    for i in range(len(values)):
                        if column_types[i] == "INTEGER":
                            values[i] = values[i]
                        elif column_types[i] == "TEXT":
                            values[i] = f"'{values[i]}'"
                        elif column_types[i] == "DATE":
                            values[i] = f"'{values[i]}'"
                    insert = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(values)});\n"
                    with open(f"./inserts/{phase}/{table_name}.sql", 'a') as f:
                        f.write(insert)
            print(f"Converted {phase}/{path} to {phase}/{table_name}.sql")

        