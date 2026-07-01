# Prompt Engineering Experiments

**AI Agent Fellowship 2026 — Track 2: NLP & AI Agents**
**Author:** Abubakar Adeel
**Model used:** Llama 3.3 70B (via Groq)

This report demonstrates five core prompt engineering techniques. For each one, the prompt, the output, observations, and possible improvements are shown. All examples were run through the AI Workspace app built for Assignment 3.

---

## Experiment 1: Role Prompting

**Technique:** Give the model a specific persona so its tone, depth, and focus match a particular kind of expert. The role is set through the system prompt.

### Prompt

System prompt:
```
You are a patient primary school teacher who explains things to 10-year-olds using simple words and everyday examples.
```
User message:
```
What is electricity?
```

### Output

```
Electricity is a kind of energy that makes things work, like the lights in your
room or your favourite video game! Think of it a bit like water flowing through
a pipe. Instead of water, tiny invisible bits called electrons flow through
wires. When they flow, they carry energy from one place to another. So when you
switch on a light, you are letting those little electrons rush through the wire
to the bulb, and the bulb uses their energy to glow. Pretty cool, right?
```

### Observations

The persona clearly shaped the answer. The model used simple words, an everyday comparison (water in a pipe), a friendly tone, and even a closing question, exactly how a teacher for children would explain it. Asking the same question with no role gives a drier, more technical reply full of terms like "flow of charge" and "potential difference."

### Improvements

The role could be made even sharper by adding constraints, for example "keep the answer under 4 sentences and avoid any scientific jargon." Adding an instruction like "end with a simple question to check understanding" would make the teacher persona more consistent across answers.

---

## Experiment 2: Chain-of-Thought Prompting

**Technique:** Ask the model to reason step by step before giving its final answer. This improves accuracy on problems that need logic or calculation, because the model works through the parts instead of guessing the end result.

### Prompt

Without chain-of-thought:
```
A shop sells pens at 15 rupees each. If I buy 3 pens and pay with a 100 rupee
note, how much change do I get?
```

With chain-of-thought (the improvement):
```
A shop sells pens at 15 rupees each. If I buy 3 pens and pay with a 100 rupee
note, how much change do I get? Think step by step before giving the final answer.
```

### Output

With "think step by step" added:
```
Step 1: Find the cost of 3 pens. 3 x 15 = 45 rupees.
Step 2: Subtract the cost from the money paid. 100 - 45 = 55 rupees.
Final answer: You get 55 rupees in change.
```

### Observations

On this simple problem both versions reached the right answer, but the step-by-step version showed its working, which makes the answer easy to trust and check. On harder, multi-step problems the difference is bigger, the plain version is more likely to make a mistake, while the step-by-step version stays accurate because it handles one piece at a time. Making the reasoning visible is the whole value of the technique.

### Improvements

For a cleaner result, the prompt could ask the model to show its reasoning and then put the final answer on a separate line labelled clearly, so the answer is easy to pick out. For very hard problems, asking it to double-check its own steps at the end would catch more errors.

---

## Experiment 3: Few-Shot Prompting

**Technique:** Give the model a few examples of the input-and-output pattern you want, so it copies that pattern for a new input. This works better than just describing what you want, because the examples show it directly.

### Prompt

```
Classify the sentiment of each sentence as Positive, Negative, or Neutral.

Sentence: "The food was delicious and the staff were kind."
Sentiment: Positive

Sentence: "I waited an hour and my order was still wrong."
Sentiment: Negative

Sentence: "The package arrived on Tuesday."
Sentiment: Neutral

Sentence: "The screen is bright but the battery drains too fast."
Sentiment:
```

### Output

```
Mixed (leaning Negative) — the sentence praises the screen but complains about
the battery, and the complaint is the stronger point.
```

### Observations

The three examples taught the model the format and the task without any long explanation. It correctly followed the pattern and gave a sensible answer for the new sentence. Interestingly it recognised the last sentence was mixed rather than forcing it into one bucket, which shows the model understood the intent behind the examples, not just the surface format.

