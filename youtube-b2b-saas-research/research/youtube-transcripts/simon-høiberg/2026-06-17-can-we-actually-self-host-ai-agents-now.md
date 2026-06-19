# Can we actually self-host AI agents now?

- Channel: Simon Høiberg
- Video URL: https://www.youtube.com/watch?v=uFlKV0AiaIQ
- Publish date: 2026-06-17

## Transcript

Mac minis, DGX Spark, and small local AI

setups. It seems like this is the next

natural evolution of AI, and I get it.

The idea that you can run your own

models, keep your data under your own

control, and stop sending [music] every

prompt, file, log, and customer

conversation to some black box API is

obviously super appealing. And people

make this look incredible. Easy to set

up, relatively affordable, and with

almost unlimited upside. But, we need a

reality check. Cuz there is a big

difference between running a model

locally and running a useful AI agent.

So, in this video, I'm testing where

self-hosted agents are today, what is

actually useful, what is worth the

tradeoffs, and what it really takes to

run a frontier open weight model fully

self-hosted. The first thing worth

understanding is that self-hosting AI is

not one thing. It's a spectrum.

On one end, you have tiny local models

running on consumer hardware. A Mac

mini, a gaming PC, maybe a single

consumer GPU. And it's awesome that you

can already do that. I like that it

exists, but for real agentic work, it's

mostly just not good enough. It might

feel impressive at first, but once you

ask it to use tools, keep track of

context, recover from mistakes, and

actually complete a useful task, it

starts falling short. On the other end,

you have the real frontier models, the

latest GPT and Opus class models. These

are the models that make agent workflows

feel magical. But, they're not open

weight, and even if they were, they are

so incredibly resource greedy that you

couldn't reliably self-host them even on

the most expensive hardware you can get

access to.

The useful area is here, in the middle.

Open weight models that are big enough

to be useful and still possible to run

on rented infrastructure. And the good

news is, there are several services out

there already that let you rent

infrastructure with access to some

serious hardware. A100s, H100s, and

other data center grade GPUs that can be

used to run serious models. One of these

services is Vast AI.

Let's have a look.

Vast public pricing gives you a rough

mental model.

A 4090 can be around 29 cents per hour.

An A100 around 67 cents per hour. And an

H100 around a dollar and 50 cents an

hour.

The exact numbers move around, but this

is currently the ranges you can expect.

Cheap consumer-ish GPU, serious 8 GB

data center GPUs, then high-end H100

territory. So, if you want serious work

done, we have to stop thinking about Mac

minis and instead consider a rented GPU

box where you can run the model

connected to something like Open Claw

and get an agent that is actually

useful. That's the version I care about

testing. So, first of all, I don't

really care if a model gets a good score

on some leaderboard cannot function

inside an agent workflow. For Open Claw,

there are a few things that matter a

lot. First, tool use. Can it call the

right tool at the right time with the

right arguments and understand what came

back? That sounds basic, but this is

where weaker models get exposed

immediately. Second, context. For normal

chatbot, you can get away with a smaller

context window, but for an agent,

context disappears fast. You have

instructions, tool schemas, previous

messages, file contents, command

outputs, errors, and then the actual

task on top of all that. For Open Claw,

I would treat a 16K token window as the

absolute floor. Not ideal, just the

floor where you can begin to do

something meaningful. More is obviously

better. And then there's quantization.

So, quantization is basically

compression for model weights. Instead

of storing the model in high precision,

you store it with fewer bits so it uses

less VRAM and can fit on cheaper

hardware. That sounds great and

sometimes it is, but the trade-off is

quality. If you squeeze too

aggressively, the model can get worse at

following instructions, using tools, and

stay coherent across longer tasks. For a

normal chatbot, that might just mean a

slightly worse answer, but for an agent,

it can mean the workflow breaks, it

calls the wrong tool, misses an

instruction, or forgets context or

confidently continues down the wrong

path. That is why I care about the full

setup here. Model size, quantization

level, available VRAM, and how much

context we can actually allocate after

the model is fully loaded. Cuz we need

to fit all of this into the memory

that's available on the GPUs we use. The

first model we'll try is Qwen 3.6 35B

A3B. This is the smallest model in the

test, but it's not a toy model. It's

small enough that you can realistically

rent hardware for it without immediately

doing into prize math. But it's also big

that it has a real chance of being

