import argparse
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


## TO-DO Move the arg parsing to this Argparsing class
## Specific to our project
class ArgumentParsing:
    def __init__(self):
        pass

