SAP Load Tool Using Python

Overview : 
This tool enables seamless data loading into SAP ECC and S/4HANA systems. It supports multiple SAP interfaces, including RFCs, BAPIs, and IDocs, allowing flexible integration. The tool simplifies data management and loading by providing a user-friendly interface and compatibility with various file formats.

Features
- Load Method Selection: Choose from RFC, BAPI, or IDoc for data loading.
- Dynamic Method Input: Input specific method names, e.g., SD_SALESORDER_CREATE, BAPI_INTERNALORDRGRP_CREATE.
- Secure SAP Login: Authenticate using secure credentials.
- Retrieve and Display Structure: Export method input structures to Excel.
- Data Import: Load data from XLS, XLSX, TXT, or XML files.
- Data Validation and Load: Validate data and load it into SAP.
- Detailed Logging: Log all transactions for audit and troubleshooting.

Tech Stack
Programming Language: Python
SAP Connectivity: pyrfc (requires SAP NetWeaver RFC SDK)
Data Handling: pandas, openpyxl, xml.etree.ElementTree
User Interface:
Desktop: Tkinter
Web: Streamlit or Flask
