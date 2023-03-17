from flask_restful import Resource,Api
from flask import request
from .. import bp_api

from ..models import Autor
from ..schemas import AutorSchema

api = Api(bp_api)

class AutorResource(Resource):
    
    def get(self):
        data = Autor.get_all()
        data_schema = AutorSchema(many=True)
        
        context = {
            'status':True,
            'content':data_schema.dump(data)
        }
        
        return context
    
    
    def post(self):
        data = request.get_json()
        nombre = data['nombre']
        foto = data['foto']
        descripcion = data['descripcion']
        objAutor = Autor(nombre,foto,descripcion)
        objAutor.save()
        
        data_schema = AutorSchema()
        
        context = {
            'status':True,
            'content':data_schema.dump(objAutor)
        }
        
        return context
    
    def put(self,id):
        data = request.get_json()
        objAutor = Autor.get_by_id(id)
        objAutor.autor_nombre = data['nombre']
        objAutor.autor_foto = data['foto']
        objAutor.autor_descripcion = data['descripcion']
        objAutor.save()
        
        data_schema = AutorSchema()
        context = {
            'status':True,
            'content':data_schema.dump(objAutor)
        }
        
        return context
    
    def delete(self,id):
        objAutor = Autor.get_by_id(id)
        objAutor.delete()
        data_schema = AutorSchema()
        context = {
            'status':True,
            'content':data_schema.dump(objAutor)
        }
        
        return context
    
class AutorIdResource(Resource):
    
    def get(self,id):
        
        data = Autor.get_by_id(id)
        data_schema = AutorSchema()
        
        context = {
            'status':True,
            'content':data_schema.dump(data)
        }
        
        return context
    
    
api.add_resource(AutorResource,'/autor')
api.add_resource(AutorResource,'/autor/<id>',endpoint='autor')
api.add_resource(AutorIdResource,'/autorid/<id>',endpoint='autorid')
        
