# Assignment 6: Builder Journal

## Why did you choose AI Engineering?

I chose AI Engineering because I wanted to move beyond just using AI tools as a consumer and actually understand how to build with them. I'm drawn to the idea of creating things that solve real problems — not just writing code, but combining APIs, models, and interfaces into products people can actually use. AI Engineering felt like the right path because it sits at the intersection of practical software development and the fast-moving world of AI, and I wanted to be someone who builds with these tools rather than just talks about them.

## What type of AI products do you want to build?

I'm most interested in building lightweight, functional AI-powered applications — the kind of tools that take a genuinely useful idea and turn it into something people can interact with quickly, like dashboards, assistants, and internal tools. Right now I'm especially interested in products built with Streamlit, since it lets me focus on the logic and the AI integration without getting stuck in heavy frontend work. Longer term, I want to build products that combine simple, clean interfaces with real intelligence underneath — things like automation tools, data-driven assistants, and apps that make everyday tasks faster.

## What was your biggest learning this week?

My biggest learning this week was how much you can accomplish with Streamlit once you understand its basic building blocks. Instead of jumping straight into writing code, I started by going through the official Streamlit documentation first — reading through the core concepts like widgets, layout, and session state before touching my editor. That approach really paid off. It meant that by the time I started coding, I wasn't guessing at syntax; I already had a mental map of how the pieces fit together. It reinforced for me that reading documentation first, even when it feels slower, actually speeds up the building process later.

## What challenges did you face?

The biggest challenge I ran into was connecting my app to an API. When I first added my API key, my requests kept failing with authentication errors, and it took me a while to realize the issue wasn't with my code logic at all — it was with the API key format itself. I had assumed the key needed dashes and could include uppercase characters, but the actual key required no dashes and had to be entered in lowercase. It was a small formatting detail, but it cost me a good chunk of time before I caught it.

## How did you solve them?

I solved it by slowing down and going back to the documentation instead of assuming I knew the correct format. I compared the example key format shown in the docs directly against the key I was using, character by character, which is how I noticed the dash and casing issue. Once I corrected the key — removing the dashes and converting it to lowercase — the API calls started working immediately. This also pushed me to add better error handling in my Streamlit app, so that if a similar issue comes up again, the app will surface a clearer error message instead of a generic failure.

## What are your goals for Week 2?

For Week 2, my goals are to:

- Get more comfortable with Streamlit's more advanced features, like session state and caching, so I can build slightly more complex, multi-step apps.
- Build a small end-to-end project that combines a Streamlit frontend with a real API integration, applying what I learned this week about careful setup and documentation-first learning.
- Get faster at debugging API and environment issues by checking documentation and key formats early, rather than assuming defaults.
- Start thinking more seriously about what specific AI product I want to prototype next, so Week 2 isn't just about learning tools but about applying them to something real.
