
def chomp(x):
    if x.endswith("\r\n"): return x[:-2]
    if x.endswith("\n"): return x[:-1]
    return x

def extract_config_info(config_path = "account.config"):
    config = open(config_path,"r")
    dict = {}
    for line in config:
        dict[line.split(':')[0]] = chomp(line.split(':')[1])
    config.close()
    return dict

def cookie_parser(cookie_str):
    dict = {}
    for line in cookie_str.split("\n"):
        value = line.split(":")[-1]
        name = line.split(value)[0]
        if value.startswith("//"):          #avoid the url parsed in wrong format
            name = line.split(":")[0]
            value = line.split(name)[1]
        dict[name] = value
    return dict
