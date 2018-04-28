import os
import csv
import pandas as pd


class Currency:
    """
    Class for storing and accessing information about a currency.
    
    Euro exchange rate parameter can be a float, int or string representation of a number;
    will be converted to float.
    """
    
    def __init__(self, code:str, country:str, euro_exch_rate):
        self._code = code
        self._country = country
        self._euro_exch_rate = float(euro_exch_rate)
        
    def get_code(self):
        return self._code
    
    def get_country(self):
        return self._country
    
    def get_euro_exch_rate(self):
        return self._euro_exch_rate  
    

class CurrenciesInfo:
    """
    Stores currency data from CSV files in dictionary
    """
    # Dictionary to store Currency objects
    _currencies_dict = {} 
        
    def __init__(self, dict_of_Currencies={}, currencies_csv:str=None, euro_rates_csv:str=None):
        """
        Create CurrenciesInfo object comprising dictionary of Currency objects.
        
        Set csv_filename parameters to construct dictionary from the CSVs; both must be non-null.
        If both not set, the specified or default dictionary will be used.
        Default is empty dictionary.
        """
        # Use dictionary or csv parameters to create object, depending on which are set
        if currencies_csv is None and euro_rates_csv is None:
            self._Currencys_dict = dict_of_Currencies
        elif currencies_csv is None or euro_rates_csv is None:
            print('Error: {} requires both CSV parameters to be set and valid.'.format(__name__))
        else:
            curr_file_path = os.path.join('/home/d/Git/flight_plan/flight_plan/input', currencies_csv) #FIXME: relative path
            exch_file_params = os.path.join('/home/d/Git/flight_plan/flight_plan/input', euro_rates_csv) #FIXME: relative path
#             
#             with open(curr_file_path, 'rt', encoding='utf8') as f_curr, open(exch_file_params, 'rt', encoding='utf8') as f_exch: 
#                 curr_reader = csv.reader(f_curr)
#                 exch_reader = csv.reader(f_exch)
#                 for curr_line, exch_line in zip(curr_reader[1:], exch_reader):
#                     self._currencies_dict[curr_line[4]] = Currency(curr_line[4], curr_line[0], exch_line[2])

            df_curr = pd.read_csv(curr_file_path, skipinitialspace=True)
            df_exch = pd.read_csv(exch_file_params, skipinitialspace=True)
            df_combined = pd.concat(df_curr[])


# class EuroExchangeRates: #FIXME: Complete class
#     """
#     Stores country euro exchange rate data from CSV file in dictionary
#     """   
#     def __init__(self):
#         self._euro_rate_dict = {}
#     
#     def load_data(self, csv_filename: str):
#         """...."""
#         with open(os.path.join('input', csv_filename), 'rt', encoding='utf8') as f:
#             reader = csv.reader(f)
#             for line in reader:
#                 self._euro_rate_dict[line[4]] = Currency(line[2], line[3], line[6], line[7])
#                 
#     def local_euro_exch_rate(self, country):
#         # TODO: get country for each Currency and then
#         exch_rate = 1 # FIXME: placeholder
#         return exch_rate