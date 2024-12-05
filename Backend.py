from pyrfc import Connection
import pandas as pd

# SAP Connection Configuration
SAP_CONFIG = {
    'user': 'srondla',
    'passwd': 'Sun@779933',
    'ashost': 'your_sap_host',  # Replace with your SAP application host
    'sysnr': '01',  # SAP system number
    'client': '202'  # SAP client number
}

# Establish SAP Connection
def connect_to_sap(config):
    try:
        conn = Connection(**config)
        print("Connected to SAP successfully!")
        return conn
    except Exception as e:
        print(f"Failed to connect to SAP: {e}")
        return None

# Fetch Data Template from SAP Table
def fetch_template_data(connection, table_name, fields, filters=None):
    try:
        query = {
            'QUERY_TABLE': table_name,
            'DELIMITER': '|',
            'FIELDS': [{'FIELDNAME': field} for field in fields]
        }
        
        if filters:
            query['OPTIONS'] = [{'TEXT': filter_condition} for filter_condition in filters]
        
        result = connection.call('RFC_READ_TABLE', **query)

        # Parse the result into a DataFrame
        data = [row['WA'].split('|') for row in result['DATA']]
        return pd.DataFrame(data, columns=fields)
    except Exception as e:
        print(f"Failed to fetch data template: {e}")
        return pd.DataFrame()

# Save Data to Excel
def save_to_excel(dataframe, file_name='sap_data_template.xlsx'):
    try:
        dataframe.to_excel(file_name, index=False)
        print(f"Data saved to {file_name}")
    except Exception as e:
        print(f"Failed to save data to Excel: {e}")

# Main Function
if __name__ == "__main__":
    # Connect to SAP
    connection = connect_to_sap(SAP_CONFIG)
    if not connection:
        exit()

    # Define parameters
    TABLE_NAME = 'YOUR_TABLE_NAME'  # Replace with the SAP table you want to extract data from
    FIELDS = ['FIELD1', 'FIELD2', 'FIELD3']  # Replace with the fields you need
    FILTERS = ["FIELD1 = 'VALUE1'"]  # Optional filters, adjust as needed

    # Fetch data template
    data_df = fetch_template_data(connection, TABLE_NAME, FIELDS, FILTERS)
    if data_df.empty:
        print("No data found. Exiting.")
        exit()

    # Save the data to an Excel file
    save_to_excel(data_df)
