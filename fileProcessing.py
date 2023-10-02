import pandas as pd

class FileTrans:
    '''
    This class could read excel file and transform it into DataFrame. 
    Also, It can receive new DataFrame and export it as a new excel file that has a new tag '(new)' comparing with the original excel file.
    FileTrans means file transformation (or transformation of files).
    
    Methods
    ----
    __init__(self, file_address):
        Receive file_address in the format of string and stored it in attribute self.address
        
    excel_to_df(self):
        This function would read excel file and transform it to the format of df.
    
    df_to_excel(self, new_df):
        The function will output the processed DataFrame as a new excel chart, which has a name that possesses additional tag of '(new1)'.
    '''

    def __init__(self, file_address):
        self.address=file_address
        
    def excel_to_df(self):
        '''
        This function would read excel file and transform it to the format of df.
        
        Parameters
        ----
        self.address (string) : 
            Same value as file_address assigned to class Read_or_Print_File
        
        Returns
        -------
        df (DataFrame) : The df generated from the given excel chart.

        Notes
        ----
        If the given excel chart is not in the xlsx version, the reading and transformation will fail.
        '''

        df = pd.read_excel(self.address)
        return df

    def df_to_excel(self, new_df):
        '''
        The function will output the processed DataFrame as a new excel chart, which has a name that possesses additional tag of '(new1)'.

        Parameters
        ----------
        new_df : DataFrame
            The df that has been proccessed and ready to be transformed into new excel chart.

        Returns
        -------
        None.

        '''
        global a
        
        if self.address[0] == '"':
            new_address = self.address[1:-1]
        if self.address[0:4] == 'file':
            new_address = self.address[8:]
        else:
            new_address = self.address
        

    
        new_address = new_address[:-5]+'(new1)'+".xlsx"
        with pd.ExcelWriter(new_address) as writer:
            new_df.to_excel(writer)
            print("处理已完成! Good luck with the experiment☆")