from flask_restful import Resource,Api
from flask import request
from .. import bp_api

from ..models import CursoTopico
from ..schemas import TopicoSchema

api = Api(bp_api)

class TopicoResource(Resource):
    
    def get(self):
        data = CursoTopico.get_all()
        data_schema = TopicoSchema(many=True)
        
        context = {
            'status':True,
            'content':data_schema.dump(data)
        }
        
        return context
    
class TopicoIdResource(Resource):
    
    def get(self,id):
        
        data = CursoTopico.get_by_id(id)
        data_schema = TopicoSchema()
        
        context = {
            'status':True,
            'content':data_schema.dump(data)
        }
        
        return context

api.add_resource(TopicoResource,'/topico')
api.add_resource(TopicoResource,'/topico/<id>',endpoint='topico')
api.add_resource(TopicoIdResource,'/topicoid/<id>')