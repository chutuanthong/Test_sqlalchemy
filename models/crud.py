storage = {
        "__length" :  0
    }
buffer = {
    }

class PRINT_YOUR_SELF:
    def __init__(self):
        ...
    def __str__(self):
        attributes_str = ""
        for attr, value in self.__dict__.items():
            attributes_str += f"{attr}: {value}, "
        return f"CLASS: ({self.__class__.__name__}) : ({attributes_str[:-2]})"
    
class Query(PRINT_YOUR_SELF):
    def __init__(self,data: list = [],table_schema =None,query_type:str = None):
        self.data = data
        self.table_schema = table_schema
        self.query_type = query_type

    def filter_by(self,**kwargs: any):
        print("Filter by" , kwargs)

        data_after_filter = []
        for data in self.data:
            checking_filter = True
            for key, value in kwargs.items():
                if hasattr(data, key) and  getattr(data,key) != value:
                    checking_filter = False
            if checking_filter:
                data_after_filter.append(data)
        
        return Query(data= data_after_filter,table_schema=self.table_schema,query_type='filter_by')
    
    def update(self,values:dict):
        print("update" , values)

        for data in self.data:
            for key, value in values.items():
                if hasattr(data, key) :
                    setattr(data,key,value)
        return self
    
    def where(self,query):
        data_after_where = []
        left_where_operator = query.left.key 
        operator = query.operator
        right_where_operator = query.right.effective_value
        for data in self.data:
            if  operator(getattr(data, left_where_operator),right_where_operator):
                data_after_where.append(data) 
        print("\nwhere:",data_after_where)
        
        return Query(data= data_after_where,table_schema=self.table_schema,query_type=self.query_type)

    def scalars(self):
        if(self.query_type == 'SELECT'):
            return self.data
    
    def scalar_one(self):
        if(self.query_type == 'SELECT'):
            return self.data[0]


def convert_query_class(table_name, query_type):
    return Query(data = storage[table_name], query_type=query_type, table_schema=table_name)

def insert(table_schema):
    return convert_query_class(table_schema.__tablename__,'INSERT')

def update(table_schema):
    return convert_query_class(table_schema.__tablename__,'UPDATE')

def delete(table_schema):
    return convert_query_class(table_schema.__tablename__,'DELETE')

def select(table_schema):
    return convert_query_class(table_schema.__tablename__,'SELECT')

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
        return Query(data=table_data,table_schema=table_name,query_type='query')
    
    def execute(self, statement, params = None):
        if statement.query_type == 'INSERT':
            self.add_all(params)
        elif statement.query_type == 'DELETE':
            table_schema = statement.table_schema
            delete_record = statement.data[0]
            for record_in_table in storage[table_schema]: 
                if record_in_table == delete_record:
                    print('fine data')
                    storage[table_schema].remove(record_in_table)
        elif statement.query_type == 'UPDATE':
            # Logic_name: PENDING
            ...
        elif statement.query_type == 'SELECT':
            return Query(**statement.__dict__)
        else:
            print("\nCan't note execute this statement :",statement,params)
        return 
    
    def __str__(self):
        return f"\nbuffer: {buffer}\nstorage: {storage}" 
   