# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:11:34 2024

@author: User
"""
import random

class QuizGame:
    def __init__(self, questions, difficulty_levels):
        self.questions = questions
        self.difficulty_levels = difficulty_levels
        self.score = 0

    def start_game(self):
        print("Welcome to the Quiz Game!")
        self.select_difficulty()

    def select_difficulty(self):
        print("\nChoose a difficulty level:")
        for i, level in enumerate(self.difficulty_levels, start=1):
            print(f"{i}. {level}")

        difficulty_choice = input("Enter the number corresponding to your choice: ")
        difficulty_choice = int(difficulty_choice) - 1

        if 0 <= difficulty_choice < len(self.difficulty_levels):
            difficulty = self.difficulty_levels[difficulty_choice]
            self.play_round(difficulty)
        else:
            print("Invalid choice. Please try again.")
            self.select_difficulty()

    def play_round(self, difficulty):
        print(f"\nYou selected {difficulty} difficulty.")
        question = random.choice(self.questions[difficulty])
        print(f"\nQuestion: {question['question']}")
        self.display_options(question['options'])

        user_answer = input("Your answer: ").strip().lower()

        if user_answer == question['correct_answer'].lower():
            print("Correct! Well done.")
            self.score += 1
        else:
            print(f"Sorry, the correct answer was: {question['correct_answer']}.")

        print(f"Your current score: {self.score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again == 'yes':
            self.select_difficulty()
        else:
            print(f"Thanks for playing! Your final score is: {self.score}")

    def display_options(self, options):
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

if __name__ == "__main__":
    # Define questions for each difficulty level
    questions = {
        'easy': [
            {'question': 'What is the capital of France?', 'options': ['Paris', 'Berlin', 'Rome'], 'correct_answer': 'Paris'},
            {'question': 'Which planet is known as the Red Planet?', 'options': ['Earth', 'Mars', 'Venus'], 'correct_answer': 'Mars'},
        ],
        'medium': [
            {'question': 'Who wrote "Romeo and Juliet"?', 'options': ['William Shakespeare', 'Jane Austen', 'Charles Dickens'], 'correct_answer': 'William Shakespeare'},
            {'question': 'What is the largest ocean on Earth?', 'options': ['Atlantic Ocean', 'Indian Ocean', 'Pacific Ocean'], 'correct_answer': 'Pacific Ocean'},
        ],
        'hard': [
            {'question': 'In what year did World War II end?', 'options': ['1945', '1939', '1950'], 'correct_answer': '1945'},
            {'question': 'Who is the author of "The Catcher in the Rye"?', 'options': ['J.D. Salinger', 'F. Scott Fitzgerald', 'Ernest Hemingway'], 'correct_answer': 'J.D. Salinger'},
        ],
    }

    # Define difficulty levels
    difficulty_levels = ['easy', 'medium', 'hard']

    # Create a QuizGame instance
    quiz_game = QuizGame(questions, difficulty_levels)

    # Start the game
    quiz_game.start_game()

