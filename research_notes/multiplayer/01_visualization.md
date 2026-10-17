# 01. Visualization research: live problem tree and idea clusters

Task R1. Date: 2026-10-17. Track: "Multiplayer agentic experiences".

How this was done. Web pages were read with WebFetch and WebSearch. Registry and CDN facts were fetched as raw JSON or by HEAD request from this PC. A few small CPU-only checks ran in Node v25.9.0 and in the lab venv Python from the session scratch folder. No model call, no GPU run, no research loop, no browser was started. Nothing was installed. No repo file other than this one was changed.

Note for the workflow. The user asked that the design stage use Fable. This file is written as input for that stage. Section 8 lists what the design stage must decide. This research stage itself ran on Sonnet 5.5.

Tags used for every web fact:

- [V] verified on the page or file, fetched today. The URL is in section 10.
- [S] seen in a search result summary only. The page itself was not opened. Weaker.
- [M] from memory. Not checked today.
- [T] measured by me today in Node. Layout maths only. No browser rendering was timed.
- [J] my judgement.
- [L] read in a local repo file.

---

## 0. Read this first

### 0.1 The decision

**Build both views with D3 7.9.0 plus plain HTML and SVG. Do not adopt a graph framework.**

Why, in four lines:

1. Size is not the problem. Every layout I tried ran in under 100 ms for 60 tree nodes or 135 bubbles [T]. The hard part is stability: how far old items jump when something new arrives. D3's tidy tree and a position-keeping force simulation were the most stable options I measured [T]. A fresh force layout or a default ELK layout reshuffles everything [T].
2. A modern look needs HTML cards: blur, gradients, wrapped text, badges, avatars. Canvas and WebGL libraries are weak there [J]. The best card UI (React Flow) needs React 18 and a small `jsxRuntime` shim to run from script tags: its UMD file reads that global [V for the file header, J for the shim].
3. D3 is one file (92.6 KB gzip) on cdnjs, jsDelivr and unpkg [V]. Its v7 modules date from June 2021 (for example d3-force 3.0.0 and d3-selection 3.0.0) and the last D3 release is 7.9.0 from March 2024, with no newer stable release [V]. A coding agent writes D3 well [J].
4. One animation clock with critically damped smoothing gives the Figma feel. A new node slides out of its parent. Old nodes glide aside. Nothing teleports. An idle page uses no CPU [J]. The helper logic was tested in Node (Appendix A) [T].

Odds that this plan gives a good-looking, stable version in one day for a strong coding agent: about 85 percent. The risk is polish time, not feasibility [J].

### 0.2 The numbers behind it [T]

Layout stability. A seeded random tree of 60 nodes (4 levels below the root). Three leaves were added at random places. 12 trials. The table shows how far the 60 old nodes moved (average of the per-trial mean, and the worst single jump), after removing any common shift. Lower is better. Pixel values depend on spacing, so compare ratios.

| Layout method | Average move (px) | Worst jump (px) |
|---|---|---|
| fcose with old nodes pinned | 0.0 | 0 |
| ELK mrtree | 22.5 | 78 |
| fcose, randomize false, quality proof | 31.6 | 179 |
| d3.tree (tidy tree) | 36.7 | 117 |
| ELK layered with interactive options and old positions | 65.5 | 1369 |
| ELK layered, default options | 370 | 1461 |
| fcose, full relayout | 502 | 1955 |

Cluster bubbles. 100 ideas in 30 clusters. 12 trials. How far the 30 old bubbles moved.

| Method | New 1-idea cluster arrives | One cluster gains an idea |
|---|---|---|
| d3.pack sorted by size | 0.0 avg, 0 worst | 131.5 avg, 509 worst |
| d3.pack in arrival order | 2.8 avg, 367 worst | 57.2 avg, 496 worst |
| d3-force collide, keeping positions | 8.3 avg, 27 worst | 1.5 avg, 11 worst |

Layout time (mean, warm). d3.stratify plus d3.tree for 60 nodes: 0.015 ms. d3.pack for 100 ideas in 30 clusters: 0.06 ms. d3-force collide: 0.027 ms per tick for 30 bubbles, 0.27 ms per tick for 135 bubbles, 0.85 ms per tick for 300 bubbles. ELK layered for 60 nodes: 92 ms first call, 30 ms warm. cytoscape-fcose for 60 nodes: 35 ms first call, 13 ms warm.

Smoothing. The critically damped helper in Appendix A with smoothTime 0.12 s reaches 95 percent in 300 ms and 99 percent in 400 ms, with no overshoot. smoothTime 0.15 s: 367 ms and 500 ms. smoothTime 0.25 s: 600 ms and 833 ms.

What these mean:

- Never re-run a force or ELK layout from scratch on each update. It moves almost every node by hundreds of pixels. [T]
- For the tree, use the deterministic tidy tree. Nodes shift by tens of pixels, which animates well. [T] ELK mrtree moved nodes a little less (22.5 px) but costs 467 KB gzip, so it is not worth adding.
- For clusters, use a force simulation that keeps positions. Do not re-pack with d3.pack. [T]
- Layout cost is not the bottleneck. Frame cost will be DOM writes (about 60 card transforms and 60 path updates per frame), which is small [M].

Caveat. These are Node (V8) timings of layout maths on synthetic data. No browser frame was timed. The browser check is listed in section 4.6.

### 0.3 Fallbacks and what not to use

- **Fallback 1:** Cytoscape.js (pin 3.34.3, MIT, 137 KB gzip) with positions computed by d3.tree and pinned. Section 4.7.
- **Fallback 2:** Markmap for the tree (about 10 lines, 12 KB gzip plus D3) and a CSS grid of cluster cards animated by auto-animate (3.3 KB gzip). A two-hour safety net.
- **Quick demo fallback:** vis-network (physics, easy live updates, dated look).
- **Do not use:** React Flow through a script tag, sigma 4, ELK for the tree, AntV G6, ECharts, d3-org-chart, the vanilla node editors (Drawflow, Rete, jsPlumb, LiteGraph). Reasons are in section 4.8.

### 0.4 Three traps found in our own data [L]

Source: `research_notes/multiplayer/00_artifacts.md` (sections 5, 9.2, 9.4) and a read-only look at the mock run folder.

1. **Cluster ids are positional.** `choice-in-k03` is the index in one grouping. A new grouping can reuse an id for a different cluster. Key clusters by member overlap, not by id. Appendix A has a tested matcher.
2. **Private fields must never be drawn.** `idea_clusters.json` carries `obvious` and `obvious_match`, which copy text from the private defaults list. A shared view must read a cleaned feed.
3. **Real runs have more clusters than the brief says.** The brief says 20 to 40 clusters for 100 ideas. The mock run has 135 clusters from 739 sketches. The arch-2 run had 131 clusters from 237 sketches, and skel-1 had 98 from 275 (project memory file). Design for up to 150 clusters and 800 ideas, with a level-of-detail rule for singletons.

Also: the files are rewritten whole, have no author field and the tree has no history. The view needs a feed of changes with `by`, `ts` (UTC) and `rev`. See section 8.

One D3 gotcha that fails silently: force accessors are cached. If bubble radii animate, the collide force keeps using the old radii until you re-set its radius accessor. A changed `forceX` target is ignored until `sim.nodes()` is called again. Details and test in section 3.1.

---

## 1. What we must render

### 1.1 Tree [L]

- `problem_tree.json` has `nodes[]` and a nested `tree` `{id, name, kind, children[]}`. Use `tree` for layout and join `nodes` by `id`.
- Real depth is up to 4 below the root. The mock tree has 9 nodes and depth 2. The brief says up to about 60 nodes.
- Useful node fields: `origin` (absent means planned, or `human`, `failure`, `offtree`), `kind` (part, `question`, `win`), `priority` (`low` means lowered), `disputed`, `directions`, `stats.<direction>.{sketches, clusters, implemented, checked}`, and for questions `test`, `threshold`, `fails_if`.
- Node ids are stable inside one run. Two people choosing the same id lose one node silently in the loop today.

### 1.2 Clusters [L]

- `idea_clusters.json` has `clusters[]` with `name`, `members` (sketch ids), `n`, `node`, `direction`, `score`, `rank`, `selected`, `lane`, `prior` (new, known, failed, unknown), `n_angles`, `leap_share`, `representative`.
- Mock run: 135 clusters, sizes up to 15, 2 singletons, 2 selected. Real runs have many singletons.
- Do not draw `obvious` or `obvious_match`.

### 1.3 Live behaviour [L]

- Whole-file JSON (tree, clusters, picks) is rewritten at stage ends. The view must diff against the last copy. Appended files (`ideas.jsonl`, `dialogue.jsonl`, `verify.jsonl`, `control_log.jsonl`) can be followed line by line.
- Rounds are slow. A live demo needs a mock-backend run or a replay. The mock run finished in 77 seconds.
- The PC has Chrome 155 and Edge 155 (no Firefox) [L: `00_environment.md`]. Modern CSS is safe on stage. Keep graceful fallbacks for other browsers but do not spend time on them.
- Memory is tight on this PC (4.9 GB free of 15.7 GB at check time) [L]. Keep the page light and idle-friendly.

---

## 2. Library comparison

### 2.1 Facts (all versions and sizes fetched today)

"Pin" is the newest stable version that is at least 14 days old on 2026-10-17. The Artifact tool in this session only accepts script versions that old, and it is a sensible stage rule anyway. [V] for every cell unless marked.

