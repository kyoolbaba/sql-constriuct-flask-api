# Params
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
            "note": "Select Target Variable",
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
    # param 2
    {
        "default": {
        "option_order" : 2,
        "required" : False,
        },
        "parameter_type": {
            "type": "INT",
            "description": "",
            "note": "Enter an Integer. Default; None",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header":{
        "name":"max_depth",
        "label":"Depth of Tree",
        "description": "",
        "type":"STATIC",
        },
    },
    # param 3
    {
        "default":{
            "option_order":3,
            "required":False,
        },
        "parameter_type": {
            "type": "FLOAT",
            "description": "",
            "note": "Enter an integer or float value (in case of fraction of data). Default; 2",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header":{
        "name":"min_samples_split",
        "label":"Min Samples Split",
        "description": "",
        "type":"STATIC"
        }
    },
    # Params 4
    {
        "default":{
            "option_order":4,
            "required":False,
        },
        "parameter_type": {
            "type": "FLOAT",
            "description": "",
            "note": "Enter an integer or float value (in case of fraction of data). Default; 1",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header":{
        "name":"min_samples_leaf",
        "label":"Min Samples Leaf",
        "description": "",
        "type":"STATIC"
        }
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
            "note": "Enter an integer or float value Default; 0.0",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "min_weight_fraction_leaf",
            "label": "Min Weight Fraction Leaf",
            "description": "",
            "type": "STATIC"
        }
    },
#     Param 6
    {
        "default": {
            "option_order": 6,
            "required": False,
        },
        "parameter_type": {
            "type": "FLOAT",
            "description": "",
            "note": "Enter an integer or float value (in case of fraction of data). Default; None",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "max_features",
            "label": "Max Features",
            "description": "",
            "type": "STATIC"
        }
    },
#     Param 7
    {
        "default": {
            "option_order": 7,
            "required": False,
        },
        "parameter_type": {
            "type": "INT",
            "description": "",
            "note": "Enter an integer value. Default; None",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "random_state",
            "label": "Random State",
            "description": "",
            "type": "STATIC"
        }
    },
#     params 8
    {
        "default": {
            "option_order": 8,
            "required": False,
        },
        "parameter_type": {
            "type": "INT",
            "description": "",
            "note": "Enter an integer value. Default; None",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "max_leaf_nodes",
            "label": "Max Leaf Nodes",
            "description": "",
            "type": "STATIC"
        }
    },
#     params 9
    {
        "default": {
            "option_order": 9,
            "required": False,
        },
        "parameter_type": {
            "type": "TEXT",
            "description": "",
            "note": "Enter class weights for class 0 first then class 1 in comma separated format",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "class_weight",
            "label": "Class Weight",
            "description": "",
            "type": "STATIC"
        }
    },
#     params 10
    {
        "default": {
            "option_order": 10,
            "required": False,
        },
        "parameter_type": {
            "type": "FLOAT",
            "description": "",
            "note": "Enter a float value between (0,1). Default: 0.5",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "prob_cutoff",
            "label": "Probability Cutoff",
            "description": "",
            "type": "STATIC"
        }
    },
#     params 11
    {
        "default": {
            "option_order": 11,
            "required": False,
        },
        "parameter_type": {
            "type": "FLOAT",
            "description": "",
            "note": "Enter Model Name(Required only if you wish to save the model)",
            "header": 9999,
            "value": "NULL"
        },
        "parameter_header": {
            "name": "dataObjectName",
            "label": "Model Name",
            "description": "",
            "type": "STATIC"
        }
    }

]

# Final
insert_data = {
    "default": {

        "function_id": "FUNC0517",
        "r_function_name": "decision_tree_cart_flyout_data",
        "r_is_chain_function": False,
        "function_name": "Function -  Decision Tree CART (Py)",
        "function_language": "PYTHON",
        "function_label": "Decision Tree CART (Py)",
    },
    "function_meta_data": {
        "is_active": True,
        "is_executable": True,
        "input_multitable_indicator": False,
        "all_data_identifier": False,
        "data_modify_indicator": False,
        "new_column_indicator": True,
        "new_datatable_indicator": True,
        "output_type": "MIXED_OUTPUT",
        "create_data_object": True,
        "use_data_object": False,
        "function_desc": "",
        "function_popup_title": "",
        "function_popup_description": "",
        "function_search_tags": "4501",
    },
    "category_id": 508,
    "params": params
}