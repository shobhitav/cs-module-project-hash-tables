def word_count(s):
    count={}
    lower_cased=s.lower()
    # ignore these list of characters in the given string
    ignore_chars= ' " : ; , . - + = / \ | [ ] { } ( ) * ^ & " ' . split()

    for chars in ignore_chars:
        # replace all non words with space
        lower_cased = lower_cased.replace(chars, "")
    
    for words in lower_cased.split():
        print(words)
        # continue if iterating through space
        if words == "":
            continue

        if words not in count:
            count[words] = 1
        else:
            count[words] += 1
    return count
    
                

    
if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))