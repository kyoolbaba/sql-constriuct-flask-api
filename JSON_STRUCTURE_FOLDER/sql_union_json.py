params = [
    # param 1
    {
        "default": {
            "option_order": 1,
            "required": False,
        },

        "parameter_type": {

            "type": "SINGLE_SELECT",
            "description": "",
            "note": """Select type of Union to perform""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "union_type",
            "label": "Union Type",
            "description": "",
            "type": "STATIC",
        },
        "parameter_value": {
            "name": "union_type",
            "label": "Union Type",
            "description": "",
            "type": "STATIC",

        },
        "options":{
            "UNION":"UNION",
            "UNION ALL":"UNION ALL"
        }
    },
    # param 2
    {
        "default": {
            "option_order": 2,
            "required": True,
        },

        "parameter_type": {

            "type": "MULTI_SELECT",
            "description": "",
            "note": """Select column(s) from left table for union""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "table1",
            "label": "Select the left table and the columns for union",
            "description": "",
            "type": "DATA_TABLE",
        },
        "parameter_value": {
            "name": "table1",
            "label": "Select the left table and the columns for union",
            "description": "",
            "type": "DATA_HEADER",

        }
    },
    # param 3
    {
        "default": {
            "option_order": 3,
            "required": True,
        },

        "parameter_type": {

            "type": "MULTI_SELECT",
            "description": "",
            "note": """Select column(s) from right table for union""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "table1",
            "label": "Select the right table and the columns for union",
            "description": "",
            "type": "DATA_TABLE",
        },
        "parameter_value": {
            "name": "table2",
            "label": "Select the right table and the columns for union",
            "description": "",
            "type": "DATA_HEADER",

        }
    },

]

insert_data = {
    "default": {

        "function_id": "FUNC1030",
        "r_function_name": "SQL_union",
        "r_is_chain_function": False,
        "function_name": "Function - SQL Union",
        "function_language": "PYTHON",
        "function_label": "SQL Union",
    },
    "function_meta_data": {
        "is_active": True,
        "is_executable": True,
        "input_multitable_indicator": True,
        "all_data_identifier": True,
        "data_modify_indicator": False,
        "new_column_indicator": False,
        "new_datatable_indicator": True,
        "output_type": "CSV",
        "create_data_object": False,
        "use_data_object": False,
        "function_desc": "",
        "function_popup_title": "",
        "function_popup_description": "",
        "function_search_tags": "sql,uni,union",
    },
    "category_id": 238,
    "params": params
}