useful inside an agent. On vast, the

realistic starting point for this class

of model is something like a high VRAM

consumer or workstation GPU. When I

checked, a single RTX Pro 6000 class

machine with 96 GB of VRAM was about $1

an hour. And that sounds cheap until you

multiply it out.

If you leave it running constantly, that

is roughly $700

per month. And that is before you start

thinking about storage, bandwidth,

mistakes, and so on. You can find

cheaper machines and you can obviously

shut it down when you're not using it,

but this is the first real pricing

reality check. $700 a month if you rent

it is the starting point for anything

useful. So, here in templates, I'll make

sure to pick the Ollama image.

And I want to set the container size to

150 GB.

Up here, we can filter to only get the

RTX Pro Blackwell series.

And we'll pick one with 96 GB of VRAM

available.

Now, it's going to show up here under

instances.

And once it's ready, we can open it here

and we'll get to this nice web UI.

Let's open the Jupiter notebook here.

Now, we can pull the model we want from

here.

There we go.

And this is going to take a few moments

to download the model.

And now we run it.

Awesome. The model itself is now loaded

and ready.

Next, let's set this up with Open Cop.

So, I'm assuming you already have an

Open Cop agent set up, so I'll just show

you how to configure it to use the

self-hosted model.

Back in the Ollama dashboard, let's

expand the advanced option under the

Ollama API and click copy URL.

This URL has two parts,

the base URL and the token.

We'll use both of these to set up Open

Cop, but we'll use them separately.

So, on your Open Cop instance, let's set

up a new model.

Pick

custom provider

and add the first part of the URL here

plus the path v1.

Then we'll paste the token as an API key

here.

And this would be the second part.

And we'll select OpenAI compatible.

And we'll put the model ID here.

Perfect. And we'll just use the one that

suggests here, and I'll give it the

alias Quinn.

Now, let's talk to our new model.

In Telegram or whatever you use, let's

just verify by running the status

command.

Looks good.

Now,

let's talk.

Nice.

Perfect.

But we don't want to just talk. We want

to see if it can behave like an agent.

I'll give it a simple task first. Read a

Notion page and summarize the key

points.

Okay.

There we go. All right.

And let's push it a bit further.

Good.

So, it handles web search, tool calling,

and gets the job done. It even handles

Notion's messy block format through the

API very well. So, I actually tried

using this for a week or so, and my

honest take, this is where self-hosted

agents start becoming real, but not

where it becomes effortless. The

benchmark numbers are decent for a model

this size, but the practical experience

is still lacking. It's great for drafts,

structured summaries, internal analysis,

and some tool workflows where the task

is clear. But when the task got messy,

ambiguous, debugging multi-step product

decisions, or anything where the model

had to recover from its own wrong turn,

it still felt lacking, especially on

longer, more iterative tasks with a lot

of back and forth, it just starts losing

track of what it's doing pretty fast.

The verdict is Qwen is the practical

entry point. It's not too bad and this

model can actually run on hardware you

can rent for bootstrap founder money.

But if you're used to GPT 5.5 or Opus

level agents, you're going to need

patience. It's just quite far from that

level still.

The second model we'll try is Minimax

M2.7.

This is where we move into the serious

middle tier. Not small anymore and

definitely not obviously cheap anymore.

Minimax is interesting because it's very

clearly aimed at complex agent work.

Building agent harnesses, coding, log

analysis, log troubleshooting,

production incidents, tool use, and long

multi-step productivity tasks. And

that's great. But the question is, what

machine do I need to rent and what does

it cost? This tier, the search starts

getting

a bit uncomfortable. Minimax own

deployment guide documents a 4 GPU VLLM

setup and it says the model needs around

220 GB just for the weights. So this is

where we move into machines like 4x

A100s. When I checked, 4x A100 80 GB

machines were roughly $3 an hour on the

cheaper end. That is around $2 to $3,000

a month if it runs constantly. And at

this point, context size and cache also

start becoming a part of the

calculation, not just whether the

weights fit. This is the moment where

self-hosting stops feeling like a cool

hacker setup and starts feeling like

infrastructure planning. So let's raise

this to 500 GB and we'll change the

template's image to VLLM here.

Then let's go and filter for these GPUs

here. We limit to A100 series.

We'll pick a 4x A100 with GB VRAM. And

again, we go to the instance and wait

