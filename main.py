import cv2
from cvzone.HandTrackingModule import HandDetector
from itertools import chain
from Button import Button


def create_buttons():
    button_positions = [[(50 + i * 125, 350, 150 + i * 125, 450) for i in range(9)],
                        [(50 + i * 125, 475, 150 + i * 125, 575) for i in range(9)],
                        [(50 + i * 125, 600, 150 + i * 125, 700) for i in range(9)]]
    button_text = [["A", "B", "C", "D", "E", "F", "G", "H", "I"],
                   ["J", "k", "L", "M", "N", "O", "p", "Q", "R"],
                   ["S", "T", "U", "V", "W", "X", "Y", "Z"]]
    text_position = [[(75 + i * 125, 430) for i in range(9)],
                     [(75 + i * 125, 555) for i in range(9)],
                     [(75 + i * 125, 680) for i in range(9)]]
    buttons = []

    for i in range(3):
        line = [Button(lu_pos=position[:2], dr_pos=position[2:], text=text, text_pos=t_position) for
                position, text, t_position in zip(button_positions[i], button_text[i], text_position[i])]
        buttons.append(line)

    return list(chain.from_iterable(buttons))


def move_across_button():


def main():
    # Setting the camera view
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    detector = HandDetector(detectionCon=0.8)

    while True:

        # Activating camera
        success, img = cap.read()
        hands, img = detector.findHands(img)

        # Drawing buttons
        buttons = create_buttons()
        for button in buttons:
            button.draw(img=img)

        if hands:
            # finding hands
            hand = hands[0]
            lm, bbox = hand["lmList"], hand["bbox"]

            if lm:
                for button in buttons:
                    x_lu, y_lu = button.luPos
                    x_dr, y_dr = button.drPos




    cv2.imshow("Image", img)
    cv2.waitKey(1)


if __name__ == '__main__':
    main()
