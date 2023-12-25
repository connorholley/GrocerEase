There is a model for each controller in the current implementation.
An sqlite db is used for testing, the specific of each db (uri etc) is included in the database-config.json


The Controller's have an environment argument, the default set to testing, when in production we would just 
set the environment argument to production