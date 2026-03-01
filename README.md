Bird Chatbot (Python)

A simple command-line chatbot that teaches users about birds and can learn new facts over time.
The chatbot stores bird information in a CSV file and allows users to contribute additional knowledge during conversations.

Features

Interactive chatbot experience in the terminal

Provides information about birds including:

Fun facts

Lifespan

Natural habitats

Automatically creates a CSV database if one does not exist

Users can teach the chatbot new birds and facts

Stores learned information for future sessions

How It Works

The chatbot uses a CSV file (birds.csv) as a simple knowledge base.

When the program starts:

It checks if the CSV file exists.

If not, it creates one with starter data.

The chatbot loads the bird information into a dictionary.

Users can ask about birds and topics.

If the bot doesn't know something, it asks the user to teach it and saves the information.

Project Structure
.
├── Chatbot 2.0.py     # Main chatbot program
├── birds.csv          # Knowledge base for bird facts (auto-created)
├── README.md
└── LICENSE
Requirements

Python 3.x

Required library:

pandas

Install with:

pip install pandas
Running the Chatbot

Run the script in your terminal:

python "Chatbot 2.0.py"

The chatbot will then ask for your name and begin the conversation.

Example interaction:

Hey, what's your name?
> Alex

Hey Alex, nice to meet you!

Do you want to know about some birds? (y/n)
> y

So which bird would you like to learn about? ['parrots', 'crows', 'owls']
> parrots

What would you like to know? (fun fact, lifespan, natural habitats)
> fun fact
Example Knowledge Stored
Bird	Topic	Example
Parrots	Fun Fact	Some parrots sleep standing on one leg
Crows	Lifespan	Around 15–20 years
Owls	Natural Habitat	Found almost everywhere except Antarctica
Possible Improvements

Some ideas for expanding the project:

Add more bird species automatically

Add fuzzy matching for bird names

Turn it into a web chatbot

Add more categories (diet, size, behavior)

Store data in a database instead of CSV

Author

Created by Kavon Allen

License

This project is licensed under the MIT License.
See the LICENSE file for details.
