# How He Turned AI Drones Into a $15M Business

- Channel: Nathan Latka
- Video URL: https://www.youtube.com/watch?v=c6DF12Pfd5g
- Publish date: 2026-06-17

## Transcript

Where are you sort of sitting in this

space?

>> I think physically I is at the same

point where Chat GPT was in around 2015,

where it's just finding its roots.

>> What's the average customer maybe paying

per year?

>> Our average deal size is about half a

million dollars per year.

>> But what does your largest customer pay

today on an annual basis or range is

fine?

>> I would say about 3 to 4 million dollars

a year.

>> How many individual customers are you

working with today?

>> About 30 to 40 logos, independent

customers.

>> Hey folks, my guest today is Sankalp

Aura. He is building gather.ai. It's a

Pittsburgh-based physical AI company

that uses autonomous drones and computer

vision to deliver real-time inventory

intelligence for warehouses, serving a

variety of customers like Geodis, Axon,

and others. He holds a PhD in robotics

from Carnegie Mellon University where he

built one of the world's first safe

autonomous helicopters for DARPA and has

raised 74 million bucks to date. We'll

talk about his series B which was led by

Keith Block Smith Point Capital.

Sankalp, already takes us to the top.

>> Yeah, sounds good. Listen, thank you for

having me.

>> Tell us for folks that are not familiar

with sort of the work, you know, Nvidia

is doing on SDKs to pro you know,

foundational models to program the

physical world. Jeff Bezos is, you know,

reportedly raising a fund to invest in

this space as well. Obviously, he's got

a lot of warehouses to manage. Where are

you sort of sitting in this space?

>> Yeah, so I think physically I as it's

being defined today is robots operating

in physical spaces, of course. And

historically, the approach to that has

been to design specific autonomy stacks

for specific use cases. And what the

latest and the greatest of industry is

trying to do is build a foundational

model much like Chat GPT that can do

anything for text purposes, can do

anything for physical spaces.

And the And I think if you get an

equivalence, I think physically I is at

the same point where Chat GPT was in

around 2015, where it's just finding its

roots, but people now have belief that

it can deliver that that wasn't possible

before. And we somehow sit in the middle

where we have a mixture of foundational

models and classical AI techniques which

are probabilistic robotics driven to

actually make these robots safely work

in physical live environments and

provide value today instead of you know

providing value 7 years down the line.

>> And in your opinion today if you looked

at every engineer in the world, every

person building something, who who's the

best sort of person to build this? I

mean I think deeply about what must be

happening in Ukraine with these folks on

the front line programming physical

spaces, commanding to the drones, you

know, having them, you know, hit and

protect certain city things like that. I

also think about obviously someone that

might have built the, you know,

inventory, you know, robotic system to

manage Amazon warehouses to get delivery

time down by a millisecond because then

we spend more. I think about someone

like you who work work with DARPA,

right? You know, great university going

to. I mean, why is your background and

your team sort of best suited to win

this space?

>> Two things. The three co-founders,

Daniel, Gitesh, and myself, like you

mentioned, worked on the world's first

fully autonomous helicopter, won

national awards for the work we did with

aerial autonomy. So we had deep

expertise in physical AI for aerial

autonomy and my thesis focused on

how to make robots curious and they're

curious here in warehouses about boxes,

barcodes, inventory, and workflows. So

that that makes the technology alignment

quite strong.

And the second thing is over the last 6

or 7 years how our stack has evolved.

Now our stack is the only stack in the

world that you can put on a moving

camera that you buy out of Best Buy and

turns it into an autonomous data

gatherer.

So that's the technical side of it where

we have a data mode and a tech mode of

of given our technical backgrounds.

But, also over the years, we have

assembled a bench of people from Amazon,

from Uber, from uh SeaGrid with deep

logistics background. So, our product

has evolved to support logistics players

in how they want to be supported. So, I

think those two combinations give us uh

an unfair advantage to to serve

effectively in this space.

>> And so, with that background, uh again,

I've got your website now pulled up

here. We'll talk about the $40 million

Series B here in a second, but you use

sort of the terminology physical AI for

intra-logistics. Is your plan here to

sort of be Switzerland an open-source

foundation model that anyone can use, or

is it really to try to, you know, walled

garden sort of Apple App Store approach

and keep it all internal?

>> It's neither. I have a very different

view on it if you'll allow me.

>> Please.

>> I think our view is squarely focused on

how do we deliver value to the end

customer, which means we can have really

good foundational models,

but the customer could not care less.

They really care about how does it hit

their top line and bottom line

performance, which is either how does it

impact their labor,

or how does it impact their shipping

rates, or in at the rate at which they

are shipping out goods, facility

throughputs.

So, we provide the value to the customer

