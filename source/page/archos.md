---
Title: Archos
Summary: A source-grounded LLM system that turns the epistemic requirements of historical scholarship into architecture.
Authors: Sebastian Oliver Eck, Ashley Duraiswamy, Puyu Wang, Yishun Lu
Date: 2026-08-23
Category: Project
Tags: [Archos, archives, LLM, digital humanities]
---

Archos is an **epistemically grounded LLM system for archival exploration**. It is built on one
commitment: an AI system is only usable in the humanities if the requirements of scholarly
practice are encoded into the architecture itself, rather than requested of the model in a
prompt and hoped for in the output. 

## What makes it different

With Archos, historians remain in control of interpretation throughout. The system assists with evidence
discovery, organisation and documentation; it does not adjudicate the history.

## Our workflow

<figure class="my-8 rounded-lg border border-oxford-200 bg-white p-3 sm:p-4 dark:border-oxford-700" markdown="1">

<a href="/image/pipeline.jpeg" class="block no-underline"><img src="/image/pipeline.jpeg" alt="The Archos pipeline. Steps, left to right: a historian writes the research statement; the system retrieves archival evidence, applies an epistemic constitution and produces source-grounded synthesis; a historian verifies the result. The first and last steps are marked as domain expert involvement, the three middle steps as scholarly AI." class="w-full rounded"></a>

<figcaption class="mt-3 text-sm text-oxford-600 dark:text-oxford-300">
<span class="mb-1 block text-xs sm:hidden">Tap the diagram to open it full size.</span>
<strong>Figure 1.</strong> The division of labour across a run. The interpretive decisions at
either end stay with the historian; the scholarly AI carries the evidentiary work in the middle,
and every claim it produces remains traceable back to a retrieved document.
</figcaption>

</figure>


## Where the historian sits in the loop

Archos is not an end-to-end answering machine. A domain expert writes the research statement
that opens a run, and a domain expert verifies the report that closes it. Between those two
points the system works under constraint: it retrieves archival evidence, holds it to an
epistemic constitution, and synthesises only from what retrieval actually returned.


## Reading an Evidence Report
<figure class="my-8 rounded-lg border border-oxford-200 bg-white p-3 sm:p-4 dark:border-oxford-700" markdown="1">

<a href="/image/example.png" class="block no-underline"><img src="/image/example.png" alt="An Evidence Report, side by side. Left: the transcribed archival source, with one passage highlighted and marked 1. Right: the synthesis for subsection 3.1, Chaloner's Printed Reformer Claims, where each sentence carries its own numbered footnote, marked 2, and a provenance card is open over the text showing the source descriptor, its id MINT01535 and the verbatim quotation, marked 3." class="w-full rounded"></a>

<figcaption class="mt-3 text-sm text-oxford-600 dark:text-oxford-300">
<span class="mb-1 block text-xs sm:hidden">Tap the screenshot to open it full size.</span>
<strong>Figure 2.</strong> The Evidence Report for one subsection of the Chaloner Prosecution run (Royal Mint papers, 1692–1700). Left: transcribed source with a
highlighted citable passage. Right: source-grounded synthesis in PEEL structure, where every claim is traceable to a specific retrieved document.
</figcaption>

</figure>
The system's output is an **Evidence Report**: the transcribed source on one side, the
source-grounded synthesis on the other.

1. A **citable passage** is highlighted in the transcribed archival source.
2. **Sentence-level citation** — every evidence sentence carries its own footnote or footnotes.
3. A **provenance card** appears on hover, giving the source id, date, verbatim quote and
   epistemic status.






## Try it on your own material

We are looking for collections to test against. See
[get involved](/page/datasets.html) for what we need and what you get back.
