import os

def make_entry_for_word(content, word):
    entry = word + "; "
    next_image_id = 1

    while True:
        next_image_name_template = word + str(next_image_id)
        next_image_name_candidates = []

        for image in content:
            if (next_image_name_template + ".") in image:
                next_image_name_candidates.append(image)

        if len(next_image_name_candidates) == 0:
            break

        if len(next_image_name_candidates) > 1:
            raise Exception("Error: more than one candidate image for " + next_image_name_template)

        next_image_name = next_image_name_candidates[0]
        
        content.remove(next_image_name)
        entry += "<img src=\"" + next_image_name + "\">"
        next_image_id += 1

    if next_image_id == 1: # No images found
        return content, None

    return content, entry


content = os.listdir("content/")

with open("freq.txt") as freq:
    with open("toaq_deck.txt", "w") as output:
        for line in freq:
            word = line.split(" ")[1]
            content, entry = make_entry_for_word(content, word)

            if entry != None:
                print(entry, file=output)

