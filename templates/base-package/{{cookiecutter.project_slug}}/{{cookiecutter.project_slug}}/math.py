"""Math.py implements euler method for {{cookiecutter.project_slug}}"""

import logging

# Create a logger for this submodule
logger = logging.getLogger('{{cookiecutter.project_slug}}.math')

def euler_method(f, y0, t0, t1, h):
    """
    Solve the ODE y' = f(t, y) using Euler's method.

    Args:
        f: Function representing the ODE y' = f(t, y)
        y0: Initial value of y at t0
        t0: Initial time
        t1: Final time
        h: Step size

    Returns:
        t_values: List of time values
        y_values: List of corresponding y values

    ??? Examples:
        ```python 
        def ode_function(t, y):
            return -2 * y + t

        t0 = 0
        t1 = 5
        y0 = 1
        h = 0.1

        t_values, y_values = euler_method(ode_function, y0, t0, t1, h)

        for t, y in zip(t_values, y_values):
            print(f"t={t:.4f}, y={y:.4f}")
        ```

    """
    logger.info("Starting Euler's method solver")
    logger.debug(f"Initial conditions: y0={y0}, t0={t0}, t1={t1}, h={h}")

    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    while t < t1:
        y_new = y + h * f(t, y)
        t += h
        t_values.append(t)
        y_values.append(y_new)
        
        logger.debug(f"At t={t:.4f}, y={y_new:.4f}")

        y = y_new

    logger.info("Completed Euler's method solver")
    return t_values, y_values