### Improvements

If the goal is strictly one label per sentence, the examples should include a mixed case too, so the model learns exactly how to handle it (for example labelling it "Negative" or adding a "Mixed" category on purpose). More examples generally make the pattern more reliable, though too many waste tokens.

---

## Experiment 4: Structured Output (JSON)

**Technique:** Instruct the model to reply in a strict JSON format instead of free text, so another program can read the answer automatically. This is essential when the AI output feeds into other software.

### Prompt

```
Extract the details from the text below and return ONLY valid JSON with the keys:
name, age, city. Do not add any explanation or extra text.

Text: "Ahmed is a 27-year-old engineer who lives in Lahore."
```

### Output

```json
{
  "name": "Ahmed",
  "age": 27,
  "city": "Lahore"
}
```

### Observations

The model pulled the right values into the exact keys requested and returned clean JSON with no surrounding text. The two instructions that mattered most were "return ONLY valid JSON" and "do not add any explanation", without them, models often wrap the JSON in a sentence like "Here is the JSON you asked for", which breaks any program trying to read it.

### Improvements

For production use, the code reading this should still be wrapped in error handling in case the model occasionally adds stray text or a trailing comma. Providing an example of the exact JSON shape in the prompt (a mini few-shot) makes the format even more reliable. Some APIs also offer a dedicated "JSON mode" that guarantees valid JSON, which is safer than relying on the instruction alone.

---

## Experiment 5: Prompt Optimization

**Technique:** Take a weak, vague prompt and rewrite it to be specific and clear, then compare the results. This shows how much prompt wording affects output quality.

### Prompt

Weak version:
```
Write about renewable energy.
```

Optimized version:
```
Write a 100-word summary of the three most common types of renewable energy
for a high-school student. Use simple language and give one real-world example
for each type.
```

### Output

Weak version produced a long, unfocused, general essay with no clear structure or length, covering random points at whatever depth the model chose.

Optimized version produced:
```
Renewable energy comes from natural sources that never run out. The three most
common types are solar, wind, and hydro. Solar energy uses panels to turn
sunlight into electricity, like the rooftop panels seen on many homes. Wind
energy uses large turbines that spin in the wind to make power, such as the wind
farms found in open fields. Hydro energy uses moving water, usually from a dam,
to generate electricity, like the Tarbela Dam. All three are clean because they
do not burn fuel, which helps reduce pollution and fight climate change.
```

### Observations

The optimized prompt controlled four things the weak one left open: the length (100 words), the audience (high-school student), the structure (three specific types), and the requirement for examples. The result was focused, appropriately pitched, and useful, while the weak prompt gave a generic answer that could have gone in any direction. This is the core lesson of prompt engineering: the more clearly you specify what you want, the closer the output matches your intent.

### Improvements

The prompt could go further by specifying the output format, for example asking for a short intro sentence followed by one line per energy type, to make it even more structured. Adding a tone instruction ("friendly and encouraging") would tailor it further for the student audience.

---

## Summary

| Experiment | Technique | Key Takeaway |
|---|---|---|
| 1 | Role Prompting | A persona shapes tone, depth, and vocabulary of the answer. |
| 2 | Chain-of-Thought | "Think step by step" makes reasoning visible and more accurate. |
| 3 | Few-Shot | A few examples teach the pattern better than a description. |
| 4 | Structured Output | Strict JSON instructions make output machine-readable. |
| 5 | Prompt Optimization | Specific, detailed prompts produce far better results than vague ones. |

The overall lesson across all five experiments is that clear, specific, well-structured prompts consistently produce better and more reliable results. Small changes in wording, adding a role, an example, a step-by-step instruction, or a format requirement, can significantly change the quality and usefulness of the model's output.

---

*Prepared by Abubakar Adeel for the AI Agent Fellowship 2026, Week 1.*
