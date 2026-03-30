from gradio_client import Client

client = Client("aijadugar/ft_slm")

def get_response(user_input):
    result = client.predict(
        user_input=user_input,
        api_name="/generate_response",
    )
    return result

print(get_response("My laptop is overheating, what should I do?"))