for the box to spin up.

Just like before, we get to the web UI

and we can set up Minimax. Again, let's

open Jupiter and install the model.

This model is huge, so it's going to

take a while, but we'll just let it run.

After it's finished and running,

configuring it with Openclaw is exactly

the same way as we did in the previous

step. Now, let's test it out.

This time I care less about whether it

can produce a nice answer once and more

about the behavior over longer task.

Tool use, recovery, staying on track,

not making weird assumptions, not

collapsing when the task gets annoying.

Yeah.

Now we're talking. This model can handle

a task with a mix of a bunch of things

and it actually does it really well. So

yes, this truly is much closer to the

kind of model I would want inside

Openclaw. The upside is that it's much

better at staying on a task, working

through tool results, and handling

ambiguous engineering-style workflows.

But the downside is the price. At

several thousand dollars a month, this

only makes sense if the agent is doing

real work often enough to justify the

machine. So, my verdict is Minimax is

the first model in this test that feels

like a serious self-hosted agent model,

but it is also where self-hosting stops

being lightweight. If the workflow is

valuable enough, coding agents, internal

automation, repetitive private

operations,

it can make sense. But again,

as long as OpenAI and Anthropic are

subsidizing the inference cost with

their Pro and Max subscriptions, it's

just very hard to justify paying several

thousand for this setup when you can get

away with closer to two or 400 a month

with OpenAI. The final tier is GLM 5.1

and Kimi K 2.6.

This is the extreme end of the test. GLM

5.1 is an open-weight model that is

built very explicitly for a genetic

engineering. It is not just a chatbot

model, it is aimed at coding, terminal

task, repository level work, and

long-running tool heavy workflows. And

Kimmy K2.6 belongs in the same category,

a huge open weight agentic model. But,

the hardware side here is brutal. We are

looking at huge multi-GPU machines. For

GLM 5.1, the official local deployment

path points to VL

or SG Lang. And the setup is clearly in

the big multi-GPU territory. And when

you start looking at this tier on Vast,

the monthly number gets ugly very

quickly. Depending on the machine, you

can end up in five-figure monthly

territory if you leave it running

constantly. $30 per hour or $21,000 to

$28,000 a month if it's running

constantly. So, let's rent one of these.

And the setup here is the same as with

Minimax, it just takes much longer to

download and load it.

But, once it's connected to Open Claw,

let's give it a real challenge. I want a

task that takes time, uses tools, has

messy context, and forces the model to

keep working after the first obvious

answer.

And I'm not going to walk you through

everything I did here, but what I can

say is capability-wise, this is the

first tier where the self-hosted agent

stops feeling like a compromise and

starts feeling like a real serious

GPT-level replacement. I tried Kimmy

K2.6 on the same kind of hardware as

well, and the experience was honestly in

the same category. Very impressive, very

capable, and much closer to what I would

expect from a serious agent model. But,

the catch is impossible to ignore. The

price is simply insane. In the last few

months, I've been looking into starting

my own small sovereign compute site here

in Switzerland, and I've been looking

into acquiring this hardware and find a

colocation where I can set it up. But,

CAPEX is easily half a million dollars

in electricity cost alone. It's three,

four thousand dollars a month to run

these. Then you need to pay for a proper

co-location where they have ventilation,

cooling, the right power supplies, and

so on. It's

steep. So, my verdict is that GLM 5.1

and Kimmy K 2.6 show that self-hosted

agents can feel very close to the

frontier, but trade-off is also

impossible to ignore. This tier is just

too expensive to self-host for most

people. So,

what can we actually learn from this?

For me, it's pretty clear. We are close,

but we're not really there yet. If you

are founder right now, the biggest edge

is to put the frontier model to insane

use while the biggest AI companies in

the world are still subsidizing for you.

If a few hundred dollars a month gives

you a agent that can actually help you

code, investigate problems, write

research, monitor systems, and move the

business forward, that's not expensive.

That is probably one of the highest ROI

things you can buy right now. So, yes,

keep one foot in self-hosted models,

learn how they work, follow the

hardware, understanding the trade-offs,

because I do think we're moving in that

direction. But if you want serious work

done today, frontier models are still

the way to go. Practical setup right now

is probably hybrid. Use the best hosted

models for the work that really matters,

and start using self-hosted models where

privacy, control, and repeated narrow

workflows actually make sense.
