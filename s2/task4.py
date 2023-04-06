class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def solution(rect1: Rect, rect2: Rect):
    arr = [rect1, rect2]
    arr.sort(key=lambda rect: rect.x1)

    distX = arr[0].x2 - arr[1].x1 if arr[0].x2 - arr[1].x1 > 0 else 0
    distY = arr[1].y1 - arr[0].y2 > 0 if arr[1].y1 - arr[0].y2 > 0 else 0

    return distX * distY
