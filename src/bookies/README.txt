Bet_terms (this is referenced throughout the user stories below):

BET TERMS:
Question: (options: 
(1) Choose your own: e.g. Will there be a snow day on Monday?

(2) Choose from current list of publicly verifiable bets that we've set up (*1))
Odds:
Yes: x%
No: (100-x)%
Minimum Bet Amount: (options include None, and they can also set their number)
Consensus Mechanism: (Choices:
Voting Threshold: (% of members necessary to agree on the outcome and be fine with distributing 100% of earnings to winners, set by user if user picks this)
(*1) Verifiable: (check if verifiable question was chosen))
(if not verifiable), timelock: (this specifies a time period in which the voting threshold % must decide on the outcome or all funds are returned to the initial participants)
Group Size: (the size of the group with the size assumed to be the size of the group if everyone bets, but as people deny, the size decrements accordingly)


USER STORIES:

1) 
As a user, I want to initiate a bet with n of my friends (for fun). 
--So, you invite each of your friends to join a group where the bet terms are displayed (you set the bet terms). Each friend chooses to join the bet (if they agree with the betting terms) and picks an amount that they will bet initially for a given choice. After this stage, the rest of the steps are explained at the bottom of this document.

2)
As an admin, how do the betting odds change once a bet is made?
--At the opening, the odds are nonexistent. Then, everyone starts making bets. Let's think about how this could occur: Person A bets $100 on outcome 0. Outcome 0 odds went from (?) to (100%) (Also change outcome 1 odds to 0%). Remember the definition of outcome odds is really the odds predicted by the betting market's bets and, in this case, the only bet made is in favor of one outcome (so 1/1). If person B bets $x on outcome 1, the odds will changing the following way:
(1) outcome 0 odds will be (100*(100/(100+x)))%
(2) outcome 1 odds will be (100*(x/(100+x)))%
This makes intuitive sense. You would have an incentive to bet on whichever side you consider to be correct depending on your conviction and the current odds. If you're sure something will occur, you should bet on it every time the odds are below 100% unless 1) you don't believe the group will concede and consensus will fail 2) you think you could achieve a higher rate of return in another bet in which you have the same conviction and better odds in terms of return. We let the user set consensus which is explained in the bet_terms file.

3)
As a user, I want to sell out of a bet.
For every participant after the first participant (and including the first participant), the percent gain/loss is the difference between the percentage when you bought into the bet and when you left the bet. The bets initiate at (?) and change immediately upon the first bet. Naturally, this would mean that the first person to bet is at a disadvantage. Therefore, the first round of bets is mandatory in order for a person to participate in later rounds so everyone has to put in a minimum amount in order for this to work.

4)
As a user, I want to double down on my bet.
The odds will change every time you buy in again so you will be getting worse odds whenever you double down (unless the odds have fallen since you previously bought in).

5)
As a user, I want to initiate a verifiable bet.
As of right now, we will show a list of verifiable bets, but we haven't developed anything beyond that list. So you may choose from that list.

6)
As a user, I want to join a group of people to bet.
You can create a group and invite your friends or have them invite you. There are also public betting pools that we will set up that are separate from the private pools.

7)
As a user, I want to make a bet in a public pool.
Making a bet in our public pool works the same way logistically as buying into a given side after the initial bets are made in a private pool. The odds will change in response to your purchase and your profit/loss is governed by the different between your odds when you bought in and when you exit.

8)
As a user, I want to deny an invite to join a group.
You can deny the invite and this will be notified in terms of the expected size of the group immediately to all invited members who are still considering. This is relevant because it is indicative of the amount of money that could be made.

9)
As an admin, I want to enter one of the results for a verifiable bet.
We would provide the infrastructure such that administrators could enter in the results of a bet.

10)
As a user, I want to flag someone.
You can submit a formal report that describes what you think they did wrong and if you think they were associating with another group of users. We log the information internally and use it to find/counter malicious nodes. We also display the number of flags someone has next to the user profile to draw attention to malicious users. The number of flags that an account submits is also logged so malicious nodes that aggressively flag other nodes will also be monitored and taken offline.

