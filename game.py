import random
import time
import os

class RockPaperScissors:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        self.rounds_played = 0
        
        # Game statistics
        self.user_choices = {"rock": 0, "paper": 0, "scissors": 0}
        self.computer_choices = {"rock": 0, "paper": 0, "scissors": 0}
        
        # ASCII art for each choice
        self.art = {
            "rock": """
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """,
            "paper": """
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """,
            "scissors": """
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """
        }
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_welcome(self):
        """Display welcome message"""
        print("🎮" * 20)
        print("       ROCK PAPER SCISSORS GAME")
        print("🎮" * 20)
        print("\nRules:")
        print("- Rock beats Scissors")
        print("- Scissors beats Paper")
        print("- Paper beats Rock")
        print("\nYou can type:")
        print("- 'rock' or 'r'")
        print("- 'paper' or 'p'")
        print("- 'scissors' or 's'")
        print("- 'quit' or 'q' to exit")
        print("- 'stats' to see statistics")
        print("-" * 40)
    
    def get_user_choice(self):
        """Get and validate user choice"""
        while True:
            choice = input("\nYour choice: ").lower().strip()
            
            if choice in ["quit", "q", "exit"]:
                return "quit"
            elif choice in ["stats", "statistics"]:
                return "stats"
            elif choice in ["rock", "r"]:
                return "rock"
            elif choice in ["paper", "p"]:
                return "paper"
            elif choice in ["scissors", "s"]:
                return "scissors"
            else:
                print("❌ Invalid input! Please enter rock/paper/scissors (or r/p/s)")
    
    def get_computer_choice(self):
        """Get random computer choice"""
        return random.choice(["rock", "paper", "scissors"])
    
    def display_choices(self, user_choice, computer_choice):
        """Display both choices with ASCII art"""
        print("\n" + "="*50)
        print("YOUR CHOICE:".center(25) + "COMPUTER CHOICE:".center(25))
        print("="*50)
        
        # Display user choice
        user_lines = self.art[user_choice].split('\n')
        computer_lines = self.art[computer_choice].split('\n')
        
        # Print side by side
        for i in range(max(len(user_lines), len(computer_lines))):
            user_line = user_lines[i] if i < len(user_lines) else ""
            computer_line = computer_lines[i] if i < len(computer_lines) else ""
            print(f"{user_line:25}{computer_line:25}")
        
        print(f"{user_choice.upper():^25}{computer_choice.upper():^25}")
        print("="*50)
    
    def determine_winner(self, user_choice, computer_choice):
        """CORRECTED: Determine round winner with proper logic"""
        # Check for tie first
        if user_choice == computer_choice:
            return "tie"
        
        # User win conditions
        user_wins = (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        )
        
        return "user" if user_wins else "computer"
    
    def display_round_result(self, winner):
        """Display round result with animation"""
        print("\n" + "•"*50)
        if winner == "tie":
            print("🤝 IT'S A TIE!".center(50))
        elif winner == "user":
            print("🎉 YOU WIN THIS ROUND!".center(50))
        else:
            print("🤖 COMPUTER WINS THIS ROUND!".center(50))
        print("•"*50)
    
    def update_statistics(self, user_choice, computer_choice, winner):
        """Update game statistics"""
        self.rounds_played += 1
        self.user_choices[user_choice] += 1
        self.computer_choices[computer_choice] += 1
        
        if winner == "user":
            self.user_score += 1
        elif winner == "computer":
            self.computer_score += 1
        else:
            self.ties += 1
    
    def display_stats(self):
        """Display game statistics"""
        print("\n" + "📊 GAME STATISTICS ".center(50, "="))
        print(f"\nRounds Played: {self.rounds_played}")
        print(f"Score: You {self.user_score} - {self.computer_score} Computer")
        print(f"Ties: {self.ties}")
        
        if self.rounds_played > 0:
            win_rate = (self.user_score / self.rounds_played) * 100
            print(f"Your Win Rate: {win_rate:.1f}%")
        
        print("\nYour Choices Distribution:")
        for choice, count in self.user_choices.items():
            percentage = (count / self.rounds_played * 100) if self.rounds_played > 0 else 0
            print(f"  {choice.capitalize()}: {count} ({percentage:.1f}%)")
        
        print("\nComputer Choices Distribution:")
        for choice, count in self.computer_choices.items():
            percentage = (count / self.rounds_played * 100) if self.rounds_played > 0 else 0
            print(f"  {choice.capitalize()}: {count} ({percentage:.1f}%)")
        
        input("\nPress Enter to continue...")
    
    def display_scoreboard(self):
        """Display current scoreboard"""
        print("\n" + "-"*40)
        print(f"SCORE: YOU {self.user_score} | COMPUTER {self.computer_score} | TIES {self.ties}")
        print(f"ROUND: {self.rounds_played}")
        print("-"*40)
    
    def play_round(self):
        """Play a single round"""
        user_choice = self.get_user_choice()
        
        if user_choice == "quit":
            return False
        elif user_choice == "stats":
            self.display_stats()
            return True
        
        computer_choice = self.get_computer_choice()
        
        # Clear screen and display choices
        self.clear_screen()
        self.display_choices(user_choice, computer_choice)
        
        # Determine winner
        winner = self.determine_winner(user_choice, computer_choice)
        
        # Small delay for suspense
        time.sleep(0.5)
        self.display_round_result(winner)
        
        # Update statistics
        self.update_statistics(user_choice, computer_choice, winner)
        
        # Display scoreboard
        self.display_scoreboard()
        
        return True
    
    def run(self):
        """Main game loop"""
        self.clear_screen()
        self.display_welcome()
        
        while True:
            if not self.play_round():
                break
        
        # Game over screen
        self.clear_screen()
        print("\n" + "🎮 FINAL RESULTS ".center(50, "="))
        print(f"\nTotal Rounds: {self.rounds_played}")
        print(f"Final Score: You {self.user_score} - {self.computer_score} Computer")
        
        if self.user_score > self.computer_score:
            print("\n🏆 YOU ARE THE CHAMPION! 🏆")
        elif self.computer_score > self.user_score:
            print("\n🤖 COMPUTER WINS THE GAME!")
        else:
            print("\n🤝 IT'S A DRAW!")
        
        print("\nThanks for playing! 👋")
        
        # Show detailed statistics
        if self.rounds_played > 0:
            self.display_stats()

def main():
    """Main function to start the game"""
    game = RockPaperScissors()
    game.run()

if __name__ == "__main__":
    main()