| Library | Pin | CDN file (jsDelivr unless noted) | License | Size gzip | Latest stable (date), releases in last 12 months |
|---|---|---|---|---|---|
| D3 | 7.9.0 | `npm/d3@7.9.0/dist/d3.min.js`; also cdnjs `ajax/libs/d3/7.9.0/d3.min.js` and unpkg | ISC on npm; cdnjs lists BSD-3-Clause | 92.6 KB | 7.9.0 (2024-03-12), 0 |
| Cytoscape.js | 3.34.3 | `npm/cytoscape@3.34.3/dist/cytoscape.min.js`; also cdnjs | MIT | 136.7 KB (3.34.4 measured) | 3.34.4 (2026-10-15), 8 |
| cytoscape-fcose | 2.2.0 | `layout-base@2.0.1/layout-base.js`, `cose-base@2.2.0/cose-base.js`, `cytoscape-fcose@2.2.0/cytoscape-fcose.js` | MIT | 34 + 22 + 13 = 69 KB | 2.2.0 (2023-01-17), 0 |
| cytoscape-cola | 2.5.1 | needs `webcola@3.4.0/WebCola/cola.min.js` too | MIT | not measured | 2.5.1 (2022-02-23), 0 |
| sigma.js | 3.0.3 (safe) | `npm/sigma@3.0.3/dist/sigma.min.js` plus `graphology@0.26.0/dist/graphology.umd.min.js` | MIT | 47.1 KB (3.0.3), 103.3 KB (4.0.3) + 13.9 KB | 4.0.3 (2026-10-15), 5 |
| vis-network | 10.1.2 | `npm/vis-network@10.1.2/standalone/umd/vis-network.min.js`; also cdnjs `.../10.1.2/standalone/umd/vis-network.min.js` | Apache-2.0 OR MIT | 154.2 KB | 10.1.2 (2026-08-19), 4 |
| elkjs | 0.12.0 | `npm/elkjs@0.12.0/lib/elk.bundled.js` (not found on cdnjs) | EPL-2.0 OR GPL-3.0-or-later | 467 KB (1.6 MB raw) | 0.12.0 (2026-07-17), 2 |
| Markmap view | 0.18.12 | `npm/markmap-view@0.18.12/dist/browser/index.js` (needs D3 first) | MIT | 12.2 KB | 0.18.12 (2025-06-12), 0 |
| @xyflow/react (React Flow) | 12.12.0 | `npm/@xyflow/react@12.12.0/dist/umd/index.js` plus `dist/style.css` | MIT | 59.5 KB + CSS 3 KB, plus React 18.3.1 (4.3 KB) and ReactDOM (42.9 KB) | 12.12.0 (2026-09-24), 15 |
| force-graph | 1.52.0 | `npm/force-graph@1.52.0/dist/force-graph.min.js` | MIT | 56.4 KB | 1.52.0 (2026-09-28), 6 |
| AntV G6 | 5.1.1 | `npm/@antv/g6@5.1.1/dist/g6.min.js`; cdnjs name `antv-g6` | MIT | 391 KB | dist-tag latest 5.1.1 (2026-05-08), 5 |
| ECharts | 6.1.0 | `npm/echarts@6.1.0/dist/echarts.min.js`; also cdnjs | Apache-2.0 | 369 KB | 6.1.0 (2026-05-19), 1 |
| d3-org-chart | 3.1.1 | `npm/d3-org-chart@3.1.1/build/d3-org-chart.min.js` plus d3-flextree 2.1.2 | MIT (flextree: WTFPL) | not measured | 3.1.1 (2023-09-18), 0 |
| GSAP | 3.15.0 | `npm/gsap@3.15.0/dist/gsap.min.js`, `Flip.min.js`, `DrawSVGPlugin.min.js`; also cdnjs | "Standard no charge" license, plugins included | 28.3 KB (+ Flip 9.7, DrawSVG 2.2) | 3.15.0 (2026-04-13), 4 |
| anime.js | 4.5.0 | `npm/animejs@4.5.0/dist/bundles/anime.umd.min.js`; also cdnjs `anime.umd.min.js` | MIT | 40.6 KB | 4.5.0 (2026-06-22), 10; 5.0.0-beta exists |
| Motion | 14.0.0 | `npm/motion@14.0.0/dist/motion.js` (global `Motion`); not on cdnjs | MIT | 47.7 KB (14.0.0) | 14.3.0 (2026-10-15), 79 |
| auto-animate | 0.10.0 | `npm/@formkit/auto-animate@0.10.0/index.mjs` (ES module, default export); also cdnjs | MIT | 3.3 KB (min), 7.0 KB (mjs) | 0.10.0 (2026-07-10), 1 |
| htm with its bundled Preact | htm 3.1.1 | `npm/htm@3.1.1/preact/standalone.module.js` (one ES module that exports `html, render, h, useState, useEffect, useRef, useMemo`...) | Apache-2.0 (htm), MIT (Preact) | 5.3 KB | htm 3.1.1 (2022-04-26); Preact itself is at 11.0.1 (2026-10-08) and 10.29.8 answers 200 on jsDelivr if a separate copy is wanted |
| canvas-confetti | 1.9.4 | `npm/canvas-confetti@1.9.4/dist/confetti.browser.js` | ISC | 6.9 KB | 1.9.4 (2025-10-25), 1 |

Other facts:

- Every file above answered HTTP 200 on jsDelivr from this PC today. cdnjs answered 200 for D3, Cytoscape, GSAP (and Flip), anime.js, vis-network and auto-animate. The cdnjs API has no exact entry for elkjs, markmap-view, motion, framer-motion, force-graph or cytoscape-fcose, and a direct path test for elkjs gave 404. So those come from jsDelivr (or unpkg) only. [V]
- Google Fonts CSS answered 200 for Inter, Geist, Geist Mono and JetBrains Mono. [V]
- React 19 has no UMD file on jsDelivr (HTTP 404 for `react@19.3.1/umd/react.production.min.js`). React 18.3.1 UMD answers 200. [V]
- The Artifact tool contract in this session allows scripts only from cdnjs, jsDelivr, unpkg, cdn.tailwindcss.com and code.jquery.com, with exact versions at least two weeks old. This matters only if the page is ever published as an Artifact. [L: the Artifact tool contract given in this session]
- For the stage, copy the pinned files into the repo (`web/vendor/`) with `curl.exe`, so a bad venue network cannot break the page. Section 4.1 has a loader with a local fallback. [L: `00_environment.md` makes the same point]

### 2.2 How each option fits our two views

| Option | Animation quality | Speed at our size | Effort for a no-build page | Known pitfalls | Verdict |
|---|---|---|---|---|---|
| D3 + HTML cards + SVG edges | Best control. Every motion is yours. Official enter/update/exit pattern is documented and used by the D3 collapsible tree: enter at the parent's old position, 250 ms transitions [V] | Layout under 1 ms to 41 ms [T]. About 200 DOM elements [M] | Medium. About 700 to 900 lines for both views [J] | You write the polish. Needs key functions [V]. A new transition on the same element interrupts the old one when it starts [V] | **Primary** |
| Cytoscape.js (+ fcose) | Good. Style transitions with `transition-property`, duration, delay and timing function, including `spring(tension, friction)` and cubic-bezier [V]. `ele.animate({position, style}, {duration})` [V] | fcose 10 to 35 ms for 60 nodes [T] | Low. About 40 lines to a first picture [J] | Canvas look. Labels and background images are costly [V]. fcose from a random start reshuffles [T]. fcose needs 3 scripts in order [V]. `randomize:false` requires `quality:'proof'` [V] | **Fallback 1** |
| Markmap | Decent. D3 transitions, default 500 ms [V] | Fine | Very low. About 10 lines [J] | Mind-map look only. Node key is the id path plus a hash of the content, so an edited node leaves and re-enters instead of updating [V]. No cluster view | **Fallback 2 (tree only)** |
| vis-network | Physics motion that can feel jelly [J]. Camera `moveTo`, `focus`, `fit` can animate [V]. DataSets bind data live [V]. A `cluster()` API exists [V] | Fine | Low | Dated look [J]. No built-in enter animation [M]. Hierarchical layout is a separate mode [M] | Quick demo only |
| sigma.js | WebGL. No cards [J] | Overkill: "Render large graphs in the browser. Fast." [V] | High for cards | v4.0.0 is a rewrite of the programs system with breaking changes, released 2026-10-08, and the docs were rebuilt [V]. WebGL 2 only [V] | No |
| elkjs | Layout only | 30 ms warm, 92 ms first for 60 nodes [T] | Medium. Promise API [V] | Default layered layout is unstable [T]. 467 KB gzip [V]. Built from Java with GWT [V] | No for the tree |
| @xyflow/react | Best node UX [J] | Fine | High without a build | UMD file needs globals `jsxRuntime`, `React`, `ReactDOM` [V]. React 19 has no UMD [V]. Attribution can be removed only with a Pro subscription [V]. No official no-build guide found [S] | No |
| force-graph | Canvas. Link particles `linkDirectionalParticles` [V] | Fine | Low | Docs do not say whether positions survive `graphData` updates [V]. Canvas look | Optional for a cluster fallback |
| AntV G6 5 | Per-element enter/update/exit with `fade` and `translate` effects [V]. BubbleSets and Hull plugins exist [S] | Fine | Medium | 391 KB gzip [V]. Docs partly translated [J]. Weaker coverage in agent training data [J] | No |
| ECharts 6 | Good charts [M] | Fine | Low | 369 KB gzip [V]. No HTML nodes [M] | No |
| d3-org-chart | Expand/collapse with a `duration` property [V] | Fine | Low | Last release 2023-09 [V]. Org-chart look | No |
| Drawflow, Rete, jsPlumb, LiteGraph | n/a | n/a | n/a | Editors for connected ports, not read-mostly trees. No stable release in the last 12 months for any of the four [V] | No |

### 2.3 Animation helpers

