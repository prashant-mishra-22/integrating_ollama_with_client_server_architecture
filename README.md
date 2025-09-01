# 🤖 Integrating Ollama with Client-Server Architecture  

This project demonstrates how to **integrate [Ollama](https://ollama.ai/)** (Large Language Model runtime) with a **custom TCP client-server architecture** in Python.  
It supports **user authentication, input filtering (emails/phone numbers/cuss words)**, and **streaming AI-generated responses** in real time.  

---

## ✨ Features
- 🔑 **User Authentication** (username & password check before connection)
- 🧹 **Message Filtering**
  - Client blocks **emails** and **phone numbers**
  - Server blocks **cuss words** (from `cuss_words.txt`)
- 🤝 **Custom Protocol**
  - Fixed **64-byte headers** for message size
  - Chunked streaming of AI responses
- 🧵 **Multi-client support** via threading
- 🧠 **Ollama-powered AI responses**
  - Uses `llama3.2` model by default

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **Socket Programming**
- **Threading**
- **Ollama Python Client**

---

## 🚀 Getting Started

### 1️⃣ Install Requirements
Make sure you have [Ollama](https://ollama.ai/download) installed and running locally.  
Then install Python dependencies:

```bash
pip install ollama
````

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/prashant-mishra-22/integrating_ollama_with_client_server_architecture.git
cd integrating_ollama_with_client_server_architecture
```

### 3️⃣ Start the Server

```bash
python s.py
```

Expected output:

```
[STARTING] server is starting ...
[LISTENING] server is listening on (your-ip, 5050)
```

### 4️⃣ Start the Client

Open another terminal:

```bash
python c.py
```

Enter:

* Username: `****`
* Password: `****`

Then start chatting with the AI 🤖.
Type `<GoodBye>` to disconnect.

---

## 📂 Project Structure

```
📦 integrating_ollama_with_client_server_architecture
 ┣ 📜 c.py              # Client code
 ┣ 📜 s.py              # Server code
 ┣ 📜 cuss_words.txt    # List of blocked words
 ┗ 📜 README.md         # Documentation
```

---

## ⚡ Example Interaction

**Client Input:**

```
enter your message: Hello AI, how are you?
```

**Server (via Ollama Response):**

```
I'm doing great! How can I help you today?
```

---

## 🔮 Future Development

* 🔐 **Secure Authentication**

  * Replace hardcoded username/password with database or JWT tokens.
* 🌍 **Unicode & Multilingual Support**

  * Switch from `ascii` → `utf-8` to allow emojis and non-English text.
* 📡 **WebSocket Integration**

  * Replace raw sockets with WebSockets for modern web compatibility.
* ☁️ **Deployment**

  * Containerize with Docker, deploy on cloud (AWS/GCP/Azure).
* 🎛️ **Admin Dashboard**

  * Track active users, blocked messages, and chat logs.
* ⚙️ **Better Moderation**

  * Integrate AI-powered toxicity detection instead of static `cuss_words.txt`.

---

## 🙌 Contribution

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Commit your changes
4. Submit a PR 🚀

---

## 📜 License

This project is licensed under the MIT License – feel free to use and modify.

---

### 🌟 If you found this useful, don’t forget to **star ⭐ the repo**!

```

Do you want me to also **add code snippets (from `c.py` and `s.py`) inside the README** for quick reference, or keep it clean and minimal?
```
