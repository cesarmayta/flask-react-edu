#create your schemas
from utils.db import ma
from marshmallow import fields

from marshmallow_sqlalchemy import SQLAlchemySchema,auto_field,SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from .models import CursoTopico,CursoTopicoClase,Curso

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('categoria_id','categoria_descripcion')
        
class NivelSchema(ma.Schema):
    class Meta:
        fields = ('nivel_id','nivel_descripcion')
        
class AutorSchema(ma.Schema):
    class Meta:
        fields = ('autor_id','autor_nombre','autor_foto','autor_descripcion')
        
class ClaseSchema(SQLAlchemySchema):
    class Meta:
        model = CursoTopicoClase
        load_instance = True
    
    id = auto_field("curtop_id")
    title = auto_field("curtopcla_descripcion")
    duration = auto_field("curtopcla_duracion")
        
class TopicoSchema(SQLAlchemySchema):
    class Meta:
        model = CursoTopico
        load_instance = True
        
    id = auto_field("curtop_id")
    title = auto_field("curtop_descripcion")
    classes = Nested(ClaseSchema,many=True)
    
class CursoSchema(SQLAlchemySchema):
    class Meta:
        model = Curso
        load_instance = True
        
    id = auto_field("curso_id")
    category = auto_field()
    title = auto_field("curso_titulo")
    description = auto_field("curso_descripcion")
    level = auto_field()
    teacher = auto_field()
    duration = auto_field("curso_duracion")
    lectures = auto_field("curso_clases")
    stars = auto_field("curso_calificacion")
    price = auto_field("curso_precio")
    img = auto_field("curso_imagen")
    topics = Nested(TopicoSchema,many=True)
               
class CursoSchemaSimple(ma.Schema):
    id = fields.Integer(attribute="curso_id")
    category = fields.String(attribute="cat.categoria_descripcion")
    title = fields.String(attribute="curso_titulo")
    description = fields.String(attribute="curso_descripcion")
    level = fields.String(attribute="niv.nivel_descripcion")
    teacher = fields.String(attribute="aut.autor_nombre")
    duration = fields.Integer(attribute="curso_duracion")
    lectures = fields.Integer(attribute="curso_clases")
    stars = fields.Integer(attribute="curso_calificacion")
    price = fields.Integer(attribute="curso_precio")
    img = fields.String(attribute="curso_imagen")
    #topics = fields.Nested(attribute="topicos")
    
    class Meta:
        fields = ('id','category','title',
                  'description',
                  'level','teacher','duration',
                  'lectures','stars','price','banner',
                  'img','topicos')
        