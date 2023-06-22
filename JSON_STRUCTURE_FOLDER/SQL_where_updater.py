params = [
    # param 1
    {
        "default": {
            "option_order": 1,
            "required": False,
        },

        "parameter_type": {

            "type": "MULTI_SELECT",
            "description": "",
            "note": """Select the columns to be displayed as output. If no columns are selected, all columns will be 
            displayed.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "col_names",
            "label": "Column Names",
            "description": "",
            "type": "STATIC",
        },
        "parameter_value": {
            "name": "col_names",
            "label": "Column Names",
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

            "type": "SINGLE_SELECT",
            "description": "",
            "note": """Select the column on which condition has to be run.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "where",
            "label": "WHERE",
            "description": "",
            "type": "STATIC",
        },
        "parameter_value": {
            "name": "where",
            "label": "WHERE",
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
            "note": """Select the operator. Default value is \'=\'""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "operator",
            "label": "Operator",
            "description": "",
            "type": "STATIC",
        },
        "parameter_value": {
            "name": "operator",
            "label": "Operator",
            "description": "",
            "type": "STATIC",

        }
        ,
        "options": {
            ">": ">",
            "<": "<",
            ">=": ">=",
            "<=": "<=",
            "!=": "!=",
            "=": "="
        }
    },
    # param 4
    {
        "default": {
            "option_order": 4,
            "required": True,
        },

        "parameter_type": {

            "type": "SINGLE_SELECT",
            "description": "",
            "note": """Select the value for the condition.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "value",
            "label": "Value",
            "description": "",
            "type": "STATIC",
        },
        "parameter_value": {
            "name": "value",
            "label": "Value",
            "description": "",
            "type": "DATA_BODY",
        }
    }
]

insert_data = {
    "default": {

        "function_id": "FUNC1026",
        "r_function_name": "SQL_where",
        "r_is_chain_function": False,
        "function_name": "Function - SQL Where",
        "function_language": "PYTHON",
        "function_label": "SQL Where",
    },
    "function_meta_data": {
        "is_active": True,
        "is_executable": True,
        "input_multitable_indicator": False,
        "all_data_identifier": True,
        "data_modify_indicator": False,
        "new_column_indicator": False,
        "new_datatable_indicator": True,
        "output_type": "MIXED_OUTPUT",
        "create_data_object": False,
        "use_data_object": False,
        "function_desc": "",
        "function_popup_title": "",
        "function_popup_description": "",
        "function_search_tags": "sql,whe,where",
    },
    "category_id": 107,
    "params": params
}