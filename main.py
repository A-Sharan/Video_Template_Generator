import os

# List of video titles or topics
video_titles =
[
  "Subscribe",
  "to",
  "Explore",
  "The",
  "Fun"
]

# List of short video titles or topics
short_titles = [
"Short #1",
  "Short #2",
  "Short #3",
  "Short #4"
]

# Create a directory for storing videos
main_directory = "videos"
os.makedirs(main_directory, exist_ok=True)

# Create a directory for storing shorts
shorts_directory = "shorts"
os.makedirs(shorts_directory, exist_ok=True)

# Function to create subfolders inside a directory
def create_subfolders(directory, subfolders):
    for title in subfolders:
        # Remove special characters that might cause issues in folder names
        folder_name = "".join([c for c in title if c.isalnum() or c.isspace()])
        # Create a directory for the title
        title_directory = os.path.join(directory, folder_name)
        os.makedirs(title_directory, exist_ok=True)
        
        # Create subfolders for "Photos," "A roll," "B roll," and "Asset" inside each title folder
        for subfolder_name in ["Photos", "A roll", "B roll", "Asset"]:
            subfolder_path = os.path.join(title_directory, subfolder_name)
            os.makedirs(subfolder_path, exist_ok=True)

# Organize video titles into "Videos" folder with subfolders for each title
create_subfolders(main_directory, video_titles)

# Organize short titles into "Shorts" folder with subcategories
create_subfolders(os.path.join(shorts_directory, "Top 1"), short_titles[:1])#chnage these acc. your vid
create_subfolders(os.path.join(shorts_directory, "Top 2"), short_titles[2:3])
create_subfolders(os.path.join(shorts_directory, "Other"), short_titles[4:])

print("Folders and subfolders created successfully.")
