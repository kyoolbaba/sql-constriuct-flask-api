def options_sql_construct(options,function_id,option_order):
  options_list=""
  for option in options:
    options_list+=f"""

INSERT INTO param_value_static_options (function_id, option_order, name, label)Values('{function_id}', {option_order}, '{option}', '{options[option]}');
"""
  return options_list