# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Remapping(Model):
    """Remapping.

    :param id:
    :type id: int
    :param unique_id:
    :type unique_id: str
    :param friendly_unique_id:
    :type friendly_unique_id: str
    :param manager_id:
    :type manager_id: str
    :param friendly_manager_id:
    :type friendly_manager_id: str
    :param mapped_id:
    :type mapped_id: str
    :param friendly_mapped_id:
    :type friendly_mapped_id: str
    """

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'int'},
        'unique_id': {'key': 'UniqueId', 'type': 'str'},
        'friendly_unique_id': {'key': 'FriendlyUniqueId', 'type': 'str'},
        'manager_id': {'key': 'ManagerId', 'type': 'str'},
        'friendly_manager_id': {'key': 'FriendlyManagerId', 'type': 'str'},
        'mapped_id': {'key': 'MappedId', 'type': 'str'},
        'friendly_mapped_id': {'key': 'FriendlyMappedId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Remapping, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.unique_id = kwargs.get('unique_id', None)
        self.friendly_unique_id = kwargs.get('friendly_unique_id', None)
        self.manager_id = kwargs.get('manager_id', None)
        self.friendly_manager_id = kwargs.get('friendly_manager_id', None)
        self.mapped_id = kwargs.get('mapped_id', None)
        self.friendly_mapped_id = kwargs.get('friendly_mapped_id', None)
