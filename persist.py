"""
Created by Jimmy (April 2017)
Load and validate persistence data
"""


def load_persist(persists_string):
    temp = []
    if len(persists_string.strip()):
        parts = persists_string.split(',')
        for part in parts:
            try:
                p = float(part.strip())

                if 0 <= p <= 1:
                    temp.append(p)
                else:
                    raise NameError("Persists value should between 0.0 and 1.0!")
            except ValueError:
                raise NameError("Incompatible Persists string! "
                                "Supply comma-separated list of floats in range [0.0,1.0]")
    else:
        # default values as used in Moffat and Zobel (2008) paper
        temp = [0.5, 0.8, 0.95]
    return temp
