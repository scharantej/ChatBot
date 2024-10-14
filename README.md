## Design for a Web UI to Chat with Gemini-1.5-Flash-002

### HTML Files

- **index.html**: Main landing page for the application, presenting a chat interface and input field for user messages.
- **chat.html**: Renders the chat history and displays incoming responses from Gemini-1.5-Flash-002.

### Routes

- **/:** Serves the **index.html** file, displaying the main chat interface.
- **chat**: Handles user input messages and sends them to the Gemini-1.5-Flash-002 server. It then processes the response and renders the **chat.html** file with the updated chat history.