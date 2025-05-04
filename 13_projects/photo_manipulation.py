from PIL import Image, ImageEnhance, ImageFilter

def welcome_message():
    print("\n\t\t\t~~~~~~ WELCOME TO THE PHOTO MANIPULATOR! ~~~~~~\n")
    print("In this tool, you can apply filters, enhance contrast, brightness, and blur your image.")
    print("Make sure your image file is in the same folder.\n")
    print("\t\t\t========== Let's start editing! ==========\n")

def manipulate_image():
    # Load image
    image_path = input("Enter the image filename (e.g., 'photo.jpg'): ")
    try:
        img = Image.open(image_path)
        img.show()

        print("\nChoose what you want to apply:")
        print("1. Enhance Contrast")
        print("2. Enhance Brightness")
        print("3. Apply Blur")
        print("4. Apply All")

        choice = input("\nEnter your choice (1/2/3/4): ")

        if choice == "1":
            factor = float(input("Enter contrast factor (e.g., 1.5): "))
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(factor)
        elif choice == "2":
            factor = float(input("Enter brightness factor (e.g., 1.2): "))
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(factor)
        elif choice == "3":
            img = img.filter(ImageFilter.BLUR)
        elif choice == "4":
            contrast = ImageEnhance.Contrast(img).enhance(1.5)
            brightness = ImageEnhance.Brightness(contrast).enhance(1.2)
            img = brightness.filter(ImageFilter.BLUR)
        else:
            print("Invalid choice. No changes made.")

        # Save edited image
        save_path = input("\nEnter filename to save edited image (e.g., 'edited.jpg'): ")
        img.save(save_path)
        print("\nEdited image saved successfully!")

    except FileNotFoundError:
        print("Image file not found. Please check the filename and try again.")

# Main loop to play again
while True:
    welcome_message()
    manipulate_image()

    play_again = input("\nDo you want to edit another image? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\nThank you for using the Photo Manipulator!")
        break
