from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.episodios_inner import EpisodiosInner
from openapi_server import util

from openapi_server.models.episodios_inner import EpisodiosInner  # noqa: E501

class TemporadasInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, numero_temporada=None, episodios=None):  # noqa: E501
        """TemporadasInner - a model defined in OpenAPI

        :param numero_temporada: The numero_temporada of this TemporadasInner.  # noqa: E501
        :type numero_temporada: int
        :param episodios: The episodios of this TemporadasInner.  # noqa: E501
        :type episodios: List[EpisodiosInner]
        """
        self.openapi_types = {
            'numero_temporada': int,
            'episodios': List[EpisodiosInner]
        }

        self.attribute_map = {
            'numero_temporada': 'numeroTemporada',
            'episodios': 'episodios'
        }

        self._numero_temporada = numero_temporada
        self._episodios = episodios

    @classmethod
    def from_dict(cls, dikt) -> 'TemporadasInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Temporadas_inner of this TemporadasInner.  # noqa: E501
        :rtype: TemporadasInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def numero_temporada(self) -> int:
        """Gets the numero_temporada of this TemporadasInner.

        Identifica el número de la temporada almacenada en la posición actual del array  # noqa: E501

        :return: The numero_temporada of this TemporadasInner.
        :rtype: int
        """
        return self._numero_temporada

    @numero_temporada.setter
    def numero_temporada(self, numero_temporada: int):
        """Sets the numero_temporada of this TemporadasInner.

        Identifica el número de la temporada almacenada en la posición actual del array  # noqa: E501

        :param numero_temporada: The numero_temporada of this TemporadasInner.
        :type numero_temporada: int
        """

        self._numero_temporada = numero_temporada

    @property
    def episodios(self) -> List[EpisodiosInner]:
        """Gets the episodios of this TemporadasInner.

        Listado de episodios que conforman la temporada a la que se está accediendo en el array. Este atributo se ha definido como un array de objetos, en el cual cada posición almacenará la información referente a un episodio de la temporada actual, es decir, numeroEpisodio, tituloEpisodio y duracionEpisodio  # noqa: E501

        :return: The episodios of this TemporadasInner.
        :rtype: List[EpisodiosInner]
        """
        return self._episodios

    @episodios.setter
    def episodios(self, episodios: List[EpisodiosInner]):
        """Sets the episodios of this TemporadasInner.

        Listado de episodios que conforman la temporada a la que se está accediendo en el array. Este atributo se ha definido como un array de objetos, en el cual cada posición almacenará la información referente a un episodio de la temporada actual, es decir, numeroEpisodio, tituloEpisodio y duracionEpisodio  # noqa: E501

        :param episodios: The episodios of this TemporadasInner.
        :type episodios: List[EpisodiosInner]
        """

        self._episodios = episodios
