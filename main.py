from end_part import add_end_part
from first_part import delete_existing_record
from insert import insert_function
from JSON_STRUCTURE_FOLDER.bar_chart_json import insert_data
from parameter import add_params_data

sql_construct=delete_existing_record(insert_data["default"]["function_id"])+\
insert_function(insert_data)+\
add_params_data(insert_data["params"],insert_data["default"])+\
add_end_part(insert_data["default"]['function_id'])

print(sql_construct)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