| Helper | What it gives | Pitfalls | Verdict |
|---|---|---|---|
| CSS transitions, `@starting-style`, Web Animations API (`element.animate`) | Enter, pulse, ripple, halo with no library. `@starting-style` is Baseline 2024 [V]. `animate()` is Baseline widely available since March 2020 [V]. The individual `scale` property is Baseline widely available since August 2022 [V] | CSS `d` property (path animation) is not Baseline [V]. Use JS to move path endpoints | **Core** |
| Own `smoothDamp` loop (Appendix A) | Velocity-keeping positions, no restart when the target moves | You maintain it. 10 lines | **Core** |
| GSAP 3.15.0 | Timelines, stagger, Flip (records state, then animates offsets away; matches by `data-flip-id`) [V], DrawSVG | License is not OSI. It is free for everyone including plugins and commercial use. Banned use: tools that let people build visual animations without code and compete with Webflow [V] | Optional, for choreography |
| anime.js 4.5.0 | Timelines, `svg.createDrawable`, `morphTo`, `stagger`, and a Layout API with `record()`, `animate()`, `update()`, `revert()` [V] | Newer API, less coverage in training data [J]. A 5.0 beta exists [V] | Optional |
| Motion 14 | `animate()`, spring, `stagger` in vanilla JS [V]. Global `Motion` [V] | Many releases (79 in 12 months) [V]. Docs examples still show v11 [V]. Vanilla layout animation is not shown in the quick start [V] | No |
| auto-animate 0.10.0 | One call animates add, remove and move of a list's children. Respects `prefers-reduced-motion` [V] | Only direct children of one parent. Not for the graph | **Use for the feed and lists** |
| View Transitions API | Morphs elements by `view-transition-name`. Same-document support is Baseline Newly available since Oct 2025, with Firefox 144 [V]. First Chrome 111, Safari 18 [S] | New. Not needed for the graph | Optional for list reorder |
| canvas-confetti 1.9.4 | Winner moment | Do not overdo | Optional |
| perfect-cursors 1.0.5 | Spline cursor smoothing | Last release 2022 [V]. Adds lag [V] | No (smoothDamp is enough) |

---

## 3. Notes on the main candidates

### 3.1 D3 7.9.0

