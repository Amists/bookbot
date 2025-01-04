import collections


def main():
    with open("books/frankenstien.txt") as f:
        file_contents = f.read()
        
        print_report(character_count(file_contents))
        
def word_count(text: str):

   return len(text.split()) 

def character_count(text: str):
    lowered_string = text.lower()
    letters = {}
        
    for character in lowered_string:
        if (character not in letters):
            letters [character] = {"character": character , "count": 0 }
        letters [character]["count"] += 1
        
    return letters

def print_report(dict: dict):
    sorted_dict = list(dict.values())
    sorted_dict.sort(reverse=True, key=sort_on)
    print(sorted_dict)
    for i in sorted_dict:
        print (f"The character '{i["character"]}' was found {i["count"]} times")
    
    print("--- End Report ---")
    
def sort_on(dict):
    return dict["count"]
               
               
main()
