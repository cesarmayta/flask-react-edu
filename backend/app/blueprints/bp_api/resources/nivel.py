from flask_restful import Resource,Api
from flask import request
from .. import bp_api

from ..models import Nivel
from ..schemas import NivelSchema

api = Api(bp_api)

class NivelResource(Resource):
    
    def get(self):
        data = Nivel.get_all()
        data_schema = NivelSchema(many=True)
        
        context = {
            'status':True,
            'content':data_schema.dump(data)
        }
        
        return context
    
    def post(self):
        data = request.get_json()
        descripcion = data['descripcion']
        objNivel = Nivel(descripcion)
        objNivel.save()
        data_schema = NivelSchema()
        
        context = {
            'status':True,
            'content':data_schema.dump(objNivel)
        }
        
        return context
    
    def put(self,id):
        data = request.get_json()
        objNivel = Nivel.get_by_id(id)
        objNivel.nivel_descripcion = data['descripcion']
        objNivel.save()
        
        data_schema = NivelSchema()
        context = {
            'status':True,
            'content':data_schema.dump(objNivel)
        }
        
        return context
    
    def delete(self,id):
        objNivel = Nivel.get_by_id(id)
        objNivel.delete()
        data_schema = NivelSchema()
        context = {
            'status':True,
            'content':data_schema.dump(objNivel)
        }
        
        return context
    
class NivelIdResource(Resource):
    
    def get(self,id):
        
        data = Nivel.get_by_id(id)
        data_schema = NivelSchema()
        
        context = {
            'status':True,
            'content':data_schema.dump(data)
        }
        
        return context

api.add_resource(NivelResource,'/nivel')
api.add_resource(NivelResource,'/nivel/<id>',endpoint='nivel')
api.add_resource(NivelIdResource,'/nivelid/<id>')