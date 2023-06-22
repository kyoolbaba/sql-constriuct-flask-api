params = [
    # param 1
    {
        "default": {
            "option_order": 1,
            "required": True,
        },

        "parameter_type": {

            "type": "MULTI_SELECT",
            "description": "",
            "note": """Select column(s) to display from left table""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "table1",
            "label": "Select the left table and the columns to join on",
            "description": "",
            "type": "DATA_TABLE",
        },
        "parameter_value": {
            "name": "table1",
            "label": "Select the left table and the columns to join on",
            "description": "",
            "type": "DATA_HEADER",

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
            "note": """Select column(s) to display from right table""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "table2",
            "label": "Select the right table and the columns to join on",
            "description": "",
            "type": "DATA_TABLE",
        },
        "parameter_value": {
            "name": "table2",
            "label": "Select the right table and the columns to join on",
            "description": "",
            "type": "DATA_HEADER",

        }

    },
    # param 3
    {
        "default": {
            "option_order": 3,
            "required": False,
        },

        "parameter_type": {

            "type": "SINGLE_SELECT",
            "description": "",
            "note": """Select the type of join to be used; Default value is INNER""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "join_type",
            "label": "Join Type",
            "description": "",
            "type": "STATIC",
        },
        "parameter_value": {
            "name": "join_type",
            "label": "Join Type",
            "description": "",
            "type": "STATIC",

        },
        "options":{
            "LEFT":"LEFT",
            "INNER":"INNER"
        }
    },
    # param 4
    {
        "default": {
            "option_order": 4,
            "required": True,
        },

        "parameter_type": {

            "type": "MULTI_SELECT",
            "description": "",
            "note": """Select a column common to both tables.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "common_table",
            "label": "Common column",
            "description": "",
            "type": "DATA_TABLE",
        },
        "parameter_value": {
            "name": "common_table",
            "label": "Common column",
            "description": "",
            "type": "DATA_HEADER",

        },
    },

]

insert_data = {
    "default": {

        "function_id": "FUNC1029",
        "r_function_name": "SQL_join",
        "r_is_chain_function": False,
        "function_name": "Function - SQL Join",
        "function_language": "PYTHON",
        "function_label": "SQL Join",
    },
    "function_meta_data": {
        "is_active": True,
        "is_executable": True,
        "input_multitable_indicator": True,
        "all_data_identifier": False,
        "data_modify_indicator": False,
        "new_column_indicator": False,
        "new_datatable_indicator": True,
        "output_type": "MIXED_OUTPUT",
        "create_data_object": False,
        "use_data_object": False,
        "function_desc": "",
        "function_popup_title": "",
        "function_popup_description": "",
        "function_search_tags": "sql,joi,join",
    },
    "category_id": 107,
    "params": params
}