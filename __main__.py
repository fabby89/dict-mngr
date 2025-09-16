#Receives a key word and a defnition from console separated by comma. 
from dictionary_class import Dictionary




if __name__ == "__main__":
    my_dict = Dictionary()
    my_dict.new_entry("chnt", "el esposo")
    my_dict.new_entry("fabby", "la esposa")
    input_look = input("Type a word to look up its definition: ")
    keyword = input_look.strip()
    print(my_dict.look_up(keyword))

