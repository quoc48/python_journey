def show_messages(message_list):
    """Print out a list"""
    for message in message_list:
        print(message)


def send_message(messages_list):
    """Print out each item and then moving to other list"""
    while messages_list:
        message = messages_list.pop()
        print(f"Sending '{message}'")
        send_messages.append(message)
    print("\n--- All messages sent ---")
    show_messages(send_messages)  # Using first function.

# Define two list.
original_messages = [
    'Say hello!',
    'Please call the police!',
    'Just do it!'
]
send_messages = []

# Using defined functions
send_message(original_messages[:])  # Make a copy from original list.
print(f"\nOriginal message: {original_messages}")