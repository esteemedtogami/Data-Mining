Sam Pickell
COMP 5540 Data Mining
samuel_pickell@student.uml.edu



Description of Implementation

"transform.py" is the first program that I wrote, and it takes the data from "input.txt" and transforms it to a binary representation in "output.txt". The data from the output file is then placed into three separate files: "training.txt", "val.txt", and "testing.txt". From there I added functionality to the incomplete functions in "formulas.py", "models.py", and "proj_test.py", as well as made some changes to the code that reflected Python 2.x (as I was using Python 3). The code that I added to the various functions was based on the logic provided in the Wikipedia page on Backpropagation that is linked to in the pdf. 



What to Know to Run the Program

The most important factor to consider is that this was written using Python 3. If my code is run using a Python 2 compiler, it will likely not work. The other important factor to consider is if you want to test "transform.py" and there are errors regarding the input and output files, their file paths may need to be set specifically to the machine. This shouldn't be an issue if "input.txt" and "output.txt" are located in the same directory, however. If you would like to simply see the neural network running on the provided mushroom dataset, please use "proj_test.py". If you would like to use test data other than the mushroom data that is provided, first put that data in "input.txt", run "transform.py", and take the data in "output.txt" and put it into "training.txt", "val.txt", and "testing.txt". Afterwards, you should be able to run "proj_test.py" on the new data.



Acknowledgement of Parts That Don't Work

"proj_test.py" successfully completes on my machine with an error of 0.48%, leading me to believe that my code is working properly.



Collaboration with Other Students

I did not collaborate with other students on this project. My work is entirely my own - the only outside help was the Wikipedia article