def count_words(text):
    #Count the number of words in a given text.
    # Split the text into words based on whitespace and count them
    words = text.split()
    return len(words)

def main():
    #Main function to handle user input and display the word count.
    # Prompt the user for input
    user_input = input("Enter a sentence or paragraph: ")
    
    # Handle empty input
    if not user_input.strip():
        print("Error: Empty input is not allowed.")
        return
    
    # Count the words in the input
    word_count = count_words(user_input)
    
    # Display the word count
    print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()