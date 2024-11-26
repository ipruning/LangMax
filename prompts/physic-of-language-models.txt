<physic_of_language_models>
Title: Physics of Language Models

URL Source: https://physics.allen-zhu.com/home

A Small Request: I'm delighted to know that multiple companies have found our philosophy/results useful for training their commercial LLMs. While I encourage this, I have a small favor to ask. If your company's policy allows, acknowledging our work — whether through a citation, an informal mention, or even a brief "thank you" email — would greatly support our future research. Exploratory work like ours can be challenging to sustain, as perhaps 95% of companies do not support this, but your recognition could help us secure resources to deliver more insights for the AI community and perhaps even address some questions you may have. Thank you!

Even today, GPT-4 and Llama-3 still provide incorrect answers to some questions that are simple for humans. Is this a problem inherent to GPT-4, or is it due to insufficient training? Is its mathematical capability too weak? Does this only affect models as of July 2024, or will GPT-6 and Llama-5 also face this problem? What about other pre-trained models?

(Spoiler alert: these are counterexamples that all today's LLMs shall fail — a.k.a. Turing tests.)

Ethology is great, but...

Pretrained LLMs (like GPT-4, LLaMA-3, Claude-3) are like monkeys used in animal behavior science, and we now live in an era where most people can interact with these monkeys and play games. This is fantastic! However, rigorous scientists need to think about the underlying "why" to uncover the "universal laws" behind these phenomena, rather than merely studying individual monkeys.

People often celebrate when an LLM ranks high on a benchmark, but is this truly accurate? Could the models have "seen" this benchmark data during training? Imagine if I were to post a French version of the GPQA benchmark on MIT’s website tomorrow. Henceforth, all LLMs trained with internet data could unknowingly "cheat," as this wouldn't be a direct copy of the original benchmark.

Data contamination is just one issue. If model A outperforms model B on the GSM8k, is it because A has better English comprehension or superior math skills? For instance, LLaMA2-70B scores 63.6% on the world knowledge benchmark, while LLaMA2-7B scores 48.9%. Does a 10x increase in model size enhance knowledge capacity by only 30%?

Moreover, the excessive pursuit of benchmark performance might lead us further away from achieving Artificial General Intelligence (AGI). Imagine incorporating Wu's method and a specialized brute-force search into LLMs, allowing GPT-5 to solve all IMO geometry problems. While this can achieve a 100% score, it does not necessarily indicate a general mastery of math.

Benchmarks are great, but...

Apples fall and boxes move, but universal laws like gravity and inertia are crucial for technological advancement. While GPT-5 or LLaMA-3 may offer revolutionary experiences tomorrow, we must look beyond the horizon. Our goal is to establish universal laws for LLMs that can guide us and provide practical suggestions on how we can ultimately achieve AGI.

Physics of language models

We propose dividing the concept of "intelligence" into multiple dimensions (such as structures, knowledge, reasoning, etc.). For each dimension, we create synthetic data and build an idealized environment for LLM training to understand the theory and push the capability of LLMs in this dimension to the extreme. By performing a large number of controlled experiments, we aim to discover the universal laws of all LLMs, not just a particular version of GPT-4.

Spherical chicken in a vacuum

This humorous phrase critiques theoretical physicists for using oversimplified models. However, without idealized environments, one might wrongly assume that iron balls fall faster than feathers. Idealized environments also help discover simple formulas like the ideal gas laws, which have broad applications.

The same is true in studying LLMs. Commercial LLMs are trained on messy, secretly preprocessed internet data. Training LLMs in a controlled, idealized environment allows us to manage the data and tweak hyperparameters — such as data amount, type, difficulty, and format — to scientifically determine factors affecting LLM performance and suggest improvements.

The law of gravitation (1666-1687) could not have emerged without Kepler's laws of planetary motion (1609-1619), which in turn relied on Tycho Brahe's 20 years of observational data (1577-1597). Studying the universal laws of LLMs also requires extensive observational data, which cannot be achieved by examining merely a few commercial LLMs. Our aim is to derive universal conclusions, regardless of model size or training parameters. How can this be achieved? By breaking down "intelligence" into manageable components, each using synthetic data with controlled size and difficulty. This allows us to repeatedly train many small models under sufficiently varied conditions to initially identify laws, and then test them more broadly.

Probing and transparent AI

Playing with "LLM monkeys" is fascinating, but we aim to delve into the inner workings of their brains and mental processes. By doing so, we gain a deeper understanding of how these AI models function, bringing us closer to creating not only more powerful, but also more transparent AI systems.

By probing into commercial LLMs pretrained on internet data, we typically uncover only basic behaviors at the token level, such as induction and inhibition heads. In our idealized environment, however, we can develop more advanced probing techniques tailored to our synthetic data. This allows us to probe not just one model, but a variety of models of different sizes and with various hyperparameters.

Acknowledgement: I am deeply grateful to my manager, Lin Xiao, for his consistent support in this exploratory research, and to Meta FAIR for generously providing the necessary GPU resources. While our individual papers have recognized many contributors for their insightful discussions, we would also like to extend a special thanks to the exceptional engineering team at FAIR. Their invaluable support has been instrumental in making the experiments in these papers possible.
</physic_of_language_models>