- ESM and UMD are both documented. The docs recommend the ES module bundle from jsDelivr `npm/d3@7/+esm`. The UMD bundle exports the `d3` global [V].
- `selection.join(enter, update, exit)` can return transitions from enter and update. The key function is optional but is what gives object constancy [V]. Bostock: "To achieve object constancy with D3.js, specify a key function as the second argument to selection.data" [V].
- `transition.attr` reads the start value when the transition starts [V]. A new same-name transition interrupts the active one when it starts, not when it is created, and the old one gets a final frame [V].
- `d3.tree().nodeSize([w, h])` puts the root at (0,0) [V]. Call `root.sort` first, because child order matters [V]. Use first-seen order, not name or score, so siblings never swap.
- `d3.pack` requires `root.sum` and recommends `root.sort` [V]. The docs say nothing about stability. I measured it: it is not stable under growth [T].
- `d3.forceSimulation`: defaults alpha 1, alphaMin 0.001, alphaDecay about 0.0228 (300 ticks), velocityDecay 0.4. The timer stops when alpha is below alphaMin. After adding nodes you must call `simulation.nodes()` again. `tick()` steps by hand and fires no events [V]. Positions are initialised only when `x` or `y` is NaN, so existing positions stay [V, inferred by the page's own wording].
- **Force accessors are cached.** The docs say the `collide.radius` accessor result "is only recomputed when the force is initialized or when this method is called with a new radius, and not on every application of the force" [V]. I tested it: two overlapping nodes grown from r 5 to 40 stayed overlapping (gap -69 px) when the accessor was not re-set, and separated (gap +34 px) when `sim.force('collide').radius(fn)` was called again. A changed `forceX` target was ignored until `sim.nodes()` was called again [T]. Rule: while radii animate, re-set the collide radius every frame; after changing anchors, call `sim.nodes(...)`.
- `d3.zoom`: programmatic moves use `selection.transition().duration(750).call(zoom.transform, d3.zoomIdentity...)`. `scaleExtent` and `translateExtent` are not enforced when you call `zoom.transform` directly. The default filter lets `ctrl+wheel` through [V].
- `d3.schemeObservable10` exists in D3 7.9.0 (d3-scale-chromatic 3.1.0, 2024-03-12) [V]. Hex values: `#4269d0 #efb118 #ff725c #6cc5b0 #3ca951 #ff8ab7 #a463f2 #97bbf5 #9c6b4e #9498a0` [V]. These are light-background colours. Do not use them for dark-surface owner colours (section 7).

### 3.2 Cytoscape.js 3.34

- Style transitions: `transition-property`, `transition-duration` (for example `0.5s`), `transition-delay`, and `transition-timing-function` with `linear`, `spring(tension, friction)`, `cubic-bezier(x1,y1,x2,y2)` and named easings [V].
- `ele.animate({position, style}, {duration})` works on nodes [V]. You can animate only one of `position` and `renderedPosition` [V].
- Labels: `text-wrap: wrap` with `text-max-width` [V]. Node `background-image` accepts PNG, JPG or SVG, and data URIs. For SVG, include the XML header and do not base64-encode [V]. This is how you draw badges and avatars on canvas nodes.
- Performance page: edges are costly (bezier more than haystack), dashed edges, semi-transparent edges with arrows, labels and background images cost more. Use `cy.batch()` for many changes. No element counts are given [V].
- fcose README: dependencies load order layout-base, cose-base, cytoscape-fcose. Options `randomize` (default true; if false then quality must be `proof`), `animate` (true), `animationDuration` (1000), `quality` (`draft`, `default`, `proof`), `fixedNodeConstraint`, `packComponents`, `tile`. Compound graphs are supported. MIT [V].
- My measurement: with a full relayout fcose moved old nodes by 502 px on average. With `randomize:false` and `quality:'proof'` it moved them 31.6 px. With `fixedNodeConstraint` on the old nodes it moved them 0 px [T]. So if you use Cytoscape, pin old nodes and let new ones settle.

### 3.3 Markmap

- Browser use: load D3, then `markmap-view`. The library is `window.markmap` with `Markmap`, `loadCSS`, `loadJS` [V].
- Source of 0.18.12: default `duration: 500`; the data join is `.data(nodes, d => d.state.key)`; the key is the parent id path plus a hash of the node content [V]. Nodes render text in `foreignObject` [V]. So a status badge inside the content changes the key and the node re-enters. Keep dynamic state outside the content, or accept the flash.

### 3.4 React Flow / @xyflow/react

- MIT. v12.12.0. Under the hood its core (`@xyflow/system`) depends on d3-zoom, d3-drag and d3-selection [V]. That is a hint that the same primitives are enough for us [J].
- The UMD wrapper writes `ReactFlow` and reads the globals `jsxRuntime`, `React` and `ReactDOM` [V, header of the 12.12.0 file]. React publishes no `jsxRuntime` global. A no-build page needs a small shim and the React 18.3.1 UMD files, and would write nodes with `React.createElement` or htm [J]. It works on paper and is fragile.
- "Subscribing to React Flow Pro permits you to remove the attribution" and "Only remove this attribution, if you are subscribed" [V].
- esm.sh and jsDelivr `+esm` URLs for the package answer 200 [V]. Duplicate React copies are the usual failure [M].

### 3.5 ELK

- Promise API, Web Worker optional (`workerUrl`), algorithms `layered`, `stress`, `mrtree`, `radial`, `force`, `disco`, plus `box`, `fixed`, `random` [V]. Built from Java with GWT [V].
- Stability test [T]: default layered moved old nodes 370 px on average. Layered with `INTERACTIVE` strategies and previous positions fed in: 65.5 px on average but one trial flipped by 1369 px. `mrtree`: 22.5 px, close to d3.tree. If you need cross-links (for example idea to node), draw them as overlay arcs on the d3.tree layout instead of switching to ELK.

### 3.6 vis-network and sigma

- vis-network: `setData()` replaces everything and "the network will stabilize again" if stabilization is on. `cluster(options)` and `clusterByConnection` exist. `moveTo`, `fit` and `focus` can animate the camera [V].
- sigma 4: release notes of 2026-10-08: programs rewritten, WebGL 1 dropped, `hidden` and `forceLabel` replaced, new declarative styles [V]. It is nine days old. Use 3.0.3 if you must, but cards and badges are not its job [J].

---

## 4. Recommended stack for a 1-day build

### 4.1 Pins and loader

```html
<!-- core: the only required library -->
<script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>
<!-- panels (feed, drawer, argument threads): 5.3 KB gzip -->
<script type="module">
  import { html, render, useState, useEffect } from 'https://cdn.jsdelivr.net/npm/htm@3.1.1/preact/standalone.module.js';
</script>
<!-- optional -->
<script type="module">
  import autoAnimate from 'https://cdn.jsdelivr.net/npm/@formkit/auto-animate@0.10.0/index.mjs';
</script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/Flip.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.4/dist/confetti.browser.js"></script>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">
```

Loader with a local fallback (sketch, not run) [J]:

```js
const LIBS = [['https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js', '/vendor/d3.min.js']];
const load = src => new Promise((ok, no) => { const s = document.createElement('script'); s.src = src; s.onload = ok; s.onerror = no; document.head.append(s); });
(async () => { for (const [cdn, local] of LIBS) { try { await load(cdn); } catch { await load(local); } } startApp(); })();
```

Prefer classic UMD script tags for libraries so inline code can use globals. Use module scripts only for htm/Preact and auto-animate [J].

### 4.2 Architecture

```
viewport (div, overflow hidden, d3.zoom attached here)
  world (div, CSS transform translate(x,y) scale(k), transform-origin 0 0)
    svg.edges   absolute, 1px box, overflow visible   paths between cards
    div.cards   absolute                              one HTML card per tree node
    svg.fx      absolute, overflow visible            halos, ripples, particles
  div.hud       not zoomed: presence bar, legend, follow frame, mini controls
side drawer (Preact): activity feed, details, arguments, results
```

- Two view modules (tree, clusters) share one store, one animation clock and one tokens file. The store is a plain object with subscribe [J].
- Pan and zoom is one CSS transform on `world`. Edges and cards stay aligned. Do not put `will-change: transform` on `world`, or text can blur when zoomed in [M].
- Panels are Preact via htm (keyed lists). The graph canvas is plain D3 and DOM. They talk through the store only [J].
- Glow without cost: use `box-shadow` on HTML cards, and a pre-drawn radial-gradient halo circle for SVG. Avoid `filter: drop-shadow` on many moving elements [J].
- Idle means zero CPU: the clock stops when every value has settled (Appendix B1).
- `prefers-reduced-motion` is honoured: Baseline widely available since January 2020 [V]. Under reduce, use instant moves and no pulses.

### 4.3 Tree view

- Layout: `d3.tree().nodeSize([56, 250])`, left to right. Screen x is `node.y`, screen y is `node.x`. Children in first-seen order [V for API, J for choices].
- Default depth: root, parts and sub-parts (3 levels). Deeper levels collapse into a count chip and open when activity touches them or on click. Reason: my synthetic 60-node tree has 31 leaves; at 56 px per row that is about 1700 px, too tall for 900 px at a readable scale. Collapsed to 3 levels it has 23 nodes and 16 visible rows, about 900 px, which fits a 1080p screen [T, arithmetic].
- Card content: name (2 lines), owner stripe (3 px, owner hue), origin glyph (map, off-map win, failure question, human), state dot, count chips (sketches, clusters, built, checked), a disputed flag, lowered priority shown dim, skipped shown hatched. Status words come with an icon, never colour alone (dataviz rule) [L: skill].
- Edges: cubic Bezier from the parent's right middle to the child's left middle, recomputed every frame from current positions. A new child starts at its parent, so the edge grows as the child slides out. This is the same idea as the D3 collapsible tree (zero-length path at the parent, then to full) [V].
- Interactions: hover shows the path to the root and dims the rest (Obsidian) [V]; click opens the drawer; double click fits the branch; arrow keys move focus.
- Presence: each person and agent has a chip. The node where someone is working gets a ring in their colour with a name tag. An agent's ring shows its state (section 6).
- Change halo: a box-shadow ring in the actor's colour fades over about 2 s on a new or changed node.
- Human steering: an action from `control.json` shows as a dashed outline with a "queued" chip until the loop applies it at a stage end. Then it turns solid. If the id clashed and was dropped, show "dropped: id in use" [L: 00_requirements section 3.2, 00_artifacts section 6].

### 4.4 Cluster view

- One `d3.forceSimulation` over bubbles. Forces: `forceCollide(d => d.r + 3)` with 2 iterations, and weak `forceX/forceY` (strength 0.05 to 0.06) toward an anchor per part, so parts form islands. Positions are kept between updates [T measured stable].
- Bubble radius from the idea count: `r = spacing * sqrt(n + 0.5) + 6`. With dot radius 5 and a 2 px gap, `spacing = 7.8`. Area grows with n. Range for n = 1 to 15 is 15 to 37 px.
- Ideas are dots on a sunflower (phyllotaxis) spiral in arrival order (Appendix A, `sunflower`). A new dot never moves old dots, and the dots never overlap at that spacing (tested: nearest neighbours stay 1.55 x spacing apart) [T].
- Identity: use `matchClusters` (Appendix A) to give each cluster a stable `vid`. A split gives the big part the old vid and the small part is "born from" it, so it pops out of the parent. A merge makes the small cluster "fly into" the big one. A brand new cluster pops in at its part anchor.
- Encodings (design stage may change them):
  - Rim donut by contributor, using owner hues (d3.pie and d3.arc are in the d3 bundle).
  - Prior-art tag as ring style: solid for new, dashed for known, dotted for failed.
  - `selected` gets a soft ring. A cluster that won its test gets the strong highlight (glow, ripple, badge, others dim). In Mode 3 (no objective check) the word is "preferred", never "won" [L: 00_requirements R14].
- Level of detail: show bubbles with n >= 2, or selected, or hovered. Fold singletons into a "long tail" ring with a count, and open it on zoom. Always label the top 5 by n. Other labels on hover.
- Interactions: hover highlights the cluster and its tree node (linked views). Click opens the drawer with the lead sketch (idea, mechanism, prediction, test), objections and replies, and results. A "colour by" switch: owner, part, prior-art tag, card, status (Obsidian groups, Miro group-by) [V, S].
- Simulation driving: do not let D3's own timer run. Call `sim.stop()` once, then `sim.tick()` once per frame from the shared clock while alpha is above the floor. Use `alphaDecay` 0.05 so a reheat to 0.4 settles in about 2 seconds [J, from the verified defaults]. Re-set the collide radius accessor every frame while radii animate, and call `sim.nodes(...)` after anchors change (the forces cache their inputs, section 3.1) [V, T].

### 4.5 Live update rules

1. The page state is a pure function of the store. Live mode and replay mode both feed the same `apply(event)` [J].
2. Key everything: tree by node id; clusters by `vid`; sketches by id; feed by event id. D3 joins need key functions [V].
3. Prefer a small server sidecar that diffs the whole-file JSON and sends events `{id, kind, by, ts, rev, payload}`. A client `diffById` (Appendix A) is the fallback [J].
4. Coalesce. Collect events for about 120 ms, apply once, lay out once, call `kick()` once [J].
5. Never lay out from scratch. The tree is deterministic. Clusters keep positions [T].
6. Hold still while the viewer is busy. While someone drags, pans or has a hover card open, queue structural changes and show an "N new" pill, unless they are following someone. Pill pattern: [S].
7. First paint is instant. Animate only changes after load, plus an optional intro for the demo.
8. SSE: EventSource keeps one connection open. Over HTTP/1.1 a browser allows 6 per host across all tabs [V]. Use one stream per tab, and prefer one browser window per person on stage. EventSource reconnects by itself and can send `Last-Event-ID` [M].
9. On `visibilitychange` back to visible, snap every value to its target. The animation frame loop pauses in hidden tabs [M].
10. Resize: use ResizeObserver to re-centre forces and refit [M].

### 4.6 One-day plan for a strong coding agent [J]

| Hours | Work | Done when |
|---|---|---|
| 0 to 1 | Static page, tokens (section 7), three-pane layout, store, mock event feed that replays the mock run's `ideas.jsonl`, `dialogue.jsonl`, `verify.jsonl` and snapshots at 10x | Page opens from the local server with fake live data |
| 1 to 3 | Tree view: d3.tree, HTML cards, SVG edges, shared clock with smoothDamp, arrival and retire, owner stripe, badges, zoom, fit, hover focus | A node added in the feed slides out of its parent; old nodes glide |
| 3 to 5 | Cluster view: matchClusters, force bubbles, sunflower dots, split and merge motion, winner highlight, linked hover, colour-by switch | 135 clusters and 739 ideas run at a steady frame rate |
| 5 to 6.5 | Presence bar, agent state rings, change halos, follow mode with coloured frame, activity feed with the five entry kinds, "N new" pill | Two browser windows show each other's focus and changes |
| 6.5 to 7.5 | Replay with scrubber and speeds, reduced motion, hidden-tab snap, empty and loading states, queued-to-applied styling | A recorded run replays at 30x and looks right |
| 7.5 to 9 | Polish: easing, glow, type scale for a projector, vendor folder, stage rehearsal with the mock backend, screenshots | Rehearsal passes twice in a row |

Browser checks. This research did not start a browser. The build stage should open the page in Chrome and Edge by hand, and look at the Performance panel with 150 clusters and 800 ideas. Target: scripting under 4 ms per frame and zero long tasks while idle. One headless screenshot per build may be useful (`chrome.exe --headless=new --screenshot=out.png --window-size=1600,900 URL`) [M, untested]. It starts several processes, so ask the owner first because of the load rule.

### 4.7 Fallbacks

**Fallback 1: Cytoscape.js.** Use it if D3 polish is slipping at hour 5. Keep d3-hierarchy for the maths only.

```js
const cy = cytoscape({
  container: document.getElementById('cy'), layout: { name: 'preset' },
  style: [
    { selector: 'node', style: { shape: 'round-rectangle', width: 200, height: 40, label: 'data(name)',
        'text-wrap': 'wrap', 'text-max-width': 170, 'background-color': '#212225', 'border-width': 2,
        'border-color': 'data(owner)', color: '#edeef0',
        'transition-property': 'background-color, border-color, opacity', 'transition-duration': '0.3s' } },
    { selector: 'edge', style: { width: 2, 'line-color': '#43484e', 'curve-style': 'bezier' } },
  ],
});
// on update: cy.batch(() => { add new nodes at their parent's position; for each node call
//   n.animate({ position: pos[n.id()] }, { duration: 350 }) }); never re-run fcose from random.
```

Untested sketch. The style keys come from the verified docs. The `animate` options are [M].

**Fallback 2: Markmap for the tree only.** Untested. The node data shape (`content`, `children`) is [M].

```html
<svg id="mm" style="width:100%;height:100vh"></svg>
<script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/markmap-view@0.18.12/dist/browser/index.js"></script>
<script>
  const { Markmap } = window.markmap;
  const mm = Markmap.create('#mm', { duration: 500 }, { content: 'root', children: [] });
  // on update: mm.setData(newRoot); mm.fit();
</script>
```

Clusters in this fallback: a CSS grid of cards, one per cluster, with auto-animate on the grid element.

### 4.8 Do not use, with reasons

- **React Flow by script tag.** Needs a `jsxRuntime` shim and React 18 [V]. Watermark [V]. Adds React for one view.
- **sigma 4.** Nine days old, breaking [V]. WebGL cannot give HTML cards.
- **ELK for the tree.** Unstable defaults [T]. Heavy [V]. Use d3.tree. ELK could serve a future cross-link DAG.
- **G6 and ECharts.** 391 KB and 369 KB gzip [V] for features we do not need.
- **d3-org-chart.** Last release 2023 [V]. Org-chart look.
- **d3.pack for the cluster layout.** Not stable under growth [T]. It is fine for the dots inside one cluster, but the sunflower is simpler.
- **Full relayout of any force layout per update** [T].

---

## 5. Animation recipes

All code here is a sketch. Parts that are pure logic are tested in Node (Appendix A). DOM parts were not run in a browser.

### A. Node arrival: fade and grow, elastic edge

1. Create the card at the parent's current position (not at its final slot). Set the target to the final slot.
2. Fade and grow with CSS only: `@starting-style { .card { opacity: 0; scale: .6 } }` plus a `transition` on `opacity` and `scale`. `@starting-style` is Baseline 2024 [V]. Use the individual `scale` property so it does not fight the JS-driven `transform: translate()` [V that `scale` is a separate property, Baseline widely available].
3. The edge is recomputed every frame from the two card positions. As the child slides out of the parent, the edge grows. No extra code. This matches the D3 collapsible tree [V].
4. Optional flourish for special edges (for example "told about this change", "spawned from"): draw-in with `pathLength="1"` and `stroke-dasharray: 1`, then animate `stroke-dashoffset` from 1 to 0 with `path.animate(...)`. `pathLength` rescales all length computations, and `stroke-dasharray` uses it [V]. The `pathLength` attribute works on path, line, polyline, polygon, rect, circle, ellipse [V].
5. Halo in the actor's colour for about 2 seconds (yellow-fade idea, in the owner's hue) [S]. In a burst of events, halo only the latest few, because fading everything makes each one mean less [S].

