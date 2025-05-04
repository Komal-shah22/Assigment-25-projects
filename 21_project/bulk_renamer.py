import os

def welcome():
    print("\n\t~~~~~~ WELCOME TO THE BULK FILE RENAMER ~~~~~~")
    print("Easily rename multiple files in a folder based on your custom pattern.\n")

def rename_files(folder_path, new_name, extension):
    try:
        files = [f for f in os.listdir(folder_path) if f.endswith(extension)]
        files.sort()  # optional: sort alphabetically
        for count, filename in enumerate(files, start=1):
            new_filename = f"{new_name}_{count}{extension}"
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_filename}")
        print("\n✅ All files renamed successfully.")
    except Exception as e:
        print("❌ Error:", e)

while True:
    welcome()
    folder = input("Enter the full folder path: ").strip()
    name = input("Enter the new base name (e.g., photo): ").strip()
    ext = input("Enter the file extension to target (e.g., .jpg, .txt): ").strip()

    if not os.path.exists(folder):
        print("❌ The folder does not exist. Please try again.\n")
    else:
        rename_files(folder, name, ext)

    again = input("\nDo you want to rename files in another folder? (yes/no): ").strip().lower()
    if again != 'yes':
        print("\n👋 Goodbye! Thanks for using the bulk file renamer.")
        break
