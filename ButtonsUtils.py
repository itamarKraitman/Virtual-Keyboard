from itertools import chain
from time import sleep

import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

from Button import Button


class ButtonsUtils:

    @staticmethod
    def create_buttons(space=125) -> (list, Button):
        """
        Create all buttons at the correct positions within the camera window, along with their respective text.
        In addition, create the output line

        :return: A list of all buttons.
        """

        button_positions = [[(50 + i * space, 150, 150 + i * space, 250) for i in range(9)],
                            [(50 + i * space, 275, 150 + i * space, 375) for i in range(10)],
                            [(50 + i * space, 400, 150 + i * space, 500) for i in range(10)]]
        button_text = [["A", "B", "C", "D", "E", "F", "G", "H", "I"],
                       ["J", "K", "L", "M", "N", "O", "P", "Q", "R", "Cle"],
                       ["S", "T", "U", "V", "W", "X", "Y", "Z", "_", "Del"]]
        text_position = [[(75 + i * space, 230) for i in range(9)],
                         [(75 + i * space, 355) for i in range(10)],
                         [(75 + i * space, 480) for i in range(10)]]
        buttons = []

        for i in range(3):
            line = [Button(lu_pos=position[:2], dr_pos=position[2:], text=text, text_pos=t_position) for
                    position, text, t_position in zip(button_positions[i], button_text[i], text_position[i])]
            buttons.append(line)

        # Output button
        output_line = Button(lu_pos=(50, 525), dr_pos=(1230, 625), text="", text_pos=(65, 600))

        return list(chain.from_iterable(buttons)), output_line

    @staticmethod
    def draw_buttons(img, buttons: list, output_line: Button, buttons_color=(0, 0, 255, cv2.FILLED)):
        """
        Draw all buttons including output line at the correct position on the window

        :param img: The image frame in which the buttons are drawn.
        :param buttons: A list of Button objects representing the buttons on the screen.
        :param output_line: Button object where the output text will be shown

        :return: None
        """

        for button in buttons:
            button.draw(img=img, color=buttons_color)
        output_line.draw(img=img, color=buttons_color)

    @staticmethod
    def hovering_over_button(detector: HandDetector, img, buttons: list, lm: list,
                             current_output: str, max_output_width=1230) -> str:
        """
        Detects if a hand is hovering over any of the provided buttons and handles button interactions.

        :param detector: An instance of the HandDetector class for hand tracking.
        :param img: The image frame in which the buttons are drawn.
        :param buttons: A list of Button objects representing the buttons on the screen.
        :param lm: A list of hand landmark points.
        :param current_output: The current output text associated with button interactions.

        :return: The updated current output text after button interactions.
        """

        def click() -> bool:
            """
            Detects if a click is made by the user.

            :return: The updated boolean value for the clicking condition.
            """
            if detector.findDistance(p1=lm[8][:2], p2=lm[12][:2], img=img)[
                0] < 30:  # 30 is the distance between the two fingers are side by side
                print("Click!")
                return True

        for button in buttons:
            x_lu, y_lu = button.luPos
            x_dr, y_dr = button.drPos
            if x_lu < lm[8][0] < x_dr and y_lu < lm[8][1] < y_dr:
                button.draw(img=img, color=(0, 255, 0, cv2.FILLED))
                if click():
                    ru_pos, ld_pos = [button.drPos[0], button.luPos[1]], [button.luPos[0], button.drPos[1]]
                    points = np.array([button.luPos, ru_pos, button.drPos, ld_pos])
                    cv2.fillPoly(img=img, pts=[points], color=(0, 255, 0))
                    cv2.putText(img=img, text=button.text, org=button.textPos, fontFace=cv2.FONT_HERSHEY_PLAIN,
                                fontScale=5,
                                color=(0, 0, 0), thickness=3)
                    print(f"Button {button.text} is clicked")
                    current_output = current_output + ' ' if button.text == '_' else '' if button.text == 'Cle' else current_output[
                                                                                                                     :-1] if button.text == "Del" else current_output + button.text
                    if \
                            cv2.getTextSize(text=current_output, fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=5,
                                            thickness=3)[0][
                                0] > max_output_width:  # If text length passed output line length, text is too long
                        print("Output is too long! Clearing output text")
                        current_output = ""
                    else:
                        print(f"Current output is : {current_output} \n")
                    sleep(0.2)  # Sleeping for 0.2 seconds in order to prevent printing more than 1 letter each click

        return current_output

    @staticmethod
    def run(cap: cv2.VideoCapture):
        """
        Activating the keyboard with all utilities
        :param cap: Video camera to display the keyboard on
        :return:
        """
        detector = HandDetector(detectionCon=0.8)
        final_output = ""

        while True:

            # Activating camera
            success, frame = cap.read()
            if not success:
                continue

            img = cv2.resize(frame, (1280, 720))  # Resize the frame to fit the window resolution

            hands, img = detector.findHands(img)

            # Drawing buttons
            buttons, output_line = ButtonsUtils.create_buttons()
            ButtonsUtils.draw_buttons(img=img, buttons=buttons, output_line=output_line)

            if hands:
                # finding hands
                hand = hands[0]
                lm, bbox = hand["lmList"], hand["bbox"]

                # Hovering over buttons
                if lm:
                    final_output = ButtonsUtils.hovering_over_button(detector=detector, img=img, buttons=buttons,
                                                                     lm=lm, current_output=final_output)

            # Drawing output on screen
            output_line.draw_with_external_text(img=img, color=(0, 0, 255, cv2.FILLED), new_text=final_output)

            cv2.imshow("Virtual Keyboard", img)
            if cv2.waitKey(1) == 27:
                break
