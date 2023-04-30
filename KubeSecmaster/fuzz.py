import traceback
from typing import List, Any
import numpy


from scanner import isValidPasswordName

def fuzz(method, fuzzed_args: List[Any]):
    for args in fuzzed_args:
        try:
            result = method(args)
        except Exception as exc:
            print(f"FUZZ: {method.__name__} FAILED :()  ")
            traceback.print_exc()
        else:
            print(f"FUZZ: {method.__name__} PASSED: ({result})")


if __name__ == "__main__":
    fuzz_methods = [
        (isValidPasswordName)
    ]
    fuzz_value = [
        #(Null),
        #(🙉),
        #(True)
        #(False)
        
    ]
    fuzz(isValidPasswordName, fuzz_value)