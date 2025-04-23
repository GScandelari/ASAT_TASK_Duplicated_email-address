from bs4 import BeautifulSoup
from collections import Counter


def extract_names_emails(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    users = []

    # Find all label elements
    for label in soup.find_all('label', class_='MuiFormControlLabel-root'):
        # Extract name
        name_tag = label.find('strong')
        name = name_tag.get_text(strip=True) if name_tag else 'Unknown'

        # Extract email
        email_tag = label.find('span', class_='AuthorEmail')
        email = email_tag.get_text(strip=True) if email_tag else 'Unknown'

        users.append({'name': name, 'email': email})

    return users


def find_duplicate_emails(users):
    # Count email occurrences
    email_counts = Counter(user['email'] for user in users)

    # Find duplicate emails
    duplicate_emails = {email for email, count in email_counts.items() if count > 1}

    # Collect users with duplicate emails
    duplicates = [user for user in users if user['email'] in duplicate_emails]

    return duplicates


def read_html_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    # Read HTML content from the file
    html_content = read_html_from_file('input.txt')

    # Extract names and emails
    user_data = extract_names_emails(html_content)

    # Find and print duplicate emails
    duplicates = find_duplicate_emails(user_data)

    for user in duplicates:
        print(f"Name: {user['name']}, Email: {user['email']}")


if __name__ == "__main__":
    main()
