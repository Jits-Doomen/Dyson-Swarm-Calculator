# The Start

The first base of the code was mainly from Googling terms and formula's for a Dyson Swarm. The idea of a swarm (and not a sphere) came from a "Kurzgesagt - In a nutshell" video I watched a couple years ago. So I did some research, and got to work.
After I made the main code advanced enough, I posted it on Reddit (r/IsaacArthur and r/Python) from which I got some advice and questions.
___
# ESA
One of the questions was were my construction capacity 1e14 constant came from. Which I told them was a pure guess that was just a baseline. But I know that that is not good enough for a project like this.
So I looked for ways to find the right constant, but couldn't find it. And then I got an idea.

I went to the ESA website and did some more research, until I stumbled upon the ESA Advanced Concepts Team, where I looked for papers but couldn't find a fitting one, then when I checked the members of the ACT, I found the perfect choice; Mr Seiler.
I told Mr. Seiler via e-mail what my code was and what I wanted to know. I expected a (if I got one) response email in 2 weeks, but I got it that same day. The most import part of the response was that he told me that my best shot was a sigmoid function variable, which I added as soon as I could.

Currently, I have an outgoing email to Mr. Williams, asking if he has an idea for better constant materials.
___
# TU Delft. 
When I recently revisited my model. I suspected the sun's angular diameter would introduce a significant vector divergense that a simple Inverse-Square-Point-Source model simply does not capture.
So I reached out to Dr. Heiligers at the TU Delft with three questions about Gossamer Spacecraft, my Point Source approximation and the N-Body perturbations between sattelites.

She taught me incredibely helpful ways to improve my code. These include information about the Point Source vs. the finite disk, active stationkeeping and how their positioning would require extreme precision. 

