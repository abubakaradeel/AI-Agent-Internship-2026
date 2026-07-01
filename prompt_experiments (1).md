# Prompt Engineering Experiments

**AI Agent Fellowship 2026 — Track 2**
**Author:** Abubakar Adeel
**Model:** Llama 3.3 70B (via Groq)

Five prompt engineering techniques, each with the prompt, the output, what I noticed, and how to improve it. All were run through my AI Workspace app.

## Experiment 1: Role Prompting

Give the model a persona so its tone and depth match a certain kind of expert. This is done through the system prompt.

**Prompt**
System: `You are a primary school teacher who explains things to 10-year-olds in simple words.`
User: `What is electricity?`

**Output**
> Electricity is a kind of energy that makes things work, like your lights or your video game. Think of it like water flowing through a pipe, but instead of water, tiny bits called electrons flow through wires and carry energy. When you switch on a light, those electrons rush to the bulb and it glows.

**Observations**
The persona clearly changed the answer. It used simple words and an everyday comparison (water in a pipe). Without the role, the same question gives a dry, technical reply full of terms like "potential difference."

**Improvements**
Add limits like "keep it under 4 sentences" to make it tighter and more consistent.

## Experiment 2: Chain-of-Thought Prompting

Ask the model to reason step by step before answering. This improves accuracy on problems that need logic or calculation.

**Prompt**
`A shop sells pens at 15 rupees each. I buy 3 and pay with a 100 rupee note. How much change do I get? Think step by step.`

**Output**
> Step 1: 3 pens cost 3 x 15 = 45 rupees.
> Step 2: 100 - 45 = 55 rupees.
> Final answer: 55 rupees change.

**Observations**
Adding "think step by step" made the model show its working, which is easy to trust and check. On harder problems this also makes it more accurate, because it solves one piece at a time instead of guessing the end.

**Improvements**
Ask it to put the final answer on its own labelled line so it is easy to spot.

## Experiment 3: Few-Shot Prompting

Give the model a few examples of the pattern you want, so it copies that pattern for a new input.

**Prompt**
```
Classify each sentence as Positive, Negative, or Neutral.

"The food was delicious." -> Positive
"My order was wrong again." -> Negative
"The package arrived Tuesday." -> Neutral
"The screen is bright but the battery drains fast." ->
```

**Output**
> Negative — the complaint about the battery outweighs the praise for the screen.

**Observations**
The three examples taught the task and the format without any long explanation. The model followed the pattern correctly on the new sentence.

**Improvements**
Add a mixed example too, so the model learns exactly how to handle sentences that have both good and bad points.

## Experiment 4: Structured Output (JSON)

Tell the model to reply in strict JSON so another program can read the answer automatically.

**Prompt**
`Return ONLY valid JSON with keys name, age, city. No extra text. Text: "Ahmed is a 27-year-old engineer who lives in Lahore."`

**Output**
```json
{ "name": "Ahmed", "age": 27, "city": "Lahore" }
```

**Observations**
The model returned clean JSON with the right values and no extra words. The key instructions were "return ONLY valid JSON" and "no extra text" — without them models often wrap it in a sentence, which breaks any program reading it.

**Improvements**
Give an example of the exact JSON shape in the prompt to make the format even more reliable.

## Experiment 5: Prompt Optimization

Take a vague prompt and rewrite it to be specific and clear, then compare the results.

**Weak prompt**
`Write about renewable energy.`

**Optimized prompt**
`Write a 100-word summary of the three most common types of renewable energy for a high-school student. Use simple language and give one real example for each.`

**Output (optimized)**
> Renewable energy comes from natural sources that never run out. The three most common types are solar, wind, and hydro. Solar uses panels to turn sunlight into electricity, like rooftop panels. Wind uses turbines that spin in the wind, like wind farms in open fields. Hydro uses moving water from a dam, like the Tarbela Dam. All three are clean because they do not burn fuel.

**Observations**
The weak prompt gave a long, unfocused essay. The optimized one controlled the length, the audience, the structure, and the examples, so the result was focused and useful. The clearer the prompt, the closer the output matches what you want.

**Improvements**
Specify the output format too, like one line per energy type, to make it even more structured.

## Summary

| Experiment | Technique | Takeaway |
|---|---|---|
| 1 | Role Prompting | A persona shapes tone and depth. |
| 2 | Chain-of-Thought | "Think step by step" makes it accurate and clear. |
| 3 | Few-Shot | Examples teach the pattern better than a description. |
| 4 | Structured Output | Strict JSON makes output machine-readable. |
| 5 | Prompt Optimization | Specific prompts beat vague ones. |

The main lesson across all five: clear, specific, well-structured prompts give better and more reliable results.

*Abubakar Adeel — AI Agent Fellowship 2026, Week 1.*
