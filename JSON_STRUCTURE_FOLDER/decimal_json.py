params = [
    # param 1
    {
        "default": {
            "option_order": 1,
            "required": False,
        },

        "parameter_type": {

            "type": "INT",
            "description": "",
            "note": """Enter a positive integer value. Default value is 2""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "Decimal Place",
            "label": "Decimal Place",
            "description": "",
            "type": "STATIC",
        },
    },

]

insert_data = {
    "default": {

        "function_id": "FUNC1093",
        "r_function_name": "round_decimal",
        "r_is_chain_function": False,
        "function_name": "Function - Round (Py)",
        "function_language": "PYTHON",
        "function_label": "Round (Py)",
    },
    "function_meta_data": {
        "is_active": True,
        "is_executable": True,
        "input_multitable_indicator": False,
        "all_data_identifier": False,
        "data_modify_indicator": True,
        "new_column_indicator": False,
        "new_datatable_indicator": False,
        "output_type": "MIXED_OUTPUT",
        "create_data_object": False,
        "use_data_object": False,
        "function_desc": "",
        "function_popup_title": "",
        "function_popup_description": "",
        "function_search_tags": "round, roun",
    },
    "category_id": 401,
    "params": params
}