import numpy as np

def perspective(right, top, near, far):
    A = near/right
    B = near/top
    C = -(far+near)/(far-near)
    D = -2*far*near/(far-near)

    return np.array((
        ( A, 0, 0, 0),
        ( 0, B, 0, 0),
        ( 0, 0, C, -1),
        ( 0, 0, D, 0)
    ))
    