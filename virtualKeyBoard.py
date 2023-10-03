import cv2

import warnings

from ButtonsUtils import ButtonsUtils

warnings.filterwarnings("ignore")

if __name__ == '__main__':
    # Setting the camera view
    cap = cv2.VideoCapture(0)

    cap.set(3, 1280)
    cap.set(4, 720)

    cv2.namedWindow("Virtual Keyboard", cv2.WINDOW_FREERATIO)
    cv2.resizeWindow("Virtual Keyboard", 1280, 720)

    ButtonsUtils.run(cap=cap)

    cap.release()
    cv2.destroyAllWindows()
