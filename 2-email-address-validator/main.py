def validate_email(email):
    """
    Corrected simple email validator.
    Rules:
    - Must have exactly one '@'
    - Local and domain parts must not be empty
    - Domain (after @) must contain a '.'
    - No spaces
    """
    email = email.strip()

    if not email:
        print("❌ Invalid: Email is empty.")
        return False

    if ' ' in email:
        print("❌ Invalid: Email cannot contain spaces.")
        return False

    if email.count('@') != 1:
        print("❌ Invalid: Email must contain exactly one '@'.")
        return False

    at_index = email.find('@')
    local = email[:at_index]
    domain = email[at_index + 1:]

    if len(local) == 0:
        print("❌ Invalid: No characters before '@'.")
        return False

    if len(domain) == 0:
        print("❌ Invalid: No characters after '@'.")
        return False

    if '.' not in domain:
        print("❌ Invalid: Domain part must contain a '.' (e.g., gmail.com).")
        return False

    if domain.startswith('.') or domain.endswith('.'):
        print("❌ Invalid: Domain cannot start or end with a '.'.")
        return False

    # All checks passed
    print("✅ Valid email address!")
    return True


# ----------------------------
# Main Program
# ----------------------------
def main():
    print("📧 Corrected Email Validator")
    print("Enter an email to check. Type 'quit' to exit.\n")

    while True:
        user_input = input("Enter email: ").strip()

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break

        validate_email(user_input)
        print()  # For readability


if __name__ == "__main__":
    main()