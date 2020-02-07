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

    def __init__(self, *, id: int=None, unique_id: str=None, friendly_unique_id: str=None, manager_id: str=None, friendly_manager_id: str=None, mapped_id: str=None, friendly_mapped_id: str=None, **kwargs) -> None:
        super(Remapping, self).__init__(**kwargs)
        self.id = id
        self.unique_id = unique_id
        self.friendly_unique_id = friendly_unique_id
        self.manager_id = manager_id
        self.friendly_manager_id = friendly_manager_id
        self.mapped_id = mapped_id
        self.friendly_mapped_id = friendly_mapped_id