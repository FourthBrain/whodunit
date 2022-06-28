import hashlib

def check_name(name: str) -> None:
    with open('.env', 'r') as f:
        if f.read() == hashlib.sha256(name.encode('utf-8')).hexdigest():
            print('Congrats! You have officially solved the crime at the Pandas Express! Thanks for participating!')
            print('And now that you\'ve completed your ML software development onramp, tell the world that you\'re ready to begin your journey! \n')
            print('---------------------------------------- Post Template 1 (MLE) ----------------------------------------------------')
            print('I just completed the #ml software development onramp from @FourthBrain and solved a #whodunit mystery!')
            print("Now I\'m ready to take my #ml career to the next level with an industry-standard tool stack, including the Unix Command Line, Git, Conda, Pip, and of course, Jupyter Notebooks!")
            print('#machinelearningengineering #mle #buildinpublic')
            print('--------------------------------------------------------------------------------------------------------------------- \n')
            print('\n')
            print('---------------------------------------- Post Template 2 (MLOps) ----------------------------------------------------')
            print('I just completed the #ml software development onramp from @FourthBrain and solved a #whodunit mystery!')
            print('Now I’m ready to take my #ml career to the next level with an industry-standard tool stack including the Unix Command Line, Git, Conda, Pip, and Jupyter Notebooks, optimized for agile development in VSCode.')
            print('#machinelearningoperations #mlops #buildinpublic')
            print('---------------------------------------------------------------------------------------------------------------------')
            print('\n')
            print("As a bonus - Please checkout the main branch and execute this command in your command line: `git cat-file -p cefafaedfff0fc1e3495252571f48bf7b0d93673`")
        else:
            print("Name is incorrect")

if __name__ == '__main__':
    pass