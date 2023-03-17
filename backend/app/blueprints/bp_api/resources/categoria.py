from flask_restful import Resource,Api
from flask import request
from .. import bp_api

from ..models import Categoria
from ..schemas import CategoriaSchema

api = Api(bp_api)

class CategoriaResource(Resource):
    
    def get(self):
        data = Categoria.get_all()
        data_schema = CategoriaSchema(many=True)
        
        context = {
            'status':True,
            'content':data_schema.dump(data)
        }
        
        return context
    
    def post(self):
        data = request.get_json()
        descripcion = data['descripcion']
        categoria = Categoria(descripcion)
        categoria.save()
        data_schema = CategoriaSchema()
        
        context = {
            'status':True,
            'content':data_schema.dump(categoria)
        }
        
        return context
    
    def put(self,id):
        data = request.get_json()
        categoria = Categoria.get_by_id(id)
        categoria.categoria_descripcion = data['descripcion']
        categoria.save()
        
        data_schema = CategoriaSchema()
        context = {
            'status':True,
            'content':data_schema.dump(categoria)
        }
        
        return context
    
    def delete(self,id):
        categoria = Categoria.get_by_id(id)
        categoria.delete()
        data_schema = CategoriaSchema()
        context = {
            'status':True,
            'content':data_schema.dump(categoria)
        }
        
        return context
    
class CatIdResource(Resource):
    
    def get(self,id):
        
        data = Categoria.get_by_id(id)
        data_schema = CategoriaSchema()
        
        context = {
            'status':True,
            'content':data_schema.dump(data)
        }
        
        return context

api.add_resource(CategoriaResource,'/categoria')
api.add_resource(CategoriaResource,'/categoria/<id>',endpoint='categoria')
api.add_resource(CatIdResource,'/catbyid/<id>')