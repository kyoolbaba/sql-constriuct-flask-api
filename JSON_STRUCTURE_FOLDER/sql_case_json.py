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
            "note": """Select column(s) to display from left table""",
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

        },
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
            "note": """Select a column for condition """,
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "condition_col",
            "label": "Column for Condition",
            "description": "",
            "type": "STATIC",
        },
        "parameter_value": {
            "name": "condition_col",
            "label": "Column for Condition",
            "description": "",
            "type": "DATA_HEADER",

        },
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
            "note": """Select an operator for the case; Default value is Equals""",
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

        },
        'options': {
            ">": ">",
            "<=": "<=",
            ">=": ">=",
            "!=": "!=",
            "equals": "equals"
        }
    },

    # param 4
    {
        "default": {
            "option_order": 4,
            "required": True,
        },

        "parameter_type": {

            "type": "TEXT",
            "description": "",
            "note": """Provide a value for condition""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "condition",
            "label": "Condition",
            "description": "",
            "type": "STATIC",
        },
    },
    # param 5
    {
        "default": {
            "option_order": 5,
            "required": True,
        },

        "parameter_type": {

            "type": "TEXT",
            "description": "",
            "note": """Provide a Text to display if case is successful""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "then_value",
            "label": "THEN",
            "description": "",
            "type": "STATIC",
        },
    },
    # param 6
    {
        "default": {
            "option_order": 6,
            "required": True,
        },

        "parameter_type": {

            "type": "TEXT",
            "description": "",
            "note": """Provide a Text to display if case is unsuccessful""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "else_value",
            "label": "ELSE",
            "description": "",
            "type": "STATIC",
        },
    },

    # param 7
    {
        "default": {
            "option_order": 7,
            "required": False,
        },

        "parameter_type": {

            "type": "TEXT",
            "description": "",
            "note": """Provide a name to the new column generated. If not provided, a default value will be used.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "alias_name",
            "label": "Alias Name",
            "description": "",
            "type": "STATIC",
        },
    },


]

insert_data = {
    "default": {

        "function_id": "FUNC1031",
        "r_function_name": "SQL_case",
        "r_is_chain_function": False,
        "function_name": "Function - SQL Case",
        "function_language": "PYTHON",
        "function_label": "SQL Case",
    },
    "function_meta_data": {
        "is_active": True,
        "is_executable": True,
        "input_multitable_indicator": False,
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
        "function_search_tags": "sql,cas,case",
    },
    "category_id": 106,
    "params": params
}