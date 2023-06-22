def delete_existing_record(function_id):
    """
    FUNCTION_ID: PASS THE FUNCTION_ID
    """

    return f"""
SET FOREIGN_KEY_CHECKS = 0;

-- Deleteing old data, if any

DELETE FROM r_chain_function_map WHERE function_id = '{function_id}';

DELETE FROM r_function_metadata WHERE function_id = '{function_id}';

DELETE FROM function_metadata WHERE function_id = '{function_id}';

DELETE FROM param WHERE function_id = '{function_id}';

DELETE FROM param_header WHERE function_id = '{function_id}';

DELETE FROM param_value WHERE function_id = '{function_id}';

DELETE FROM param_value_static_options WHERE function_id = '{function_id}';

DELETE FROM function_category_map WHERE function_id = '{function_id}';

-- End of Delete
  """