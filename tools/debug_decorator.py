def debug(func):
    """Print input arguments and output value(s) of any function.

    Args:
        func (function): Any function.
    
    Returns:
        debug_internal_logic: The input function passed into the 
        debug_internal_logic function.
    """
    
    def debug_internal_logic(*args, **kwargs):
        """Print the input arguments of any function while debugging. This 
        function is wrapped by the "debug" function so as to be used as 
        a decorator.

        Args:
            *args: A varying number of positional arguments
            **kwargs: A varying number of keyword arguments
        
        Returns:
            output: The original input function defined as "func" from 
            the "debug" wrapper function above.
        """

        print("Function name", func.__name__)
        print("Input arguments:", ' '.join(map(str, args)))
        print("Input keyword arguments:", kwargs.items())
        output = func(*args, **kwargs)
        print("Output:", output)
        return output
    return debug_internal_logic