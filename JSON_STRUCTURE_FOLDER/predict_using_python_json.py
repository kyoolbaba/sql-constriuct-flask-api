params = [
    # param 1
    {
        "default": {
            "option_order": 1,
            "required": True,
        },

        "parameter_type": {

            "type": "SINGLE_SELECT",
            "description": "",
            "note": """Select Model Object""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "dataObjectPath",
            "label": "Model Name",
            "description": "",
            "type": "STATIC",
        },
        "parameter_value": {
            "name": "dataObjectPath",
            "label": "Model Name",
            "description": "",
            "type": "DATA_FILE",

        }
    },
    # param 2
    {
        "default": {
            "option_order": 2,
            "required": False,
        },

        "parameter_type": {

            "type": "SINGLE_SELECT",
            "description": "",
            "note": """Select Target Variable(if present)""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "target_variable",
            "label": "Target Variable",
            "description": "",
            "type": "STATIC",
        },
        "parameter_value": {
            "name": "target_variable",
            "label": "Target Variable",
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

            "type": "FLOAT",
            "description": "",
            "note": """Enter a float between (0,1) in case of binary classification. Default; 0.5""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "prob_cutoff",
            "label": "Probability Cutoff",
            "description": "",
            "type": "STATIC",
        },
    },

]

insert_data = {
    "default": {

        "function_id": "FUNC0629",
        "r_function_name": "predict_using_python",
        "r_is_chain_function": False,
        "function_name": "Function - Apply ML Algorithm (Py)",
        "function_language": "PYTHON",
        "function_label": "Apply ML Algorithm (Py)",
    },
    "function_meta_data": {
        "is_active": True,
        "is_executable": True,
        "input_multitable_indicator": False,
        "all_data_identifier": True,
        "data_modify_indicator": False,
        "new_column_indicator": True,
        "new_datatable_indicator": False,
        "output_type": "MIXED_OUTPUT",
        "create_data_object": False,
        "use_data_object": True,
        "function_desc": "",
        "function_popup_title": "",
        "function_popup_description": "",
        "function_search_tags": "4501           ",
    },
    "category_id": 513,
    "params": params
}