as an end result, which is mostly

actually accessed by them through our

web dashboards and insights, not through

our physical AI. Our physical AI is a

mode to get them that that value. So, we

really uh think of ourselves as the

solution that generates the end value

and not just provides the empowering

technology to do so.

>> So, you're There's a trend in AI right

now, which is charge against the job to

be done, not necessarily for credit

usage or seat-based approach. Am I

hearing you correctly? You're charging

Barrett Distribution Centers on some job

to be done. There's not a massive

engineering team there calling, you

know, you know, tool calling your

different foundation models to do work.

You're you're doing the work for them.

>> That's right. That's right.

>> Interesting. Make this hit home. Can you

use this real example that's on your

website? So, you know, they have uh to

store 400 500,000 series baggage shoe

box Is it so Okay, so they're a shoe

company. Tell us the work you're doing

for Barrett.

>> Okay. So, Barrett we had actually

multiple kinds of facilities. They are

one of the leading third-party logistics

players in US. But, for this specific

example, do you know Stadia Goods? They

sell It's a It's a marketplace for

vintage shoes.

>> Spell it. Stadium?

>> Stadia. S T A D I A.

>> Okay. Go ahead. I'm pulling it up.

>> Yep. So, you get all these collectibles,

collectible sneakers that range anywhere

from uh $100 to $15,000.

And uh that shoe facility that you were

showing images of holds over half a

million pairs of these shoes.

And when customers pay, you know, even

in this case when customers pay, let's

say $1,000 for the shoes, they want it

next day. But, where a person goes there

to pick this pair of shoes, which is a

case, and they don't find it there, they

basically have to pull a software and on

and say, "Oh, I can't find the shoes

there. So, let's spread out and find

that pair of shoes that needs to go

out." And suddenly, a pick that was

supposed to cost $2 ends up costing $10

to $15. What we came in and were able to

do in partnership with Barrett was

reduce that those kind of location

errors by 70%.

>> And that's because of this drone we see

here in the graph. This is you basically

going and finding the SKU that was

purchased on new sneakers to get to the

delivery time faster.

>> Yes, but it's even better than that.

That those drones are continuously

flying, taking images. So, you not only

need to find that targeted shoe, you

actually know at any given point how

your warehouse is laid out and how

things are moving. So, you can make

decisions in real time on how to do

better picking, how to do better

sorting. And that 70% decrease in in

inventory misplacement errors for

someone like Barrett was the difference

between keeping the Stadia goods account

and making them happy versus having them

move to someone else cuz they came to

Barrett cuz they were unhappy with their

last 3PL and how their inventory was

maintained.

>> Guys, remember I am not just a YouTuber.

I'm investing in my third fund. We've

deployed $250 million into 550 software

companies so far. Again, at

founderpath.com. If you're interested in

capital, I would love to cut you a check

because I know you're investing in your

education. You watch my show. So, sign

up at founderpath.com and when you get

the onboarding email, I reply and I see

all those. Just reply and say, "Nathan,

I found you through YouTube." and I'll

make sure to prioritize you. I would

love to cut you a check. Check out

founderpath.com.

This makes a lot of sense to me. Thank

you for educating me on how this works.

How do you price this thing? What's the

average customer maybe paying per year?

Is this sort of an enterprise motion

with million-dollar per year accounts or

is it more sort of bottoms-up? I imagine

it's probably more enterprise, but

please you tell me.

>> Actually, it's a bit of both. When we

So, just one thing I'm really proud of,

I'm proud of the of the thing that we've

built, our team, is our net revenue

retention annualized is 170%

annualized. So, it is best in class. So,

we start with, you know, five to seven

facilities in a network, which is

usually our average deal size is about

half a million dollars per year in terms

of subscription.

>> For [snorts] those seven facilities?

>> Yeah, five to six facilities, I would

say, yes. And

then that ends up by second year going

to 50 odd facilities and by third year

we are looking at 100 plus facilities

and and taking that forward. So, it

starts with a little enterprise deal,

but expands into network wide fairly

quickly and fairly often.

>> This is a traditional land and expand by

but coming from the guy that built the

world's first autonomous helicopter,

which we love. This is your engineering

sort of sales kicking in here. What is

don't name the customer, that wouldn't

be appropriate obviously, but what is

your largest customer paid today on an

annual basis or range is fine.

>> I would say about 3 to 4 billion dollars

a year.

>> This is so impressive. How many I'm just

not familiar with how many warehouses

exist in the world. You have 170% net

dollar retention. How many customers are

in the world that you think you could

get, you know, on Gather AI and deliver

that 3 to 4 million dollars of sort of

contract value annually?

>> Also, this is very interesting. So,

looking at uh warehouses in US, let's

