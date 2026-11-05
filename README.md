Discord Status Rotator — StatusFlow
   2 │
   3 │ StatusFlow is a Python-based Discord status rotation to
     │ ol with a simple, minimalist terminal dashboard.
   4 │
   5 │ It is designed to make status management easier through
     │  configurable text rotation and optional profile featur
     │ es.
   6 │
   7 │ ---
   8 │
   9 │ > Features
  10 │
  11 │ - Status Rotation — Automatically rotates through text
     │ statuses.
  12 │ - HypeSquad Rotation — Optional HypeSquad house rotatio
     │ n.
  13 │ - Bio Rotation — Optional About Me rotation.
  14 │ - Minimalist Dashboard — Clean terminal interface.
  15 │ - Live Progress Display — Displays rotation progress.
  16 │ - Configurable Settings — Manage features through "conf
     │ ig.json".
  17 │ - Termux Support — Can be run on Android using Termux.
  18 │
  19 │ ---
  20 │
  21 │ 📥 Installation
  22 │
  23 │ Termux (Android)
  24 │
  25 │ 1. Update packages
  26 │
  27 │ pkg update && pkg upgrade -y
  28 │
  29 │ 2. Install Python and Git
  30 │
  31 │ pkg install python git -y
  32 │
  33 │ 3. Clone the repository
  34 │
  35 │ git clone https://github.com/YOUR-USERNAME/StatusFlow.g
     │ it
  36 │
  37 │ 4. Enter the project directory
  38 │
  39 │ cd StatusFlow
  40 │
  41 │ 5. Install dependencies
  42 │
  43 │ pip install requests colorama
  44 │
  45 │ ---
  46 │
  47 │ >⚙️ Configuration
  48 │
  49 │ Before running StatusFlow, configure your project using
     │  "config.json".
  50 │
  51 │ Keep your private configuration file out of GitHub. Use
     │  "config.example.json" as a template for other users.
  52 │
  53 │ Add your desired status text to:
  54 │
  55 │ text.txt
  56 │
  57 │ If you use bio rotation, add your bio entries to:
  58 │
  59 │ aboutme.txt
  60 │
  61 │ ---
  62 │
  63 │ >🚀 Usage
  64 │
  65 │ Run the program with:
  66 │
  67 │ python main.py
  68 │
  69 │ To stop the program, press:
  70 │
  71 │ CTRL + C
  72 │
  73 │ ---
  74 │
  75 │
  76 │ >📁 Project Structure
  77 │
  78 │ StatusFlow/
  79 │ │
  80 │ ├── main.py
  81 │ ├── config.json
  82 │ ├── config.example.json
  83 │ ├── text.txt
  84 │ ├── aboutme.txt
  85 │ ├── README.md
  86 │ ├── LICENSE
  87 │ └── .gitignore
  88 │
  89 │ ---
  90 │
  91 │ >📦 Requirements
  92 │
  93 │ - Python 3
  94 │ - requests
  95 │ - colorama
  96 │ - Termux or another Python environment
  97 │
  98 │ ---
  99 │
 100 │ >⚠️ Disclaimer
 101 │
 102 │ - This project is provided for educational purposes.
 103 │ - Use it responsibly and at your own risk.
 104 │ - Automating a personal Discord account through unoffic
     │ ial endpoints may violate Discord's Terms of Service an
     │ d could result in account restrictions.
 105 │ ---
 106 │
 107 │ >📄 License
 108 │
 109 │ This project is licensed under the MIT License.
 110 │
 111 │ See the "LICENSE" (LICENSE) file for details.
 112 │
 113 │ ---
 114 │
 115 │ >⭐ Support
 116 │
 117 │ If you find StatusFlow useful, consider giving the repo
     │ sitory a ⭐ on GitHub.
 118 │
 119 │ Made with Python.
