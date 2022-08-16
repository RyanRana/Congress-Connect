# Congress-Connect

https://www.youtube.com/watch?v=Iedfkfz8FHY&ab_channel=RyanRana2

Hi, My name is Ryan Rana. I like to present to you the consumer app I have been working on called Congress Connect. Congress Connect is an app that allows people to learn about congresmmens views on various subjects, based on their tweets using sentiment analysis and machine learning. 

When citizens want to learn more about politicians' views on subjects they are often overloaded with tons of articles and information which may contain contradictions, bias, and unreliable information. They can also read congremmens twitter pages but even then there is a vast amount of posts that they have to simmer through to easily get what they are looking for. Because of this many are left uneducated as to what the true views their congressmen and forever leaving a barrier between the people and the congress. I was inspired to make an app to solve this issue and better connect people with there government.

Congress Connect provides a solution to this issue and it's super easy to use. All the user has to do is open the app, and enter a congressmen's Twitter handle, and a word relating to a subject they want to learn about, examples include, mask, abortion, gun poliecies, etc. Then the app displays a short statement about the political views of said congressmen on said topic, as well as  other information.

Once an input is made by the user the program uses a Python library called TWINT that scrapes all tweets from that congremmen that also contain the word. Then this data must be stored in a data frame in order to be analyzed.
 
However we still need to find the political views. To do this we are using is sentiment analysis which is a machine analysis to find the sentiment of a text  combined with reccurent machine learning models.

To do this a dataset of over 14000 tweets data samples classified into 3 types: positive, negative, neutral is used. Machines don’t understand words and can only understand numbers, so we convert the text into an array of vector embeddings where each different word gets represented numeracilly and then break the . Each tweet is then padded with filler words so all are at the same length. The machine learning model to be used is called LSTM or Long short-term memory. This is an artificial neural network, and it is optimal because it resuses the data and gives feedback to the model for each part of the tweet. This model is trained and tested with an 80/20 % ratio. Training is essentially calibrating all the calculations of the model from random values to stronger connections for higher accuracy by running the model thousands of times. The testing stage is simply evaluating the accuracy of the model. The LSTM reacehed 95.43% accuracy

For the users input, each tweet in the data frame goes through the model and it is given a number as the output, 1: negative, 2:neatrul, 3:positive. The average of all the tweets outputs are calculated and it rounds to either negative, neutral or positive. The program takes the 3 tweets with the highest prediction confidence and formulates it into a proper argumentative stance and displays it to the user, in the format “ Congressman, _____ has a ______ stance on ______, because he said, _______, _______, and ______”. The app can also display additional information such as a table of all the tweets, congressmen with similar viewpoints, a link if there is one in the congressmen twitter, as well as suggestions for other topics.

This app used Python for all the backend functions including organizing and altering the data as well, the semantic analysis, and the LSTM. ReactJS was used for the the frontend, to take in the inputs, to display the timeline, the sentence, as well as the other information, React was especially chosen so it can be launched on all platforms including IOS and Android.

In the future this app can be expanded on by tuning the accuracy to get it close to 100% as well as enhancing the layout and design. This app can have real potential of help educating the people of this nation about there congressmen. Thank you.





