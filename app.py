from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['GET'])
def chatbot():
    try:
        # Extract the user's message from the request
        user_prompt = request.args.get('prompt')
        user_type = request.args.get('user_type')

        # Check if user_prompt is provided
        if not user_prompt:
            raise ValueError("Missing 'prompt' parameter in the request.")

        # Process the user's message (you can implement your chatbot logic here)
        content = chatgpt_query(user_prompt, 240)

        # Return the chatbot's response
        return jsonify({'response': content})

    except ValueError as ve:
        # Handle missing or invalid parameters
        return jsonify({'error': str(ve)}), 400

    except Exception as e:
        # Handle other unexpected errors
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
