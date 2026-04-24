# Vote-Poll-Project

# Blockchain Voting System

A desktop-based voting application that leverages blockchain concepts to ensure transparency, integrity, and immutability of votes. The project includes a graphical user interface (GUI) built with Tkinter and visualizes election results using Matplotlib.

This project has been enhanced with additional features such as vote history tracking, search functionality, and blockchain export capabilities.

## Features

### Core Features

- Secure Voting : Voter IDs are hashed using SHA-256 for privacy.
- Blockchain Integrity : Each vote is stored in blocks linked via cryptographic hashes.
- Proof-of-Work Mining : Blocks are mined using a configurable difficulty level.
- Tamper Detection : Detects any inconsistencies in the blockchain.

### GUI Features

- Interactive Interface : Simple and user-friendly Tkinter-based GUI.
- Submit Votes : Add votes securely.
- Mine Votes : Convert pending votes into a blockchain block.

### Visualization & Data

- Results Pie Chart : Visual representation of voting results.
- Results Table View : Tabular display of vote counts per candidate.

### New & Advanced Features (Updated Version)

- Vote History Viewer : View all votes stored across blockchain blocks.
- Pending Votes Viewer : See votes that are yet to be mined.
- Candidate Search : Search total votes received by a specific candidate.
- Export Blockchain : Export the entire blockchain data into a JSON file.
- Results Table : Clean tabular format for results alongside chart visualization.


## Tech Stack

- Python
- Tkinter (GUI Development)
- Matplotlib (Data Visualization)
- Hashlib (Cryptographic Hashing)
- JSON (Data Storage & Export)

## How It Works

1. Users input a Voter ID and Candidate Name.
2. The system hashes the voter ID for anonymity.
3. Votes are stored as pending transactions.
4. When mining is triggered:
    - A new block is created.
    - A proof-of-work algorithm generates a valid hash.
    - The block is added to the blockchain.
5. The blockchain ensures immutability via hash linking.
6. Results are calculated from all mined blocks.
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

For updated version (recommended):

```
python Updated.py
```

## Usage
- Submit Vote : Enter voter ID and candidate name.
- Mine Pending Votes : Add votes to the blockchain.
- Show Results (Chart): View results as a pie chart.
- Show Results (Table) : View results in table format.
- View Vote History : Browse all votes block-by-block.
- View Pending Votes : See unmined votes.
- Search Candidate Votes : Find total votes for a candidate.
- Export Blockchain : Save blockchain data to a JSON file.
- Check Blockchain Validity : Ensure data integrity.

## Screenshots

Project Ouptut :-

<img width="985" height="523" alt="Image" src="https://github.com/user-attachments/assets/041e7bcc-897e-4382-8715-f3044776401b" />

Updated Output :-

<img width="857" height="642" alt="Output" src="https://github.com/user-attachments/assets/19f1d009-09bd-4ce6-abf2-3d78b175f738" />

## Output Example

- Exported file : blockchain_export.json
- Contains:
      - Block index
      - Votes
      - Timestamp
      - Previous hash
      - Current hash
      - Nonce

## Future Improvements

- User authentication system
- Real-time distributed blockchain (networked nodes)
- Database integration (SQLite / MongoDB)
- Web-based interface (Flask / React)
- Digital signature-based voting

## License

This project is open-source and available under the MIT License.

## Author

Abhinav Dixit

Python Developer | Data & ML Enthusiast

- Feel free to fork, star, or contribute to this project!

