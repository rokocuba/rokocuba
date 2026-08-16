<div align="center">

# Roko Čubrić

<sub>MSc Computer Science at ETH Zürich from September 2026.<br>
Machine Intelligence major, Theoretical Computer Science minor.</sub>

<sub><a href="https://www.linkedin.com/in/roko-cubric/">LinkedIn</a></sub>

</div>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/timeline-dark.svg">
  <img src="assets/timeline-light.svg" width="100%" alt="Timeline. 09.2026, ETH Zürich, MSc Computer Science, Machine Intelligence major and Theoretical CS minor. Summer 2026, CERN, Summer Student in Geneva. 06.2026, BSc in Computing at FER, Josip Lončar Award, top 1.5% of the class. 03 to 06.2026, Shapley-Guided VAE, BSc thesis. 05.2026, STEM Games 2026 Mathematics Arena, detecting AI-written Reddit comments. 12.2025, Computational Modeling Challenge 2025, 1st place. 10.2025 to 02.2026, GaussVAE, compressing 2D Gaussian splatting. Summer 2025, Abysalto, AI Academy internship on a RAG and agent platform. 05.2025, STEM Games 2025 Mathematics Arena, 1st place, error-correcting codes. 11.2024, Computational Modeling Challenge 2024, evolutionary mirror placement in Julia. 09.2023, start of the BSc at the University of Zagreb, FER.">
</picture>

<br>

---

## In detail

### CERN, Summer Student

<sub>Summer 2026</sub>

Summer Student at CERN in Geneva.

<!-- TODO Roko: expand once you can describe the work publicly.
     Match the register of the entries below: what the problem was, what you built,
     the numbers, and the limitation. Three to five sentences is enough.
     Then add a stack line and, if one exists, a link. -->

<br>

### Shapley-Guided VAE

<sub>03–06.2026 · BSc thesis no. 2381 · <a href="https://github.com/roko-cubric/shapley-guided-vae">roko-cubric/shapley-guided-vae</a></sub>

A model trained on several objectives needs a rule for how much each objective counts. That rule is normally a set of constants found by grid search and then held fixed for the rest of the run, which assumes the split that is right at epoch 10 is still right at epoch 150. I estimated it during training instead. The five auxiliary blocks of the UCI Multiple Features set are treated as players in a cooperative game, and their Shapley values distribute a fixed auxiliary budget across the loss terms. Coalition values live as 32 nodes with a rolling mean discounted by training progress, sampled by variance rather than uniformly, so the estimate stays valid while the network underneath it changes.

All three masking tactics beat static uniform weighting. The effect is real and small, and the honest result sits underneath it: a model with no auxiliary tasks at all still reconstructs pixels best.

<details><summary>Numbers</summary><br><samp>4 configurations x 50 independent runs = 200 trainings<br>every model finishes at KL 5.00 +/- 0.02<br><br>baseline&nbsp;&nbsp;&nbsp;&nbsp;beta_2 = 0.001106&nbsp;&nbsp;p = 0.0007<br>marginal&nbsp;&nbsp;&nbsp;&nbsp;beta_2 = 0.000980&nbsp;&nbsp;p = 0.0018<br>conditional&nbsp;&nbsp;beta_2 = 0.002910&nbsp;&nbsp;p &lt; 1e-14<br><br>sampling overhead: 7.5% to 9.5% (12.85 s against 14.08 s per run)<br>absolute effect: 0.001 to 0.003 reconstruction loss, 0.3% to 0.9% relative (small)<br>pix_only, no auxiliary tasks: 0.304 against 0.318 static baseline (expected)</samp></details>

<sub>PyTorch · Shapley values · Multi-task learning</sub>

<br>

### STEM Games 2026, Mathematics Arena

<sub>05.2026 · team ReinFERcement learning · <a href="https://github.com/roko-cubric/STEM-Games-M-2026">roko-cubric/STEM-Games-M-2026</a></sub>

Bot detection normally works at the account level, on post counts, follower ratios and account age. This system uses none of those. The only input is one Reddit comment and the way it is written, and the output is a probability that this particular comment is AI-generated rather than a claim about who owns an account. Three subsystems read the same comment along three axes, and a stacking meta-model learns how to combine what they report.

The meta-model is best on every metric, and the gain is larger on the probabilistic ones than on accuracy. The corpus is the limitation rather than the model: two of the three sources are `gpt-slop` sets, so 0.984 is accuracy on a narrow family of generators. The delivered Chrome extension also serves the TF-IDF model alone, so the calibration gain from stacking is not what the user sees.

<details><summary>Numbers</summary><br><samp>282,000 comments, 70-15-15 split, test set used once<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;accuracy&nbsp;&nbsp;&nbsp;F1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ROC AUC&nbsp;&nbsp;&nbsp;log loss<br>semantic SVM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.90948&nbsp;&nbsp;&nbsp;0.90810&nbsp;&nbsp;0.96885&nbsp;&nbsp;&nbsp;0.22646<br>boosted trees&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.90487&nbsp;&nbsp;&nbsp;0.90423&nbsp;&nbsp;0.96696&nbsp;&nbsp;&nbsp;0.23115<br>TF-IDF logreg&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.98085&nbsp;&nbsp;&nbsp;0.98033&nbsp;&nbsp;0.99780&nbsp;&nbsp;&nbsp;0.06739<br>meta-model&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.98406&nbsp;&nbsp;&nbsp;0.98366&nbsp;&nbsp;0.99840&nbsp;&nbsp;&nbsp;0.04564<br><br>held-out test, meta-model: accuracy 0.98406, ROC AUC 0.99842, log loss 0.04499<br>log loss falls 32% against the best base model<br>TF-IDF feature space: 1,557,681 sparse features (793,698 word + 763,983 char)<br>meta-model trained on 5-fold out-of-fold predictions only</samp></details>

