# How AI Agents Run My SaaS (OpenClaw/Hermes)

- Channel: Simon Høiberg
- Video URL: https://www.youtube.com/watch?v=RP1k5QN1TYw
- Publish date: 2026-06-08

## Transcript

First it was an AI agent, then cloud

code, and now tools like Open Claw and

Hermes. AI agents are moving from simple

automations and coding assistance into

something much, much bigger. Systems

that can actually run your business.

And yet, I see people ask again and

again, what do you actually use these

systems for? I run multiple SaaS

products, and over the past months, Open

Claw has become a huge part of how I run

my business. And in this video, I'll

show you five ways I use it as a SaaS

founder that has completely [music]

changed how I run my business. So, first

of all, not surprisingly, I use it to

code.

I'm shipping around 5,000 lines pretty

consistently every single day. But not

only do I not write code anymore at all,

I barely ever open VS Code or any other

code editor for that matter. Instead, I

use Telegram to talk to my agent through

voice, and he does all the coding while

I come with inputs and we brainstorm and

iterate together. By the way, I have a

small team of AI agents now, each with a

name, profile image, designated role,

and so yeah, I use he and she when I

talk about them now. It just feels kind

of weird saying it at this point.

Anyway, using AI for coding isn't really

new, but this particular style of

working is different. My Open Claw setup

is installed on a Hetzner dedicated

server. I pay around $29 a month for it,

and it has a good amount of both RAM and

space on it, so I can have my agents

clone down a bunch of repositories,

easily work cross-repo, and spin up the

development server there, and then

tunnel back localhost to my laptop so I

can see the results in my browser as

he's working. In this way, I can see

what's going on, but I don't have to

keep my laptop on. I can easily change

to mobile if I'm on the go, and it's

just also much better for battery and

performance since my laptop doesn't need

to run the heavy local dev server. And

my agent isn't interrupted by where I am

or what else I'm doing. It's just a much

nicer way to work than sitting with a

code editor open, even if it has cursor

or AI copilot or whatever doing things.

Of course, we still have proper QA

process in place, and we have a separate

development and staging environment. So,

even though I don't review every single

line of code my agent writes anymore, I

still do QA and test things thoroughly

before pushing it out to production and

out to all my users. The next thing I

use it for is system and product

monitoring. So, as you may already know,

last year I moved my entire SaaS

portfolio off the cloud, which means I

moved it away from AWS to instead run on

a fully self-hosted setup using

Kubernetes on Docker and bare metal

servers that I rent with Hetzner. It's

saving me tens of thousands of dollars

every year. It's faster, it's more

robust, and I'm less locked in by

specific vendors. And it's just a huge

overall win that I recommend everyone

else to strongly consider. One downside,

though, is that it can make you a little

worried and have to sleep a little less

at night, especially in the beginning

when the Grafana dashboard and

Prometheus logs look very scary and

overwhelming if you're not used to it.

So, what I did is give my open core

agent direct read-only access to both

Grafana and the servers which my

Kubernetes cluster runs on. Turns out,

AI is really good at gathering a ton of

system logs, reading a ton of stats, and

running a bunch of kubectl commands

really quickly, and making sense of it.

So, I have my agent watch my cluster

around and as soon as something looks

abnormal, he super duper quickly

troubleshoots it, finds the root cause,

figures out if it's serious, and

escalates it to me through Telegram if I

have to do something. And in the past 6

months or so, we've had more or less

zero downtime. AI is just really good at

staying on top of all the critical infra

and making sure everything is running

smoothly. The third thing I use it for

is support.

So, we keep all customer conversations

in Aircall, which is one of the tools I

run in my portfolio. It's an AI-powered

support platform with knowledge bases,

chatbots, inboxes, and most importantly,

a public API.

So, my Open Thought team can completely

control and inspect our support setup

through Aircall. And this is where it

gets really useful because support is

almost never just the ticket itself. If

a customer writes in, I don't want to

only know what they wrote. I want to

