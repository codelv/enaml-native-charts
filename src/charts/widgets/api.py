"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 23, 2017

@author: jrm
"""
from .chart_view import DataSet, LineChart, ScatterChart, BarChart, PieChart


def install():
    from enamlnative.widgets import api

    setattr(api, 'DataSet', DataSet)
    setattr(api, 'LineChart', LineChart)
    setattr(api, 'ScatterChart', ScatterChart)
    setattr(api, 'BarChart', BarChart)
    setattr(api, 'PieChart', PieChart)