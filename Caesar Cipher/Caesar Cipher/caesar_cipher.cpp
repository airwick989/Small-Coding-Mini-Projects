/*
Caesar Cipher
*/

#include <iostream> //required for cout, cin, etc.
#include <string>	//required for use of strings

using namespace std;

int main() {

	//declare and initialize variables
	string input, choice, check("c");
	int cipher(7); //Uses cipher key 7

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	//While continue ('c' or 'C') is selected (selected at first iteration by default), continue encrypting/decrypting
	while (check.compare("c") == 0 || check.compare("C") == 0) {

		//Obtains user selection for encryption/decryption options
		cout << "Please select whether you would like to encrypt (enter '1') or decrypt (enter '2'): " << endl;
		getline(cin, choice);
		cout << endl;

		//Ensures input is valid
		while (choice.compare("1") != 0 && choice.compare("2") != 0) {
			cout << "That is not a valid input, please enter '1' to encrypt, or '2' to decrypt" << endl;
			getline(cin, choice);
			cout << endl;
		}

		char place; //Placeholder for each character of the user inputted message

		if (choice.compare("1") == 0) {

			//Prompts user to enter a message for encryption
			cout << "Please enter the word/message you would like to encrypt: " << endl;
			getline(cin, input);
			cout << endl;

			//Obtains each character of the user input, encrypts the character, and then outputs the character
			//Ignores any non-digit and any non-alphabetical characters
			for (int i = 0; i < input.length(); i++) {
				if (input.at(i) < 48 || (input.at(i) > 57 && input.at(i) < 65) || (input.at(i) > 90 && input.at(i) < 97) || input.at(i) > 122) {
					place = input.at(i); //If character is non-digit or non-alphabetical, simply takes the character
				}
				else {
					place = (input.at(i) - '0' + cipher) % 93 + '0'; //If character is a digit or letter, encrypts the character
				}

				cout << place; //Outputs the character
			}
		}
		else {

			//Prompts user to enter a message for decryption
			cout << "Please enter the word/message you would like to decrypt: " << endl;
			getline(cin, input);
			cout << endl;

			//Obtains each character of the user input, decrypts the character, and then outputs the character
			//Ignores any non-digit and any non-alphabetical characters
			for (int i = 0; i < input.length(); i++) {
				if (input.at(i) < 48 || (input.at(i) > 57 && input.at(i) < 65) || (input.at(i) > 90 && input.at(i) < 97) || input.at(i) > 122) {
					place = input.at(i); //If character is non-digit or non-alphabetical, simply takes the character
				}
				else {
					place = (input.at(i) - '0' - cipher) % 93 + '0'; //If character is a digit or letter, decrypts the character
				}

				cout << place; //Outputs the character
			}

		}

		cout << endl;
		cout << endl;

		//Prompts the user to either continue encrypting/decrypting or exit the program
		cout << "Would you like to continue encrypting/decrypting (enter 'c') or would you like to exit program (enter 'e')?" << endl;
		getline(cin, check);
		cout << endl;

		//Ensures input is valid
		while (check.compare("c") != 0 && check.compare("C") != 0 && check.compare("e") != 0 && check.compare("E") != 0) {
			cout << "That is not a valid input, please enter 'c' to continue or 'e' to exit" << endl;
			getline(cin, check);
			cout << endl;
		}

	}


	//exits the program if user enters 'e' or 'E'
	return 0;
}