import sh
from os.path import join, abspath, exists
from pythonforandroid.recipe import PythonRecipe, current_directory


class EnamlNativeRecipe(PythonRecipe):
    version = '1.0'
    depends = ['enaml-native']
    name = 'enaml-native-charts'
    url = 'src.zip'

    def download(self):
        """ Copy it right from the source """
        #: Zip the srz
        src_root = abspath(join(self.ctx.root_dir, '..', '..'))
        with current_directory(src_root):
            sh.zip('-r', join(self.ctx.packages_path, self.name, self.url), 'src')


def get_recipe():
    return (EnamlNativeRecipe(), __file__)