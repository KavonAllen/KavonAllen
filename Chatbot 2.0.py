import pandas as pd
import os

FILENAME = "birds.csv"


#Create CSV file
def initialize_csv():
    if not os.path.isfile(FILENAME):
        data = {
            "bird": [
                "parrots", "parrots", "parrots",
                "crows", "crows", "crows",
                "owls", "owls", "owls"
            ],
            "topic": [
                "fun fact", "lifespan", "natural habitats",
                "fun fact", "lifespan", "natural habitats",
                "fun fact", "lifespan", "natural habitats"
            ],
            "response": [
                "Some parrots sleep standing on one leg!",
                "Some parrots like macaws can live over 90 years.",
                "Parrots live mainly in rainforests and savannas across South America, Africa, Australia, and Asia.",

                "Crows can remember human faces and hold grudges for up to 17 years!",
                "Wild crows live around 15 to 20 years, longer in captivity.",
                "Crows live almost everywhere—cities, forests, farms, and parks.",

                "Owls fly silently and often steal abandoned nests instead of building their own.",
                "Owls usually live about 12 years, but some reach 60 years in captivity.",
                "Owls live everywhere except Antarctica—from deserts to tundras."
            ]
        }

        df = pd.DataFrame(data)
        df.to_csv(FILENAME, index=False)

# Load Bird data from CSV 
def load_birds():
    df = pd.read_csv(FILENAME)
    birds = {}
    for _, row in df.iterrows():
        bird = row["bird"].lower()
        topic = row["topic"].lower()
        response = row["response"]
        birds.setdefault(bird, {})[topic] = response
    return birds
        

# Save new bird/fact to CSV
def save_bird_fact(bird, topic, response):
    bird = bird.lower()
    topic = topic.lower()
    new_row = pd.DataFrame({"bird": [bird], "topic": [topic], "response": [response]})
    new_row.to_csv(FILENAME, mode="a", header=False, index=False)
    print(f"Thanks! Your new fact about {bird} has been added to my collection of fun facts!")

# User interaction
def ask_yes_no(prompt):
    return input(prompt).lower() in ["y", "yes", "yeah", "sure"]

def choose_bird(birds):
    return input(f"So which bird would you like to learn about? {list(birds.keys())} ").strip().lower()

def choose_topic():
    return input("What would you like to know? (fun fact, lifespan, natural habitats) ").strip().lower()

def end_conversation():
    print("I've enjoyed our talk! Have a great day!")
    exit()


# Main Program
print("Hey, what's your name?")
name = input().strip()

if name.lower() == "kavon":
    print("Hey thats my creator! Hope you are well as always!")
else:
    print(f"Hey {name}, nice to meet you!")

initialize_csv()
birds = load_birds()
valid_topics = ["fun fact", "lifespan", "natural habitats"]

if not ask_yes_no("Do you want to know about some birds? (y/n) "):
    print("No worries! Maybe we can chat about something else next time.")
    end_conversation()

while True:
    bird = choose_bird(birds)

    # If bird not known, offer to add
    if bird not in birds:
        print(f"Sorry, I don't know much about {bird} yet.")
        if ask_yes_no("Would you like to teach me about it? (y/n) "):
            topic = choose_topic()
            response = input(f"Please share a {topic} about {bird}: ")
            save_bird_fact(bird, topic, response)
            birds = load_birds()  # Reload to include new bird
        continue

    topic = choose_topic()

    # If fact or knowledge about this bird is not known, offer to add
    if topic not in valid_topics:
        print("Sorry, I don't have information on that topic. Please choose from the options.")
        continue

    #If bird are known but topic is not, offer to add
    if topic not in birds[bird]:
        print(f"Sorry, I don't currently know about {topic} when it comes to those {bird} yet.")
        if ask_yes_no("Would you like to teach me about it? (y/n) "):
            response = input(f"Enter your fact about {bird} ({topic}) ")
            save_bird_fact(bird, topic, response)
            birds = load_birds()  # Reload to include new fact
        continue

    #show the facts
    print(birds[bird][topic])

    # Ask to continue or exit
    if not ask_yes_no("Would you like to learn about another bird? (y/n) "):
        end_conversation()


