# Adventure Game Python Coursework
This is coursework for the OCR Entry Level Certificate in Computer Science (R354). It is a text-based adventure game made in Python, using CSV files.

## Description
I am creating a text-based adventure game based in the future on a space station. It will offer scenarios and multiple-choice options which will determine the story path. There will also be a few fights, where the user must answer a general knowledge question to win. If they lose, the user will lose an amount of hit points (they start with 100). The game ends when the story resolves (win), the user runs out of hit points (lose) or the story ends with the aliens winning (lose).

The story is based on a space station where an alien is discovered. The user is a scientist investigating the effects of zero-g on rocket seeds and who suddenly discovers an alien onboard. The aliens are plotting to take over the space station and use the humans as slaves, but they can be stopped if the user makes the right choices and knows the correct answers.

All the question and scene data will be stored in CSV files to make editing each scene or question quick and easy.

## Success Criteria
*	The program must ask the user for their name and refer to it throughout the program
*	The program must allocate 100 hit points to the character at the start
*	The program must remove hit points when the character loses a fight 
*	The program must display the right text at each scene
*	The program must give the user multiple choices and questions
*	The program must change the scene depending on the user decision or answer
*	The program must end if the character reaches 0 hit points
*	The program must have a way to win
*	The program must have verification in decisions and some types of question, and ask the user to re-enter their decision/answer if they don’t enter it correctly/in the correct format
