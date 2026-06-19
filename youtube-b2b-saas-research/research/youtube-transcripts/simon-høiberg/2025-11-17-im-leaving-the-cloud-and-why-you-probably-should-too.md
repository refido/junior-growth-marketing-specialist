# I'm leaving the cloud! (...and why you probably should too)

- Channel: Simon Høiberg
- Video URL: https://www.youtube.com/watch?v=tWz4Eqh9USc
- Publish date: 2025-11-17

## Transcript

Until recently, all of my SaaS products

were running entirely on AWS.

But at the beginning of this year, I

started moving everything to run on

dedicated bare metal servers hosted by a

small German company called Hetzner.

80% of my systems now run on dedicated

servers using open source software with

only about 20% left in the cloud. And

this has been a truly pivotal moment for

my business. Not only did I see a

dramatic cost reduction, but my products

also run faster. My team and I deploy

new features faster, and it's opened new

business opportunities I wouldn't

otherwise have. But moving off the cloud

certainly comes with downsides as well.

So, the question is, was it worth it?

And should you take your SaaS off the

cloud and start self-hosting, too? In

this video, I'll share the top three

reasons why I'm moving off the cloud.

I'll show you my exact self-hosted

setup, and I'll share which services I'm

keeping on AWS and probably won't ever

self-host. If you're new to this

channel, welcome here. My name is Simon

Høiberg, and I run a SaaS portfolio of

five SaaS tools, which is used by more

than 50,000 users and is about to hit $2

million in ARR this year. And before we

get into the reasons why I chose to move

these tools off the cloud, let's just

get a quick overview of how this new

setup looks. So, this is how I used to

run my products. I would use ECS,

Fargate, and Lambda functions to run all

of my code. I would use AWS Amplify to

host my apps. I would use DynamoDB to

store all of my data. I would use SQS to

run my message queues, and I would use

CloudWatch to monitor the systems and

access logs. And I don't think I have to

sell you the benefits here. All of this

is entirely managed by AWS. I don't have

to worry about where and how this runs.

I just know that it runs. And AWS will

bill me for my exact usage. So, I'm

billed for exactly how many milliseconds

my code takes to execute, how many times

I read or write to my database, for how

long I store my logs, and so on and so

on. Now, let's take a look at the new

setup.

I now have three dedicated servers with

Hetzner.

All my code now runs in Docker

containers and is managed by Kubernetes.

I use Postgres to store my data. I use

Redis for caching. I use BullMQ to run

my message queues, and I use Grafana and

Prometheus to monitor the systems and

access logs. And the pricing model here

is completely different from AWS.

Kubernetes, Postgres, Redis, BullMQ, and

Prometheus are open source and free.

Grafana has a free community edition,

and it offers more than enough. So, the

only thing I pay for are the three

dedicated servers I have with Hetzner.

And this comes with a low, fixed monthly

cost. On the other hand, I now need to

manage all of this myself. So, this is

what I mean when I say we're leaving the

cloud. I know I'm using the word a

little loosely here. We're still renting

servers at a data center, so we're not

really self-hosting as in we have our

own servers in our own house. So, what I

mean is that we're moving away from

managed serverless infrastructure and

instead managing our own dedicated

servers. So, why would I make this

decision?

Well, it probably won't come as a huge

surprise that one of the top three

reasons is cost.

At the beginning of 2025, I would pay

AWS $7,800 per month on average to run

my SaaS products. Because I pay per

usage with AWS, this average is slowly

climbing month after month as my user

base grows. After moving more than 80%

of my infrastructure to run on dedicated

servers, this cost is now below $2,000

per month, and it's likely to go even

further below $1,000 per month as we're

wrapping up the last migrations. The

cost of running my service on Hetzner

itself is around $200 per month. The

rest of the cost is the remaining 20% of

infrastructure I still run on AWS. And

that sounds amazing, right? We can save

money. But in all fairness, let's just

get a bit of perspective. My products

are generating more than $100,000 per

month. Is $7,800 for the servers really

that big of a deal? And what about all

the time I've spent this year migrating

all of these systems from AWS to Hetzner

and having to learn about Kubernetes,

Docker, and basic system admin stuff,

which was all pretty new to me. If I

factor in the time spent, is there

