import os
import genanki

# Create the note for a single word.

def make_note_for_word(media_list, model, word):
    image_names = ""
    next_image_id = 1

    while True:
        next_image_name_template = word + str(next_image_id)
        next_image_name_candidates = []

        for image in media_list:
            if (next_image_name_template + ".") in image:
                next_image_name_candidates.append(image)

        if len(next_image_name_candidates) == 0:
            break

        if len(next_image_name_candidates) > 1:
            raise Exception("Error: more than one candidate image for " + next_image_name_template)

        next_image_name = next_image_name_candidates[0]
        
        media_list.remove(next_image_name)
        image_names += "<img src=\"" + next_image_name + "\">"
        next_image_id += 1

    if next_image_id == 1: # No images found
        return media_list, None

    return media_list, genanki.Note(model=model, fields=[word, image_names])


# Create the model of the deck.

model = genanki.Model(
        2083704285,     # Randomly-generated ID for this deck
        "Toaq cards model",
        fields = [
            {"name": "Predicate"},
            {"name": "Images"}
        ],
        templates = [
            {
                "name": "Card 1 (Images -> Predicate)",
                "qfmt": "{{Images}}",
                "afmt": "{{Predicate}}<hr>{{Images}}"
            }
        ])


# Create the deck.

deck = genanki.Deck(1510915964, "Toaq cards deck")


# Create the notes.

media = os.listdir("media/")

with open("freq.txt") as freq:
    for line in freq:
        word = line.split(" ")[1]
        media, note = make_note_for_word(media, model, word)

        if note != None:
            deck.add_note(note)


# Create the package.

package = genanki.Package(deck)

# Write the package out.

package.write_to_file("toaq.apkg")

