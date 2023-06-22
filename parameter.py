from add_options import options_sql_construct


def construct_params_sql(index, param, default):
    '''

    :param index: type:int, It contains index of Parameter
    :param param: type:dict/json, It will have all information related to the parameter i.e. (type, header , value)
    :param default: type:dict/json, It will have all the default information about the function
    :return: type : string, It returns sql construct for parameter section which contains
                   1. Parameter Type
                   2. Parameter Header
                   3. Parameter Value
    '''


    # Section 1 : Paramter Type
    parameter_type = f''' 
  -- Param {index + 1});

INSERT INTO param (function_id, name, option_order, required, type, description, note, header, value)Values('{default["function_id"]}','{default["function_label"]}',{param["default"]["option_order"]},{param["default"]['required']},'{param["parameter_type"]["type"]}','{param["parameter_type"]["description"]}','{param["parameter_type"]["note"]}',{param["parameter_type"]["header"]},{param["parameter_type"]["value"]});
   '''
    # Section 2 : Paramter Header
    parameter_header = f"""
INSERT INTO param_header (name, label, description, type, function_id, option_order)Values('{param["parameter_header"]['name']}','{param["parameter_header"]['label']}','{param["parameter_header"]['description']}','{param["parameter_header"]['type']}','{default["function_id"]}',{param["default"]["option_order"]});

SET @Header_ID = (SELECT MAX(ID) FROM param_header);

SET @Function_ID = (SELECT function_id FROM param_header WHERE id = @Header_ID);

SET @Option_Order = (SELECT Option_Order FROM param_header WHERE id = @Header_ID);

UPDATE param SET header = @Header_ID WHERE function_id = @Function_ID AND Option_Order = @Option_Order;

  """

    # Section 3 : Parameter Value
    parameter_value = ''
    if param["parameter_type"]['type'] in ["SINGLE_SELECT", "MULTI_SELECT"]:
        parameter_value = f'''
INSERT INTO param_value (name, label, description, type, function_id, option_order)Values('{param["parameter_value"]['name']}','{param["parameter_value"]['label']}','{param["parameter_value"]['description']}','{param["parameter_value"]['type']}','{default["function_id"]}',{param["default"]["option_order"]});

SET @Value_ID = (SELECT MAX(ID) FROM param_value);

SET @Function_ID = (SELECT function_id FROM param_value WHERE id = @Value_ID);

SET @Option_Order = (SELECT Option_Order FROM param_value WHERE id = @Value_ID);

UPDATE param SET value = @Value_ID WHERE function_id = @Function_ID AND Option_Order = @Option_Order;
    '''

    option_section=""
    try:
      if((param["parameter_type"]['type'] in ["SINGLE_SELECT","MULTI_SELECT"]) & (param["parameter_value"]['type']=="STATIC")):
        option_section=options_sql_construct(param["options"],default["function_id"],param["default"]["option_order"])
        print(option_section)
    except:pass
    return parameter_type + parameter_header + parameter_value+option_section



def add_params_data(params, default):
    '''

    :param params: type:json/dict , It contains parameter list with all the information of all the parameters
    :param default:type:json/dict, It contains all the default information related to the function
    :return: type:String, It returns all the sql construct related to the parameter section
    '''
    # Initializing param_list variable to append all sql construct of parameter section
    param_list = ""
    # Running List of parameters on loop for SQL construct
    for index, param in enumerate(params):
        param_construct = construct_params_sql(index, param, default)
        param_list += param_construct

    return param_list