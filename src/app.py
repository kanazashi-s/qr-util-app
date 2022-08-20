import os
from PIL import Image
import streamlit as st
from amzqr import amzqr


def save_image(image_file, img_name):
    img = Image.open(image_file)
    img.save(img_name, quality=95)
    return


def main():
    st.title("QR Code Generator")
    input_url = st.text_input("Enter Target URL", "https://www.google.com/?hl=ja")
    input_img = st.file_uploader("Upload Base Image[jpg, png, bmp].", type=["jpg", "png", "bmp"])
    if input_url is not None:
        if input_img is not None:
            extension = input_img.name.split(".")[-1]
            img_name = f"tmp_img.{extension}"
            save_image(input_img, img_name)
            use_img = True
        else:
            use_img = False

        save_dir = "output"
        os.makedirs(save_dir, exist_ok=True)
        version, level, qr_name = amzqr.run(
            input_url,
            version=1,
            level='H',
            picture=img_name if use_img else None,
            colorized=False,
            contrast=1.0,
            brightness=1.0,
            save_name=None,
            save_dir="output"
        )

        st.image(qr_name)
        with open(qr_name, "rb") as f:
            btn = st.download_button(
                label="Download QR Code",
                data=f,
                file_name="created_qr.png",
                mime="image/png"
            )


if __name__ == "__main__":
    main()