global_var = "I am a global variable, and I'm accessable everywhere."

def outer_func():
    enclosing_var = "I am an enclosing variable, and am accessable to nested functions."

    def inner_func():
        local_var = "I am a local variable, and only accessable in this function."