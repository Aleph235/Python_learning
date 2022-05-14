def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages,sent_messages):
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)

messages = ['hello', 'hi', 'hola', 'ciao']
sent_messages = []

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)

show_messages(messages)
show_messages(sent_messages)
