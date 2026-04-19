# Vote-Poll-Project

# Blockchain Voting System

A simple desktop-based voting application that leverages blockchain concepts to ensure transparency, integrity, and immutability of votes. The project includes a graphical user interface (GUI) built with Tkinter and visualizes election results using Matplotlib.


## Features

- **Secure Voting**: Voter IDs are hashed using SHA-256 for privacy.
- **Blockchain Integrity**: Each vote is stored in blocks linked via cryptographic hashes.
- **Proof-of-Work Mining**: Blocks are mined with a configurable difficulty level.
- **Tamper Detection**: Built-in validation to detect any changes in the blockchain.
- **Interactive GUI**: User-friendly interface for submitting votes and managing the system.
- **Results Visualization**: Displays election results as a pie chart.

## Tech Stack

- Python
- Tkinter (GUI)
- Matplotlib (Data Visualization)
- Hashlib (Cryptography)
- JSON (Data Structuring)

## How It Works

1. Users enter a **Voter ID** and **Candidate Name**.
2. Votes are stored temporarily as pending transactions.
3. When mining is triggered:
   - A new block is created.
   - A proof-of-work algorithm generates a valid hash.
   - The block is added to the chain.
4. The blockchain maintains integrity via hash linking.
5. Results are aggregated from all blocks and displayed graphically.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/blockchain-voting-system.git
   cd blockchain-voting-system

2. Install dependencies:

```
pip install matplotlib
```

Run the application:

```
python Project.py
```

## Usage
- Submit Vote: Enter voter ID and candidate name, then click Submit Vote.
- Mine Votes: Click Mine Pending Votes to add votes to the blockchain.
- Show Results: View a pie chart of current voting results.
- Check Validity: Verify blockchain integrity.


## Screenshots

<img width="985" height="523" alt="Image" src="https://github.com/user-attachments/assets/041e7bcc-897e-4382-8715-f3044776401b" />



## License

This project is open-source and available under the MIT License.

## Author

Abhinav Dixit

Python Developer | Data & ML Enthusiast

- Feel free to fork, star, or contribute to this project!

