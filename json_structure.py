# Params
params = [
    {
        "default": {
            "option_order": 1,
            "required": False,
        },

        "parameter_type": {

            "type": "INT",
            "description": "",
            "note": """Provide a desired number of decimal places to keep after truncation. Default value is 0.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "decimal_places",
            "label": "Decimal Places",
            "description": "",
            "type": "STATIC",
        },
    },
]

# Final
insert_data = {
    "default": {
        "function_id": "FUNC1095",
        "r_function_name": "truncate",
        "r_is_chain_function": False,
        "function_name": "Function - Truncate (Py)",
        "function_language": "PYTHON",
        "function_label": "Truncate (Py)",
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
        "use_data_object": True,
        "function_desc": "",
        "function_popup_title": "",
        "function_popup_description": "",
        "function_search_tags": "truncate, trun",
    },
    "category_id": 207,
    "params": params
}


# # Params
# params = [
#     {
#         "default": {
#             "option_order": 1,
#             "required": True,
#         },
#
#         "parameter_type": {
#
#             "type": "SINGLE_SELECT",
#             "description": "",
#             "note": "Select Model Object",
#             "header": 9999,
#             "value": "NULL"
#         },
#         "parameter_header": {
#             "name": "dataObjectPath",
#             "label": "Model Name",
#             "description": "",
#             "type": "STATIC",
#         },
#         "parameter_value": {
#             "name": "dataObjectPath",
#             "label": "Model Name",
#             "description": '',
#             "type": "DATAFILE",
#         }
#     },
# ]
#
# # Final
# insert_data = {
#     "default": {
#
#         "function_id": "FUNC_001",
#         "r_function_name": "predict_using_python",
#         "r_is_chain_function": False,
#         "function_name": "Apply ML Algorithm (Py)",
#         "function_language": "PYTHON",
#         "function_label": "Function - Apply ML Algorithm (Py)",
#     },
#     "function_meta_data": {
#         "is_active": True,
#         "is_executable": True,
#         "input_multitable_indicator": False,
#         "all_data_identifier": False,
#         "data_modify_indicator": False,
#         "new_column_indicator": False,
#         "new_datatable_indicator": True,
#         "output_type": "MIXED_OUTPUT",
#         "create_data_object": False,
#         "use_data_object": True,
#         "function_desc": "",
#         "function_popup_title": "",
#         "function_popup_description": "",
#         "function_search_tags": 4501,
#     },
#     "category_id": 513,
#     "params": params
# }