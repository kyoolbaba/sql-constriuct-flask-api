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
            "note": """Select a column to position marks along X-axis.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "x_variable",
            "label": "X-Axis",
            "description": "",
            "type": "STATIC",
        },
        "parameter_value": {
            "name": "x_variable",
            "label": "X-Axis",
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
            "note": """Select a column to position marks along Y-axis.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "y_variable",
            "label": "Y-Axis",
            "description": "",
            "type": "STATIC",
        },
        "parameter_value": {
            "name": "y_variable",
            "label": "Y-Axis",
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
            "note": """Enter a column name to assign color to marks. The default value is None.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "color",
            "label": "Color",
            "description": "",
            "type": "STATIC",
        },
        "parameter_value": {
            "name": "color",
            "label": "Color",
            "description": "",
            "type": "DATA_HEADER",

        }
    },
    # param 4
    {
        "default": {
            "option_order": 4,
            "required": False,
        },

        "parameter_type": {

            "type": "TEXT",
            "description": "",
            "note": """Provide a title for the bar chart, if not entered, a default title will be added to the 
            figure.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "title",
            "label": "Title",
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

            "type": "TEXT",
            "description": "",
            "note": """Provide a name for labeling the X-axis, if not entered, a default X-Axis Label will be added to the figure.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "Xlabel",
            "label": "X-Axis Label",
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

            "type": "TEXT",
            "description": "",
            "note": """Provide a name for labeling Y-axis, if not entered, a default Y-Axis Label will be added to the figure.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "Ylabel",
            "label": "Y-Axis Label",
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
            "note": """Provide a name to label the color bar, if not entered, a default Color Label will be added to the figure.""",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "Clabel",
            "label": "Color Label",
            "description": "",
            "type": "STATIC",
        },
    },

]

insert_data = {
    "default": {

        "function_id": "FUNC0925",
        "r_function_name": "new_bar_chart_plotly",
        "r_is_chain_function": False,
        "function_name": "Function - Bar Chart (Py) (IN)",
        "function_language": "PYTHON",
        "function_label": "Bar Chart (Py) (IN)",
    },
    "function_meta_data": {
        "is_active": True,
        "is_executable": True,
        "input_multitable_indicator": False,
        "all_data_identifier": False,
        "data_modify_indicator": False,
        "new_column_indicator": False,
        "new_datatable_indicator": False,
        "output_type": "MIXED_OUTPUT",
        "create_data_object": False,
        "use_data_object": False,
        "function_desc": "",
        "function_popup_title": "",
        "function_popup_description": "",
        "function_search_tags": "bar,chart",
    },
    "category_id": 303,
    "params": params
}