not even look at the world. If you look

for uh warehouses that are above 100,000

square feet,

>> Okay.

>> that's about 150,000 warehouses.

>> Wow.

>> And for us, for example, to serve a

decent chunk of that business so that we

are generating a 100 million dollars

worth of revenue on our side cuz that

usually means that we are generating a

value of about 3 to 400 uh

million dollars, sorry, 100 100 million

dollars of ARR on our side. That is

usually means we are generating 3 to 400

million dollars of revenue for our

customers is just serving about 100

customers with 10 warehouses each. So,

that's just 0.1%

of the market that's available.

So, this we have an opportunity here to

really serve a massive number of

customers to alleviate their day-to-day

day-to-day uh pain points.

>> And how many you just gave the 0.1%

number, but how many individual

customers are you working with today?

Like like a bear, are we talking like 10

or 1,000 or 100 or

>> Oh, yeah, we are we are I like to say we

are just just starting out. This is

still very much day one. So, I would say

about uh 30 to 40 logos, independent

customers.

>> Okay.

And I don't want to put you on the spot,

but I mean, can I multiply the 30 logos

times a half million bucks a year? That

would put you at about a 10 or 15

million run rate today.

>> Let's say roughly right.

>> Okay, great. And can you share what

growth looks like? If you're at 15

million-ish today, where were you 1 year

ago? Obviously, you're growing cuz net

revenue retention is 170%, but that

doesn't even include new logos added.

>> was in year. So, we grew 2.5x last year,

year over year.

And this year we are forecasting

anywhere between 2 to 3x as again.

>> Wild. I want to get your more your

background story. We know about the

great work you did at DARPA and

autonomous helicopter, but you list many

industries on your website. 3PL

logistics, retail, manufacturing, life

sciences, and four separate solutions.

AI Co-Pilot, MHA Vision, AI Vision, and

and sort of how it works solution.

When did you write the first line of

code for this platform? And what was

your first target industry and solution?

>> Our first target solution was helping

warehouses get their inventory accuracy

much higher, which is our drones flying

around in the warehouse taking

inventory. The first line of code was

for the solution was written right after

my PhD defense, so for late 2018.

And it took us 3 years from then to get

to the market, to get the tech ready cuz

no one had ever built this tech around

things that you can buy out of Best Buy.

And we really wanted that for

scalability, for serving our customers

with effective hardware, which is

robust, but at the same time

for our unit economics to look like SaaS

instead of RaaS. So, it took us 3 years

to get the tech stack out there where it

was performing reliably for our

customers, and since then we've grown

dramatically year over year.

>> So, 2018 was first line of code. Did I

hear you correctly? 2021 is first

customer?

>> Yes, that's right.

>> How did you fund the business over those

3 years?

>> We have

since we were pitching a tech that was

not being done in the world, so we knew

we needed sufficient capital.

>> And then you just recently announced to

all of you, I don't want to spoil the

announcement. Talk to us about the

series B. And we don't love celebrating

funding sort of on the show, but

obviously you need it to build a

revolutionary technology. So, talk about

how much you raised and then what you

plan to use the money for to help your

customers like Barrett.

>> So, we, as I said, we grew 2.5x

year-over-year last year with those

retention numbers that we are really

thankful for.

But at the same time, the sales motion

had scaled beyond founder-led sales,

beyond me. And thankfully so. Because

our new sellers were doing much better

than I was. And as a result, we had

sufficient proof points to say that now

we need to pour more gas into this GTM

engine and scale, which is where our $40

million Series B round came about with

Smith Point Capital

leading and taking most of that round.

That is,

I think, was just founded by Keith

Block, ex-CEO of Salesforce, and Chris

Little.

And they they just saw how enterprise

physical operations are going to change.

Even if they won't be fully autonomous,

they will be fully digitized. And that's

what we do.

Digitize those physical operations. And

now it is going towards

not just scaling our drone-based

inventory monitoring product, but also

scaling our forklift vision product,

which puts cameras on forklifts. The

same tech stack on forklifts.

And suddenly, whatever your forklifts

are carrying and wherever they are

placing it is digitized. So, your

warehouse turns into an Amazon Go store

without a wide network of cameras that

Amazon Go stores needed. So, instead of

things, we think of it like drones were

finding things that were

>> you show me a picture? So, I'm sunk up

I'm trying to find As you're getting,

I'm trying to find a picture. Do you

have the forklift anywhere on the site?

>> Let's see. I'll have to check. Give me a

second.

>> Okay.

>> I think if you go to solutions and go to

MHE Vision

>> MHE Vision, okay. Oh, here we go.

Forklift number two This is you?

>> Yes.

>> Okay, so you're the software and the

hardware.

