from instagrapi import Client
import time
import os

USERNAME = "nocti1ux"
PASSWORD = "Yubraj$$2ins2"

cl = Client()

# 🔐 2FA challenge handler
def handle_challenge(username):
    print("🔐 Instagram sent a code (email/SMS)")
    code = input(f"Enter the 6-digit code for @{username}: ")
    cl.challenge_resolve(code)

# 📂 Load session if available
SESSION_FILE = "session.json"
if os.path.exists(SESSION_FILE):
    cl.load_settings(SESSION_FILE)

try:
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(SESSION_FILE)
except Exception as e:
    print("Login failed:", e)
    handle_challenge(USERNAME)
    cl.dump_settings(SESSION_FILE)

# 📌 Post target
shortcode = "DLw75utzg67"
media_id = cl.media_id(cl.media_pk_from_code(shortcode))

# 📁 Load previously replied users
replied_users_file = "users.txt"
if os.path.exists(replied_users_file):
    with open(replied_users_file, "r") as f:
        replied_users = set(line.strip() for line in f if line.strip())
else:
    replied_users = set()

# 💬 Fetch all comments
comments = cl.media_comments(media_id)

for comment in comments:
    username = comment.user.username.strip()
    comment_text = comment.text.lower()

    if "rice" in comment_text and username not in replied_users:
        reply_text = "Here’s the product link: https://amzn.to/4lllqVV"

        try:
            # ✅ Direct threaded reply (like Instagram comment reply)
            cl.media_comment(media_id, reply_text, replied_to_comment_id=comment.pk)
            print(f"✅ Replied directly to @{username}")
            
            replied_users.add(username)
            with open(replied_users_file, "a") as f:
                f.write(username + "\n")

            time.sleep(5)
        except Exception as e:
            print(f"❌ Failed to reply to @{username} | Error: {e}")
