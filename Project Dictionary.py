import json
from difflib import get_close_matches

# Load the JSON data
data = json.load(open("data.json"))

def translate(word):

    word = word.lower()
    # search exact word
    if word in data:
        return data[word]
    elif word.title() in data:  
        return data[word.title()]
    elif word.upper() in data:  
        return data[word.upper()]
    
    # Handle close matches
    close_matches = get_close_matches(word, data.keys())
    if close_matches:
        suggested_word = close_matches[0]
        user_input = input(f"Did you mean '{suggested_word}' instead? (y/n): ").strip().lower()
        
        if user_input == "y":
            return data[suggested_word]
        elif user_input == "n":
            return "The word does not exist in the dictionary. Please double-check your input."
        else:
            return "Invalid input. Please respond with 'y' or 'n'."
    
    # No matches found
    return "The word does not exist in the dictionary. Please double-check your input."

# Main user interaction loop
if __name__ == "__main__":
    word = input("Enter the word you want to search: ").strip()
    output = translate(word)
    
    # Handle list and string outputs
    if isinstance(output, list):
        print("\n".join(output))
    else:
        print(output)
