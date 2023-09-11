import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from itertools import chain
from Button import Button


def create_buttons():
    button_positions = [[(50 + i * 125, 150, 150 + i * 125, 250) for i in range(9)],
                        [(50 + i * 125, 275, 150 + i * 125, 375) for i in range(9)],
                        [(50 + i * 125, 400, 150 + i * 125, 500) for i in range(10)]]
    button_text = [["A", "B", "C", "D", "E", "F", "G", "H", "I"],
                   ["J", "k", "L", "M", "N", "O", "p", "Q", "R"],
                   ["S", "T", "U", "V", "W", "X", "Y", "Z", "_", "Del"]]
    text_position = [[(75 + i * 125, 230) for i in range(9)],
                     [(75 + i * 125, 355) for i in range(9)],
                     [(75 + i * 125, 480) for i in range(10)]]
    buttons = []

    for i in range(3):
        line = [Button(lu_pos=position[:2], dr_pos=position[2:], text=text, text_pos=t_position) for
                position, text, t_position in zip(button_positions[i], button_text[i], text_position[i])]
        buttons.append(line)

    # Output button
    output_button = Button(lu_pos=(50, 525), dr_pos=(1150, 625), text="", text_pos=(65, 600))

    return list(chain.from_iterable(buttons)), output_button


def hovering_over_button(detector: HandDetector, img, buttons: list, lm: list,
                         final_output: str):
    for button in buttons:
        x_lu, y_lu = button.luPos
        x_dr, y_dr = button.drPos
        if x_lu < lm[8][0] < x_dr and y_lu < lm[8][1] < y_dr:
            button.draw(img=img, color=(0, 255, 0, cv2.FILLED))
            if click(detector=detector, img=img, lm=lm):
                ru_pos, ld_pos = [button.drPos[0], button.luPos[1]], [button.luPos[0], button.drPos[1]]
                points = np.array([button.luPos, ru_pos, button.drPos, ld_pos])
                cv2.fillPoly(img=img, pts=[points], color=(0, 255, 0))
                cv2.putText(img=img, text=button.text, org=button.textPos, fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=5,
                            color=(0, 0, 0), thickness=3)
                print(button.text)
                final_output = final_output + ' ' if button.text == '_' else '' if button.text == 'Del' else final_output + button.text
                print(final_output)

    return final_output


def click(detector: HandDetector, img, lm: list):
    if detector.findDistance(p1=lm[8][:2], p2=lm[12][:2], img=img)[0] < 30:
        print(lm[8][:2], lm[12][:2])
        print("Click!")
        return True


def main():
    # Setting the camera view
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    detector = HandDetector(detectionCon=0.8)
    final_output = ""

    while True:

        # Activating camera
        success, img = cap.read()
        hands, img = detector.findHands(img)

        # Drawing buttons
        buttons, output_button = create_buttons()
        for button in buttons:
            button.draw(img=img, color=(0, 0, 255, cv2.FILLED))
        output_button.draw(img=img, color=(0, 0, 255, cv2.FILLED))

        if hands:
            # finding hands
            hand = hands[0]
            lm, bbox = hand["lmList"], hand["bbox"]

            # Hovering over buttons
            if lm:
                final_output = hovering_over_button(detector=detector, img=img, buttons=buttons,
                                                    lm=lm, final_output=final_output)

        # Drawing output on screen
        output_button.draw_with_external_text(img=img, color=(0, 0, 255, cv2.FILLED), text=final_output)

        cv2.imshow("Virtual Keyboard", img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()
