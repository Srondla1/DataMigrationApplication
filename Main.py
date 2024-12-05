import pandas as pd

#pip install pyrfc pandas openpyxl


from pyrfc import Connection

connection = Connection(user='your_user', passwd='your_pass', ashost='host', sysnr='00', client='100')



def fetch_texts(connection, object_type, text_id, language='EN'):
    # Fetch text headers from STXH
    headers = connection.call('RFC_READ_TABLE', QUERY_TABLE='STXH',
                              DELIMITER='|', FIELDS=['TDOBJECT', 'TDNAME', 'TDID', 'TDSPRAS'],
                              OPTIONS=[{'TEXT': f"TDOBJECT = '{object_type}' AND TDID = '{text_id}' AND TDSPRAS = '{language}'"}])
    header_data = [row['WA'].split('|') for row in headers['DATA']]
    header_df = pd.DataFrame(header_data, columns=[field['FIELDNAME'] for field in headers['FIELDS']])

    # Fetch text lines from STXL
    lines = []
    for _, header in header_df.iterrows():
        result = connection.call('RFC_READ_TABLE', QUERY_TABLE='STXL',
                                  DELIMITER='|', FIELDS=['TDLINE'],
                                  OPTIONS=[{'TEXT': f"TDOBJECT = '{header['TDOBJECT']}' AND TDNAME = '{header['TDNAME']}'"}])
        for row in result['DATA']:
            lines.append({'Header': header['TDNAME'], 'Line': row['WA']})

    return pd.DataFrame(lines)

connection = Connection(user='your_user', passwd='your_pass', ashost='host', sysnr='00', client='100')
data = fetch_texts(connection, 'MATERIAL', 'GRUN')
data.to_excel('long_texts.xlsx', index=False)
