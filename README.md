# Risk Simulator

![Risk README intro](/resources/risk_readme_pic.jpg "Risk Intro")

## WHY
Are you tired of getting your butt kicked when playing the popular "Risk" board game with your friends? Well I feel you bro, I am as well.<br>
But today may be your lucky day: use the "___Risk simulator___" to learn with pinpoint accuracy what are the odds of your attack (or defense) to be successful and dramatically improve your chances of winning, so that ___YOU___ can be the one kicking everyone else's butt at the table next time.

## WHAT
- Insert the no. of attacking armies (red armies)
- Insert the no. of defending armies (blue armies).
- Specify how many armies you want to keep on the ground before stopping the attack.<br>
_E.g._ you attack with 10 red armies, while 6 blue armies are defending. You decide to stop the attack when 2 red armies are left on the ground in order not to preserve the territory and not let it completely unguarded.<br>
- Finally, decide how many attack simulations to run (up to 1,000,000).

The program will roll the dice for you and compute as many attack outcomes as specified by the simulation number. It will compute the no. of successful attacks won by red armies and the no. of successful defenses won by blue armies, eventually computing the odds of a successful attack (or defense).

## HOW
The program's logic is based upon the ___Monte Carlo Simulation___ method, _a mathematical technique that predicts possible outcomes of an uncertain event by means of repeated random sampling versus a set of fixed input values._<br>
In other words, a Monte Carlo Simulation builds a model of possible results by leveraging a probability distribution, such as a uniform or normal distribution, for any variable that has inherent uncertainty (_i.e_ in our case those variable are dices). It then recalculates the results over and over, each time using a different set of random numbers between minimum and maximum values and a given set of fized input variables (_i.e._ in our case those variables are the no. of red and blue armies, as well as the no. of red armies to keep on the ground).<br>
In a typical Monte Carlo experiment, this exercise can be repeated thousands of times to produce a large number of likely outcomes.
