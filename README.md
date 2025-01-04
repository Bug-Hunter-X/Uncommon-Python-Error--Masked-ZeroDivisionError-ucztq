# Uncommon Python Error: Masked ZeroDivisionError

This repository demonstrates a subtle error in Python that can be difficult to identify. The code appears to handle the case where 'a' is 0, but it still results in a `ZeroDivisionError` due to implicit type conversion.

## Bug Description

The function `function_with_uncommon_error` aims to prevent a `ZeroDivisionError`. However, the error is not directly triggered by a division by zero, making it difficult to detect. The condition checks only for the case where `a` is equal to 0. Even if a is 0, the code will still produce an error since the return statement depends on whether `a` or `b` is 0.