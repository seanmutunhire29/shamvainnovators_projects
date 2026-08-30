from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# Data storage (resets when you restart the script)
forum_posts = [
    {"id": 1, "issue": "Balancing a high-stress job with family.", "advice": ["Set a strict no-phone rule for an hour when you reach home."]},
    {"id": 2, "issue": "Feeling lonely in a new city.", "advice": ["Join a sports league."]}
]

# Simple HTML Page Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Men's Forum</title>
</head>
<body>
    <h1>Men's Anonymous Forum for sharing problems</h1>

    <!-- Form to Share a New Issue -->
    <h3>Share an Issue:</h3>
    <form action="/share" method="POST">
        <input type="text" name="issue" placeholder="What is on your mind?" required>
        <button type="submit">Post</button>
    </form>

    <hr>

    <!-- Display Forum Posts -->
    <h3>Current Posts:</h3>
    {% for post in posts %}
        <div style="border: 1px solid black; padding: 10px; margin-bottom: 10px;">
            <p><strong>Issue:</strong> {{ post.issue }}</p>

            <p><strong>Advice given:</strong></p>
            <ul>
                {% for reply in post.advice %}
                    <li>{{ reply }}</li>
                {% endfor %}
            </ul>

            <!-- Form to Reply to this Post -->
            <form action="/reply/{{ post.id }}" method="POST">
                <input type="text" name="advice" placeholder="Give advice..." required>
                <button type="submit">Reply</button>
            </form>
        </div>
    {% endfor %}
</body>
</html>
"""


@app.route('/')
def home():
    # Show the HTML template and pass the data to it
    return render_template_string(HTML_TEMPLATE, posts=forum_posts)


@app.route('/share', methods=['POST'])
def share_issue():
    # Get text from the input form
    issue_text = request.form.get('issue')

    # Calculate a unique ID and add the post to the list
    new_id = len(forum_posts) + 1
    forum_posts.append({"id": new_id, "issue": issue_text, "advice": []})

    # Send user back to the home page to see changes
    return redirect('/')


@app.route('/reply/<int:post_id>', methods=['POST'])
def give_advice(post_id):
    # Get text from the reply form
    advice_text = request.form.get('advice')

    # Find the matching post and add the reply
    for post in forum_posts:
        if post['id'] == post_id:
            post['advice'].append(advice_text)
            break

    # Send user back to the home page to see changes
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)