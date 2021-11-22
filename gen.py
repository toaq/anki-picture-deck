import os

def make_entry_for_word(media, word):
    entry = word + "; "
    next_image_id = 1

    while True:
        next_image_name_template = word + str(next_image_id)
        next_image_name_candidates = []

        for image in media:
            if (next_image_name_template + ".") in image:
                next_image_name_candidates.append(image)

        if len(next_image_name_candidates) == 0:
            break

        if len(next_image_name_candidates) > 1:
            raise Exception("Error: more than one candidate image for " + next_image_name_template)

        next_image_name = next_image_name_candidates[0]
        
        media.remove(next_image_name)
        entry += "<img src=\"" + next_image_name + "\">"
        next_image_id += 1

    if next_image_id == 1: # No images found
        return media, None

    return media, entry


media = os.listdir("media/")

with open("freq.txt") as freq:
    with open("toaq_deck.txt", "w") as output:
        for line in freq:
            word = line.split(" ")[1]
            media, entry = make_entry_for_word(media, word)

            if entry != None:
                print(entry, file=output)