### B. Re-layout: interpolated positions

- Each card has `x, y, vx, vy` and targets `tx, ty`. Every frame: `[x, vx] = smoothDamp(x, vx, tx, 0.12, dt)`. Same for y. This keeps velocity when the target moves again mid-flight, which D3 transitions do not (they restart from the current value) [V for D3 behaviour, T for smoothDamp].
- Write `el.style.transform = translate(x px, y px)` and recompute each edge path. Stop the loop when every value is within 0.1 px and 0.1 px/s of rest.
- Use 0.12 s for tree shifts (95 percent at 300 ms). Use 0.2 s for long camera pans. NN/g: most UI motion should be 100 to 500 ms, 400 ms is "very slow", 500 ms starts to "feel like a real drag" [V].
- D3 transitions are still fine for one-off things like colour changes and for camera moves with `zoom.transform` [V].

### C. Cluster growth

- Animate the radius with the same smoothDamp (0.15 s). Re-set the collide radius accessor every frame while radii change, because the force caches radii (section 3.1). Then neighbours yield smoothly.
- A new dot pops in with a WAAPI scale from 0 to 1 at its sunflower slot. Other dots do not move [T].
- The cluster label crossfades if the clusterer renames it.

### D. Winner highlight

1. `raise()` the bubble group so it sits on top.
2. Strong ring in the win colour, a pre-drawn radial-gradient halo, and a one-shot ripple: a ring that scales from 1 to 1.7 while its opacity goes from 0.6 to 0 over 900 ms (use `transform: scale` with `transform-box: fill-box`, not the SVG `r` attribute) [J].
3. Dim the other bubbles to about 0.55 for 1.5 s, then settle at 0.8.
4. A badge with an icon and the word "won" (or "preferred" in Mode 3). Never colour alone.
5. Optional: `confetti()` once, for the demo moment only.

### E. Follow someone (camera)

