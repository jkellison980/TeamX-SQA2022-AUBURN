import traceback
from typing import List, Any
import numpy as np 
#Comment for testing 
from scanner import isValidUserName
from scanner import scanKeys
from scanner import isValidPasswordName
from scanner import scanForSecrets
from scanner import isValidKey

def fuzz(method, fuzzed_args: List[Any]):
    for args in fuzzed_args:
        try:
            result = method(*args)
        except Exception as exc:
            print(f"FUZZ: {method.__name__} FAILED :()  ")
            traceback.print_exc()
        else:
            print(f"FUZZ: {method.__name__} PASSED: ({result})")


# if __name__ == "__main__":
#     fuzz_methods = [
#         (isValidPasswordName)
#     ]
#     fuzz_value = [
#         (Null),
#         (🙉),
#         (True)
#         (False)
        
#     ]
#     fuzz(isValidPasswordName, fuzz_value)





if __name__ == "__main__":
    fuzz_method = [
        (
            isValidUserName, [
                (None),
            ]
        ),
        (
            scanKeys,[
                (False),
            ]
        ),
        (
            isValidPasswordName, [
                (True),
            ]
        ),
        (
            scanForSecrets, [
                # (None),
                # ("yaml"),
                ([]),
                # (""),
                # (float("-inf")),
                # (1j),
                # (np.NAN),
            ]
        ),
          (
            isValidKey, [
                # (None, None),
                # (1, 2),
                # (1.0, 2.0),
                ([], {}),
                # ("bad-filename", "random"),
            ]
        )

    ]
    for method, fuzzed_args in fuzz_method:
        fuzz(method, fuzzed_args)
