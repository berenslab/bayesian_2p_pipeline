  
def fill_bounds(x, upper, lower, axis, c = 'k', alpha = 0.2):
    """
    Plot upper and lower bounds on current axis.
    """
    axis.fill_between(
        x, 
        upper[:, 0], 
        lower[:, 0], 
        facecolor = c,
        alpha = alpha
    )