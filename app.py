from flask_restful import Api, Resource;
from flask import Flask, request, jsonify, Response

from end_part import add_end_part
from first_part import delete_existing_record
from insert import insert_function
from parameter import add_params_data

app = Flask(__name__)
api = Api(app)


@app.route("/", )
def root_page():
    return "<h1>For sql construct page Hit <a href='http://127.0.0.1:5000/sql_construct' >http://127.0.0.1:5000/sql_construct<a/> in postman with POST method <h1/>"


@app.route("/sql_construct", methods=["POST"])
def input_json():
    '''

    :return:It returns sql script in string
    '''
    insert_data = request.get_json()
    try:
        sql_construct = delete_existing_record(insert_data["default"]["function_id"]) + \
                        insert_function(insert_data) + \
                        add_params_data(insert_data["params"], insert_data["default"]) + \
                        add_end_part(insert_data["default"]['function_id'])
    except Exception as e:
        print(e)

    return sql_construct


if __name__ == "__main__":
    app.run()
