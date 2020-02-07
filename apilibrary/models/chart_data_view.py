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

    def __init__(self, **kwargs):
        super(ChartDataView, self).__init__(**kwargs)
        self.chart_id = kwargs.get('chart_id', None)
        self.start_value = kwargs.get('start_value', None)
        self.depth = kwargs.get('depth', None)
        self.data = kwargs.get('data', None)