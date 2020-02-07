# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChartDataView(Model):
    """ChartDataView.

    :param chart_id:
    :type chart_id: str
    :param start_value:
    :type start_value: str
    :param depth:
    :type depth: int
    :param data:
    :type data: list[~teamorgchart.apilibrary.models.ChartNode]
    """

    _attribute_map = {
        'chart_id': {'key': 'chartId', 'type': 'str'},
        'start_value': {'key': 'startValue', 'type': 'str'},
        'depth': {'key': 'depth', 'type': 'int'},
        'data': {'key': 'Data', 'type': '[ChartNode]'},
    }

    def __init__(self, *, chart_id: str=None, start_value: str=None, depth: int=None, data=None, **kwargs) -> None:
        super(ChartDataView, self).__init__(**kwargs)
        self.chart_id = chart_id
        self.start_value = start_value
        self.depth = depth
        self.data = data