You should use this as a tool that will help you cement your understanding of how you want your create-listing/add to ES/search flow to work as well as a tool to help you divide up the work among your group members.

11)
As a user, I want to search for an outstanding bet.
I can search the relevant parameters (and not include the parameters that I am not aware of). Relevant search results will appear. The search result ordering is done using ES to determine relevance and ordering.

12)
As a user, I want to search for all bets made by a specific user.
I can search for the user and all bets will show up (this works because ES works).

13)
As a user, I want to search or all bets with a specific minimum or maximum.
ES makes it such that sometimes* (not every time), searching for this arbitrary value will return all bets with this number included as one of the parameters (it must be the exact value, not a value that is close).


System logistics description:
A person starts a bet by inviting a group of people to make a bet with him/her. This creates a group and every member that was invited either joins the group for the bet or leaves depending on whether or not they agree with the bet_terms. The bet_terms (which are documented in another txt file) contain information such as the question, the outcomes, the minimum bet amount (this must be set to some nonzero amount because otherwise people could join the bet and make their bet last therefore increasing their payoff---see (1)), and the consensus mechanism. At a certain point, everyone initiates their bets at the same time. After this point, everyone can sell out of their bets, double down, or buy into the other side (1).

The odds change dynamically based on new bets. This is explained here:
All the bets are initiated at the same time after all the participants agree with the original bet_terms and submit their bet. The system waits for all participants to submit this form (which contains their signature and bet amount for initialization). The odds are initiated in the following way. For outcomes 1,...,i,...,n, the odds of outcome i (such that 1<=i<=n) is equal to the 100*(sum_{all bets on outcome i}/sum_{all bets made}). This holds true for all outcomes. In our Beta version, we will be working with binary events so there will only be two outcomes. A worked out example with two outcomes is explained below:

The group of size n makes bets b_1, b_2, ..., b_n. Each of these bets corresponds to one participant. The message that is sent to the system from each participant contains the signature that indicates explicit acceptance of the initial bet_terms along with the initial betting amount. If their initial betting amount is below the minimum amount, they are not allowed into the betting pool. The odds of outcome 0 are expressed as 100*(sum_{all b_i that bet on outcome 0}/sum_{b_i}). The odds of outcome 1 are similarly expressed as 100*(sum_{all b_i that bet on outcome 1}/sum_{b_i}). From this point forward, a participant's profit/loss can be understood to be the odds when they entered a bet on outcome i less the odds when they exited a bet on outcome i. In the end, all outstanding bets are distributed to the winning side. As we approach the outcome's occurrence and the winning outcome becomes more obvious, we would expect to see convergence.

Our consensus mechanism is very important because it helps us pick the winner. If we could verify all outcomes this would be preferred, but our target audience of private bets will probably consists of mostly unverifiable bets. In these cases, we will let the person who sends the invite to the rest of the group decide in the bet_terms what they want to set the voting threshold to. This is the percent necessary to decide on the outcome. If you do not reach that percent, the bets are returned to the remaining participants in the fairest way possible that corresponds to the initial betting state (when all the first bets were initiated). The problem is that some players might have made a profit and then exited before the final state. We cannot punish those players now as they played no part in consensus. Instead, we will use a matching algorithm to distribute the remaining pool to the participants based on the amount left in the total pool and the initial distribution of bets for the bet itself. 

Even so, this matching algorithm will not be perfect and malicious accounts will be penalized. This punishment will be incorporated into the incentive scheme for choosing groups. Naturally, you're only going to want to join groups with individuals who do not cheat or get cited for cheating frequently. Of course, this could result in malicious accounts reporting legitimate accounts, but we think that this risk is unlikely. We could refine this scheme in other ways to prevent spam and bots, but there are existing systems in which it already works very well. (So, we can refine the details of this flagging system later)

(1) The reason behind having all of the bets initiated at the same time is because in every situation in which bets are linked to the timing of user responses, it is in everyone's interests to submit their bet last (because as the odds become stacked against them, their payoff increases until they submit their bet). 

We need to put a lower bound on the griefing factor (the ratio of harm done to victims relative to cost to malicious actors). This will require some thought. 
