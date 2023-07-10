# final
def insert_function(data):
  '''

  :param data:
  :return:
  '''
  return f"""
  -- Start Data INSERT

INSERT INTO r_function_metadata (function_id,r_function_name,r_is_chain_function,function_language)Values('{data["default"]['function_id']}','{data["default"]['r_function_name']}',{data["default"]['r_is_chain_function']},'{data["default"]['function_language']}');


INSERT INTO material (name,code) SELECT * FROM (SELECT 'Function - {data["default"]['function_label']}', 'MAT_{data["default"]['function_id']}') as tmp WHERE NOT EXISTS ( SELECT id FROM material WHERE code = 'MAT_{data["default"]['function_id']}') LIMIT 1 ;

SET @FUNC_MATERIAL_ID = (SELECT id FROM material WHERE code = 'MAT_{data["default"]['function_id']}');


INSERT INTO function_metadata (function_id, function_name,is_active, is_executable, input_multitable_indicator, all_data_identifier, data_modify_indicator, new_column_indicator, new_datatable_indicator,output_type,create_data_object,use_data_object, function_desc, function_popup_title, function_popup_description, function_search_tags, material_id)Values('{data["default"]['function_id']}','{data["default"]['function_label']}',{data["function_meta_data"]['is_active']},{data["function_meta_data"]["is_executable"]},{data['function_meta_data']['input_multitable_indicator']},{data["function_meta_data"]["all_data_identifier"]},{data["function_meta_data"]['data_modify_indicator']},{data["function_meta_data"]["new_column_indicator"]},{data["function_meta_data"]["new_datatable_indicator"]},'{data["function_meta_data"]["output_type"]}',{data["function_meta_data"]["create_data_object"]},{data["function_meta_data"]["use_data_object"]},'{data["function_meta_data"]["function_desc"]}','{data["function_meta_data"]["function_popup_title"]}','{data["function_meta_data"]["function_popup_description"]}','{data["function_meta_data"]["function_search_tags"]}', @FUNC_MATERIAL_ID);


INSERT INTO function_category_map (Function_id, category_id) values('{data["default"]['function_id']}','{data["default"]['category_id']}');"""


