# 3rd-party packages
import yaml


class Builder:
    """
    Implements an abstract generic builder class to use with ObjectFactory

    implementation based on https://realpython.com/factory-method-python/
    """

    def __init__(self):
        """
        Builder constructor. Just sets the internal instance references to None
        """

        self._instance = None
        self._config_name = None

    def __call__(self, **kwargs):
        """
        Abstract implementation of the constructor for the object to be
        built.

        :param      kwargs:  The keywords arguments for the object to be
                             built's constructor
        :type       kwargs:  dictionary

        :returns:   a concrete instance of the object to be built
        :rtype:     { return_type_description }
        """

        return NotImplementedError

    @staticmethod
    def load_YAML_config_data(config_file_name):
        """
        reads in the object configuration parameters from a YAML config file

        :param      config_file_name:  The YAML configuration file name
        :type       config_file_name:  (filepath) string

        :returns:   configuration data dictionary for the simulation
        :rtype:     dict
        """

        with open(config_file_name, 'r') as stream:
            config_data = yaml.load(stream, Loader=yaml.Loader)

        return config_data
