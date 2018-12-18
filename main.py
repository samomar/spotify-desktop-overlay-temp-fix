import pyautogui
import cv2
from PIL import Image

im_spotify_logo = cv2.imread('spotify_logo.png')
spotify_logo = Image.fromarray(im_spotify_logo)

pyautogui.FAILSAFE = True

screen_size_x, screen_size_y = pyautogui.size()


def find_spotify_logo(x=15, y=15):
    try:
        settings_down_arrow = pyautogui.locateCenterOnScreen("settings_down_arrow.png", grayscale=True, confidence=.7)
        if settings_down_arrow:
            return True
        spotify_x, spotify_y = pyautogui.locateCenterOnScreen(spotify_logo.resize((x, y)), grayscale=True,
                                                              confidence=.6)
        pyautogui.moveTo(spotify_x, spotify_y)
        pyautogui.doubleClick(spotify_x, spotify_y)
        search = pyautogui.locateCenterOnScreen('search.png', grayscale=True, confidence=.7)
        if search:
            return True
        else:
            x += 5
            y += 5
            find_spotify_logo(x, y)
    except TypeError:
        x += 5
        y += 5
        print(x, y)
        find_spotify_logo(x, y)
        find_spotify_logo()


if find_spotify_logo():
    pass


def find_and_click_settings_down_arrow():
    try:
        settings_down_arrow = pyautogui.locateCenterOnScreen("settings_down_arrow.png", grayscale=True, confidence=.7)
        pyautogui.click(settings_down_arrow[0], settings_down_arrow[1])
        settings_x, settings_y = pyautogui.locateCenterOnScreen('spotify_settings_button.png', grayscale=True,
                                                                confidence=.7)
        if settings_x:
            pyautogui.moveTo(settings_x, settings_y)
            pyautogui.click(settings_x, settings_y)
        else:
            find_and_click_settings_down_arrow()
    except TypeError:
        find_and_click_settings_down_arrow()


find_and_click_settings_down_arrow()


def main_settings():
    try:
        locate_big_settings_text = pyautogui.locateCenterOnScreen("big_settings.png", grayscale=True, confidence=.7)
        if locate_big_settings_text:
            def show_desktop_overlay_option():
                pyautogui.scroll(-2000)
                locate_show_desktop_overlay_option = pyautogui.locateCenterOnScreen("show_desktop_overlay_option.png",
                                                                                    grayscale=True,
                                                                                    confidence=.7)
                if locate_show_desktop_overlay_option:
                    pass
                else:
                    show_desktop_overlay_option()

            show_desktop_overlay_option()
        else:
            main_settings()
    except TypeError:
        main_settings()


main_settings()


def off_button():
    try:
        locate_off_buttons = pyautogui.locateAllOnScreen("off_button.png")

        last_off_button = list(i for i in locate_off_buttons)[-1]  # Finds the last visible deactivated switch.
        pyautogui.moveTo(last_off_button[0] + 5, last_off_button[1] + 10)
        pyautogui.click(last_off_button[0] + 5, last_off_button[1] + 10)
        pyautogui.moveTo(last_off_button[0] + 10, last_off_button[1] + 20)
        pyautogui.click(last_off_button[0] + 10, last_off_button[1] + 20)
    except TypeError:
        off_button()


off_button()


def go_back():
    try:
        back_arrow = pyautogui.locateCenterOnScreen('back_arrow.png', grayscale=True, confidence=.7)
        pyautogui.moveTo(back_arrow[0], back_arrow[1])
        pyautogui.click(back_arrow[0], back_arrow[1])
    except TypeError:
        go_back()


go_back()
