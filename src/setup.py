#: ====================================================================
#: Created with 'enaml-native init-package'
#: Modify as needed
#: ====================================================================
from setuptools import setup, find_packages

#: Put your library dependencies here
setup(
    name="enaml-native-charts",
    version="1.0",
    author="jrm",
    author_email="",
    license='MIT',
    url="",
    entry_points={
        'enaml_native_widgets': [
            'install = charts.widgets.api:install'
        ],
        'enaml_native_android_factories': [
            'install = charts.android.factories:install'
        ],
    },
    description="enaml-native-charts package for enaml-native",
    packages=find_packages(),
    install_requires=['enaml-native'],
)