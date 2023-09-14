import cv2
import numpy as np


class Button:

    def __init__(self, lu_pos: tuple, dr_pos: tuple, text: str, text_pos: tuple):
        self.luPos = lu_pos
        self.drPos = dr_pos
        self.text = text
        self.textPos = text_pos

    def draw(self, img, color: tuple) -> np.array:
        """
        Draw the Button object at the correct position with its text on the image using its position properties

        :param img: The image frame where the button is drawn
        :param color: The color which the button is drawn with

        :return: The image itself
        """
        cv2.rectangle(img=img, pt1=self.luPos, pt2=self.drPos, color=color, thickness=3)
        if self.text == "Del" or "Cle":  # Delete and clear buttons
            cv2.putText(img=img, text=self.text, org=self.textPos, fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                        color=(0, 0, 0), thickness=3)
        else:  # all other buttons and output line
            cv2.putText(img=img, text=self.text, org=self.textPos, fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=5,
                        color=(0, 0, 0), thickness=3)
        return img

    def draw_with_external_text(self, img, color: tuple, new_text: str):
        """
        Draw the button at the correct position with a text that supplied as argument on the image using its position properties

        :param img: The image frame where the button is drawn
        :param color: The color which the button is drawn with
        :param new_text: The text the button should contain

        :return: The image itself
        """

        self.text = new_text
        self.draw(img=img, color=color)
