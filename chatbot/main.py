# chatbot/main.py

from chatbot.chatbot import Chatbot
from chatbot.handlers.faq_handler import FAQHandler
from chatbot.handlers.order_handler import OrderHandler
from chatbot.handlers.product_inquiry_handler import ProductInquiryHandler

def main():
    # Example usage
    chat_bot = Chatbot("Bot")
    faq_bot = FAQHandler("FAQBot")
    order_bot = OrderHandler("OrderBot")
    product_bot = ProductInquiryHandler("ProductBot")

    user_input = input("Ask the chatbot: ")
    print(chat_bot.get_response(user_input))

if __name__ == "__main__":
    main()
