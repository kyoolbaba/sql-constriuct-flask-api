def add_end_part(function_id):
    '''
    :param function_id:type:string, function_id
    :return:type:string, sql construct of end part
    '''

    return f'''
UPDATE param_value_static_options

SET value_id = (SELECT id

FROM param_value

WHERE param_value.function_id = param_value_static_options.function_id

AND param_value.option_order = param_value_static_options.option_order )

WHERE function_id = '{function_id}';

SET FOREIGN_KEY_CHECKS= 1 ;
  '''