really that big of an ROI here? Is this

actually a financially sound decision?

Well, let's take a look.

The time I spent doing

infrastructure-related stuff absolutely

spiked at the beginning of this year

compared to the previous years on AWS.

This was valuable time I could have

spent marketing, growing, and improving

my products instead. However, as I

started to learn and as AI got better at

helping me, the time spent on this type

of work slowly came back to more

reasonable levels. And while the whole

promise of the cloud is to manage

servers for you, time spent on dealing

with AWS infrastructure still isn't

zero. In fact, it can get very complex,

and there's certainly a learning curve

here as well. So, now, after an

adjustment period, the time I spent

dealing with infrastructure is back to

the same levels, if not even less than

it was before. And assuming it's going

to stay that way, the money I save on

this is going to increase month after

month after month without a ceiling. So,

yes, unless you're already expert on

this, there's obviously going to be an

upfront cost in terms of time spent. But

that upfront cost is fixed. And I have a

feeling that most people who are afraid

of going self-hosted thinks that the

effort it takes to maintain this somehow

stays up here, all in the red.

In my experience, it really doesn't. The

cost savings, on the other hand, are

potentially unlimited and will just keep

going up. So, one thing is the cost

savings, but there's another, and to me,

much more important reason. All of those

services I mentioned, DynamoDB, Lambda,

Fargate, and so on, they're all really

good, robust, battle-tested products. In

terms of performance and reliability,

they're great, and I honestly think

their pricing is pretty fair. But

they're all AWS services. They don't run

anywhere else. If AWS were to raise

their prices or decide they don't want

you as a customer anymore, well, you're

cooked. Your products just stop running,

and migrating isn't something you can do

quickly. It requires careful planning,

and if you're forced to do that in a

rush, yeah, that might mean your whole

business goes in the dumpster. Honestly,

users aren't going to wait around. It's

what we call a vendor lock, and it's

absolutely something you should avoid.

It's not in the interest of AWS or Azure

or Google Cloud Platform to have you

easily leave. And this is probably the

biggest reasons to consider leaving the

cloud. I'm super happy using Hetzner to

run my infrastructure, but with my new

setup, I can run it just about anywhere.

Any hosting company that offers a VPS or

a dedicated server can run my products.

I'm not locked in in the same way. And

I'm being a little bit crazy, but to

really hammer this point home, I

actually ran one of my products for two

whole days on these three Raspberry Pis

right here in my office. Now, that's not

ideal. The internet here isn't fast

enough, and I kept hitting memory

issues, but I did this with a smaller

product of mine, and I honestly don't

think any of my users even noticed. And

I did this for fun, but also because it

was satisfying to prove to myself that

my products really can run anywhere

using this setup. I wouldn't recommend

using Raspberry Pis for this, obviously,

but I absolutely would recommend

removing as many hard dependencies on

specific vendors as you possibly can.

There's just something about that

feeling that you own your setup fully.

Now, after moving off AWS, I still have

at least two major dependencies left,

Stripe and OpenAI. But I am actively

looking into how I can mitigate this,

too. I'm looking into Coinbase as an

alternative payment method, and I'm

experimenting with running our AI on

dedicated GPU instances from more

independent vendors. It's not a simple

task, though. And the last reason for me

to move off the cloud is, I would say, a

little bit more specific to my

situation, but something you probably

could consider for your products, too.

It has to do with how my products are

offered. As I mentioned earlier, I run a

portfolio of SaaS products, and they all

come with a monthly or yearly

subscription. But at the same time, I'm

also selling access to all five tools on

a lifetime deal.

This means that you can pay once and

then use the tools forever. And selling

something for a one-time purchase that

has ongoing, rising cost is obviously

super problematic. Selling software on a

lifetime deal, which have ongoing

operational cost, is totally possible,

but if you can at least make those

ongoing cost fixed instead of gradually

rising as the number of users goes up,

it's obviously going to be much easier

and much less risky to do proper

financial planning when offering a deal

like this. And at the same time, I do

have users asking, "How can you

guarantee that you can keep running this

business, and what happens to our

so-called lifetime deals if your

business goes down?" And it's a totally

legitimate question that I currently

have a hard time giving a good answer to

other than, "Don't worry, my business is

doing well, and it's not going to go