know who they are, what plan they're on,

what they've tried to do, whether they

hit an error, whether they opened

similar tickets before, and if something

changed recently in the product. That

context lives in a bunch of different

places. Aircall, Stripe, the database,

Grafana, logs, previous tickets,

sometimes even the code base or

documentation. So, when something gets

escalated, I can ask Open Thought to

investigate the whole thing. It can look

up the user in the database, read the

conversation in Aircall, check recent

logs, compare to other tickets, and give

me a short explanation of what probably

happened. And you have no idea how much

time this saves me. Instead of me

opening six tools to understand one

ticket, the agent can give me the full

picture in one place. Not just what the

customer said, but what actually

happened around the account. Support

used to be this daily, almost hourly

thing I had to mentally keep track of

just to make sure all important customer

issues were handled properly. Now it

feels much less mentally exhausting and

our users get proper help much, much

faster. We actually surveyed users after

we started using AI for support in this

way, and support satisfaction has gone

up noticeably since we started doing

this. The fourth thing I use it for is

content. So, I run a lot of content

through Feed Hive, which is another tool

my team and I run. It's a social media

automation tool, and it's where we

create posts, plan the calendar,

schedule content, review drafts, and

reply to comments. And we recently

launched an official Open Floor skill

for FeedHive, so my Open Floor team can

control the whole workflow directly

through FeedHive. It can create drafts,

upload media, add labels, check what's

already scheduled, and plan posts into

the right slots.

But the useful part is not just that it

can call an API. The really useful part

is that it can sit across the whole

content process. I can start with a

rough idea, a voice note, a screenshot,

a comment from someone, or something we

talked about earlier, and my content

agent helps turn that into an actual

piece of content. In fact, one of my

favorite ways to create content now is

to just bring my phone with me on a nice

long walk here in the Swiss mountains,

then just talk for

30 minutes straight and send that as a

voice note in Telegram. My agent then

takes all of this yapping and structures

it and turns it into content. He creates

graphics using Remotion, prepares the

asset, and puts the whole thing into

FeedHive for me to review. And I also

don't have to manually carry all the

small operational pieces around in my

head. What did we post last week? What

is already scheduled? Does this need a

graphic? Should this be a carousel? Is

this more of a quick hit? Which account

did it go to? All of that stuff just

piles up. So the AI doesn't replace the

thinking. The ideas still come from me,

but it removes a lot of the friction

between having an idea and actually

getting it out there. And the final

thing I use agents for is running ads.

Because running ads is messy. The ad

platforms have terrible interfaces. The

numbers never tell the whole story, and

the real work is connecting all the

pieces. What did Meta report? What did

Google report? How many people actually

started a trial on Stripe? Did they

activate? And are they using our tool or

just sniffing around? And then there's

the harder part, deciding what to

promote, what to kill, and what to

ignore. Sometimes a creative you really

liked just doesn't perform. Sometimes a

campaign looks good in the ad platform,

but the users are low quality. And

sometimes the platform is basically

rewarding garbage because it optimizes

for the wrong event. So, I use Open Claw

to do the boring but important work

around paid acquisition. For example,

with Feed app, we've used it to compare

Meta ads against Google search and PMax

and then find the garbage search terms

and negative keywords. Check whether

specific ads are getting real signal and

separate what looks like curiosity

sign-ups from real sign-ups from users

that seem to have a real problem they

want to get solved. That second opinion

is incredibly valuable. Not because the

AI magically knows everything, but

because it doesn't get emotionally

attached to a campaign or landing page

version or a piece of creative. And

honestly, just being able to tell my

agent to raise a budget or pause a

campaign without having to go through

the miserable little ceremony of having

to click around Meta's ad manager. So,

five highlights I wanted to bring here,

but I already use it for at least like

25 other things. It's slowly taking over

my [music] entire company and big parts

of my personal life, too. And I want to

push it even further. Are you using it?

And what are you using it for? Please

share with us in the comments and I'll

talk to you there.

See you.
