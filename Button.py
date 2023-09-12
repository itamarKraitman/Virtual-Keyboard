import cv2


class Button:
    def __init__(self, lu_pos: tuple, dr_pos: tuple, text: str, text_pos: tuple):
        self.luPos = lu_pos
        self.drPos = dr_pos
        self.text = text
        self.textPos = text_pos

    def draw(self, img, color: tuple):
        cv2.rectangle(img=img, pt1=self.luPos, pt2=self.drPos, color=color, thickness=3)
        if len(self.text) == 1:
            cv2.putText(img=img, text=self.text, org=self.textPos, fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=5,
                        color=(0, 0, 0), thickness=3)
        else: # Delete and clear buttons
            cv2.putText(img=img, text=self.text, org=self.textPos, fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                        color=(0, 0, 0), thickness=3)
        return img

    def draw_with_external_text(self, img, color: tuple, text: str):
        cv2.rectangle(img=img, pt1=self.luPos, pt2=self.drPos, color=color, thickness=3)
        cv2.putText(img=img, text=text, org=self.textPos, fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=5,
                    color=(0, 0, 0), thickness=3)
        return img
