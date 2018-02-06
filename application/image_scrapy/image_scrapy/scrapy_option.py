import configparser

def  get_options(section):

    config = configparser.ConfigParser()
    config.read('../../config.ini')
    if section not in config:
         print(section)
         print(config.sections())
         return{}
    return (dict(config[section]))

def set_option (section,in_dict):
    pass


if __name__ == '__main__':
    section = 'https://pixabay.com/en/editors_choice'
    out_dict = get_options(section)
    print (out_dict)
