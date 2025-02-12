from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.temporadas_inner import TemporadasInner
from openapi_server import util

from openapi_server.models.temporadas_inner import TemporadasInner  # noqa: E501

class Contenido(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id_contenido=None, titulo=None, tipo=None, sinopsis=None, duracion=None, temporadas=None, genero=None, director=None, elenco=None, imagen=None):  # noqa: E501
        """Contenido - a model defined in OpenAPI

        :param id_contenido: The id_contenido of this Contenido.  # noqa: E501
        :type id_contenido: int
        :param titulo: The titulo of this Contenido.  # noqa: E501
        :type titulo: str
        :param tipo: The tipo of this Contenido.  # noqa: E501
        :type tipo: str
        :param sinopsis: The sinopsis of this Contenido.  # noqa: E501
        :type sinopsis: str
        :param duracion: The duracion of this Contenido.  # noqa: E501
        :type duracion: int
        :param temporadas: The temporadas of this Contenido.  # noqa: E501
        :type temporadas: List[TemporadasInner]
        :param genero: The genero of this Contenido.  # noqa: E501
        :type genero: str
        :param director: The director of this Contenido.  # noqa: E501
        :type director: str
        :param elenco: The elenco of this Contenido.  # noqa: E501
        :type elenco: List[str]
        :param imagen: The imagen of this Contenido.  # noqa: E501
        :type imagen: List[str]
        """
        self.openapi_types = {
            'id_contenido': int,
            'titulo': str,
            'tipo': str,
            'sinopsis': str,
            'duracion': int,
            'temporadas': List[TemporadasInner],
            'genero': str,
            'director': str,
            'elenco': List[str],
            'imagen': List[str]
        }

        self.attribute_map = {
            'id_contenido': 'idContenido',
            'titulo': 'titulo',
            'tipo': 'tipo',
            'sinopsis': 'sinopsis',
            'duracion': 'duracion',
            'temporadas': 'temporadas',
            'genero': 'genero',
            'director': 'director',
            'elenco': 'elenco',
            'imagen': 'imagen'
        }

        self._id_contenido = id_contenido
        self._titulo = titulo
        self._tipo = tipo
        self._sinopsis = sinopsis
        self._duracion = duracion
        self._temporadas = temporadas
        self._genero = genero
        self._director = director
        self._elenco = elenco
        self._imagen = imagen

    @classmethod
    def from_dict(cls, dikt) -> 'Contenido':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Contenido of this Contenido.  # noqa: E501
        :rtype: Contenido
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id_contenido(self) -> int:
        """Gets the id_contenido of this Contenido.

        Identificador único del contenido  # noqa: E501

        :return: The id_contenido of this Contenido.
        :rtype: int
        """
        return self._id_contenido

    @id_contenido.setter
    def id_contenido(self, id_contenido: int):
        """Sets the id_contenido of this Contenido.

        Identificador único del contenido  # noqa: E501

        :param id_contenido: The id_contenido of this Contenido.
        :type id_contenido: int
        """

        self._id_contenido = id_contenido

    @property
    def titulo(self) -> str:
        """Gets the titulo of this Contenido.

        Nombre del contenido  # noqa: E501

        :return: The titulo of this Contenido.
        :rtype: str
        """
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str):
        """Sets the titulo of this Contenido.

        Nombre del contenido  # noqa: E501

        :param titulo: The titulo of this Contenido.
        :type titulo: str
        """

        self._titulo = titulo

    @property
    def tipo(self) -> str:
        """Gets the tipo of this Contenido.

        Categoría multimedia a la cual pertenece el contenido (Película, documental, serie…)  # noqa: E501

        :return: The tipo of this Contenido.
        :rtype: str
        """
        return self._tipo

    @tipo.setter
    def tipo(self, tipo: str):
        """Sets the tipo of this Contenido.

        Categoría multimedia a la cual pertenece el contenido (Película, documental, serie…)  # noqa: E501

        :param tipo: The tipo of this Contenido.
        :type tipo: str
        """
        allowed_values = ["serie", "pelicula", "corto", "documental"]  # noqa: E501
        if tipo not in allowed_values:
            raise ValueError(
                "Invalid value for `tipo` ({0}), must be one of {1}"
                .format(tipo, allowed_values)
            )

        self._tipo = tipo

    @property
    def sinopsis(self) -> str:
        """Gets the sinopsis of this Contenido.

        Resumen general e información referente al contenido  # noqa: E501

        :return: The sinopsis of this Contenido.
        :rtype: str
        """
        return self._sinopsis

    @sinopsis.setter
    def sinopsis(self, sinopsis: str):
        """Sets the sinopsis of this Contenido.

        Resumen general e información referente al contenido  # noqa: E501

        :param sinopsis: The sinopsis of this Contenido.
        :type sinopsis: str
        """

        self._sinopsis = sinopsis

    @property
    def duracion(self) -> int:
        """Gets the duracion of this Contenido.

        Intervalo de tiempo en minutos que transcurre entre el comienzo y el fin del contenido  # noqa: E501

        :return: The duracion of this Contenido.
        :rtype: int
        """
        return self._duracion

    @duracion.setter
    def duracion(self, duracion: int):
        """Sets the duracion of this Contenido.

        Intervalo de tiempo en minutos que transcurre entre el comienzo y el fin del contenido  # noqa: E501

        :param duracion: The duracion of this Contenido.
        :type duracion: int
        """

        self._duracion = duracion

    @property
    def temporadas(self) -> List[TemporadasInner]:
        """Gets the temporadas of this Contenido.

        Conjunto de temporadas que conforman la serie (solo en el caso de que el contenido sea de tipo serie. Si el contenido no es de tipo serie este array estará vacío y no contendrá información útil). Este atributo se ha definido como un array de objetos, en el cual cada posición almacenará la información referente a una temporada, es decir, numeroTemporada y episodios  # noqa: E501

        :return: The temporadas of this Contenido.
        :rtype: List[TemporadasInner]
        """
        return self._temporadas

    @temporadas.setter
    def temporadas(self, temporadas: List[TemporadasInner]):
        """Sets the temporadas of this Contenido.

        Conjunto de temporadas que conforman la serie (solo en el caso de que el contenido sea de tipo serie. Si el contenido no es de tipo serie este array estará vacío y no contendrá información útil). Este atributo se ha definido como un array de objetos, en el cual cada posición almacenará la información referente a una temporada, es decir, numeroTemporada y episodios  # noqa: E501

        :param temporadas: The temporadas of this Contenido.
        :type temporadas: List[TemporadasInner]
        """

        self._temporadas = temporadas

    @property
    def genero(self) -> str:
        """Gets the genero of this Contenido.

        Temática en la que puede clasificarse el contenido multimedia (Horror, comedia, romance, fantasía…)  # noqa: E501

        :return: The genero of this Contenido.
        :rtype: str
        """
        return self._genero

    @genero.setter
    def genero(self, genero: str):
        """Sets the genero of this Contenido.

        Temática en la que puede clasificarse el contenido multimedia (Horror, comedia, romance, fantasía…)  # noqa: E501

        :param genero: The genero of this Contenido.
        :type genero: str
        """
        allowed_values = ["horror", "aventura", "comedia", "thriller", "drama", "romance", "fantasia", "ciencia ficcion"]  # noqa: E501
        if genero not in allowed_values:
            raise ValueError(
                "Invalid value for `genero` ({0}), must be one of {1}"
                .format(genero, allowed_values)
            )

        self._genero = genero

    @property
    def director(self) -> str:
        """Gets the director of this Contenido.

        Responsable principal encargado de dirigir la filmación o rodaje del contenido en términos artísticos  # noqa: E501

        :return: The director of this Contenido.
        :rtype: str
        """
        return self._director

    @director.setter
    def director(self, director: str):
        """Sets the director of this Contenido.

        Responsable principal encargado de dirigir la filmación o rodaje del contenido en términos artísticos  # noqa: E501

        :param director: The director of this Contenido.
        :type director: str
        """

        self._director = director

    @property
    def elenco(self) -> List[str]:
        """Gets the elenco of this Contenido.

        Conjunto de personas, normalmente los actores y actrices principales, que han participado en la producción y grabación del contenido  # noqa: E501

        :return: The elenco of this Contenido.
        :rtype: List[str]
        """
        return self._elenco

    @elenco.setter
    def elenco(self, elenco: List[str]):
        """Sets the elenco of this Contenido.

        Conjunto de personas, normalmente los actores y actrices principales, que han participado en la producción y grabación del contenido  # noqa: E501

        :param elenco: The elenco of this Contenido.
        :type elenco: List[str]
        """

        self._elenco = elenco

    @property
    def imagen(self) -> List[str]:
        """Gets the imagen of this Contenido.

        Fotografía representativa del contenido multimedia  # noqa: E501

        :return: The imagen of this Contenido.
        :rtype: List[str]
        """
        return self._imagen

    @imagen.setter
    def imagen(self, imagen: List[str]):
        """Sets the imagen of this Contenido.

        Fotografía representativa del contenido multimedia  # noqa: E501

        :param imagen: The imagen of this Contenido.
        :type imagen: List[str]
        """

        self._imagen = imagen
