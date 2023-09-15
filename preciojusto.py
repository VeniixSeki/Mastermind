"""Requirements

pip install pipwin
pip install readchar
pipwin install PIL
"""
import os
from io import BytesIO
from PIL import Image
import random
import readchar
from requests_html import HTMLSession
from speak_and_listen import speak, hear_me


def start_game():
    """Start the game"""
    speak("Welcome to the just price!!"
          "Can you guess the correct price of a product?")


def press_key():
    """Say 'Press a key' message to the user"""
    speak("Press enter to start the game. Or press Q to exit.")
    message = "Press ENTER to continue or Q to exit the game"
    print("-" * len(message) + "\n" + message + "\n" + "-" * len(message))


def win_message():
    """Say a short win message for the user"""
    speak("Congratulations, you guess the correct price of this product!")


def game_over_message():
    """Say a game over message for the user"""
    speak("Game over, this is not the correct price of this product.")


def hear_price_and_get_number():
    """Consult the user for the product price

    Returns
    -------
        user_price : int
            The number that the user say
    """
    user_price = None
    try:
        speak("What's the price of this product?")
        user_price = int(hear_me().replace(",", ""))
    except TypeError:
        speak("This is not a number. Try again.")
        hear_price_and_get_number()
    return user_price


def get_product(session):
    """Choose a random product in extreme tech website

    Parameters
    ----------
        session : requests_html.HTMLSession
            The html session
    Returns
    -------
        jpg : list
            A list with the name, price and the image of a product
    """

    """Choose a subcategory in the main page"""
    main_side = session.get("https://extremetechcr.com/tienda/")
    categories = main_side.html.find(".inner")
    category = random.choice(categories)
    selected_category = random.choice(list(category.absolute_links))

    """Enter in the sub category link"""
    sub_category = session.get(selected_category)
    products_images = sub_category.html.find(".product_img_link")
    products_prices = sub_category.html.find(".content_price")
    products_names = sub_category.html.find(".name")

    """Select a random product of the subcategory"""
    try:
        selected_product = random.randint(0, len(products_prices) - 1)
    except ValueError:
        selected_product = 0
    selected_product_image = products_images[selected_product]
    selected_product_price = products_prices[selected_product]
    selected_product_name = products_names[selected_product]

    """Get the product name"""
    name = selected_product_name.full_text.replace("\n", "")

    """Get the price"""
    price = selected_product_price.full_text.replace(" ", "").replace("\n", "").replace("₡", "").replace(",", "")

    """Get the image path"""
    image_link = selected_product_image.attrs['href']
    image = session.get(image_link)
    jpg_selected = image.html.find("#bigpic")
    jpg = jpg_selected[0].attrs['src']

    return [name, price, jpg]


def show_product(product_info, session):
    """Show the image and the name of the product

    Parameters
    ----------
        product_info : list
            A list with the product information
            (name, price, image)
        session : requests_html.HTMLSession
            The html session

    Returns
    -------
        image_and_name : None
            The product image and name
    """
    img = product_info[2]
    img_downloaded = session.get(img)
    image = Image.open(BytesIO(img_downloaded.content))
    image.show()
    name = product_info[0]
    print(f"The product name is {name}")
    speak(f"The product name is {name}")


def compare_answer(product_info, user_price):
    """Compare the product price with the user answer

    Parameters
    ----------
        product_info : list
            A list with the product information
        user_price : int
            The value that the user says
    Returns
    -------
        answer : bool
            The answer to the comparative between product price and the user answer
    """
    answer = False

    if product_info[1] == user_price:
        answer = True

    return answer


def correct_price(price):
    """Say the correct price of the product

    Parameters
    ----------
        price : int
            The product correct price
    """
    speak(f"The correct price is {price}")


def run_game(session, key):
    """Run the game as long as the user wants

        Parameters
        ----------
            session : requests_html.HTMLSession
                The html session
            key : str
                key pressed by the user
        """
    while key != "Q" and key != "q":
        os.system("cls")
        got_number_condition = False
        product_info = []

        while not got_number_condition:

            try:
                product_info = get_product(session)
                got_number_condition = True
            except IndexError:
                pass

        if product_info:
            show_product(product_info, session)

        user_price = hear_price_and_get_number()
        win_condition = compare_answer(product_info, user_price)

        if win_condition:
            win_message()
        else:
            game_over_message()
            correct_price(product_info[1])

        press_key()
        key = readchar.readchar().decode()


def main():
    """Start the game"""
    session = HTMLSession()
    os.system("cls")
    start_game()
    press_key()
    key = readchar.readchar().decode()
    run_game(session, key)


if __name__ == "__main__":
    main()