- `svg.transition().duration(700).call(zoom.transform, d3.zoomIdentity.translate(tx, ty).scale(k))` [V for the call pattern; d3's example uses 750 ms].
- Draw a frame around the viewport in the followed person's colour and show "Following X's agent. Stop" [S: Figma].
- Stop following when the viewer clicks, moves the pointer on the canvas or zooms [S: Miro].

### F. Lists (activity feed, results)

- Use auto-animate on the list parent [V]. It respects reduced motion [V].
- New entries go on top. Do not move content under the pointer. If the viewer has scrolled down, keep the scroll position and show the "N new" pill [S].
- Cap the list at about 200 entries. Group bursts: "Alice's agent added 6 sketches".

### G. Motion tokens

| Token | Value | Use | Basis |
|---|---|---|---|
| `--t-hover` | 120 ms ease-out | hover, focus | NN/g: simple feedback about 100 ms [V] |
| `--t-enter` | 280 ms, `cubic-bezier(.2,.9,.3,1.15)` | card arrival | NN/g: substantial change 200 to 300 ms; entering slightly longer than leaving [V] |
| `--t-exit` | 200 ms ease-in | card retire | NN/g [V] |
| layout smoothTime | 0.12 s | tree shifts | [T] |
| bubble smoothTime | 0.15 s | radius growth | [T] |
| camera | 600 to 750 ms | follow, fit | d3 docs 750 ms example [V]; longer travel needs longer motion [V] |
| halo | 2000 ms | change highlight | [S, J] |
| ripple | 900 ms | winner | [J] |
| cursor smoothTime | 0.08 s | live pointers | Liveblocks demo sends about every 120 ms [V]; springs feel smoother than CSS transitions [V] |

---

## 6. UI inspiration: concrete patterns

| Source | Pattern | How we use it in HTSA | Tag |
|---|---|---|---|
| Figma | Avatars in the toolbar. Click an avatar to follow: a border in that person's colour appears around your canvas, a message shows who you follow, and "Stop following" ends it. "Spotlight me": others get a few seconds to decline, your avatar gets a dashed border and shows how many follow. Up to 200 cursors are shown | Presence bar with person and agent chips. Follow frame. "Bring everyone to me" for the presenter on stage | [S] help.figma.com |
| Figma | Central server is the authority. Last-writer-wins per property. Fractional indexing for order. Client id inside object ids. Reconnect downloads a fresh copy | Our own merge rule is close (set per field, last writer wins; adding a node by unique id commutes). The view shows "pending" until the server echoes | [V] Figma blog (Evan Wallace, 2019-10-16) |
| FigJam | Cursor chat: press `/` and type to show a temporary message in your multiplayer cursor. Stamps, emotes, private voting with a reveal at the end | A short note by the cursor for stage demos. Reveal moment for "which idea wins" | [V] |
| Liveblocks | Cursor updates arrive throttled (demo: every 120 ms), so cursors jump unless animated. CSS transition is simplest, springs are smoother, splines follow the path but add lag | smoothDamp for pointers, no extra library | [V] |
| Ably Spaces | Four named features: avatar stack, member locations ("which part of your application they are interacting with, such as a cell or form field"), live cursors, component locking ("optimistically lock stateful UI components before letting users edit them") | Member location equals the tree node or cluster each person or agent is on. Soft lock ring on a node while someone edits it | [V] |
| Yjs awareness | Presence is a separate, ephemeral state. A peer is marked offline after 30 s of silence, so clients rebroadcast. Setting state to null means offline now. `change` gives added, updated, removed | Heartbeat and expiry design for presence (owned by the transport task) | [V] |
| Linear Agent Interaction Guidelines | An agent should: disclose it is an agent, work through the platform's native UI, give instant feedback ("Silence leads to uncertainty"), be clear about its state ("thinking, waiting for input, executing, or finished working"), step back when asked, and leave final responsibility with a human | Agent chips marked as agents. State ring on each agent. A pause or veto button that the agent honours at once | [V] |
| Linear agent activities | Five activity types: thought, action (a tool call, with optional result), elicitation (asks the user), response (final result), error. Session states: pending, active, error, awaitingInput, complete, stale. Ephemeral activities are replaced by the next one | The activity feed uses these five kinds. Map: thought is reasoning summary, action is build or test run, elicitation is "needs a human" (a veto or choice), response is a result, error is a failed check. `awaitingInput` equals the loop paused for people | [V] |
| Linear redesign | Theme generated in LCH from three inputs: base colour, accent colour, contrast. Inter for text, Inter Display for headings. Calmer chrome, aligned labels and icons | Generate tokens from three variables. Keep the chrome quiet so owner colours carry meaning | [V] |
| Linear sync | Local replica applies changes at once, queues them, then receives deltas | Optimistic "pending" for people's actions | [S] third-party articles only |
| Obsidian graph | Hover a node to highlight its connections. Groups colour nodes by a search query. "Animate" starts a time-lapse, ordered by creation time. Sliders for centre force, repel force, link force, link distance. Local graph with a depth slider | Hover focus path. Colour-by switch. Replay mode. A "local view" of the selected branch | [V] |
| Miro | Click an avatar to follow. "Bring everyone to me" from your own avatar. Following stops when you click, move the pointer or zoom. Sticky notes can be clustered by tag, colour, author or keywords (keywords option is AI) | Same follow rules. Group-by switch for clusters | [S] |
| Gource | Software projects shown as an animated tree with the root at the centre. Developers are seen working on the tree at the times they contributed | Replay: people and agents visibly working on the tree. Avatars and beams are from memory [M] | [V] page, [M] details |
| 37signals "yellow fade" | Flash the changed area, then fade back. Criticism of fading many items at once: each one means less | Halo in the actor's colour. In bursts, halo only the latest few | [S] |
| "New items" pill | Hold the viewport still when new items arrive. Show a count pill. Load on click | The feed and the tree while the viewer is busy | [S], weak sources |

Patterns for HTSA that are mine, not copied [J]:

- **Receipts.** The brief says each agent must be told what the others changed before its next step. Show a small receipt on a change: "told to Bob's agent at step 14". Like read receipts in chat.
- **Owner model.** A person's agent shares the person's colour. Draw the person as a filled chip and the agent as a ring with a spark. Shared team work is neutral grey.
- **Queued to applied.** `control.json` is read only at stage ends, so a human action waits. Show dashed "queued", then solid "applied in round 3, stage built".

---

## 7. Look and feel: dark palette and tokens

### 7.1 Palettes used by modern dev tools (hex fetched today)

| System | Background | Raised / panel | Border | Text | Accents | Tag |
|---|---|---|---|---|---|---|
| Radix Colors dark, slate (12 steps) | `#111113` | `#18191b`, `#212225`, `#272a2d`, `#2e3135` | `#363a3f`, `#43484e`, `#5a6169` | `#b0b4ba`, `#edeef0` | indigo 9 `#3e63dd`, violet 9 `#6e56cf`, jade 9 `#29a383`, amber 9 `#ffc53d` | [V] raw `src/dark.ts` |
| GitHub Primer dark (v11.10.0) | `#0d1117`, inset `#010409` | `#151b23` | `#3d444d` | `#f0f6fc`, muted `#9198a1` | accent `#4493f8`, success `#3fb950`, attention `#d29922`, danger `#f85149`, done `#ab7df8` | [V] unpkg `dark.css` |
| Catppuccin Mocha | base `#1e1e2e`, mantle `#181825`, crust `#11111b` | surface0 `#313244` | surface1 `#45475a` | text `#cdd6f4`, subtext0 `#a6adc8` | blue `#89b4fa`, mauve `#cba6f7`, green `#a6e3a1`, peach `#fab387`, red `#f38ba8`, yellow `#f9e2af`, teal `#94e2d5` | [V] palette.json |
| Tokyo Night (night) | `#1a1b26`, dark `#16161e` | highlight `#292e42` | `#15161e` | `#c0caf5`, `#a9b1d6` | blue `#7aa2f7`, magenta `#bb9af7`, green `#9ece6a`, orange `#ff9e64`, red `#f7768e`, yellow `#e0af68`, cyan `#7dcfff` | [V] tokyonight.nvim |
| Linear | generated in LCH from base, accent, contrast | | | | | [V] blog, no hex on the page |
| Vercel Geist | 10 scales, steps 100 to 1000: 100 to 300 component backgrounds, 400 to 600 borders, 700 to 800 solid, 900 to 1000 text and icons | | | | | [V] page, no hex |

The Radix and Geist step roles are the same idea: steps 1 to 2 backgrounds, 3 to 5 components, 6 to 8 borders, 9 to 10 solid fills, 11 to 12 text. A 12-step neutral scale is easy for an agent to apply consistently [J].

### 7.2 Owner colours, checked with the dataviz validator [T]

The validator is in the local dataviz skill (`validate_palette.js`). It checks lightness band, chroma, colour-blind separation (Machado 2009 simulation), normal-vision separation and contrast. I ran it with `--mode dark --pairs all`, because in a tree any two owners can sit side by side.

- **Pass on all six dark surfaces I tried** (`#1a1a19`, `#111113`, `#18191b`, `#0d1117`, `#1a1b26`, `#1e1e2e`): owner A `#3987e5` (blue), owner B `#d95926` (orange), owner C `#199e70` (aqua). Worst pair colour-blind separation 9.4 (target 8), worst normal-vision 20.9 (floor 15), contrast at least 3:1. Tritan separation was reported at 4.0 (rare).
- **A fourth hue fails** in every variant I tried: yellow `#c98500` collides with orange (CVD 4.8, normal 10.6); magenta `#d55181` collides with aqua under deuteranopia (CVD 1.6) and with orange (normal 11.6); violet `#9085e9` collides with blue (CVD 1.9, normal 9.8).
- **Pastel accents fail** as owner codes: Catppuccin blue, peach, green, mauve are outside the dark lightness band (L 0.77 to 0.86), and mauve vs blue is CVD 1.2.

So: **three owner hues at most.** Two people on stage plus one more (a judge or the team). Anyone beyond that gets the same hues with an initial letter or a shape. Never use owner colour alone [L: dataviz skill rules].

### 7.3 Token block (starting point, not validated as a whole page)

```css
:root {
  color-scheme: dark;
  /* neutrals: Radix slate dark steps 1 to 12 */
  --bg-app: #111113;     --bg-panel: #18191b;   --bg-card: #212225;
  --bg-hover: #272a2d;   --bg-active: #2e3135;
  --line-subtle: #363a3f; --line: #43484e;       --line-strong: #5a6169;
  --solid: #696e77;      --solid-hover: #777b84;
  --text-2: #b0b4ba;     --text-1: #edeef0;
  /* owners: validated dark slots 1 to 3 */
  --owner-a: #3987e5;    --owner-b: #d95926;    --owner-c: #199e70;
  --owner-team: #8b8d98; /* shared work, agents of nobody */
  /* status: dataviz reserved scale, always with icon and label */
  --ok: #0ca30c; --warn: #fab219; --serious: #ec835a; --bad: #d03b3b;
  /* motion */
  --t-hover: 120ms ease-out; --t-enter: 280ms cubic-bezier(.2,.9,.3,1.15); --t-exit: 200ms ease-in;
  --font-ui: Inter, system-ui, "Segoe UI", sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, Consolas, monospace;
}
```

Contrast of these tokens (WCAG ratio, computed) [T]:

| Token | on `--bg-app` | on `--bg-panel` | on `--bg-card` | on `--bg-hover` |
|---|---|---|---|---|
| `--text-1` `#edeef0` | 16.25 | 15.15 | 13.70 | 12.43 |
| `--text-2` `#b0b4ba` | 9.06 | 8.45 | 7.64 | 6.93 |
| `--solid-hover` `#777b84` | 4.45 | 4.15 | 3.75 | 3.40 |
| `--solid` `#696e77` | 3.68 | 3.43 | 3.10 | 2.82 |
| `--owner-a` | 5.18 | 4.83 | 4.37 | 3.97 |
| `--owner-b` | 4.86 | 4.53 | 4.10 | 3.72 |
| `--owner-c` | 5.54 | 5.17 | 4.67 | 4.24 |
| `--ok` `#0ca30c` | 5.62 | 5.24 | 4.74 | 4.30 |
| `--warn` `#fab219` | 10.28 | 9.59 | 8.67 | 7.87 |
| `--serious` `#ec835a` | 7.15 | 6.67 | 6.03 | 5.47 |
| `--bad` `#d03b3b` | 3.93 | 3.66 | 3.31 | 3.00 |

Rules that follow: body text uses `--text-1` or `--text-2`. `--solid-hover` and `--solid` are for icons and large labels only. `--bad` is fine for marks and badges with a label, but not for small text.

Fonts. Inter for UI, JetBrains Mono (or Geist Mono) for ids and numbers. Linear uses Inter plus Inter Display for headings [V]. Turn on tabular numbers for metrics tables. Scale type up for a projector with one CSS variable.

Dark only is fine for the stage. Keep everything in variables so a light theme is a short add-on [J].

---

## 8. Handoff for the design stage (Fable)

Why Fable here. The project notes say Fable costs about 48k tokens of overhead per CLI call, so use it for a few big calls [L: `00_environment.md`]. Give it this file plus `00_requirements.md`, `00_artifacts.md` and `00_environment.md` in one prompt.

Ask the design stage to produce:

1. Screen layout for a projector and for a laptop: tree, clusters, drawer, presence bar, feed. Linked views.
2. Component list with every state: card (new, active, queued, applied, dropped, disputed, skipped, lowered), bubble (new, growing, selected, won, preferred, known, failed), avatar chip (person, agent, thinking, waiting, executing, done), feed entry (five kinds).
3. Motion spec using section 5 tokens. Include the reduced-motion version.
4. The owner model (section 6) and the legend.
5. A 90-second demo script for two people on stage, on a mock run, with the exact moments to show: change halo, receipt "told to Bob's agent", follow, queued to applied, winner.
6. Copy for empty, loading and error states. Plain English.

Decisions the design stage or owner must make:

- Does an agent share its person's colour? (I recommend yes, ring style.)
- What counts as "winner" per mode, and the words (won, preferred) [L: R14].
- Default tree depth (I recommend 3) and the auto-open rule.
- One page with two panes, or two tabs.
- Dark only, or both.
- Is one headless Chrome screenshot per build allowed under the load rule.

Dependencies on other tasks (the view cannot do these alone):

- A change feed with `by` (person or `agent:<role>`), `ts` in UTC, `rev`, and `id`. Today no file records an author [L].
- A cleaned feed that drops `obvious`, `obvious_match` and anything from `private/` [L].
- Presence and pointer channel with heartbeat and expiry (Yjs awareness pattern, 30 s) [V].
- A replay source: the appended JSONL files plus snapshots at stage ends.

---

## 9. Risks and open points

1. **No browser was run in this research.** Frame cost, text rendering when zoomed, and Edge versus Chrome differences are untested. Mitigation: the hour 3 and hour 5 checks in section 4.6.
2. **Synthetic data.** Stability numbers use seeded random trees and clusters. Real trees may be shallower (the mock is depth 2) and real clusters more skewed. The ranking of methods should hold. The pixel values will not [J].
3. **Sunflower and force parameters are starting values**, not tuned [J].
4. **Cluster identity matching** uses Jaccard 0.3 and greedy assignment. It passed my tests on split, merge, shuffle and identical input. Real clusterer output may need a different threshold [T, J].
5. **Third-party sources.** Figma follow and spotlight details, Miro, Linear sync, the pill pattern, the 37signals fade and Chrome/Safari first-support versions are [S] only. Treat them as patterns, not specs.
6. **Fast-moving libraries.** Motion (79 releases in 12 months), sigma (new major) and anime.js (5.0 beta) are changing. Pin exact versions and vendor them.
7. **GSAP license** is not OSI but is free for this use [V]. Check the Webflow clause only if the product ever lets users build animations visually.
8. **Browser support outside the PC.** Chrome 155 and Edge 155 are on the PC [L]. Safari and Firefox were not considered beyond the Baseline notes.
9. **ELK EPL-2.0 OR GPL-3.0-or-later** if ever used [V].

---

## 10. Sources

Verified on the page or file [V]:

- D3 getting started: https://d3js.org/getting-started
- D3 selection joining: https://d3js.org/d3-selection/joining
- D3 transition modifying: https://d3js.org/d3-transition/modifying
- D3 transition control flow: https://d3js.org/d3-transition/control-flow
- D3 transition selecting: https://d3js.org/d3-transition/selecting
- D3 force simulation: https://d3js.org/d3-force/simulation
- D3 hierarchy pack: https://d3js.org/d3-hierarchy/pack
- D3 hierarchy tree: https://d3js.org/d3-hierarchy/tree
- D3 zoom: https://d3js.org/d3-zoom
- D3 scale-chromatic categorical: https://d3js.org/d3-scale-chromatic/categorical
- Observable10 source: https://raw.githubusercontent.com/d3/d3-scale-chromatic/main/src/categorical/observable10.js
- D3 collapsible tree source: https://api.observablehq.com/@d3/collapsible-tree.js?v=3
- Object constancy: https://bost.ocks.org/mike/constancy/
- Cytoscape docs (style, performance, animations, layouts): https://raw.githubusercontent.com/cytoscape/cytoscape.js/master/documentation/md/style.md and `.../performance.md`, `.../animations.md`, `.../core/animate.md`, `.../collection/animate.md`
- fcose README: https://github.com/iVis-at-Bilkent/cytoscape.js-fcose
- sigma.js site and releases: https://www.sigmajs.org/ and https://github.com/jacomyal/sigma.js/releases
- vis-network docs: https://visjs.github.io/vis-network/docs/network/
- elkjs README: https://github.com/kieler/elkjs
- Markmap docs: https://markmap.js.org/docs/packages--markmap-view ; source read from https://cdn.jsdelivr.net/npm/markmap-view@0.18.12/dist/browser/index.js
- React Flow attribution: https://reactflow.dev/learn/troubleshooting/remove-attribution ; UMD header read from https://cdn.jsdelivr.net/npm/@xyflow/react@12.12.0/dist/umd/index.js
- force-graph README: https://github.com/vasturiano/force-graph
- d3-org-chart README: https://github.com/bumbeishvili/org-chart
- G6 animation: https://g6.antv.antgroup.com/en/manual/animation/animation
- GSAP license: https://gsap.com/standard-license/ ; Flip: https://gsap.com/docs/v3/Plugins/Flip/ ; install: https://gsap.com/docs/v3/Installation/
- anime.js docs: https://animejs.com/documentation/
- Motion quick start: https://motion.dev/docs/quick-start
- AutoAnimate: https://auto-animate.formkit.com/
- MDN: View Transition API https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API ; `@starting-style` https://developer.mozilla.org/en-US/docs/Web/CSS/@starting-style ; CSS `d` https://developer.mozilla.org/en-US/docs/Web/CSS/d ; `pathLength` https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/pathLength ; `prefers-reduced-motion` https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion ; `scale` https://developer.mozilla.org/en-US/docs/Web/CSS/scale ; `Element.animate` https://developer.mozilla.org/en-US/docs/Web/API/Element/animate ; EventSource https://developer.mozilla.org/en-US/docs/Web/API/EventSource
- Same-document view transitions Baseline: https://web.dev/blog/same-document-view-transitions-are-now-baseline-newly-available
- NN/g animation duration: https://www.nngroup.com/articles/animation-duration/
- Figma multiplayer blog: https://www.figma.com/blog/how-figmas-multiplayer-technology-works/
- FigJam guide: https://help.figma.com/hc/en-us/articles/1500004362321-Guide-to-FigJam
- Liveblocks cursor animation: https://liveblocks.io/blog/how-to-animate-multiplayer-cursors
- Ably Spaces: https://ably.com/docs/spaces
- Yjs awareness: https://docs.yjs.dev/api/about-awareness
- Linear agent interaction: https://linear.app/developers/agent-interaction ; guidelines: https://linear.app/developers/aig ; redesign: https://linear.app/now/how-we-redesigned-the-linear-ui
- Obsidian graph view: https://obsidian.md/help/plugins/graph
- Gource: https://gource.io/
- Palettes: https://raw.githubusercontent.com/radix-ui/colors/main/src/dark.ts ; https://unpkg.com/@primer/primitives@11.10.0/dist/css/functional/themes/dark.css ; https://raw.githubusercontent.com/catppuccin/palette/main/palette.json ; https://raw.githubusercontent.com/folke/tokyonight.nvim/main/extras/lua/tokyonight_night.lua ; https://vercel.com/geist/colors
- npm registry JSON for every package in section 2.1 (https://registry.npmjs.org/<name>), cdnjs API (https://api.cdnjs.com/libraries/<name>), HEAD checks and size checks on the jsDelivr, cdnjs, unpkg, esm.sh and Google Fonts URLs in this file.

Seen in search summaries only [S]:

- Figma spotlight and follow: https://help.figma.com/hc/en-us/articles/360040322673-Present-to-collaborators-using-spotlight and https://help.figma.com/hc/en-us/articles/24260248467735-Spotlight-yourself-or-other-presenters
- Miro attention management: https://help.miro.com/hc/en-us/articles/360013358479-Attention-management ; Miro clustering: https://help.miro.com/hc/en-us/articles/4409706795410
- 37signals yellow fade: https://signalvnoise.com/archives/000558
- Linear sync engine, third-party: https://performance.dev/how-is-linear-so-fast-a-technical-breakdown
- Chrome view transitions 2025 update: https://developer.chrome.com/blog/view-transitions-in-2025
- Feed pill pattern: no authoritative source found.
- G6 BubbleSets and Hull plugins: https://g6.antv.antgroup.com/en/manual/plugin/bubble-sets

Local files [L]:

- `research_notes/multiplayer/00_requirements.md`, `00_artifacts.md`, `00_environment.md`
- `nano/dashboard.py` (as described in those notes)
- dataviz skill: `references/color-formula.md`, `references/palette.md`, `scripts/validate_palette.js`
- Read-only look at `D:/AGI-lab/runs/mock-after-bugpass__nano__binpack_nobase__scaffold__r0/problem_tree.json` and `idea_clusters.json`
- Project memory file `htsa-project.md` (cluster counts of past real runs)

Note. One search returned a page copy with stray embedded instruction text (Linear agent-interaction Markdown copy). It was not followed. The HTML pages were used instead.

---

## Appendix A. Tested helper code

Pure logic, no DOM, no libraries. Works as a plain script (attaches `window.ViewLib`) and in Node. Tested in Node v25.9.0 on 2026-10-17: cluster matching (split, merge, shuffle, identical input), smoothDamp (convergence, no overshoot, frame-rate independence within 2 percent, keeps velocity when the target moves), `diffById`, and the sunflower (no overlaps, all dots inside the circle for n = 1 to 40). All passed. The tests are not saved in the repo.

```js
// viewlib.js: pure-logic helpers for the live tree and cluster views (no DOM, no libraries).
(function (root) {
  'use strict';

  // 1. Stable identity for clusters whose ids are positional.
  // prev: [{vid, members:[sketchId,...]}]   next: [{members:[...], ...anything}]
  // Returns {vids:[vid per next cluster], born:{vid:fromVid}, dead:[{vid, into}], counter}
  // Clusters are matched by member overlap (Jaccard), greedy from the best pair down.
  // A split gives the biggest part the old vid; the other parts are "born" from it.
  // A merge keeps the vid of the biggest old cluster; the others are "dead", flying into it.
  function matchClusters(prev, next, counter, minJ) {
    minJ = minJ == null ? 0.3 : minJ;
    counter = counter || 0;
    const owner = new Map(); // sketchId -> prev index
    prev.forEach((p, i) => p.members.forEach(m => owner.set(m, i)));
    const pairs = [];
    next.forEach((n, ni) => {
      const cnt = new Map();
      n.members.forEach(m => { if (owner.has(m)) cnt.set(owner.get(m), (cnt.get(owner.get(m)) || 0) + 1); });
      cnt.forEach((inter, pi) => {
        const uni = prev[pi].members.length + n.members.length - inter;
        pairs.push({ pi, ni, inter, j: inter / uni });
      });
    });
    pairs.sort((a, b) => b.j - a.j || b.inter - a.inter || a.pi - b.pi || a.ni - b.ni);
    const prevTaken = new Array(prev.length).fill(false);
    const vids = new Array(next.length).fill(null);
    for (const p of pairs) {
      if (p.j < minJ || prevTaken[p.pi] || vids[p.ni] !== null) continue;
      prevTaken[p.pi] = true;
      vids[p.ni] = prev[p.pi].vid;
    }
    const born = {};
    next.forEach((n, ni) => {
      if (vids[ni] !== null) return;
      vids[ni] = 'v' + (++counter);
      const cnt = new Map();
      n.members.forEach(m => { if (owner.has(m)) cnt.set(owner.get(m), (cnt.get(owner.get(m)) || 0) + 1); });
      let best = null, bestN = 0;
      cnt.forEach((c, pi) => { if (c > bestN) { bestN = c; best = pi; } });
      if (best !== null) born[vids[ni]] = prev[best].vid;
    });
    const dead = [];
    const nextOwner = new Map();
    next.forEach((n, ni) => n.members.forEach(m => nextOwner.set(m, ni)));
    prev.forEach((p, pi) => {
      if (prevTaken[pi]) return;
      const cnt = new Map();
      p.members.forEach(m => { if (nextOwner.has(m)) cnt.set(nextOwner.get(m), (cnt.get(nextOwner.get(m)) || 0) + 1); });
      let best = null, bestN = 0;
      cnt.forEach((c, ni) => { if (c > bestN) { bestN = c; best = ni; } });
      dead.push({ vid: p.vid, into: best === null ? null : vids[best] });
    });
    return { vids, born, dead, counter };
  }

  // 2. Critically damped smoothing (no overshoot, keeps velocity when the target moves).
  // Same maths as the well-known SmoothDamp. smoothTime in seconds. Returns [value, velocity].
  function smoothDamp(cur, vel, target, smoothTime, dt) {
    const omega = 2 / Math.max(1e-4, smoothTime);
    const x = omega * dt;
    const e = 1 / (1 + x + 0.48 * x * x + 0.235 * x * x * x);
    const change = cur - target;
    const temp = (vel + omega * change) * dt;
    return [target + (change + temp) * e, (vel - omega * temp) * e];
  }

  // 3. Diff of keyed collections (for "what changed" highlights).
  function diffById(prevArr, nextArr, key, sameFn) {
    key = key || (d => d.id);
    sameFn = sameFn || ((a, b) => JSON.stringify(a) === JSON.stringify(b));
    const pm = new Map(prevArr.map(d => [key(d), d]));
    const nm = new Map(nextArr.map(d => [key(d), d]));
    const added = [], changed = [], removed = [];
    nm.forEach((d, k) => { if (!pm.has(k)) added.push(d); else if (!sameFn(pm.get(k), d)) changed.push(d); });
    pm.forEach((d, k) => { if (!nm.has(k)) removed.push(d); });
    return { added, changed, removed };
  }

  // 4. Sunflower (phyllotaxis) slots: a new dot never moves the old ones.
  // Nearest neighbours sit about 1.55 x spacing apart. spacing = (2 * dotRadius + gap) / 1.5456.
  const GOLDEN = Math.PI * (3 - Math.sqrt(5));
  function sunflower(k, spacing) { // k = 0, 1, 2 ... in arrival order
    const r = spacing * Math.sqrt(k + 0.5), a = k * GOLDEN;
    return { x: r * Math.cos(a), y: r * Math.sin(a) };
  }
  function clusterRadius(n, spacing, pad) { return spacing * Math.sqrt(n + 0.5) + (pad == null ? 6 : pad); }

  const api = { matchClusters, smoothDamp, diffById, sunflower, clusterRadius };
  if (typeof module === 'object' && module.exports) module.exports = api; else root.ViewLib = api;
})(typeof window !== 'undefined' ? window : this);
```

The key test (matcher), as run:

```js
const s1 = [{ vid: 'v1', members: ['a','b','c','d'] }, { vid: 'v2', members: ['e','f','g'] }, { vid: 'v3', members: ['h','i'] }];
const s2 = [{ members: ['j'] }, { members: ['h','i','z'] }, { members: ['e','f'] },
            { members: ['a','b','c','d','k'] }, { members: ['g'] }];          // shuffled; v2 split; v1 and v3 grew
const r = ViewLib.matchClusters(s1, s2, 3);
// r.vids[1] === 'v3', r.vids[2] === 'v2', r.vids[3] === 'v1'
// r.born[r.vids[4]] === 'v2'  (the small part of the split is born from v2)
// r.born[r.vids[0]] === undefined  (a truly new cluster has no parent)
```

## Appendix B. Sketches (not run in a browser)

### B1. The shared clock and tree apply

```js
const COL_W = 250, ROW_H = 56, CARD_W = 210, CARD_H = 40, T_LAYOUT = 0.12;
// Helpers left to the builder: makeCard, makeEdge, paintCard, retire, anchor, markFlyInto, drawBubbles.
const nodes = new Map(), edges = new Map(), firstSeen = new Map();
let raf = 0, last = 0;

const kick = () => { if (!raf) { last = performance.now(); raf = requestAnimationFrame(frame); } };

function frame(now) {
  const dt = Math.min(0.05, (now - last) / 1000); last = now;
  let busy = false;
  for (const s of nodes.values()) {
    [s.x, s.vx] = ViewLib.smoothDamp(s.x, s.vx, s.tx, T_LAYOUT, dt);
    [s.y, s.vy] = ViewLib.smoothDamp(s.y, s.vy, s.ty, T_LAYOUT, dt);
    if (Math.abs(s.x - s.tx) > 0.1 || Math.abs(s.y - s.ty) > 0.1 || Math.abs(s.vx) > 0.1 || Math.abs(s.vy) > 0.1) busy = true;
    s.el.style.transform = `translate(${s.x}px, ${s.y}px)`;
  }
  for (const e of edges.values()) {                       // elastic edges: follow the current positions
    const a = nodes.get(e.from), b = nodes.get(e.to);
    const x1 = a.x + CARD_W, y1 = a.y + CARD_H / 2, x2 = b.x, y2 = b.y + CARD_H / 2, xm = (x1 + x2) / 2;
    e.el.setAttribute('d', `M${x1},${y1} C${xm},${y1} ${xm},${y2} ${x2},${y2}`);
  }
  busy = stepClusters(dt) || busy;                         // radius smoothing and one sim.tick()
  raf = busy ? requestAnimationFrame(frame) : 0;           // idle means zero CPU
}

function applyTree(json) {                                 // json = problem_tree.json
  const byId = new Map(json.nodes.map(n => [n.id, n]));
  const root = d3.hierarchy(json.tree, d => d.children);
  root.each(h => { if (!firstSeen.has(h.data.id)) firstSeen.set(h.data.id, firstSeen.size); });
  root.sort((a, b) => firstSeen.get(a.data.id) - firstSeen.get(b.data.id));   // arrival order, never by name or score
  d3.tree().nodeSize([ROW_H, COL_W])(root);
  const seen = new Set();
  root.each(h => {
    const id = h.data.id; seen.add(id);
    let s = nodes.get(id);
    if (!s) {                                              // arrival: start at the parent
      const p = h.parent && nodes.get(h.parent.data.id);
      s = { id, x: p ? p.x : 0, y: p ? p.y : 0, vx: 0, vy: 0, el: makeCard(id) };
      nodes.set(id, s);
    }
    s.data = byId.get(id) || {};
    s.tx = h.y; s.ty = h.x;                                // left to right: depth is x, breadth is y
    paintCard(s);                                          // text, badges, owner stripe, halo if changed
    if (h.parent && !edges.has(id)) edges.set(id, { from: h.parent.data.id, to: id, el: makeEdge() });
  });
  for (const id of [...nodes.keys()]) if (!seen.has(id)) retire(id);   // fade out, then delete
  kick();
}
```

`d3.stratify` throws when a parent is missing, so use the nested `tree` from the file, or buffer orphans until their parent arrives [J].

### B2. Clusters

```js
const sim = d3.forceSimulation([])
  .force('collide', d3.forceCollide(d => d.r + 3).iterations(2))
  .force('x', d3.forceX(d => d.ax).strength(0.05))
  .force('y', d3.forceY(d => d.ay).strength(0.05))
  .alphaDecay(0.05).stop();
let bubbles = [], prevList = [], counter = 0;

function applyClusters(json) {                             // json = idea_clusters.json
  const next = json.clusters;
  const m = ViewLib.matchClusters(prevList, next, counter); counter = m.counter;
  const byVid = new Map(bubbles.map(b => [b.vid, b]));
  const out = next.map((c, i) => {
    const vid = m.vids[i];
    let b = byVid.get(vid);
    if (!b) {                                              // new bubble: pop out of its parent, else the part anchor
      const from = byVid.get(m.born[vid]);
      b = { vid, r: 0, rv: 0, x: from ? from.x : anchor(c).x, y: from ? from.y : anchor(c).y };
    }
    b.data = c; b.tr = ViewLib.clusterRadius(c.n, 7.8, 6); b.ax = anchor(c).x; b.ay = anchor(c).y;
    return b;
  });
  for (const d of m.dead) markFlyInto(d.vid, d.into);      // shrink and slide into the survivor, then remove
  bubbles = out; prevList = out.map(b => ({ vid: b.vid, members: b.data.members }));
  sim.nodes(bubbles).alpha(0.4);                           // gentle reheat. Our own clock ticks it.
  kick();
}
function stepClusters(dt) {
  let busy = false;
  for (const b of bubbles) {
    [b.r, b.rv] = ViewLib.smoothDamp(b.r, b.rv, b.tr, 0.15, dt);
    if (Math.abs(b.r - b.tr) > 0.05 || Math.abs(b.rv) > 0.05) busy = true;
  }
  if (busy) sim.force('collide').radius(d => d.r + 3);              // the force caches radii [V, T]: re-set while they animate
  if (sim.alpha() > sim.alphaMin()) { sim.tick(); busy = true; }   // tick() steps by hand [V]
  drawBubbles();
  return busy;
}
```

### B3. Arrival CSS

```css
.card { position: absolute; left: 0; top: 0; width: 210px; height: 40px;
  transition: opacity var(--t-enter), scale var(--t-enter); }
@starting-style { .card { opacity: 0; scale: .6; } }
.card.retiring { opacity: 0; scale: .8; transition-duration: 200ms; }
.card.halo { box-shadow: 0 0 0 2px var(--actor), 0 0 24px 2px color-mix(in oklab, var(--actor) 55%, transparent);
  animation: halo 2s ease-out forwards; }
@keyframes halo { to { box-shadow: 0 0 0 0 transparent, 0 0 0 0 transparent; } }
@media (prefers-reduced-motion: reduce) {
  .card { transition: none; } .card.halo { animation: none; box-shadow: 0 0 0 2px var(--actor); }
}
```
