storage = {
        "__length" :  0
    }
buffer = {
    }

    
class Query:
    def __init__(self,data: list,type:str = None):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_data(self, new_data):
        self.__data = new_data
    
    def filter_by(self,**kwargs: any):
        print("Filter by" , kwargs)

        data_after_filter = []
        for data in self.__data:
            checking_filter = True
            for key, value in kwargs.items():
                if hasattr(data, key) and  getattr(data,key) != value:
                    checking_filter = False
            if checking_filter:
                data_after_filter.append(data)
        
        return Query(data_after_filter)
    
    def update(self,values:dict):
        print("update" , values)

        for data in self.__data:
            for key, value in values.items():
                if hasattr(data, key) :
                    setattr(data,key,value)
        return self
    
    

class Execute:
    def __init__(self,table_schema : object, query_type = None):
        self.table_schema = table_schema
        self.query_type = query_type
    
    def where(self,query):
        data_after_where = []
        left_where_operator = query.left.key 
        operator = query.operator
        right_where_operator = query.right.effective_value
        for data in self.__data:
            if  operator(getattr(data, left_where_operator),right_where_operator):
                data_after_where.append(data) 
        print("\nwhere:",data_after_where)
        
        return Query(data_after_where)

def insert(table_schema):
    return Execute(table_schema,"INSERT")

def update(table_schema):
    return Execute(table_schema,"UPDATE")

def delete(table_schema):
    return Execute(table_schema,"DELETE")


def select(table_schema):
    table_name = table_schema.__tablename__
    print("\nselect" , table_name)
    return(Query(storage[table_name]))

class MockSQLSession:
    def __init__(self) -> None:
        pass

    def add(self, data: any):
        table_name = data.__tablename__
        
        # Logic_name:add id for records
        storage['__length'] += 1
        setattr(data, "id", storage['__length'])
        
        # Logic_name: add relationship for records
        # Status: Pending
        ...

        # Logic_name: add records to buffer
        if table_name in buffer:
            buffer[table_name].append(data)
        else:
            buffer[table_name] = [data]
        
    def add_all(self, all_data):
        for data in all_data:
            self.add(data)

    def commit(self):
        global buffer, storage
        for table_name, values in buffer.items():
            if table_name in storage:
                storage[table_name].extend(values)
            else:
                storage[table_name]= values
        buffer = {}

    # Get all data from buffer 
    def query(self, table: any):
        table_name = table.__tablename__

        # Logic_name: Get all data of table in buffer and return Query class
        table_data = []
        if table_name in buffer:
            table_data = buffer[table_name] 
        return Query(table_data)
    
    def execute(self, statement, params):
        
        return ...
    
    def scalars(self, data: any):
        return data 
    
    def scalar_one(self, data: any):
        return data 
    
    def __str__(self):
        return f"\nbuffer: {buffer}\nstorage: {storage}" 
   