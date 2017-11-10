# enaml-native-charts
Charts for enaml-native using [MPAndroidChart](https://github.com/PhilJay/MPAndroidChart)


[![enaml-native-charts](https://img.youtube.com/vi/crKQpns_vL8/0.jpg)](https://youtu.be/crKQpns_vL8)


### Installation

Install using the [enaml-native-cli](https://github.com/codelv/enaml-native-cli) 
(or pip install and run `enaml-native link`)

```bash

enaml-native install enaml-native-charts

```

Then add `enaml-native-charts` to your `project.json`.

Finally in `main.py` install the chart widgets 

```python
from charts.android.factories import install
install()

```

Then import and use in your `view.enaml`

```python

from charts.widgets.api import *

#etc...


```

### Features

Adds the following widgets

- LineChart
- ScatterChart
- PieChart
- BarChart (stacked and regular)

Data is added to a chart using the `DataSet` component.

> Note: Live data updating has not yet been implemented (but I'm working on it) 


### Examples

See the [examples](examples/) directory.




