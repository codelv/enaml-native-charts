"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 29, 2017

@author: jrm
"""

def bar_chart_factory():
    from .android_chart_view import AndroidBarChart
    return AndroidBarChart


def data_set_factory():
    from .android_chart_view import AndroidDataSet
    return AndroidDataSet


def line_chart_factory():
    from .android_chart_view import AndroidLineChart
    return AndroidLineChart


def pie_chart_factory():
    from .android_chart_view import AndroidPieChart
    return AndroidPieChart


def scatter_chart_factory():
    from .android_chart_view import AndroidScatterChart
    return AndroidScatterChart

def install():
    from enamlnative.android import factories

    ANDROID_FACTORIES = {
        'BarChart': bar_chart_factory,
        'DataSet': data_set_factory,
        'LineChart': line_chart_factory,
        'PieChart': pie_chart_factory,
        'ScatterChart': scatter_chart_factory,
    }


    factories.ANDROID_FACTORIES.update(ANDROID_FACTORIES)