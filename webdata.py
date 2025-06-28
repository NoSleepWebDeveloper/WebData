import requests

def display_disclaimer():
    print("""
Welcome to WebData

WebData is committed to responsibly collecting and securely managing personal information provided by our participants. Our primary goal is to support law enforcement agencies in their investigative efforts and to contribute valuable data for educational and research purposes.

The information you provide will be handled with the highest standards of privacy and security. We store your data in encrypted systems to prevent unauthorized access and ensure confidentiality.

By participating and submitting your personal information, you acknowledge and agree that your data may be used by authorized personnel for lawful investigations and academic research aimed at improving online safety, security, and awareness.

Your trust is important to us. If you have any questions or concerns about how your data is collected, stored, or used, please do not hesitate to reach out to our support team.

Please note that your information will not be given out to any businesses, nor databrokers. Your information is secure here and not given to anyone except our team (rarely) and law enforcement.

By continuing, you provide your explicit consent for WebData to collect, store, and utilize your information in accordance with these terms.

Thank you for contributing to a safer and more informed digital community.
    """)

def get_user_info():
    print("\nPlease enter the following details to participate in the database:")

    user_data = {}
    user_data['full_name'] = input("Full Name: ").strip()
    user_data['email'] = input("Email Address: ").strip()
    user_data['physical_address'] = input("Physical Address: ").strip()
    user_data['phone_number'] = input("Phone Number: ").strip()
    user_data['online_handle'] = input("Online Handle: ").strip()

    return user_data

def send_to_discord(webhook_url, user_data):
    content = (
        "**New User Submission to WebData:**\n"
        f"Full Name: {user_data['full_name']}\n"
        f"Email: {user_data['email']}\n"
        f"Physical Address: {user_data['physical_address']}\n"
        f"Phone Number: {user_data['phone_number']}\n"
        f"Online Handle: {user_data['online_handle']}\n\n"
        "_Note: This data is collected for law enforcement and educational purposes._"
    )

    data = {
        "content": content
    }

    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print("\nSuccessfully logged.")
    else:
        print(f"\nFailed to log data. Status code: {response.status_code}")
        print(response.text)

def main():
    webhook_url = "https://discord.com/api/webhooks/1388626884908286113/Izo1T9bb4E34tblLpG2nq3KD1OryZNZMs9LVyll6HzRftLlhuWnR1xPhDxS3jXTqcXKS"  # Replace with your Discord webhook URL

    display_disclaimer()
    consent = input("Do you consent to providing your data? (yes/no): ").strip().lower()

    if consent not in ['yes', 'y']:
        print("Consent not given. Exiting program.")
        return

    user_info = get_user_info()
    send_to_discord(webhook_url, user_info)

if __name__ == "__main__":
    main()
