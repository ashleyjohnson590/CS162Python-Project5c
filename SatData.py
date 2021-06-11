#Author: Ashley Johnson
#Date: 4/22/2021
#Description: Program reads a json file and writes the data to a txt file in csv format.
import json
import time
class SatData:
    """class opens SAT file"""
    def __init__(self):
        self._data = None
        try:
            with open('sat.json', 'r')as infile:
                self._data=json.load(infile)
        except FileNotFoundError:
            print("file not found")
        self.add_data()

    def get_columns(self):
        """gets relevant columns"""

        columns = {
            "DBN": 8,
            "School Name": 9,
            "Number of Test Takers":10,
            "Critical Reading Mean": 11,
            "Mathematics Mean":12,
            "Writing Mean":13
        }
        return columns
    def get_column_as_string(self):
        """function turns relevant columns into strings"""
        columns = self.get_columns()
        my_columns = columns.keys()
        quoted_columns = []
        for column in my_columns:
            new_column = "{}".format(column)
            quoted_columns.append(new_column)
        column_string = ",".join(quoted_columns)
        return column_string

    def column_range(self):
        """deletes irrelevant columns"""
        columns = self.get_columns()
        keys = list(columns.keys())
        lower_range = columns[keys[0]]
        upper_range = columns[keys[-1]]
        return [lower_range, upper_range]

    def add_data(self):
        """function appends list with relevant columns"""
        my_data = self.get_data()
        data = my_data["data"]
        key_range = self.column_range()
        select_data = []
        for items in data:
            selected_items = items[key_range[0]:]
            select_data.append(selected_items)
        self._select_data = select_data

    def get_select_data(self):
        """returns SAT data"""
        return self._select_data


    def data_to_string(self, dbns):
        """function turns data into strings"""
        my_data = self.get_data()
        data = my_data["data"]
        new_data = []
        for entry in data:
            string_items = []
            for item in entry:
                string_items.append(str(item))

            new_data.append(",".join(string_items))
        return new_data

    def filter_data(self, dbns):
        """eliminates irrelevant data"""
        my_columns = self.get_columns()
        raw_data = self.get_select_data()
        filtered_data = []
        for dbn in dbns:
            for line in raw_data:
                if line[0] == dbn:
                    filtered_data.append(line)
        return filtered_data


    def save_as_csv(self, dbns):
        """function saves filtered data as csv"""
        my_columns = self.get_column_as_string()
        print(my_columns)
        filtered_data = self.filter_data(dbns)
        print(filtered_data)
        csv_list = []
        csv_list.append(my_columns)
        for e in filtered_data:
            stringed_e = self.list_to_csv(e)
            csv_list.append(stringed_e)
        with open("output.csv", "w") as fileout:
             for e in csv_list:
                fileout.write(e +"\n")
    def list_to_csv(self, in_data):
        """function turns data into list for csv"""
        stringed_list = []
        for item in in_data:
            stringed_list.append(str(item))
        string_list = ",".join(stringed_list)
        return string_list



    def get_data(self):
        """function gets SAT data"""
        return self._data


if __name__ == '__main__':
    sd = SatData()
    data = sd.get_data()
    range = sd.column_range()
    dbns = ['02M475', '75X754','02M489', '02M500']
    sd.save_as_csv(dbns)