<sub>scikit-learn · Stacking · Platt calibration · FastAPI · Chrome extension</sub>

<br>

### Computational Modeling Challenge 2025

<sub>12.2025 · 1st place · <a href="https://github.com/roko-cubric/cmc25">roko-cubric/cmc25</a></sub>

Stains on a stage have to be covered by patches cut from a 12x12 cm grid leaf, at a cost combining cutting perimeter and travel distance between the cutting area and each final position. I designed a small set of reusable patch shapes by hand on the grid, picked a configuration that already scored well, then fine-tuned the continuous parameters of each patch with a Monte Carlo local search: sample candidates from a multivariate Gaussian, keep the top-k valid ones, update mean and covariance, iterate to convergence.

Most of the gain came from the manual geometry. The search only polished the parameters.

<sub>Python · Simulated annealing · Computational geometry</sub>

<br>

### GaussVAE

<sub>10.2025–02.2026 · <a href="https://github.com/roko-cubric/GaussVAE-showcase">roko-cubric/GaussVAE-showcase</a></sub>

Image compression through the Gaussian parameters rather than the pixels. Image-GS encodes an image as 512 2D Gaussian splats at 8 parameters each, and the VAE compresses those 4096 values into a 512-dimensional latent, 8:1. Morton Z-order sorting linearises the splats first, so the 1D convolutions have local spatial structure to find.

Position and scale converge. Rotation and colour do not, and scaling the decoder to 42M parameters did not fix it. My hypothesis was that the decoder is the bottleneck, but the deeper flaw is running an autoencoder over an input that is fundamentally a set: mapping a latent vector back to a set of parameters with complex interdependencies stays hard even with Morton ordering. I paused the project in January 2026 and moved the underlying question to my thesis.

<details><summary>Numbers</summary><br><samp>Position (xy) parameters: loss converges to ~0.1 (acceptable)<br>Scale parameters:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loss converges to ~0.2 (acceptable)<br>Rotation parameters:&nbsp;&nbsp;&nbsp;loss plateaus at ~1.0-1.2 (poor)<br>Color features:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loss plateaus at ~1.0 (poor)<br><br>Total parameters: 54,207,063<br>Encoder parameters: 12,246,304 (22.6%)<br>Decoder parameters: 41,911,848 (77.3%)<br><br>Trained 500+ epochs. Rotation, scale and features struggled to converge.<br>Dataset: Delaunay, 11,501 images, 10,502 / 500 / 499 split<br>Hardware: Tesla T4 16GB</samp></details>

<sub>TensorFlow · Gaussian splatting · Morton order · ResNet Conv1D · Docker</sub>

<br>

### Abysalto, AI Agent Factory

<sub>Summer 2025 · <a href="https://github.com/roko-cubric/AI-Agent-RAG-Platform">roko-cubric/AI-Agent-RAG-Platform</a></sub>

AI Academy internship on a platform for building and deploying document-processing agents. I worked on architecture and implementation. I pushed for the Strategy pattern so that retrieval methods, chunking methods and evaluation could be swapped without touching the services around them, and built several of the nine retrieval methods, among them Multi-Query, Hybrid Meta and Graph-Walk RAG. Documents carry separate embeddings for content, summary and generated questions, so a query can match on more than surface text. I wrote FastAPI microservices and the PostgreSQL and `pgvector` layer, including dynamic table generation that adapts to the dimension of whichever embedding model is selected.

The source is proprietary to Abysalto. The repository documents the architecture and my part in it rather than shipping the code.

<sub>Python · FastAPI · LangChain · LangGraph · PostgreSQL · pgvector · Docker</sub>

<br>

### STEM Games 2025, Mathematics Arena

<sub>05.2025 · 1st place · <a href="https://github.com/roko-cubric/Stem-Games-2025">roko-cubric/Stem-Games-2025</a></sub>

Theory and programming on information theory and error-correcting codes. The main task was protecting a 100-bit message on a channel that flips up to 10 bits at random. We split it into eight 12-bit blocks under the extended binary Golay code [24, 12, 8] and one 4-bit block under Hamming [7, 4, 3], for 199 bits on the wire. Decoding runs off a precomputed syndrome table, so correcting a block is a dictionary lookup rather than a search.

A second task capped protection at exactly 20 bits against scattered errors. We treated the 100 bits as a 10x10 grid and took 10 column parities plus 10 diagonal ones at stride 11, so a single error trips one check in each set and the intersection locates it.

<sub>Python · Coding theory · Golay [24,12,8] · Hamming [7,4,3]</sub>

<br>

### Computational Modeling Challenge 2024

<sub>11.2024 · <a href="https://github.com/roko-cubric/cmc24">roko-cubric/cmc24</a></sub>

Light path optimisation in Julia. One ray enters a 2D temple and eight mirrors have to be placed to illuminate as much of its area as possible. I wrote a tree-based evolutionary algorithm that grows the mirror set one at a time, scores candidates on covered area and a positional heuristic, keeps the best two and branches each into two more. A rearrangement pass over adjacent pairs afterwards maximises ray distance and reflection angles.

The emphasis was on getting a working algorithm inside the competition deadline, not on code that survives maintenance.

<sub>Julia · Evolutionary algorithms · Ray optics</sub>

---

<div align="center">
<sub>Zürich, from September 2026 · <a href="https://www.linkedin.com/in/roko-cubric/">LinkedIn</a></sub>
</div>