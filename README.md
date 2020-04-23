# The Words of Adam Smith

"*On the road from the City of Skepticism, I had to pass through the Valley of Ambiguity*" - Adam Smith, 17th-century philosopher and economist
## Table of Contents
1. [Motivation](#motivation)
2. [But what is a Markov Chain?](#but-what-is-a-markov-chain)
3. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [How to Contribute To This Project](#how-to-contribute-to-this-project)
    - [Installing Requirements](#installing-requirements)
4. [Running the Tests](#running-the-tests)
5. [Tech Stack](#tech-stack)
6. [Open Source License](#open-source-license)
7. [Acknowledgements](#acknowledgements)
8. [Resources](#resources)

## Motivation
![This project is intended to inspire critical debate and discussion around economics and computer science, not political grandstanding.](https://i.postimg.cc/yxRXL2ZL/Screen-Shot-2020-04-21-at-3-31-13-PM.png)

What if you could go back and have a conversation with Adam Smith?

Smith's work has inspired the basis for much of what became consumer capitalism - and also predicted much of its worst excesses.

This aim of this project is NOT to espouse any particular political viewpoint.

### The Real Aim of the Project
At the end of the day, I, Zain Raza, aim to help myself and others take a critical look at the following questions:

1. Why does society struggle with poverty?
2. Who was the real Adam Smith?
3. How does capitalism even work?
4. and What can we do to de-polarize economic debates?

## But what is a Markov Chain?
The technical foundation of this is nothing more than a *Markov Chain*, a mathematical construct that enables **stochastic sampling between random states.**

If that didn't a whole lot of make sense, don't worry! I remember Markov Chains being one of the most difficult concepts to grasp, when I first learned about them in the CS 1.2: Intro to Data Structures course taught at [Make School](https://makeschool.com).

For our purposes, let it suffice to say this data structure is what allows the underlying backend for this project to work. Currently, the project is nothing more than a website, where users can send Tweets to the [@Adam-Chain](https://twitter.com/AdamChain) twitter account (managed by Zain Raza).

These tweets are built by randomly picking words of the text of Smith's magnum opus, *The Wealth of Nations* (1776). I encourage you whole heartedly to check out the website and the Twitter profile - looking at some of these Tweets, you may get a little nervous... for instance, how was the Markov Chain model able to generate a sentence like *this* on its own?

"Of discerning the remote parts of the people."

"Is artificially split and divided in the second offence to."

"Of negligence which does not diminish the necessity of diligence."

Are these phrases life-like enough for you? Please take a look at the [deployed version of this site](https://adam-smith-tweets.herokuapp.com/), and share your feedback by opening an issue on this repository! And to learn more about Markov Chain, be sure to check out the links in the [Resources](#resources) section of this document.

## Getting Started
### Prerequisites
- Must have Git installed
- Must have a GitHub account
- Must have Python 3.7.* installed
- Must know how to work in a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/)
(Docker should work as well, I've just never used it before)

### How to Contribute To This Project:
These instructions will help you get a copy of the repository up and running on your local machine.
- Fork this repository (click the "Fork" button at the top right of the page, then click on your profile image).
- Clone your forked repository onto your local machine
```
git clone https://github.com/<YOUR_GITHUB_USERNAME>/adam-smith-tweet-generator.git
```
- Start your virtual environment, and be sure to see the 'Installing Requirements' section below to make sure you have all the required dependencies!

- Create a new branch for the feature you want to work on, or the bug fix you want to make:
```
git checkout -b feature/branch-name or bugfix/branch-name
```
- Make your changes (be sure to commit and push!)
```
git add .
git commit -m "[YOUR COMMIT MESSAGE HERE]"
git push origin branch-name
```
- Don't forget to add yourself to the [CONTRIBUTORS.md](CONTRIBUTORS.md) file!
Please credit your own work, by adding your name to the list in this format:
```
Name: [YOUR_NAME](Link to your GitHub Account, social media, or other personal link)
About Me: 2-3 sentences to introduce yourself
Feature: What did you contribute?
Technologies: What did you use to build your contribution?
Fun Fact: optional trivia about yourself!
```
- Create new Pull Request from your forked repository - Click the "New Pull Request" button located at the top of your repo
- Wait for your PR review and merge approval!
- If you care about this work, then I humbly ask you to **please star this repository and spread the word with more developers! Thank you!**

### Installing Requirements
To ensure you have a development experience that's **as smooth as possible**, please follow these instructions:

- Once you have activated your Python virtual environment (here mine is called "env"), please be sure to run the following command from the command line, to ensure you have all the dependencies
you may need to use for this project:
```
(env) python -m pip install -r requirements.txt
```
- You may always double check the dependencies you have using this command:
```
(env) python -m pip list
```
- If you install any new dependencies, please be sure to record them using
```
(env) python -m pip freeze > requirements.txt
```
Thank you in advance for contributing to this project!

## Running the Tests
Tests are not implemented for this site at the moment. Please come back to this section later, I appreciate your patience.

## Frameworks/APIs Used
- Flask - web framework for the backend
- Bootstrap 4 - styling the front end
- Twitter API - used to send Tweets [@AdamChain](https://twitter.com/AdamChain) on Twitter, using HTTP POST requests.

## Open Source License
This project is licensed under the MIT License - see [LICENSE](LICENSE) for more details. I welcome all open source efforts!

## Acknowledgements
- [Alan Davis](https://github.com/neptunius), instructor at Make School, alias "Captain Rainbow" - thanks for introducing me to the concepts behind this project in CS 1.2!

## Resources
This project taught me a lot about how data structures work, and what they can be used to accomplish. To learn more about how Markov Chains work, and as well as help in implementing Markov Chains using data structures, please check out the following links!

*On Markov Chains:*
1. [Alex Dejeu's Explanation and Guide on Building Markov Models](https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71)
2. [Victor Powell's Visual Explanation of Markov Chains](https://setosa.io/blog/2014/07/26/markov-chains/)
3. [Make School's Tutorial on Building a Tweet Generator Bot](https://www.makeschool.com/academy/track/tweet-generator--data-structures---probability-with-python)
4. [Make School's Lecture on Markov Chains](https://youtu.be/dNaJg-mLobQ)
5. [Khan Academy's Deep Dive into the Origin of Markov Chain](https://www.khanacademy.org/computing/computer-science/informationtheory/moderninfotheory/v/markov_chains)
*On Adam Smith:*
6. [The School of Life's Historical Lesson on Adam Smith's Life and Ideas](https://youtu.be/ejJRhn53X2M)
7. "Rescuing Adam Smith from myth and misrepresentation", [on The Economist website](https://www.economist.com/books-and-arts/2018/07/26/rescuing-adam-smith-from-myth-and-misrepresentation)
