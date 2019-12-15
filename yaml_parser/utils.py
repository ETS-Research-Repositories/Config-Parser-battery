import collections
from copy import deepcopy as dcopy
from typing import Dict, Any


# merge hierarchically two dictionaries
# todo: improve this function
def dict_merge(dct: Dict[str, Any], merge_dct: Dict[str, Any], re=True):
    """
    Recursive dict merge. Inspired by :meth:``dict.update()``, instead of
    updating only top-level keys, dict_merge recurses down into dicts nested
    to an arbitrary depth, updating keys. The ``merge_dct`` is merged into``dct``.
    :param dct: dict onto which the merge is executed
    :param merge_dct: dct merged into dct
    :return: None
    """
    # dct = dcopy(dct)
    if merge_dct is None:
        if re:
            return dct
        else:
            return
    for k, v in merge_dct.items():
        if (
                k in dct
                and isinstance(dct[k], dict)
                and isinstance(merge_dct[k], collections.Mapping)
        ):
            dict_merge(dct[k], merge_dct[k])
        else:
            dct[k] = merge_dct[k]
    if re:
        return dcopy(dct)


merge_dict = dict_merge
