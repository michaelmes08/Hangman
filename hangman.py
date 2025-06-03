#!/usr/bin/env python3

import random
import sys
import os

class HangmanGame:
    
    def __init__(self):
        self.word_list = [
            "python", "programming", "computer", "keyboard", "monitor", "software",
            "hardware", "internet", "website", "database", "algorithm", "function",
            "variable", "language", "developer", "engineer", "technology", "science",
            "mathematics", "physics", "chemistry", "biology", "history", "geography",
            "literature", "philosophy", "psychology", "education", "university",
            "student", "teacher", "library", "research", "knowledge", "wisdom",
            "creativity", "imagination", "innovation", "discovery", "adventure",
            "journey", "destination", "exploration", "mystery", "challenge",
            "solution", "problem", "question", "answer", "success", "achievement",
            "excellence", "quality", "performance", "efficiency", "productivity",
            "communication", "collaboration", "teamwork", "leadership", "management",
            "strategy", "planning", "organization", "structure", "system",
            "network", "connection", "relationship", "friendship", "family",
            "community", "society", "culture", "tradition", "celebration",
            "happiness", "joy", "laughter", "smile", "kindness", "compassion",
            "generosity", "gratitude", "appreciation", "respect", "honesty",
            "integrity", "courage", "determination", "persistence", "patience",
            "discipline", "focus", "concentration", "attention", "awareness",
            "mindfulness", "meditation", "relaxation", "balance", "harmony",
            "peace", "tranquility", "serenity", "calmness", "stability",
            "security", "safety", "protection", "defense", "strength",
            "power", "energy", "vitality", "health", "wellness", "fitness",
            "exercise", "nutrition", "medicine", "healing", "recovery",
            "growth", "development", "progress", "improvement", "evolution",
            "transformation", "change", "adaptation", "flexibility", "resilience"
        ]
        
        self.hangman_stages = [
            """
   +---+
   |   |
       |
       |
       |
       |
=========
            """,
            """
   +---+
   |   |
   O   |
       |
       |
       |
=========
            """,
            """
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
            """,
            """
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
            """,
            """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========
            """,
            """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========
            """,
            """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========
            """
        ]
        
        self.reset_game()
    
    def reset_game(self):
        self.word = random.choice(self.word_list).upper()
        self.guessed_letters = set()
        self.correct_letters = set()
        self.wrong_guesses = 0
        self.max_wrong_guesses = 6
        self.game_over = False
        self.won = False
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        print("=" * 50)
        print("🎮 HANGMAN GAME 🎮".center(50))
        print("=" * 50)
        print()
    
    def display_hangman(self):
        print(self.hangman_stages[self.wrong_guesses])
    
    def display_word_progress(self):
        display_word = ""
        for letter in self.word:
            if letter in self.correct_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"Word: {display_word.strip()}")
        print(f"Word length: {len(self.word)} letters")
        print()
    
    def display_game_stats(self):
        remaining_guesses = self.max_wrong_guesses - self.wrong_guesses
        
        print(f"Wrong guesses: {self.wrong_guesses}/{self.max_wrong_guesses}")
        print(f"Remaining guesses: {remaining_guesses}")
        
        if self.guessed_letters:
            sorted_guesses = sorted(list(self.guessed_letters))
            print(f"Letters guessed: {', '.join(sorted_guesses)}")
        else:
            print("Letters guessed: None")
        
        print()
    
    def get_user_guess(self):
        while True:
            try:
                guess = input("Enter a letter (or 'quit' to exit): ").strip().upper()
                
                if guess.lower() == 'quit':
                    return None
                
                if len(guess) != 1:
                    print("❌ Please enter exactly one letter!")
                    continue
                
                if not guess.isalpha():
                    print("❌ Please enter a valid letter (A-Z)!")
                    continue
                
                if guess in self.guessed_letters:
                    print(f"❌ You already guessed '{guess}'. Try a different letter!")
                    continue
                
                return guess
            
            except KeyboardInterrupt:
                print("\n\nGame interrupted by user. Goodbye!")
                return None
            except EOFError:
                print("\n\nGame ended. Goodbye!")
                return None
    
    def process_guess(self, guess):
        self.guessed_letters.add(guess)
        
        if guess in self.word:
            self.correct_letters.add(guess)
            print(f"✅ Great! '{guess}' is in the word!")
            
            if all(letter in self.correct_letters for letter in self.word):
                self.won = True
                self.game_over = True
        else:
            self.wrong_guesses += 1
            print(f"❌ Sorry! '{guess}' is not in the word.")
            
            if self.wrong_guesses >= self.max_wrong_guesses:
                self.game_over = True
        
        print()
    
    def display_game_result(self):
        print("=" * 50)
        if self.won:
            print("🎉 CONGRATULATIONS! YOU WON! 🎉".center(50))
            print(f"You correctly guessed: {self.word}")
            print(f"Total guesses: {len(self.guessed_letters)}")
            print(f"Wrong guesses: {self.wrong_guesses}")
        else:
            print("💀 GAME OVER! YOU LOST! 💀".center(50))
            print(f"The word was: {self.word}")
            print("Better luck next time!")
        print("=" * 50)
        print()
    
    def play_round(self):
        while not self.game_over:
            self.clear_screen()
            self.display_header()
            self.display_hangman()
            self.display_word_progress()
            self.display_game_stats()
            
            guess = self.get_user_guess()
            if guess is None:
                return False
            
            self.process_guess(guess)
            
            if not self.game_over:
                input("Press Enter to continue...")
        
        self.clear_screen()
        self.display_header()
        self.display_hangman()
        print(f"Final word: {self.word}")
        print()
        self.display_game_result()
        
        return True
    
    def play(self):
        print("Welcome to Hangman!")
        print("Guess the hidden word one letter at a time.")
        print("You have 6 wrong guesses before the game ends.")
        print("\nPress Enter to start...")
        input()
        
        while True:
            completed = self.play_round()
            if not completed:
                break
            
            while True:
                try:
                    play_again = input("Do you want to play again? (y/n): ").strip().lower()
                    if play_again in ['y', 'yes']:
                        self.reset_game()
                        break
                    elif play_again in ['n', 'no']:
                        print("\nThanks for playing Hangman! Goodbye!")
                        return
                    else:
                        print("Please enter 'y' for yes or 'n' for no.")
                except (KeyboardInterrupt, EOFError):
                    print("\n\nThanks for playing Hangman! Goodbye!")
                    return


def main():
    try:
        game = HangmanGame()
        game.play()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please try running the game again.")
    finally:
        sys.exit(0)


if __name__ == "__main__":
    main()
