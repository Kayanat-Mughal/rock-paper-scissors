import tkinter as tk
from tkinter import ttk, messagebox, font
import random
import os

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Rock Paper Scissors")
        self.root.geometry("800x700")
        self.root.configure(bg='#2c3e50')
        
        # Initialize scores
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        self.rounds_played = 0
        
        # User choices tracking
        self.user_choices = {"rock": 0, "paper": 0, "scissors": 0}
        
        # Emoji and color mapping
        self.choices = {
            "rock": {"emoji": "🪨", "color": "#e74c3c", "beats": "scissors"},
            "paper": {"emoji": "📄", "color": "#3498db", "beats": "rock"},
            "scissors": {"emoji": "✂️", "color": "#2ecc71", "beats": "paper"}
        }
        
        # Setup fonts
        self.title_font = font.Font(family="Arial", size=24, weight="bold")
        self.button_font = font.Font(family="Arial", size=16)
        self.score_font = font.Font(family="Arial", size=18, weight="bold")
        
        self.setup_ui()
        self.reset_game()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Main container
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="🎮 ROCK PAPER SCISSORS 🎮", 
            font=self.title_font,
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        title_label.pack(pady=(0, 20))
        
        # Score Frame
        score_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RAISED, bd=2)
        score_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Score Labels
        self.user_score_label = tk.Label(
            score_frame,
            text="You: 0",
            font=self.score_font,
            bg='#34495e',
            fg='#2ecc71'
        )
        self.user_score_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.tie_score_label = tk.Label(
            score_frame,
            text="Ties: 0",
            font=self.score_font,
            bg='#34495e',
            fg='#f39c12'
        )
        self.tie_score_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.computer_score_label = tk.Label(
            score_frame,
            text="Computer: 0",
            font=self.score_font,
            bg='#34495e',
            fg='#e74c3c'
        )
        self.computer_score_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Choice Display Frame
        display_frame = tk.Frame(main_frame, bg='#2c3e50')
        display_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # User Choice Display
        user_frame = tk.Frame(display_frame, bg='#34495e', relief=tk.SUNKEN, bd=3)
        user_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        tk.Label(
            user_frame,
            text="YOUR CHOICE",
            font=("Arial", 14, "bold"),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(pady=10)
        
        self.user_display = tk.Label(
            user_frame,
            text="❓",
            font=("Arial", 80),
            bg='#34495e',
            fg='#bdc3c7'
        )
        self.user_display.pack(expand=True)
        
        self.user_choice_label = tk.Label(
            user_frame,
            text="Waiting...",
            font=("Arial", 16),
            bg='#34495e',
            fg='#ecf0f1'
        )
        self.user_choice_label.pack(pady=10)
        
        # VS Label
        vs_label = tk.Label(
            display_frame,
            text="VS",
            font=("Arial", 24, "bold"),
            bg='#2c3e50',
            fg='#f1c40f'
        )
        vs_label.pack(side=tk.LEFT, padx=20)
        
        # Computer Choice Display
        computer_frame = tk.Frame(display_frame, bg='#34495e', relief=tk.SUNKEN, bd=3)
        computer_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        tk.Label(
            computer_frame,
            text="COMPUTER",
            font=("Arial", 14, "bold"),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(pady=10)
        
        self.computer_display = tk.Label(
            computer_frame,
            text="🤖",
            font=("Arial", 80),
            bg='#34495e',
            fg='#bdc3c7'
        )
        self.computer_display.pack(expand=True)
        
        self.computer_choice_label = tk.Label(
            computer_frame,
            text="Thinking...",
            font=("Arial", 16),
            bg='#34495e',
            fg='#ecf0f1'
        )
        self.computer_choice_label.pack(pady=10)
        
        # Result Display
        self.result_label = tk.Label(
            main_frame,
            text="Make your move!",
            font=("Arial", 20, "bold"),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        self.result_label.pack(pady=20)
        
        # Buttons Frame
        buttons_frame = tk.Frame(main_frame, bg='#2c3e50')
        buttons_frame.pack(pady=20)
        
        # Create choice buttons
        button_configs = [
            ("ROCK 🪨", "rock", "#e74c3c"),
            ("PAPER 📄", "paper", "#3498db"),
            ("SCISSORS ✂️", "scissors", "#2ecc71")
        ]
        
        for text, choice, color in button_configs:
            btn = tk.Button(
                buttons_frame,
                text=text,
                command=lambda c=choice: self.make_choice(c),
                font=self.button_font,
                bg=color,
                fg='white',
                activebackground=color,
                activeforeground='white',
                relief=tk.RAISED,
                bd=3,
                padx=30,
                pady=15,
                cursor='hand2'
            )
            btn.pack(side=tk.LEFT, padx=10)
        
        # Control Buttons Frame
        control_frame = tk.Frame(main_frame, bg='#2c3e50')
        control_frame.pack(pady=20)
        
        # Reset Button
        reset_btn = tk.Button(
            control_frame,
            text="🔄 Reset Game",
            command=self.reset_game,
            font=("Arial", 12),
            bg='#f39c12',
            fg='white',
            padx=20,
            pady=10
        )
        reset_btn.pack(side=tk.LEFT, padx=10)
        
        # Stats Button
        stats_btn = tk.Button(
            control_frame,
            text="📊 Show Stats",
            command=self.show_stats,
            font=("Arial", 12),
            bg='#9b59b6',
            fg='white',
            padx=20,
            pady=10
        )
        stats_btn.pack(side=tk.LEFT, padx=10)
        
        # Rules Button
        rules_btn = tk.Button(
            control_frame,
            text="📖 Rules",
            command=self.show_rules,
            font=("Arial", 12),
            bg='#1abc9c',
            fg='white',
            padx=20,
            pady=10
        )
        rules_btn.pack(side=tk.LEFT, padx=10)
        
        # Quit Button
        quit_btn = tk.Button(
            control_frame,
            text="🚪 Quit",
            command=self.quit_game,
            font=("Arial", 12),
            bg='#e74c3c',
            fg='white',
            padx=20,
            pady=10
        )
        quit_btn.pack(side=tk.LEFT, padx=10)
        
        # Status Bar
        self.status_label = tk.Label(
            main_frame,
            text="Game Started! Choose Rock, Paper, or Scissors.",
            font=("Arial", 10),
            bg='#34495e',
            fg='#bdc3c7',
            relief=tk.SUNKEN,
            bd=1,
            padx=10,
            pady=5
        )
        self.status_label.pack(fill=tk.X, pady=(20, 0))
    
    def make_choice(self, user_choice):
        """Handle user's choice"""
        # Update user display
        self.user_choice_label.config(text=user_choice.upper())
        self.user_display.config(
            text=self.choices[user_choice]["emoji"],
            fg=self.choices[user_choice]["color"]
        )
        
        # Update user choices tracking
        self.user_choices[user_choice] += 1
        self.rounds_played += 1
        
        # Get computer choice
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        # Update computer display
        self.computer_choice_label.config(text=computer_choice.upper())
        self.computer_display.config(
            text=self.choices[computer_choice]["emoji"],
            fg=self.choices[computer_choice]["color"]
        )
        
        # Determine winner
        result = self.determine_winner(user_choice, computer_choice)
        
        # Update result display
        self.display_result(result, user_choice, computer_choice)
        
        # Update scores
        self.update_scores(result)
        
        # Update status
        self.status_label.config(
            text=f"Round {self.rounds_played}: You chose {user_choice}, Computer chose {computer_choice}"
        )
    
    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner"""
        if user_choice == computer_choice:
            return "tie"
        
        if self.choices[user_choice]["beats"] == computer_choice:
            return "user"
        else:
            return "computer"
    
    def display_result(self, result, user_choice, computer_choice):
        """Display the result with animations"""
        result_texts = {
            "user": f"🎉 YOU WIN!\n{user_choice.upper()} beats {computer_choice.upper()}",
            "computer": f"🤖 COMPUTER WINS!\n{computer_choice.upper()} beats {user_choice.upper()}",
            "tie": f"🤝 IT'S A TIE!\nBoth chose {user_choice.upper()}"
        }
        
        result_colors = {
            "user": "#2ecc71",  # Green
            "computer": "#e74c3c",  # Red
            "tie": "#f39c12"  # Orange
        }
        
        self.result_label.config(
            text=result_texts[result],
            fg=result_colors[result]
        )
        
        # Flash animation for the winner
        if result == "user":
            self.flash_color(self.user_display, "#ffffff", self.choices[user_choice]["color"])
        elif result == "computer":
            self.flash_color(self.computer_display, "#ffffff", self.choices[computer_choice]["color"])
        else:
            self.flash_color(self.user_display, "#ffffff", self.choices[user_choice]["color"])
            self.flash_color(self.computer_display, "#ffffff", self.choices[computer_choice]["color"])
    
    def flash_color(self, widget, color1, color2):
        """Create a flash animation"""
        def change_color(color, count=0):
            if count < 3:  # Flash 3 times
                widget.config(fg=color1 if widget.cget("fg") == color2 else color2)
                self.root.after(200, lambda: change_color(color, count + 1))
            else:
                widget.config(fg=color2)
        
        change_color(color1)
    
    def update_scores(self, result):
        """Update and display scores"""
        if result == "user":
            self.user_score += 1
        elif result == "computer":
            self.computer_score += 1
        else:
            self.ties += 1
        
        self.user_score_label.config(text=f"You: {self.user_score}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")
        self.tie_score_label.config(text=f"Ties: {self.ties}")
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        self.rounds_played = 0
        self.user_choices = {"rock": 0, "paper": 0, "scissors": 0}
        
        # Reset displays
        self.user_display.config(text="❓", fg="#bdc3c7")
        self.computer_display.config(text="🤖", fg="#bdc3c7")
        self.user_choice_label.config(text="Waiting...")
        self.computer_choice_label.config(text="Thinking...")
        self.result_label.config(text="Make your move!", fg="#ecf0f1")
        
        # Reset scores
        self.user_score_label.config(text="You: 0")
        self.computer_score_label.config(text="Computer: 0")
        self.tie_score_label.config(text="Ties: 0")
        self.status_label.config(text="Game reset! Choose Rock, Paper, or Scissors.")
        
        messagebox.showinfo("Game Reset", "Game has been reset to initial state!")
    
    def show_stats(self):
        """Show game statistics"""
        stats_text = f"""
📊 GAME STATISTICS
══════════════════════════

Rounds Played: {self.rounds_played}
Score: You {self.user_score} - {self.computer_score} Computer
Ties: {self.ties}

Your Choices Distribution:
"""
        
        for choice, count in self.user_choices.items():
            percentage = (count / self.rounds_played * 100) if self.rounds_played > 0 else 0
            stats_text += f"  {choice.upper()}: {count} ({percentage:.1f}%)\n"
        
        if self.rounds_played > 0:
            win_rate = (self.user_score / self.rounds_played) * 100
            stats_text += f"\nWin Rate: {win_rate:.1f}%"
        
        messagebox.showinfo("Game Statistics", stats_text)
    
    def show_rules(self):
        """Show game rules"""
        rules = """
🎮 ROCK PAPER SCISSORS RULES

HOW TO PLAY:
1. Choose Rock, Paper, or Scissors
2. Computer makes a random choice
3. Winner is determined by:

ROCK 🪨 beats SCISSORS ✂️
SCISSORS ✂️ beats PAPER 📄
PAPER 📄 beats ROCK 🪨

Same choices result in a TIE!

SCORING:
• Win: +1 point
• Tie: +0 points
• Loss: +0 points

TIPS:
• Try to predict computer patterns
• Don't be too predictable yourself
• Have fun! 🎉
"""
        messagebox.showinfo("Game Rules", rules)
    
    def quit_game(self):
        """Quit the game with confirmation"""
        if messagebox.askyesno("Quit Game", "Are you sure you want to quit?"):
            final_stats = f"""
FINAL STATISTICS:
Rounds: {self.rounds_played}
Score: You {self.user_score} - {self.computer_score} Computer
"""
            if self.user_score > self.computer_score:
                final_stats += "\n🏆 YOU ARE THE CHAMPION! 🏆"
            elif self.computer_score > self.user_score:
                final_stats += "\n🤖 COMPUTER WINS THE GAME!"
            else:
                final_stats += "\n🤝 IT'S A DRAW!"
            
            messagebox.showinfo("Game Over", final_stats)
            self.root.quit()

def main():
    """Main function to start the GUI game"""
    root = tk.Tk()
    
    # Set window icon (optional)
    try:
        root.iconbitmap(default='icon.ico')  # If you have an icon file
    except:
        pass
    
    app = RockPaperScissorsGUI(root)
    
    # Center the window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    # Prevent window resizing
    root.resizable(False, False)
    
    root.mainloop()

if __name__ == "__main__":
    main()