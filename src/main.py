import falcon
from sqlalchemy import select
from engine import *

from model import *
import json

class GetList:
    def on_get(self, request, response):
        result = Session.query(App_base).order_by(App_base.ID).all()
        response.status = falcon.HTTP_200 
        response.content_type = falcon.MEDIA_TEXT
        response.text = (str(result))

class GetObjectInfo:
    def on_get(self, request, response,var_id):
        result = Session.query(App_base).get(var_id)
        response.status = falcon.HTTP_200 
        response.content_type = falcon.MEDIA_TEXT
        if str(result)=="None":
            response.text = "Object does not exist"
        else:
            response.text = (str(result))

class DeleteObject:
    def on_get(self, request, response,var_id):
        record = Session.query(App_base).get(var_id)
        response.status = falcon.HTTP_200 
        response.content_type = falcon.MEDIA_TEXT
        if str(record)=="None":
            response.text = "Object does not exist"
        else:
            record.is_deleted = "yes"
            Session.commit()
            response.text = ("Successfully deleted! \n"+ str(record))

class UpdateObject:
    def on_get(self, request, response,var_id):
        record = Session.query(App_base).get(var_id)
        if record.is_deleted == "no" :
            response.status = falcon.HTTP_200
            response.content_type = 'text/html'
            response.body = "<form method='POST' action='/update/"+str(var_id)+"' enctype='application/x-www-form-urlencoded'>\
                                <textarea name='text_form'>"+str(record.text)+"</textarea> <br>\
                                <label for='finished'>Is finished:</label>\
                                <select name='finished' id='finished'>\
                                    <option value='finished'>finished</option>\
                                    <option value='not'>not</option>\
                                </select><br>\
                                <input type='submit' value='Update record'>\
                            </form>"
        else:
            response.status = falcon.HTTP_200
            response.content_type = 'text/html'
            response.body = "This object is deleted!"

    def on_post(self, request, response, var_id):
        record = Session.query(App_base).get(var_id)
        if record.is_deleted == "no" :
            text_field = request.get_param("text_form")
            is_finished_field = request.get_param("finished")
            record.text = str(text_field)
            record.status = str(is_finished_field)
            Session.commit()
            response.status = falcon.HTTP_200 
            response.content_type = falcon.MEDIA_TEXT
            response.text = ("Successfully updated! \n"+ str(record))
        else:
            response.status = falcon.HTTP_200
            response.content_type = 'text/html'
            response.body = "This object is deleted!"


class HealthCheck():
    def on_get(self, request, response):
        is_database_working = True
        output = '{"status":"ok"}'

        try:
            Session.execute('SELECT 1')
        except Exception as e:
            output = str(e)
            is_database_working = False
            output = '{"status":"unavailable"}'

        if is_database_working:
            response.status = falcon.HTTP_200
        else:
            response.status = falcon.HTTP_503

        response.content_type = falcon.MEDIA_TEXT
        response.text = (output)


app = falcon.App()
app.req_options.auto_parse_form_urlencoded=True

app.add_route('/index', GetList())
app.add_route('/get/{var_id:int}', GetObjectInfo())
app.add_route('/delete/{var_id:int}', DeleteObject())
app.add_route('/update/{var_id:int}', UpdateObject())
app.add_route("/status",  HealthCheck())
