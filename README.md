Discord Status Rotator — StatusFlow

StatusFlow is a Python-based Discord status rotation tool with a simple, minimalist terminal dashboard.

It is designed to make status management easier through configurable text rotation and optional profile features.

---

> Features

- Status Rotation — Automatically rotates through text statuses.
- HypeSquad Rotation — Optional HypeSquad house rotation.
- Bio Rotation — Optional About Me rotation.
- Minimalist Dashboard — Clean terminal interface.
- Live Progress Display — Displays rotation progress.
- Configurable Settings — Manage features through "config.json".
- Termux Support — Can be run on Android using Termux.

---

📥 Installation

Termux (Android)

1. Update packages

pkg update && pkg upgrade -y

2. Install Python and Git

pkg install python git -y

3. Clone the repository

git clone https://github.com/YOUR-USERNAME/StatusFlow.git

4. Enter the project directory

cd StatusFlow

5. Install dependencies

pip install requests colorama

---

>⚙️ Configuration

Before running StatusFlow, configure your project using "config.json".

Keep your private configuration file out of GitHub. Use "config.example.json" as a template for other users.

Add your desired status text to:

text.txt

If you use bio rotation, add your bio entries to:

aboutme.txt

---

>🚀 Usage

Run the program with:

python main.py

To stop the program, press:

CTRL + C

---

 
>📁 Project Structure

StatusFlow/
│
├── main.py
├── config.json
├── config.example.json
├── text.txt
├── aboutme.txt
├── README.md
├── LICENSE
└── .gitignore

---

>📦 Requirements

- Python 3
- requests
- colorama
- Termux or another Python environment

---

>⚠️ Disclaimer

- This project is provided for educational purposes.
- Use it responsibly and at your own risk.
- Automating a personal Discord account through unofficial endpoints may violate Discord's Terms of Service and could result in account restrictions.
---

>📄 License

This project is licensed under the MIT License.

See the "LICENSE" (LICENSE) file for details.

---

>⭐ Support

If you find StatusFlow useful, consider giving the repository a ⭐ on GitHub.

Made with Python.
