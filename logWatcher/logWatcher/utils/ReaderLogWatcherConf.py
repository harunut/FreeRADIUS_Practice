import configparser 

CONF_PATH = "/etc/raddb/logWatcher/logWatcher/logWatcher.conf"

conf = configparser.ConfigParser()
conf.read(CONF_PATH)

version = conf.get('configure', 'version')
mode = conf.get('configure', 'mode')
log_dir = conf.get('configure', 'log_dir')
log_file = conf.get('configure', 'log_file')