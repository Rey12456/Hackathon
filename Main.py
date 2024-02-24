import instaloader

# Create an instance of Instaloader class
L = instaloader.Instaloader()

# Optionally, login
# Replace 'USER' and 'PASSWORD' with your Instagram credentials
L.login(USER, PASSWORD)

try:
    # Get a Post object using the shortcode of the post
    post = instaloader.Post.from_shortcode(L.context, 'SHORTCODE_OF_POST')

    # Retrieve comments
    comments = post.get_comments()

    # Iterate through comments and print them
    for comment in comments:
        print(comment.text)

except instaloader.exceptions.InstaloaderException as e:
    print("An error occurred:", e)
