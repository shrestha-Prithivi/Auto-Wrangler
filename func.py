import os
import operator
import random
import pandas as pd 
import numpy as np
from pandas import json_normalize
import json
import io
from visions.functional import detect_series_type, infer_series_type
from visions.typesets import StandardSet

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors




typeset = StandardSet()
typeset.types




def Main_func(data):

    flag = 0
    #Handling Datatype

    if flag == 0:
      
        data_type_sam = {}
        row=data.shape[0]
        data_sam = data.sample(int(row/10))

        #First Sample for the initialization of main dictionary
        for (columnName, columnData) in data_sam.iteritems():

            data_type_sam[columnName] = {str(infer_series_type(data_sam[columnName], typeset)):1}

        #Taking sample for 10 times for accuracy
        for i in range(9):

            data_sam = data.sample(int(row/10))

            for (columnName, columnData) in data_sam.iteritems():

                dataTypeValue = str(infer_series_type(data_sam[columnName], typeset))

                if data_type_sam[columnName].__contains__(dataTypeValue):

                    data_type_sam[columnName][str(infer_series_type(data_sam[columnName], typeset))] += 1

                else:
                    
                    data_type_sam[columnName][dataTypeValue] = 1


            data_type = {}

    
        #Making a dictionary with the datatype with maximum rate
        for (columnName, columnData) in data_sam.iteritems():

            max_value = max(data_type_sam[columnName].items(), key=operator.itemgetter(1))[0]

            data_type[columnName] = max_value

        print(data_type)

        #Changing the datatype

        change = []

        for (columnName, columnData) in data.iteritems():

            if data_type[columnName] ==  'DateTime':

                data_type_before = str(detect_series_type(data[columnName],typeset))

                data[columnName] = pd.to_datetime(data[columnName], errors = 'coerce')

                if data_type_before != str(detect_series_type(data[columnName],typeset)):

                    print(columnName, " column data was changed from ", data_type_before , " to ", str(detect_series_type(data[columnName],typeset)))


            elif (data_type[columnName] ==  'Integer') or (data_type[columnName] ==  'Float'):

                data_type_before = str(detect_series_type(data[columnName],typeset))

                data[columnName] = pd.to_numeric(data[columnName], errors = 'coerce')

                if data_type_before != str(detect_series_type(data[columnName],typeset)):

                    print(columnName, " column data was changed from ", data_type_before , " to ", str(detect_series_type(data[columnName],typeset)))

                
            elif data_type[columnName] ==  'TimeDelta':

                data_type_before = str(detect_series_type(data[columnName],typeset))

                data[columnName] = pd.to_timedelta(data[columnName], errors = 'coerce')

                if data_type_before != str(detect_series_type(data[columnName],typeset)):

                    print(columnName, " column data was changed from ", data_type_before , " to ", str(detect_series_type(data[columnName],typeset)))

            else:

                data[columnName] = data[columnName]

    
        #Finding the number of missing data
        before = data.shape[0]
        data_copy = data.copy()
        data_copy.dropna(inplace = True)
        after = data_copy.shape[0]
        null_data = before - after

        print("There are altogether ", null_data, "null in the dataset.")

        percent_missing = data.isnull().sum() * 100 / len(data)
        for (colName,colValue) in data.iteritems():
          if percent_missing[colName] >= 40:
              data = data.drop([colName], axis=1)
              print(colName, " column was dropped.")
  
        for (colName,colValue) in data.iteritems():
          #Filling the missing value with median for only numerical columns
          type_of_column = str(detect_series_type(data[colName],typeset))
          if (type_of_column == "Integer") or (type_of_column == "Float"):
            med = data[colName].median()
            data[colName] = data[colName].fillna(med)

        data = data.dropna()

        after = data.shape[0]

        dropped_rows = before - after
        print(dropped_rows, " rows were dropped.")

        #Checking Duplicate

        before = data.shape[0] 
        bool_series = data.duplicated(keep = False) 
            
        # bool series 
        bool_series 
            
        # passing NOT of bool series to see unique values only 
        data = data[~bool_series] 
        after = data.shape[0]

        data_drop = before - after

       

    return data