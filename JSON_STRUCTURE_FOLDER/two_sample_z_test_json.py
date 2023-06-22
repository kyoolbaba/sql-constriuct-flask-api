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
            "note": """Please select the categorical column with two classes.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "class_variable",
            "label": "Class Column",
            "description": "",
            "type": "STATIC",
        },
        "parameter_value": {
            "name": "class_variable",
            "label": "Class Column",
            "description": "",
            "type": "DATA_HEADER",

        },
    },
    # param 2
    {
        "default": {
            "option_order": 2,
            "required": False,
        },

        "parameter_type": {

            "type": "FLOAT",
            "description": "",
            "note": """Please enter the Hypothesized Mean Difference. Default value is 0.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "hypo_mean_diff",
            "label": "Hypothesized Mean Difference",
            "description": "",
            "type": "STATIC",
        },
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
            "note": """Please enter the Population Standard Deviation of Group 1. Default value is Sample Standard Deviation.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "std_dev1",
            "label": "Group 1 Population Standard Deviation",
            "description": "",
            "type": "STATIC",
        },
    },
    # param 4
    {
        "default": {
            "option_order": 4,
            "required": False,
        },

        "parameter_type": {

            "type": "FLOAT",
            "description": "",
            "note": """Please enter the Population Standard Deviation of Group 2. Default value is Sample Standard Deviation.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "std_dev2",
            "label": "Group 2 Population Standard Deviation",
            "description": "",
            "type": "STATIC",
        },
    },
    # param 5
    {
        "default": {
            "option_order": 5,
            "required": False,
        },

        "parameter_type": {

            "type": "FLOAT",
            "description": "",
            "note": """Please enter the Level of Significance between 0 and 1. Default value is 0.05.   """,
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "alpha",
            "label": "Level of Significance",
            "description": "",
            "type": "STATIC",
        },
    },

    # param 6
    {
        "default": {
            "option_order": 6,
            "required": False,
        },

        "parameter_type": {

            "type": "SINGLE_SELECT",
            "description": "",
            "note": """Please select the Alternate Hypothesis. Default value is Two-sided.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "alternate_hypo",
            "label": "Alternate Hypothesis",
            "description": "",
            "type": "STATIC",
        },
        "parameter_value": {
            "name": "alternate_hypo",
            "label": "Alternate Hypothesis",
            "description": "",
            "type": "STATIC",
        },
        "options":{
            "Less Than":"Less Than",
            "Greater Than":"Greater Than",
            "Two-sided":"Two-sided"
        }
    },



]

insert_data = {
    "default": {

        "function_id": "FUNC1124",
        "r_function_name": "two_sample_z_test",
        "r_is_chain_function": False,
        "function_name": "Function - Two Sample Z-Test (Py)",
        "function_language": "PYTHON",
        "function_label": "Two Sample Z-Test (Py)",
    },
    "function_meta_data": {
        "is_active": True,
        "is_executable": True,
        "input_multitable_indicator": False,
        "all_data_identifier": False,
        "data_modify_indicator": False,
        "new_column_indicator": False,
        "new_datatable_indicator": False,
        "output_type": "TEXT",
        "create_data_object": False,
        "use_data_object": False,
        "function_desc": "",
        "function_popup_title": "",
        "function_popup_description": "",
        "function_search_tags": "two,sample,z test,two sample",
    },
    "category_id": 238,
    "params": params
}