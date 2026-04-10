import hashlib
import time
import json
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# ------------------ Blockchain Logic ------------------ #

class Block:
    def __init__(self, index, votes, timestamp, previous_hash):
        self.index = index
        self.votes = votes
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "votes": self.votes,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_votes = []

    def create_genesis_block(self):
        return Block(0, [], time.time(), "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_vote(self, voter_id, candidate):
        vote = {
            "voter_id": hashlib.sha256(voter_id.encode()).hexdigest(),
            "candidate": candidate
        }
        self.pending_votes.append(vote)

    def mine_block(self):
        if not self.pending_votes:
            return False
        new_block = Block(len(self.chain), self.pending_votes, time.time(), self.get_latest_block().hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_votes = []
        return True

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

    def get_results(self):
        results = {}
        for block in self.chain:
            for vote in block.votes:
                candidate = vote["candidate"]
                results[candidate] = results.get(candidate, 0) + 1
        return results

# ------------------ GUI Interface ------------------ #

blockchain = Blockchain()

def submit_vote():
    voter_id = entry_voter_id.get()
    candidate = entry_candidate.get()
    if not voter_id or not candidate:
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return
    blockchain.add_vote(voter_id, candidate)
    messagebox.showinfo("Vote Added", "Vote added successfully.")
    entry_voter_id.delete(0, tk.END)
    entry_candidate.delete(0, tk.END)

def mine_votes():
    if blockchain.mine_block():
        messagebox.showinfo("Block Mined", "Pending votes mined into a new block.")
    else:
        messagebox.showwarning("No Votes", "No votes to mine.")

def show_results():
    results = blockchain.get_results()
    if not results:
        messagebox.showinfo("No Results", "No votes yet.")
        return
    candidates = list(results.keys())
    votes = list(results.values())

    plt.figure(figsize=(6,6))
    plt.pie(votes, labels=candidates, autopct='%1.1f%%', startangle=140)
    plt.title("Election Results")
    plt.axis('equal')
    plt.show()

def check_chain():
    valid = blockchain.is_chain_valid()
    status = "valid" if valid else "invalid"
    messagebox.showinfo("Blockchain Status", f"The blockchain is {status}.")

# ------------------ TKINTER WINDOW ------------------ #

root = tk.Tk()
root.title("Blockchain Voting System")
root.geometry("400x400")

# Labels and Entries
tk.Label(root, text="Voter ID:").pack()
entry_voter_id = tk.Entry(root)
entry_voter_id.pack()

tk.Label(root, text="Candidate Name:").pack()
entry_candidate = tk.Entry(root)
entry_candidate.pack()

# Buttons
tk.Button(root, text="Submit Vote", command=submit_vote).pack(pady=5)
tk.Button(root, text="Mine Pending Votes", command=mine_votes).pack(pady=5)
tk.Button(root, text="Show Results (Chart)", command=show_results).pack(pady=5)
tk.Button(root, text="Check Blockchain Validity", command=check_chain).pack(pady=5)

tk.Label(root, text="").pack()  # Spacer

# Run GUI
root.mainloop()