down." That's obviously not a very

satisfying answer, and for that reason,

I'm working on making all of my products

fully self-hostable. So, everyone who

bought lifetime access to my software

can, in the unlikely event that my

business won't be able to host it,

simply install it on their own servers

and host it themselves. This is the best

way I can guarantee that lifetime access

really does mean lifetime access. All

right, so we talked about the reasons

why I'm doing this, and we talked about

the setup. But as I mentioned, I still

have 20 or so percent of my

infrastructure that still runs on AWS,

and I'm actually not sure if I can ever

get these migrated, but let me share

what they are and what I've tried so

far. So, first of all, storage. I use S3

for this and it was rather difficult to

find a good replacement. Hetzner now has

storage buckets and I know Cloudflare

has something called R2, which is their

version of S3. Both of these are S3

compatible, which means that they use

the same API structure as S3. They're

also both a fair bit cheaper than S3,

honestly, the cost of storing data on S3

isn't really that big of an issue. It

actually doesn't cost that much. My main

issue here is, again, the vendor lock.

And neither Hetzner's or Cloudflare's

solutions are going to solve that. They

lock me in just as much. And so, this is

when I heard about MinIO, which is an

open-source S3 compatible object store

that you can install on your system and

host yourself, which sounds perfect. So,

my approach was to order a 15 TB hard

drive with Hetzner and have them attach

that to the main dedicated server and

then use that with MinIO. And actually,

it

worked, kind of. But it got a bit

complicated to deal with backups and the

way MinIO is built is kind of meant to

be using a distributed system. So,

ideally, you would need to have multiple

of these hard drives for each node in

your system and yeah, it got a bit

complex and it wasn't very stable.

Probably a skill issue, but I went back

to S3. The next one is user

authentication. This whole time I've

used Cognito user pool at AWS, which is

similar to Auth0. Basically, a service

that allows you to handle user

authentication with all the security

built in. This is a highly sensitive

point due to security, so it's one of

the areas where you really should be

cautious. I tried one open-source

alternative, which I believe is the only

one really and it's called Keycloak. And

I'm sure it's great. It's just I think

this was done by some pretty hardcore

Java developers and both user experience

and developer experience was so bad. And

since this is such a critical point in

any system, you really don't want to

mess this one up. So, I simply chose to

go back to AWS and continue using

Cognito. And finally, I use AWS

CloudFront as the public entry point,

which proxies all requests to my Hetzner

servers. So, that means that all

incoming traffic to my Hetzner server is

protected by default and has to go

through CloudFront. And that's simply

because CloudFront offers a lot of

security, firewalls, DDoS prevention and

a lot of other things I wouldn't know

exactly how to install myself. And for

now, we still rely on services like

OpenAI, Replicate and Vesta AI to run

anything related to AI. Though, I'm

really hoping standalone servers will

soon come with the GPU power needed to

offer reliable AI inference in a

self-hostable way. If you have a lot of

experience with this, I would love to

get your recommendations in the comments

below. How would you approach getting

these last 20% off the cloud or is it

even doable? Please, share your take.

I'm very eager to learn more about this

and see if it's possible to stretch it

even further than I've done already.

Now, the biggest question is, should you

move away from the cloud and build your

next product off the cloud? Well, I

think it depends on where you're at. If

you're here, building a small hobby

project and you don't expect it to

become much more than a hobby project,

then you should stay on the cloud. Use

Vercel, Netlify, lovable or any of these

one-click deploy types of tools. If

you're here, on the other end of the

spectrum and you're expecting to build a

really big business that needs very

serious scaling capabilities or a

business that is absolutely

mission-critical to your users, then

using a managed hyper-scaler platform

like AWS is the way to go. But if you're

anywhere on here, somewhere in the

middle, it makes perfect sense to

consider leaving the cloud and using

dedicated servers instead. It is

absolutely doable to manage your

infrastructure yourself and there is

serious money to be saved here. Now, one

thing is the tech stack that powers your

product, but another huge win from

running on prem is that you get to

benefit from some of all the amazing

open-source tools that you can use

internally to run your business. I have

a video where I break down how I was

able to save another $10,000 per year by

replacing some of my most expensive

tools with self-hostable alternatives.

You can watch that one right here.
