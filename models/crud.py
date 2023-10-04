storage = {
        "__length" :  0
    }
buffer = {
    }

class Query:
    def __init__(self,data):
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
    

    

class Insert:
    def __init__(self):
        ...
class Update:
    def __init__(self):
        ...
class Delete:
    def __init__(self):
        ...

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
        # if buffer:
        #     buffer[0].id = 1
        # storage.append(buffer)
        # buffer = []
        # return storage[0]
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
    
    class Select(data):
        def __init__(self):
            ...
        
    
    def execute(self, data: any):
        return data 
    
    def scalars(self, data: any):
        return data 
    
    def scalar_one(self, data: any):
        return data 
    
    def __str__(self):
        return f"buffer: {buffer}\nstorage: {storage}\n" 
   