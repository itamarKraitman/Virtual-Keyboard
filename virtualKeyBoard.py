import cv2
from cvzone.HandTrackingModule import HandDetector

import warnings

from ButtonsUtils import ButtonsUtils

warnings.filterwarnings("ignore")


# def main():
#     # Setting the camera view
#     cap = cv2.VideoCapture(0)
#
#     cap.set(3, 1280)
#     cap.set(4, 720)
#
#     cv2.namedWindow("Virtual Keyboard", cv2.WINDOW_FREERATIO)
#     cv2.resizeWindow("Virtual Keyboard", 1280, 720)
#
#     # detector = HandDetector(detectionCon=0.8)
#     # final_output = ""
#
#     # while True:
#     #
#     #     # Activating camera
#     #     success, frame = cap.read()
#     #     if not success:
#     #         continue
#     #
#     #     img = cv2.resize(frame, (1280, 720))  # Resize the frame to fit the window resolution
#     #
#     #     hands, img = detector.findHands(img)
#     #
#     #     # Drawing buttons
#     #     buttons, output_line = ButtonsUtils.create_buttons()
#     #     ButtonsUtils.draw_buttons(img=img, buttons=buttons, output_line=output_line)
#     #
#     #     if hands:
#     #         # finding hands
#     #         hand = hands[0]
#     #         lm, bbox = hand["lmList"], hand["bbox"]
#     #
#     #         # Hovering over buttons
#     #         if lm:
#     #             final_output = ButtonsUtils.hovering_over_button(detector=detector, img=img, buttons=buttons,
#     #                                                                   lm=lm, current_output=final_output)
#
#     # # Drawing output on screen
#     # output_line.draw_with_external_text(img=img, color=(0, 0, 255, cv2.FILLED), new_text=final_output)
#     #
#     # cv2.imshow("Virtual Keyboard", img)
#     # if cv2.waitKey(1) == 27:
#     #     break
#
#     ButtonsUtils.run(cap=cap)
#
#     cap.release()
#     cv2.destroyAllWindows()


if __name__ == '__main__':
    # Setting the camera view
    cap = cv2.VideoCapture(0)

    cap.set(3, 1280)
    cap.set(4, 720)

    cv2.namedWindow("Virtual Keyboard", cv2.WINDOW_FREERATIO)
    cv2.resizeWindow("Virtual Keyboard", 1280, 720)

    # detector = HandDetector(detectionCon=0.8)
    # final_output = ""

    # while True:
    #
    #     # Activating camera
    #     success, frame = cap.read()
    #     if not success:
    #         continue
    #
    #     img = cv2.resize(frame, (1280, 720))  # Resize the frame to fit the window resolution
    #
    #     hands, img = detector.findHands(img)
    #
    #     # Drawing buttons
    #     buttons, output_line = ButtonsUtils.create_buttons()
    #     ButtonsUtils.draw_buttons(img=img, buttons=buttons, output_line=output_line)
    #
    #     if hands:
    #         # finding hands
    #         hand = hands[0]
    #         lm, bbox = hand["lmList"], hand["bbox"]
    #
    #         # Hovering over buttons
    #         if lm:
    #             final_output = ButtonsUtils.hovering_over_button(detector=detector, img=img, buttons=buttons,
    #                                                                   lm=lm, current_output=final_output)

    # # Drawing output on screen
    # output_line.draw_with_external_text(img=img, color=(0, 0, 255, cv2.FILLED), new_text=final_output)
    #
    # cv2.imshow("Virtual Keyboard", img)
    # if cv2.waitKey(1) == 27:
    #     break

    ButtonsUtils.run(cap=cap)

    cap.release()
    cv2.destroyAllWindows()
