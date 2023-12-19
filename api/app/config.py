import os
import toml


class ServiceConfig:

    """
    Provides configuration variables to the entire service.
    """

    db_host: str
    db_user: str
    db_database: str
    db_password_key: str

    
    @property
    def db_password(self):
        return self._access_secret(self.db_password_key)

    
    def __init__(self, config_filename):

        with open(config_filename, 'r') as infile:
            data = toml.load(infile)

        for field, typehint in ServiceConfig.__annotations__.items():

            if not isinstance(data.get(field), typehint):
                raise ValueError(
                    f"ServiceConfig expected the field '{field}' to be of type '{typehint}', "
                    f"instead found type '{typehint}'"
                )
            
            setattr(self, field, data.get(field))

    def _access_secret(self, secret_key):
        """
        Returns the value of a secret so secrets can
        be accessed via the config variable without
        risking the secret getting logged to a file.
        """
        return os.getenv(secret_key)