>> Yes. So, the operators get live feedback

on whether they're doing the right

transaction, where they're picking up

the right thing, where they're putting

away the right thing from the truck to

put away, to replan, back onto the

truck. So, as a result, your whole

operations becomes digitized. And then

we can start providing insights on how

to run operations better and not just

find your missing things in the

warehouse. So, we've gone

>> the decision not to be heavy Sorry to

cut you off, but you've made the

decision not to be heavy opex. You're

not selling all the the yellow forklift

here. You're You're basically saying,

"Look, we're going to build software

that's so flexible, you can plug it into

any off-the-shelf hardware." So, you are

hardware Switzerland.

>> That's it. Yes, that's true.

>> Smart. Really, really smart. Okay, very,

very interesting. Sankalp, do you have a

data advantage here? In other words, the

more I have T devices installed, and

whether it's a drone or a forklift that

you have installed, you're collecting, I

imagine, millions of data points every

single month at this point. How have you

structured sort of your database to

normalize the data, run an ETL process

on it, and help the next Barrett that

signs up have a lower sort of loss rate

or inventory loss rate? Like, is there a

compounding data machine underneath

here?

>> Yes, I'm so glad you asked that

question. I think that's what keeps us

in the lead in terms of the data

insights we offer to the customers. Cuz

we And we have proven examples. I would

I would request Amanda to share them

with you. Now, we can Our our neural

nets can read barcodes that not even a

barcode scanner, a line scanner that you

have on your grocery store, can read.

And mostly because the millions of data

points, the millions of barcodes, and

boxes that we have seen, bunch of our

neural nets are running self-supervised

experiments on them. So, there is no

human in the loop. They improve

themselves as they run these

experiments. And then a small number

that they have trouble with in

self-supervised fashion get to people

annotating those examples and then

feeding it into the training loops.

>> So, I appreciate you coming on today. Is

there anything I missed that you want to

make sure we talk about here over the

last 60 seconds?

>> Yes. Uh there's something that I It's a

bit of a personal message cuz you said a

lot of the audience is existing founders

and some VCs. I would say the biggest

struggle that a founder faces and this

is every founder that I've ever talked

to is the loneliness and the mental

health cost that comes with dealing with

uncertainty. So, the best thing I would

encourage the fellow co-founders is

across across the world is to be

vulnerable with that side and seek help

cuz I think to me, as well, that's

something I discovered has changed the

quality at which and the level at which

I was performing when I was able to

address and seek help in those domains

actively.

>> Is there a personal story you're

comfortable referencing? Did you deal

with a bout of depression?

>> Oh, yeah, sure. Yeah, no, I'm super

super comfortable sharing. Actually, up

until 1 and 1/2 years ago, I didn't know

that life that people were existing that

don't have suicidal thoughts. Like that

was my life up until then and I thought

everyone deals with it. So, so am I cuz

that's how I

>> were having You were having suicidal

thoughts as you're passing 9 million of

revenue. Everyone would say, "Oh my

gosh, this is an amazing." At least if

they're just reading your Twitter bio,

but you were dealing with suicidal

thoughts at the time.

>> Yes. Yes. Yes. And that that was being

That was my as sort of I was carrying

that since my teenage years, but they

were getting really louder and mostly

because of the sense of responsibility

and pressure. And I discovered the right

mixture of medicines and discovered that

there is life without suicidal thoughts

and I think that just made me a much

happier operator and a much happier

builder and that shows in our work and

what we're doing.

>> Well, I I can't wait to see the impact

that you and your team, obviously, are

going to have on the world. To your

point, you're like touching 0.001%

of your market right now. My only regret

is I didn't find you earlier and demand

that you let me put in a $100,000 check

because I think what you're building is

really compelling intellectually. It's

interesting and the growth speaks for

itself. So, SunRob, if people want to

follow your journey going forward after

this interview, where can they find you

online?

>> The best place is actually LinkedIn or

reach us through our website.

>> Just did a series B of 40 million with

Smith Point Capital selling 10 to 15% of

the business. That would be about a 270

to 400 million valuation somewhere in

that range with 75 people, but more

importantly, he's really touching one of

the first founders I'm seeing really

touch on foundation models for the

physical space, which is the next big

frontier. He's touching a very small

percentage of his potential customer

base right now. There's over 150,000

warehouses in the US with more than

100,000 square feet. He's touching just

30 customers today. Largest ACV 3 to 4

million as he

continues to expand his solutions like

MHA MHE vision into multiple industries

like retail, manufacturing, and more 3PL

companies like Barrett. SunRob, thank

you for taking us to the top.

>> Thank you for having me on this and

letting me share.

>> You won't believe this CEO's revenue.

Click here to watch the next episode

right now.
